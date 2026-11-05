# 1. What You Need First

Before you touch a single setting, let's make sure you have what you need. This page takes five minutes to read and saves you an hour of head-scratching later.

## Hardware

**The main computer.** This is the machine that will actually run the AI — the workhorse. It lives in one spot and does its job while other devices talk to it. Any of these works:

- A desktop or laptop you leave plugged in
- A spare laptop from a few years ago (this is genuinely a great use for one)
- A small desktop PC in a corner

What matters most, in order:

1. **RAM — 16 GB is the comfortable minimum.** The AI model lives in RAM while it runs. 8 GB can work for small models, but 16 GB gives the family a model that actually sounds smart. 32 GB is luxury.
2. ** Anything with Apple silicon (M1 or newer)** works great, as does a Windows/Linux PC with a decent graphics card.
3. **It must stay on.** If the main computer sleeps, the family AI goes with it. Plan for its power settings to allow "never sleep while plugged in" — we cover exactly where that setting is on setup day.

**The other devices.** Family laptops, phones, tablets — if they can open a web page, they can use your shared AI. Nothing to install on most of them.

## Software and counts

| You need | Why |
|---|---|
| **Ollama** (free) — we install it on the main computer, page 2 | The program that runs the AI |
| **Ollama version 0.1.24 or newer** | Older versions simply can't accept connections from other devices. Anything from roughly mid-2024 onward is fine; if you installed Ollama in the last couple of years, you're set. |
| One internet connection **during setup only** | To download Ollama and the AI model. After that, the AI works with no internet at all. |

> **A moment on that last point, because it surprises people:** once the model is downloaded, this whole setup runs without internet. Power cut? Internet cut? As long as your Wi-Fi/router is up, your family AI is up. That's the "local-first" promise, and it's worth the one-time download.

## Two jargon words, gently

You only need two pieces of network vocabulary today. The [glossary](glossary.html) has more, but these two show up constantly:

**IP address** — a number like `192.168.1.42` that identifies one device on your home network. Think "house number." Your main computer has one; it's how the other devices will find it.

**Port** — a specific "door" on one computer. Ollama uses door **11434**. When we "share the AI," we mean: let other devices knock on door 11434 of the main computer. It sounds like sci-fi; it's just plumbing.

## Sanity check before you continue

- [ ] Pick the main computer and confirm it has 16 GB of RAM or close to it (on Windows: Settings → System → About. On Mac: About This Mac. On Linux: `free -h`.)
- [ ] Know the main computer's admin password — we'll touch a firewall setting.
- [ ] All the family devices are on the **same Wi-Fi network** at home. (Not cellular data, not a relative's Wi-Fi — same network.)

All three checked? On to [installing Ollama](02-run-ollama-on-the-main-computer.html).
