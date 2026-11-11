# Unmatched (board-game engine)

A pure-Python, framework-agnostic implementation of the core rules of the
[Unmatched](https://restorationgames.com/unmatched/) board game, intended to be
driven headlessly by tests, a bot AI, or a web backend (Django) — with a Next.js
frontend rendering the game state.

## Goals

- Faithful, testable implementation of the turn, combat, and card rules.
- A bot AI that can play 2–4 player games.
- Clean separation: engine (this repo) → Django backend → Next.js frontend.

## Layout

- `src/unmatched/` — the engine package (core, cards, game, ai, serialization)
- `tests/` — pytest suite mirroring the package

## Development

```bash
uv sync           # create venv + install dev tools
uv run pytest     # run tests
uv run ruff check .
uv run mypy src
```

## Roadmap

- M0 — project skeleton (this commit)
- M1 — board & fighters (zones, adjacency, movement)
- M2 — cards & decks (draw, hand limit, exhaustion)
- M3 — turn structure & actions
- M4 — combat resolution
- M5 — targeting (melee vs ranged)
- M6 — card effects & timing
- M7 — sidekicks & teams
- M8 — schemes & hero abilities
- M9 — heuristic bot AI
- M10 — persistence & replay
