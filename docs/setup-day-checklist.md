# Setup Day Checklist

This is the printable version of the whole manual — every step in order, tick-box ready. Print it or keep it open on a device other than the main computer (you'll see why). Estimated time: **stroll = 90 minutes, brisk = 45**.

Work top-to-bottom. If a box won't tick, don't push forward — the [troubleshooting table](troubleshooting.html) is on standby.

## Phase 1 — Prepare (10 min)

- [ ] Main computer picked: 16 GB RAM-ish, plugged in, in its corner
- [ ] Power set: **never sleep while plugged in** ([exact spots](02-run-ollama-on-the-main-computer.html#one-setting-to-change-now))
- [ ] Main computer elsewhere-employee-free: no other big jobs running today
- [ ] Home Wi-Fi confirmed reachable from main computer **and** a second device (like your phone)
- [ ] This checklist open on the second device

## Phase 2 — Install the engine (20–40 min, download time)

- [ ] Ollama installed from <https://ollama.com/download>
- [ ] Menu bar / system tray llama icon present
- [ ] Model downloaded via `ollama pull llama3.1:8b` (5 GB; or `phi3` if the machine is weak)
- [ ] Terminal test: `ollama run llama3.1:8b` → chat works → `/bye`

## Phase 3 — Prove it works *before* sharing (5 min)

- [ ] Main computer's browser: `http://localhost:11434` → "Ollama is running"

## Phase 4 — Write down the family AI's address (2 min)

- [ ] IP address found ([how](03-open-it-to-your-network.html#step-1-find-the-main-computers-address)) and written down, e.g. `192.168.1.42`
- [ ] Address tested from the other device, **failure at this stage is normal** — the next phase fixes it

## Phase 5 — Open the door (10 min)

- [ ] `OLLAMA_HOST=0.0.0.0:11434` set ([per-system commands](03-open-it-to-your-network.html#step-2-tell-ollama-to-accept-knocks))
- [ ] `OLLAMA_ORIGINS='*'` set
- [ ] Ollama **fully quit and restarted** (tray icon — the number-one miss)
- [ ] Firewall: Ollama **Allow** on **Private** networks ([details](04-firewall-basics.html))
- [ ] Windows folks: home Wi-Fi marked **Private** in Settings → Network

## Phase 6 — The moment (5 min)

- [ ] Other device's browser: `http://192.168.1.42:11434` → **"Ollama is running"** 🎉
- [ ] Terminal on family laptop (optional double-check): `ollama run llama3.1:8b` path works too

## Phase 7 — Phones in the wild (15 min)

- [ ] Chat app installed on phone (Reins on iPhone, ChatterUI on Android, [page 5](05-phone-access.html))
- [ ] Server address entered → test message → friendly answer
- [ ] Address → **Add to Home Screen**, so the family never types numbers again
- [ ] Airplane-mode-with-Wi-Fi test → chat survives → *proof it's local*

## Phase 8 — Family rollout (10 min)

- [ ] Each family device: same app, same address, same five minutes
- [ ] Show the family how it works — person-to-person beats a memo
- [ ] "Family corkboard" norms set (shared machine = no truly private secrets, [agreed](06-when-this-is-a-bad-idea.html))
- [ ] **Bookmark this page** — it's the rebuild map. A second setup day (new router, new computer) takes half the time

## If the main computer will be replaced some day

Keep two numbers: the model name (`llama3.1:8b`) and this page title. Follow the phases again on the new machine — half the boxes tick themselves, because the family devices just need the *new* address in their app settings.

*Built by [Asdale Dynamics, LLC](https://dylanasdale.github.io) — AI explained like a friend would.*
