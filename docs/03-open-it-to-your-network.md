# 3. Open It to Your Family's Devices

This is the page where "an AI on one computer" becomes "the family AI." Take it slow — this page does the real work of the whole manual, and five careful minutes beat an evening of guesswork.

## Plain-English networking, briefly

Picture your home network as an apartment building. Every device is an apartment with a number on the door — its **IP address**. The router decides who lives where. Inside the building, everyone can knock on everyone's door without going through the street.

Your setup will look like this:

```
        Your home Wi-Fi — the apartment building
   ┌──────────────────────────────────────────────────┐
   │                                                  │
   │  Main computer: 192.168.1.42, door 11434  ⭐      │
   │    (Ollama lives here and answers knocks)        │
   │                                                  │
   │  Family laptop: 192.168.1.51   → knocks ⭐        │
   │  Kid's tablet:  192.168.1.63   → knocks ⭐        │
   │  Your phone:    192.168.1.77   → knocks ⭐        │
   │                                                  │
   └──────────────────────────────────────────────────┘
        Outside world (the internet): sees NOTHING new
```

Two facts worth keeping in your pocket:

1. Addresses starting `192.168.` (also `10.` and `172.16.`–`172.31.`) are **private** — they only exist inside your home. The router hands them out. Nobody outside can dial `192.168.1.42` from a coffee shop; to the outside world your home is one rented address, and nothing we do here exposes the inside rooms.
2. By default, Ollama answers knocks **only from the same computer**. That's a sensible default we're now choosing to widen — deliberately, on our terms.

## Step 1 — find the main computer's address

On the main computer:

- **Windows:** Settings → Wi-Fi (or Ethernet) → Properties. Look for **IPv4 address** — something like `192.168.1.42`. (Or press Win+R, type `cmd`, then `ipconfig` and read the IPv4 line.)
- **Mac:** System Settings → Network → your connection → Details. (Terminal alternative: `ipconfig getifaddr en0`.)
- **Linux:** run `hostname -I` in a terminal.

**Write it down.** Something like `192.168.1.42`. This is *the number for the family AI*, like your street address for pizza delivery.

## Step 2 — tell Ollama to accept knocks

Ollama listens to two settings:

- **OLLAMA_HOST** — which doors to listen behind. Default `127.0.0.1:11434` means "only this computer." Change it to `0.0.0.0:11434` — `0.0.0.0` means "listen on all doors, accept family knocks."
- **OLLAMA_ORIGINS** — which web *apps* may call it. Default is local pages only. We'll set it so the phone/tablet apps (which use URLs and app pages) and simple browser apps can talk to it. For a household LAN, `*` (meaning "any app page") is the standard pragmatic choice — what data could these pages reach, after all? They're inside your walls. If the phrase `*` gives you pause, [page 6](06-when-this-is-a-bad-idea.html) discusses tightening it.

How to set them, per system:

**Mac or Linux (one-time try, in a terminal):**

```bash
export OLLAMA_HOST=0.0.0.0:11434
export OLLAMA_ORIGINS='*'
ollama serve
```

Keep that window open for the test; if it works, make it permanent:

```bash
# Mac/Linux — add the two export lines to ~/.bashrc or ~/.zshrc,
# or set them as launchd/systemd environment variables for Ollama.
```

**Windows (per-user, set-and-forget):**

```powershell
setx OLLAMA_HOST 0.0.0.0:11434
setx OLLAMA_ORIGINS *
```

Then **quit Ollama from the system tray and start it again** (setx only applies to *new* programs — the llama icon must be restarted).

> **The 90% of all troubleshooting in one sentence:** if a setting doesn't seem to take effect, it's almost always because the running Ollama needs a full quit-and-restart. Close the tray icon, reopen the app.

## Step 3 — open the one firewall door

Full details live on the next page; here's the quick version so you can test immediately. On the main computer, allow incoming connections on port 11434 (Windows will likely pop a firewall prompt when Ollama restarts — click **Allow** for **Private networks**).

## Step 4 — test from *another* device

This is the moment. On a **phone or family laptop** (whatever's handy, main computer excluded), open a browser and go to:

```
http://192.168.1.42:11434
```

— with **your** address from step 1, obviously.

If you see "Ollama is running," the family AI has officially left the nest. If not, the [troubleshooting table](troubleshooting.html) is built for this exact moment — the two most common causes are *Ollama wasn't restarted* and *firewall said no*.

## Checkpoint

- [ ] Main computer's IP address written down (e.g. `192.168.1.42`)
- [ ] `OLLAMA_HOST` and `OLLAMA_ORIGINS` set, Ollama **fully restarted**
- [ ] `http://192.168.1.42:11434` reachable from a phone or other laptop
- [ ] Same Wi-Fi on every device that needs it

Ready for the door-keeping details? That's [firewall basics](04-firewall-basics.html).
