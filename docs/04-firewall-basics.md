# 4. Firewall Basics

"Firewall" is a serious word for a simple idea: **decide who can knock on which doors.** Every main computer has one built in. Today, our whole firewall job is one sentence: *let family knocks through door 11434, keep the rest as-is.*

You don't need to become a network engineer. You need to pass exactly one allow-rule through and confirm nothing else changed.

## The one rule we're making

| What | Value |
|---|---|
| Direction | Incoming |
| Door (port) | **11434** (TCP) |
| Allowed | Only **private/LAN** connections — your own devices |
| Not allowed | Anything from outside your home |

When you restarted Ollama with `OLLAMA_HOST=0.0.0.0:11434`, it started *listening* at the family door. The firewall is the doorman who now politely blocks everyone from knocking, until you tell him it's the weekend and family's over.

## Do it — Windows

Windows usually makes this painless: when Ollama restarted, Windows Defender likely popped the dialog **"Windows Defender Firewall has blocked some features of Ollama"**:

1. Click **Allow access**.
2. Make sure the checkbox for **Private networks** is ticked, and **Public networks** is ticked **off** if offered as separate checkboxes (in recent Windows builds it's a single checkbox list — tick Home/Work "private," leave Public unchecked). *Private* is how Windows knows "family's Wi-Fi" vs. "coffee shop Wi-Fi."

To check or set it manually:

1. Start menu → type **"Allow an app through Windows Firewall"** → open it.
2. Scroll to **Ollama**. If it's there, make sure **Private** is ticked.
3. If it's missing: **Change settings** → **Allow another app** → browse to `C:\Users\<you>\AppData\Local\Programs\Ollama\ollama.exe` — though simpler by far: Settings → Firewall & network protection → **Allow an app through firewall**.

Also confirm your home Wi-Fi is marked **Private**, not **Public** (Settings → Network → your Wi-Fi → check the "Network profile type"). If it's Public, the firewall won't even let *family* through — the #1 silent cause of "phone can't connect."

## Do it — Mac

Good news: Apple's app-firewall is off by default for inbound app connections, and even when enabled, it typically merely prompts once per app ("Do you want Ollama to accept incoming connections?" → **Allow**).

Check where you stand: System Settings → Network → **Firewall**.

- If it's **off** — you're done; skip ahead. (Home Wi-Fi routers already provide outside protection; see below.)
- If it's **on** — set it to prompt, then when the Ollama dialog appears, choose **Allow**; or under Options, add Ollama with "Allow incoming connections."

## Do it — Linux

Depends on your distro; the two usual suspects:

```bash
# Ubuntu family — allow the app profile:
sudo ufw allow 11434/tcp
sudo ufw status

# Fedora family:
sudo firewall-cmd --add-port=11434/tcp --permanent
sudo firewall-cmd --reload
```

(If `ufw` says "inactive," your firewall isn't running and there's nothing to change.)

## "But what about outsiders?" — the router shield

Breathe easy: you did not just open the front door of your house to the internet. Here's why.

Your **router** does "network address translation": it only forwards connections that started *from inside* the house. A stranger on the internet can knock on your router's public door all day; without deliberate forwarding rules, those knocks go nowhere. The firewall setting you just changed only affects **inside-the-house** traffic — device-to-device on your own Wi-Fi.

| Ask | Answer |
|---|---|
| Can someone in the coffee shop boss my AI around? | No. Private addresses (`192.168…`) aren't reachable from outside. |
| What about the router's public door? | Closed unless you deliberately set up port forwarding. **Don't.** |
| Is door 11434 visible from a neighbor's house? | Only if they're on your Wi-Fi — which means they know your password, a different problem. |
| Do I need a VPN for this? | Not in this guide's design. A VPN is a great *later* upgrade when you want to use it away from home — see [page 6](06-when-this-is-a-bad-idea.html). |

## Checklist

- [ ] Firewall pop-up correctly answered (Private **yes**, Public **no**)
- [ ] Home Wi-Fi marked as a "Private" network (Windows folks especially)
- [ ] Test-connection from another device still works, after all firewall wrangling
- [ ] No port-forwarding or "DMZ" settings were touched in the router

Next stop: making it beautiful — [phone access](05-phone-access.html).
