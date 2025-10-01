# Contributing to BrainBurst

Thank you for your interest in contributing to BrainBurst.

## How to Contribute

### Adding Ideas

1. Edit `data/ideas.json` or `data/ideas.yaml`
2. Add your idea object to the array
3. Include required fields: `slug`, `title`, `category`, `description`, `content`
4. Write Markdown content inline using the `content` field
5. Test locally before submitting

Example JSON:

```json
[
  {
    "slug": "your-idea-slug",
    "title": "Your Idea Title",
    "category": "Technology",
    "description": "Brief one-line description",
    "content": "# Your Idea\n\n## Overview\n\nDetailed content here..."
  }
]
```

Example YAML (recommended for readability):

```yaml
- slug: your-idea-slug
  title: Your Idea Title
  category: Technology
  description: Brief one-line description
  content: |
    # Your Idea

    ## Overview

    Detailed content here...
```

### Adding Plans

1. Edit `data/plans.json` or `data/plans.yaml`
2. Add your plan object to the array
3. Include required fields: `slug`, `title`, `category`, `description`, `content`
4. Write roadmap or strategy in Markdown inline
5. Test locally before submitting

### Code Contributions

1. Leave a star ⭐ to the repository
2. Fork the repository
3. Create a feature branch
4. Make your changes
5. Run tests: `uv run python manage.py test`
6. Submit a pull request

## Content Guidelines

- Keep titles concise and descriptive
- Write clear, actionable descriptions
- Use proper Markdown formatting
- Include relevant sections in content files
- Avoid jargon unless necessary
- Proofread before submitting

## Categories

Ideas: Technology, Education, Health, Business, Sustainability, Social, Entertainment

Plans: Learning, Career, Business, Personal, Technical, Strategy

## Testing Locally

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py load_ideas
uv run python manage.py load_plans
uv run python manage.py runserver
```

Visit http://127.0.0.1:8000 and verify your content appears correctly.

## Pull Request Process

1. Update documentation if needed
2. Ensure all tests pass
3. Request review from maintainers
4. Address any feedback
5. Wait for approval and merge

## Questions

Open an issue for questions or clarifications before starting major contributions.
