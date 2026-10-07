# Online Fraud Fighter Team — Blog Bot

Generates up to 50 crypto-fraud educational blog **drafts per day** with GitHub Actions.

## Setup
1. Copy this project into your website repository.
2. Add GitHub Actions secret `OPENAI_API_KEY`.
3. Optionally add repository variable `BLOG_DAILY_LIMIT` (1–50; default 50).
4. Run **Blog Bot — Generate** manually or wait for the daily schedule.
5. Review drafts. Change `status: draft` to `status: approved` for posts you want published.
6. Run **Blog Bot — Publish Approved**.

The bot is deliberately approval-first: mass-producing thin pages can hurt search visibility. It checks duplicates, length, and basic safety requirements.

Never place API keys in website files. Never publish seed phrases, private keys, passwords, authentication codes, fabricated testimonials, guaranteed recovery claims, or instructions for hacking/unauthorized access.
