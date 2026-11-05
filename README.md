# Share Your Local AI — One Household Manual

Run AI entirely inside your house: **Ollama on one main computer**, opened safely to the rest of the family's phones, tablets, and laptops over your own Wi-Fi. No cloud, no accounts, nothing uploaded — an AI your household shares the way it shares a printer.

**Who it's for:** beginners who can follow instructions but have never typed "IP address" without flinching. If you want an AI that works even when the internet doesn't, and you'd rather your family's questions never leave the building, this manual was written exactly for you.

## What's inside

The guide lives in [`docs/`](docs/) — ten short pages, one afternoon:

- **[Start here](docs/index.md)** — what this is, how to use it
- **[1. What you need](docs/01-what-you-need.md)** — hardware and gentle jargon
- **[2. Install Ollama](docs/02-run-ollama-on-the-main-computer.md)** — prove the AI works *before* sharing it
- **[3. Open to family](docs/03-open-it-to-your-network.md)** — plain-English networking, step by step
- **[4. Firewall basics](docs/04-firewall-basics.md)** — one door open, the rest shut
- **[5. Phones](docs/05-phone-access.md)** — free apps and home-screen shortcuts
- **[6. When this is a bad idea](docs/06-when-this-is-a-bad-idea.md)** — the honest limits page
- **[Setup day checklist](docs/setup-day-checklist.md)** — printable, tick-the-boxes
- **[Troubleshooting](docs/troubleshooting.md)** — the usual suspects, their fixes
- **[Glossary](docs/glossary.md)** — every word, explained like a friend would

## Build the website

The Markdown manual doubles as a static HTML site — a small dependency-light build script turns it into `site/`:

```bash
./build.sh
```

Then open `site/index.html` in a browser, or serve it locally:

```bash
python3 -m http.server 8000 --directory site
```

and visit <http://localhost:8000>. Everything renders and works offline.

**Requirements:** Python 3 with the [`markdown`](https://pypi.org/project/markdown/) package (`pip install markdown`) and `bash`. No network access is needed at build time.

## Where this fits

A deliberate niche, so it doesn't step on its neighbors' toes:

- It is **not** a general self-homelab guide (Docker, VLANs, domains — a *homelab self-hosting* guide covers that).
- It is **not** "get started with local AI on one machine" (a *local AI handbook* covers that).
- It is exactly the middle: **one household, one main computer, several friendly devices.**

## Safe by design

Every recommendation keeps traffic inside your home network. The guide teaches you to open exactly one door (port 11434) to LAN-only traffic, explains why nothing is exposed to the internet, and includes a dedicated page on when this setup is the wrong tool — including dorms, shared networks, and anything a professional should handle instead.

**Educational content only** — never medical, legal, or security advice.

## License

MIT — see [`LICENSE`](LICENSE).

Copyright (c) 2026 Asdale Dynamics, LLC. This guide is part of [Asdale Dynamics, LLC](https://dylanasdale.github.io)'s beginner-friendly AI library — AI explained like a friend would, in *The Massive AI Manual* and beyond.
