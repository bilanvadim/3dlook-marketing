/**
 * The slice of the old @libsql/client API that the tests use for FIXTURES, on top of better-sqlite3.
 *
 * store.ts moved off @libsql/client on 2026-08-14 (it leaked a connection per transaction — see
 * RUNBOOK). The tests never used that client to exercise the store: they use it to create the
 * schema, seed rows, read a value back, and — in contention.test/callback.test — to hold a real
 * write lock on a second connection. The code under test always went through Store.
 *
 * So the honest migration is to swap what the fixtures are built on and leave every assertion
 * exactly as it was. Rewriting ~60 fixture call sites by hand is how you introduce a bug in the
 * harness that exists to catch bugs.
 */
import Database from 'better-sqlite3';

type Stmt = string | { sql: string; args?: any[] };

function norm(s: Stmt, args?: any[]): { sql: string; args: any[] } {
  return typeof s === 'string' ? { sql: s, args: args ?? [] } : { sql: s.sql, args: s.args ?? [] };
}

export function createClient({ url }: { url: string }) {
  const db = new Database(url.replace(/^file:(\/\/)?/i, ''));

  const run = (s: Stmt, args?: any[]) => {
    const { sql, args: a } = norm(s, args);
    // PRAGMA has its own entry point in this driver, and `journal_mode = WAL` is the case that
    // matters: it RETURNS a row, so it is neither a plain read nor a plain write.
    if (/^\s*pragma\s/i.test(sql)) {
      const out = db.pragma(sql.replace(/^\s*pragma\s+/i, ''));
      return { rows: (Array.isArray(out) ? out : []) as any[], rowsAffected: 0, lastInsertRowid: 0 };
    }
    const st = db.prepare(sql);
    if (st.reader) return { rows: st.all(...a) as any[], rowsAffected: 0, lastInsertRowid: 0 };
    const info = st.run(...a);
    return { rows: [] as any[], rowsAffected: info.changes, lastInsertRowid: info.lastInsertRowid };
  };

  return {
    async execute(s: Stmt, args?: any[]) { return run(s, args); },
    async executeMultiple(sql: string) { db.exec(sql); },
    /**
     * A real second-connection write lock, which is the only reason the tests want a transaction
     * object at all: contention.test and callback.test hold one to make the Store lose the race.
     */
    async transaction(_mode: 'write' | 'read' | 'deferred' = 'write') {
      db.exec('BEGIN IMMEDIATE');
      return {
        async execute(s: Stmt, args?: any[]) { return run(s, args); },
        async commit() { db.exec('COMMIT'); },
        async rollback() { db.exec('ROLLBACK'); },
      };
    },
    close() { db.close(); },
  };
}
