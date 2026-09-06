# Daily TIL Bot

Automates a daily commit that assigns you one DSA/backend problem to work
through, logged in `TIL.md`. It rotates through `data/problems.json` in
order, one per day, and tracks progress in `data/state.json`.

This is **not** a fake-commit generator — it commits a real, checkable
assignment each day. Solving it and filling in your notes is on you, and
that part is genuine work you can point to.

## Setup (5 minutes)

1. Create a new (or reuse an existing) GitHub repo, e.g. `daily-til`.
2. Copy all files in this folder into that repo, preserving the folder
   structure (`.github/workflows/daily-til.yml` must stay at that exact path).
3. Push to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: daily TIL bot"
   git branch -M main
   git remote add origin https://github.com/<your-username>/daily-til.git
   git push -u origin main
   ```
4. On GitHub, go to **Settings → Actions → General → Workflow permissions**
   and select **"Read and write permissions"**. This lets the workflow's
   default `GITHUB_TOKEN` push commits back to the repo.
5. Go to the **Actions** tab, open "Daily TIL", and click **"Run workflow"**
   once to test it manually. Confirm a new entry appears in `TIL.md` and a
   commit shows up.

That's it — after that it runs automatically every day at the scheduled
time (12:00 UTC / 5:00 PM PKT by default).

## Customizing

- **Change the time**: edit the `cron` line in
  `.github/workflows/daily-til.yml`. Cron is in UTC.
  (e.g. `0 3 * * *` = 8:00 AM PKT)
- **Add more problems**: append entries to `data/problems.json` in the same
  `{"topic", "title", "link"}` format. The rotation just keeps going.
- **Different content entirely**: edit `scripts/daily_til.py` — it's a
  plain Python script, easy to point at a different data source.

## A note on GitHub streaks

This keeps your graph active with real, inspectable content (a logged
problem + a place for your notes) rather than empty or meaningless
commits. It won't make your streak "look good" if you never actually
solve any of the problems — but it will give you a low-friction daily
nudge and a visible log of practice if you do.
