# Deep Generative Models — UPenn

Course website for **Deep Generative Models** at the University of Pennsylvania (Fall 2026), hosted at [vidal-lab.github.io/dgm](https://vidal-lab.github.io/dgm).

Built with [Jekyll](https://jekyllrb.com/) and deployed via GitHub Pages.

---

## Repository Structure

```
dgm/
├── _config.yml               # Jekyll site configuration (title, collections, theme)
├── Gemfile                   # Ruby gem dependencies (jekyll, github-pages)
│
├── index.md                  # Homepage
├── lectures.md               # Lectures listing page
├── assignments.md            # Assignments listing page
├── schedule.md               # Course schedule page
├── materials.md              # Course materials and prerequisites
├── project.md                # Final project page
│
├── _data/                    # YAML content and configuration data
│   ├── lectures.yml          # Master list of all lectures (date, title, topics)
│   ├── assignments.yml       # Assignment release dates and Canvas links
│   ├── events.yml            # Calendar events and due dates
│   ├── people.yml            # Instructor and TA profiles
│   ├── nav.yml               # Navigation menu items
│   ├── late_policy.yml       # Late submission policy
│   ├── projects.yml          # Final project information
│   └── previous_offering.yml # Links to previous course offerings
│
├── _lectures/                # Individual lecture markdown files (one per lecture)
│   ├── 01_introduction.md
│   ├── 02_mle.md
│   └── ...                   # 23 lectures total
│
├── _assignments/             # Individual assignment markdown files
│   ├── hw_01.md
│   └── hw_02.md
│
├── _announcements/           # Course announcements
│   └── 01_homework_policy.md
│
├── _layouts/                 # Jekyll HTML page templates
│   ├── default.html          # Base template (header/footer wrapper)
│   ├── home.html             # Homepage (description, team, announcements)
│   ├── lectures.html         # Lecture card grid
│   ├── assignments.html      # Assignment listings
│   ├── schedule.html         # Calendar/schedule view
│   ├── class.html            # Individual lecture page
│   ├── assignment.html       # Individual assignment page
│   └── page.html             # Generic page wrapper
│
├── _includes/                # Reusable Liquid template components
│   ├── head.html             # Meta tags, fonts, analytics
│   ├── header.html           # Site header and navigation bar
│   ├── footer.html           # Site footer
│   ├── nav.html              # Navigation menu (driven by _data/nav.yml)
│   ├── announcements.html    # Announcements display
│   ├── lecture_links.html    # Lecture resource links (slides, recordings)
│   ├── late_policy.html      # Late policy display
│   ├── embedpdf.html         # PDF viewer embed
│   ├── image.html            # Image rendering utility
│   └── schedule_row_*.html   # Row templates for each schedule event type
│
├── _sass/                    # SCSS source stylesheets
│   ├── _base.scss            # Typography and base styles
│   ├── _layout.scss          # Page layout and component styles
│   ├── _header.scss          # Header/nav styling
│   ├── _mobile-header.scss   # Responsive mobile header
│   ├── _user_vars.scss       # Color variables and theme settings
│   ├── _fancy-image.scss     # Image display effects
│   └── _syntax-highlighting.scss
│
├── _css/
│   └── main.css              # Compiled CSS output
│
├── _images/                  # Image assets
│   ├── logo.png / logo.svg   # Site logo
│   ├── cover1.jpg, cover2.jpg # Reference book covers
│   ├── pp/                   # Instructor and TA profile photos
│   └── screenshots/          # Site screenshot previews
│
├── static_files/             # Downloadable course materials
│   ├── lectures/             # PDF lecture slides (30+ files)
│   └── presentations/        # Presentation thumbnail images
│
├── scripts/                  # Automation scripts
│   ├── generate_schedule.py  # Generates _data/*.yml from a CSV schedule file
│   └── update_schedule.sh    # Bash wrapper for the Python script
│
└── _site/                    # Jekyll build output (auto-generated, not committed)
```

---

## How It Works

Content, templates, and data are separated:

- **Content pages** (`*.md`) declare their layout in YAML frontmatter and contain minimal markup.
- **`_data/` YAML files** drive dynamic content — the schedule, people list, and navigation are all pulled from these files by Liquid templates.
- **`_lectures/` and `_assignments/`** are Jekyll [collections](https://jekyllrb.com/docs/collections/); each file generates a standalone page at build time.
- **`_layouts/` and `_includes/`** are Liquid templates that render the above content into HTML.
- **`scripts/generate_schedule.py`** can regenerate `_data/lectures.yml`, `_data/assignments.yml`, and `_data/events.yml` from a CSV file when the schedule changes.

---

## Local Development

```bash
bundle install
bundle exec jekyll serve
```

The site will be available at `http://localhost:4000`.

---

## Course Topics

1. Probability fundamentals and MLE
2. Latent variable models: PPCA, Gaussian models
3. Variational inference and VAEs
4. Shallow models: HMMs, Markov models, Linear Dynamical Systems
5. Deep autoregressive models: RNNs, Attention, Transformers
6. BERT and Vision Transformers
7. Diffusion models: DDPM, DDIM, score matching, image editing

---

## Changelog

### 2026-08-25
- Fixed local `bundle install`/`jekyll serve` setup on macOS:
  - Added `vendor` to `_config.yml`'s `exclude` list so Jekyll doesn't try to build the installed gems as site content.
  - Added `faraday` (`~> 2.7`) and `faraday-net_http` to the `Gemfile` — the resolved `faraday 2.0.0` shipped without a usable default HTTP adapter, which broke `jekyll-github-metadata`/`jekyll-feed` locally.
- Archived the Fall 2025 offering as a standalone site at [vidal-lab.github.io/dgm-25](https://vidal-lab.github.io/dgm-25) (repo: `dgm-25`, `baseurl: /dgm-25`), and added it to `_data/previous_offering.yml`.
- Rolled this repo forward to **Fall 2026** (`course_semester` in `_config.yml`, and the README description); content updates (lectures, schedule, assignments) for the new semester are being made manually.
- Updated the teaching team in `_data/people.yml`: Uday Kiran Reddy Tadipatri (webpage now LinkedIn), Yuyan Ge, Buyun Liang, Nghia Nguyen, and Leandro Palma; removed prior TAs no longer on the course. Added their photos to `_images/pp/`.
- Homepage: removed the auto-generated "Updates" box's stale Fall 2025 content; the box now always renders (heading kept) but stays empty via a `show_updates` toggle in `_includes/announcements.html` until real Fall 2026 updates are ready. Updated the Canvas link in `index.md` to the new course (`1937189`).
- Schedule page (`_layouts/schedule.html`):
  - Hid Assignment/Due/Project rows from the table for now (only Lecture rows show); re-add `site.data.events`/`projects`/`assignments` to the concat to bring them back.
  - Updated Location to AGH 203 and added Semester Dates (8/25/2026 - 12/3/2026).
  - Replaced the stale per-TA office-hours rotation with updated Fall 2026 assignments (Prof. Vidal: Thu 5-5:45pm, AGH 609, starting 09/04; Yuyan & Leandro Fridays / Buyun & Nghia Tuesdays, AGH 615) and a contact note for extra office hours.
  - Added a gray "Fall Break" row (`_includes/schedule_row_break.html`, `.table-row-break` style) noting no classes Oct 1-4, and shifted all subsequent lecture dates one class later to account for it.
- Lectures: trimmed `_lectures/` and `_data/lectures.yml` down to just the first two sessions (Introduction, Background/MLE) for now, dated to the actual Fall 2026 Tue/Thu calendar; the remaining Fall 2025 lecture files and the original full schedule data are preserved (not deleted) under `develop/_lectures/` and `develop/lectures_fall2025_full.yml` for reuse later in the semester. Lecture 1's syllabus/slides now point at new `dgm26-*` PDFs; placeholder slide/recording links (where no Fall 2026 material exists yet) point at `/lectures/`.
- Assignments page: parked `hw_01.md`/`hw_02.md` under `develop/_assignments/` (not deleted) and set `assignments.md` to show "TBA" until new assignments are posted.
- Added a favicon (`_images/favicon.png`, cropped tightly to the Penn logo's content and padded to a square so it isn't stretched) via `_includes/head.html`.

---

## Acknowledgments

Portions of this repository's local development setup, documentation, and site maintenance were assisted by [Claude](https://claude.com/claude-code) (Anthropic).
