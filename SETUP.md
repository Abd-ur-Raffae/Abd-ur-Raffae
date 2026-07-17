# 🚀 Setup Guide — Profile README

This bundle turns your GitHub profile into a polished, auto-updating landing page.

## 1. Create the special repo
On GitHub, create a **public** repository whose name is **exactly your username**
(e.g. if you're `usman-qa`, the repo must be `usman-qa/usman-qa`). GitHub renders
its `README.md` on your profile automatically.

## 2. Add these files
Copy the bundle into the repo, keeping the structure:

```
README.md
quotes.json
SETUP.md
scripts/
  └── update_quote.py
.github/
  └── workflows/
        ├── daily-quote.yml
        └── snake.yml
```

## 3. Replace the placeholders
Open `README.md` and swap every `{{...}}` token:

| Placeholder            | Replace with                                  |
|------------------------|-----------------------------------------------|
| `{{YOUR_NAME}}`        | Your display name                             |
| `{{GITHUB_USERNAME}}`  | Your GitHub handle (used by stats & snake)    |
| `{{LINKEDIN_URL}}`     | Full LinkedIn profile URL                     |
| `{{EMAIL}}`            | Contact email                                 |
| `{{PORTFOLIO_URL}}`    | Portfolio / personal site                     |
| `{{TWITTER_URL}}`      | X / Twitter profile URL                       |
| `{{WHAT_YOU_ARE_LEARNING}}`, `{{A_FUN_FACT}}` | Your own text            |

> Tip: in VS Code press `Ctrl/Cmd + Shift + H` and find-replace each token in one go.

## 4. Fill your "About Me"
Everything between `<!-- SELF-REPRESENTATION:START -->` and
`<!-- SELF-REPRESENTATION:END -->` is yours. Rewrite freely — the markers are
just comments and won't show on GitHub.

## 5. Enable the automations
- Push the files. Go to the repo's **Actions** tab and enable workflows if prompted.
- **Daily quote:** runs at 00:15 UTC daily. Trigger it once manually
  (Actions → *Daily Dev & QA Quote* → *Run workflow*) to confirm it commits.
- **Snake animation:** runs on push + daily. After its first successful run it
  creates an `output` branch that serves `snake.svg`. The image in the README
  will start showing once that branch exists.

## 6. Adding new skills later
The tech-stack section uses [shields.io](https://shields.io) badges. To add one:

```md
![Tool](https://img.shields.io/badge/Tool%20Name-HEXCOLOR?style=for-the-badge&logo=SIMPLEICON&logoColor=white)
```

Find the right `logo=` slug at https://simpleicons.org.

## 7. Adding new quotes
Append objects to `quotes.json`:

```json
{ "quote": "Your quote here", "author": "Someone" }
```

The daily job rotates through the whole list automatically — no other changes needed.

---
Enjoy your new profile! 🎉
