# 5. Phone Access

Phones and tablets are where this setup earns its keep: it *feels* special to ask your household its own AI from the couch, and it happens nowhere but inside your walls. This page is short on theory and long on do-it.

## The plumbing intuition

A phone on Wi-Fi is just another device inside the building. It can't run big AI models itself — but it doesn't need to. It **knocks on the same door** as the laptop, and the main computer mutters an answer that shows up right there on the couch.

One address gets you everything:

```
http://192.168.1.42:11434
```

(your own address from [page 3](03-open-it-to-your-network.html), `Settings app → that address.)

## The easy way: a free chat app

The `:11434` page itself is tiny (just "Ollama is running") — it's the *engine room*, not the living room. For a real chat surface, point a chat app at the engine room. Good free options, no accounts required:

**iPhone/iPad:**

- **Reins** (App Store) — clean, minimal, made for talking to Ollama servers.
- Or any app that lets you set a "server URL" to `http://192.168.1.42:11434`.

**Android:**

- **ChatterUI** — open-source, no account, "Remote (Online)" mode pointed at `http://192.168.1.42:11434` works out of the box.

**Either phone, via phone browser:** open `http://192.168.1.42:11434` in Chrome/Safari — some Ollama-aware browser tools and notepads found in browser stores can use that URL directly.

Setup pattern is identical in every app: look for **"server"** or **"remote"** or **"API endpoint,"** enter the address, save, and send a test message like *"What's your favorite number?"*

## Make it feel like an app: home-screen shortcut

You don't need to type that number ever again after once.

- **iPhone (Safari):** address → Share icon → **Add to Home Screen**. Instant icon, one tap away.
- **Android (Chrome):** address → ⋮ menu → **Add to Home screen**.

Think "the family AI as an app icon" — with zero app-store hunting, and uninstalling is as trivial as deleting the icon.

## Why phones *particularly* benefit from this

Your remote workmate asked an interesting question about phone battery: it's easier than you'd think — the whole burden of thought sits on the main computer, and the phone is a lightweight keyboard + screen. Works basically great even on older phones, since the phone never computes the answer itself.

Battery cost: negligible. Data usage: none — same wall, same house.

## Test, gently

Against your phone, after entering the address:

1. Chat works (send a simple message; see a friendly reply).
2. Turn **off cellular data only** (Airplane mode with Wi-Fi re-enabled) — chat still works. That's your proof-call it local.
3. Add the home-screen icon; name it something the family will recognize.

## Where you'll see it fail (and fixes exist)

| Symptom | Usually means |
|---|---|
| App says "connection refused" / error on save | Firewall door still closed, or Ollama not restarted → back to [the table](troubleshooting.html) |
| Works on Wi-Fi, breaks away from home | Expected — see [when it's a bad idea / away from home](06-when-this-is-a-bad-idea.html) |
| "Address not found" from the app | Typo'd the IP, or a leading `https://` where there should be `http://` (no s!) |

Once you've got family devices chatting painlessly, the last page is the honest one: [when this is a bad idea](06-when-this-is-a-bad-idea.html).
