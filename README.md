# CASE-FRAMEWORK

## Case Study Framework

All case studies in this portfolio are developed using a consistent UX framework that emphasizes:

- Human-centered design
- Research-backed decision making
- Real-world operational constraints
- Accessibility and clarity
- Ethical responsibility

Each case study documents:
- Problem framing
- Research and competitive analysis
- User flows and wireframes
- Design rationale
- Reflection and learnings

This approach reflects how I think, not just what I design.

## Master System PDF

The `generate_master_system_pdf.py` script generates a comprehensive PDF document that includes:

- **Master Prompt (v1)**: Foundational structured prompt for building UX case studies
- **Master Prompt v2A — UX-Heavy Variant**: Design-forward variant prioritizing flows, wireframes, and interaction
- **Master Prompt v2B — Research-Heavy Variant**: Research-driven variant emphasizing systems thinking and strategy
- **Canva Master Template Specification**: Standardized slide structure and visual guidelines
- **Case Study Intake Checklist**: Pre-project checklist for clarity and focus
- **Portfolio / GitHub README Attachment**: Reusable README block explaining the framework
- **System Usage & Versioning Guide**: Instructions for maintaining and evolving the Master System

### Usage

```bash
pip install -r requirements.txt
python3 generate_master_system_pdf.py
```

The PDF will be generated at `/mnt/data/UI_UX_Case_Study_Master_System_v1.pdf`.

## Tech Badge Assets

The `extract_badge_assets.py` script extracts the Tech Badge design assets from a ZIP archive.

### Usage

Place the `Design Concept for Tech Badge.zip` file in `/mnt/data/`, then run:

```bash
python3 extract_badge_assets.py
```

The badge assets will be extracted to `/mnt/data/badge_assets/`.
