---
track: pr
task_id: 2026-08-23-awards-and-rankings
product: mixed
status: needs Vadim answers before any submission
created: 2026-08-23
---

# Open questions — answer before submitting anything from this batch

Per CLAUDE.md hard rule #3 ("если контекста не хватает — стоп и вопрос"), these are flagged rather
than guessed.

1. **FT Americas' Fastest Growing Companies asks for revenue verification with a third party
   (Statista).** 3DLOOK's 2025 ARR ($1.084M) is below their stated $1.5M floor anyway, so this is
   likely moot — but before drafting anything for a revenue-verified ranking in general: are we
   comfortable disclosing exact revenue to a third-party verifier, even if it isn't published in the
   final list? This is a financial-disclosure decision, not a content decision — needs your explicit
   go, not mine.

2. **Katerina Galich's founder status is not documented.** `overview.md` lists her as CEO and Whitney
   Cathcart as "Co-founder & CCO" — it does not say Katerina co-founded 3DLOOK. VivaTech's Female
   Founder Award and some "40 under 40 founder" type programs specifically require founder status.
   Is Katerina a co-founder (just not labeled that way in our docs), or should female-founder-specific
   programs be routed to whoever actually holds that title?

3. **Entry fees.** Research found fee *ranges* for most programs (e.g., Stevie tiers roughly
   $195–$995 depending on submission date and category count, Fast Company roughly $200–$800+,
   BIG Innovation Awards roughly $295–$495) but not exact current-year numbers — award sites gate
   exact pricing behind the entry portal itself. Who approves spend, and what's the ceiling per
   program? (Note: entering closer to a deadline is usually more expensive — the Stevie Women in
   Business late/final window may already carry a higher fee than an earlier tier would have.)

4. **Category selection.** Several programs (Stevie IBA/ABA, Fast Company, Globee, BIG) have dozens
   of possible categories (e.g., "Health/Wellness Product," "Achievement in Innovation," "女性
   Executive of the Year," "AI Solution," "Startup of the Year"). I've recommended one category per
   program in each draft based on best fit, but final category selection affects the entry form and
   sometimes the fee tier — needs your sign-off, not just mine.

5. **Legal entity / HQ details.** A few of the "hard no" programs (Deloitte UK Fast 50, InsurTech100)
   turn on where 3DLOOK is legally headquartered and whether there's a UK or EU registered entity.
   CLAUDE.md doesn't state this. If there is a UK/EU entity, some of the "hard no" list may actually
   be open — worth a 5-minute confirmation before writing those off for good.

6. **Whose name goes on company-level (not founder-specific) awards?** Fast Company, BIG Innovation
   Awards, Fierce Healthcare, Digital Health Awards, MedTech Breakthrough are company/product
   submissions, not individual awards — draft language below uses Katerina as the quoted
   spokesperson (consistent with her being the public-facing CEO across LinkedIn/press) but confirm
   that's still correct, or if Whitney Cathcart (Co-founder & CCO) should be the named quote instead
   for any of them.

7. **Supporting assets.** Most of these programs allow or require attachments (logo, product
   screenshots, a demo video, customer quote/testimonial, executive headshot). None of that exists
   in this workspace folder — flagging so someone pulls the asset list together in parallel with
   essay review, rather than discovering it's missing at submission time.

8. **Frontmatter `product:` value for this artifact type.** CLAUDE.md §4 defines the enum as
   `fitxpress | mobile_tailor` only. These award drafts genuinely span both products (the company-level
   ones especially), so every file in this batch uses `product: mixed` as a working value. That's not
   an approved enum value today — confirm whether `mixed` should be formally added for award/PR
   artifacts, or whether each submission should be forced to pick a primary product lens instead.
