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

---

## Acknowledgments

Portions of this repository's local development setup, documentation, and site maintenance were assisted by [Claude](https://claude.com/claude-code) (Anthropic).
