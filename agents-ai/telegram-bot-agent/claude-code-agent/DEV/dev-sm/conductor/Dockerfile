# Hermes Conductor — runs the autonomous loop in isolation.
FROM node:22-slim
# git + ripgrep help the agent; add others your repos need
RUN apt-get update && apt-get install -y --no-install-recommends git ripgrep ca-certificates \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev || npm install --omit=dev
COPY . .
# the working repo is mounted at runtime (read-write), e.g. -v /srv/myrepo:/work
# secrets come from --env-file, NOT baked into the image
ENV NODE_ENV=production
CMD ["npx", "tsx", "src/core/conductor.ts"]
