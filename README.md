# BrainBurst

Community-driven idea builder for projects, goals, and future plans.

## Quick Start

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py load_ideas
uv run python manage.py load_plans
uv run python manage.py runserver
```

Visit http://127.0.0.1:8000

## Features

- Full-screen hero homepage
- Ideas: Browse and contribute project concepts
- Plans: Share roadmaps, goals, and future strategies
- Multi-format support: JSON, YAML, TOML with Markdown content
- Slug-based individual pages for all content

## Structure

```
brainburst/
├── data/
│   ├── ideas.json      # Array of idea objects
│   ├── ideas.yaml      # Array of idea objects (alternative)
│   ├── plans.json      # Array of plan objects
│   └── plans.yaml      # Array of plan objects (alternative)
├── builder/            # Main Django app
├── templates/          # Tailwind UI templates
└── brainburst/         # Project settings
```

## Adding Content

Edit `data/ideas.json` or `data/ideas.yaml` to add new ideas:

```json
[
  {
    "slug": "mobile-app",
    "title": "Mobile Learning Platform",
    "category": "Education",
    "description": "Brief overview",
    "content": "# Full Markdown Content\n\n## Section\n\nYour detailed content here..."
  }
]
```

Or use YAML for better readability:

```yaml
- slug: mobile-app
  title: Mobile Learning Platform
  category: Education
  description: Brief overview
  content: |
    # Full Markdown Content

    ## Section

    Your detailed content here...
```

Load into database:

```bash
uv run python manage.py load_ideas
uv run python manage.py load_plans
```

Existing entries are automatically skipped.

## Testing

```bash
uv run python manage.py test
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT
