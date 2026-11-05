# 2. Run Ollama on the Main Computer

Golden rule of sharing anything: **prove it works for you before you share it.** We'll get the AI running on the main computer only, first. No network settings yet — that's the next page, and that's deliberate.

## Install Ollama

Go to <https://ollama.com/download> on the main computer and grab the installer for its system:

- **Windows / Mac:** download and run the installer like any app. Double-click, next, done. Ollama starts automatically afterward — you'll see a small icon (a llama silhouette) in the menu bar or system tray.
- **Linux:** one command in a terminal:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## Download a model

Ollama is the engine; a **model** is what makes the engine talk. Download one, family-sized:

```bash
ollama pull llama3.1:8b
```

That's about 5 GB and takes a while — good moment for tea. (If the main computer has less RAM than we hoped, `ollama pull phi3` is a small-but-clever alternative near 2 GB.)

> **Why 8 billion parameters?** It's the sweet spot for a shared household AI: smart enough to be genuinely useful, small enough to run while Aunt Karen is also asking a question. Bigger models are possible later; start here.

## Test it — keyboard first

In a terminal or command window on the main computer:

```bash
ollama run llama3.1:8b
```

You'll get a `>>>` prompt. Ask it something friendly:

```
>>> Say hello and tell me what you are in one sentence.
```

If a sentence wanders back out — **congratulations, you have local AI.** Nothing was uploaded to anyone. Type `/bye` to leave.

## Test it — the browser

Ollama quietly includes a web chat page. On the **main computer** open:

```
http://localhost:11434
```

You should see a short "Ollama is running" message. Right now it says very little — that's fine and *expected*. We're not testing the chat yet; we're proving the engine is awake. `localhost` means "this same computer," so if this works, the engine is confirmed running.

## Prove it stays local (optional but satisfying)

Keep curiosity humble; with the AI running, try asking it about something you just typed with the internet router **unplugged**. It'll answer fine. That's the whole selling point of local AI in one trick: turn your Wi-Fi off and it still works.

## One setting to change now

On the main computer, keep it awake while plugged in — otherwise the "family AI" hibernates the moment somebody walks away:

- **Windows:** Settings → System → Power → change "Put my device to sleep (plugged in)" to **Never**.
- **Mac:** System Settings → Displays → Advanced → enable **Prevent automatic sleeping when the display is off** (and uncheck "Put hard disks to sleep").
- **Linux:** in your desktop's Power settings, disable automatic sleep on AC power.

Done correctly, nothing changes about how you use that computer day to day — the screen still sleeps, only the *computer* stays awake underneath.

## Checkpoint

- [ ] Ollama installed and its icon appears in menu bar/system tray
- [ ] `ollama run llama3.1:8b` chats with you
- [ ] `http://localhost:11434` shows "Ollama is running" in the browser **on this same computer**
- [ ] Main computer no longer auto-sleeps while plugged in

Everything green? Now the part you actually came for: [opening it to the family](03-open-it-to-your-network.html).
