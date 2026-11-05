# Glossary

Plain-English meanings of every technical word used in this manual. No prior degree required; ask the family AI for further explanation — it owes you.

**Airplane mode** — a phone switch that turns off all its radios. In this manual's favorite test, you flip it on *and then re-enable Wi-Fi only*, proving your chat works without a live internet connection.

**ChatterUI** — a free, open-source Android app for chatting with an AI server. Our pick for Android phones.

**Chat history** — the record of conversations. On this setup, stored on your main computer, inside your house. Not on a company's servers, not in "the cloud."

**Firewall** — software (built into your computer) that decides which outside computers can knock on which of its doors. The doorman.

**IP address** — the "house number" that identifies one device on a network, like `192.168.1.42`. Written this way only inside homes; every home's numbers are independent of every other's.

**LAN** — **L**ocal **A**rea **N**etwork: the bubble of devices in your home, connected by your router's Wi-Fi or cables. "On the LAN" = "inside this bubble."

**LLM** — **L**arge **L**anguage **M**odel: the kind of AI that chats. On your setup, the friendly chatter is a model running in your main computer's RAM.

**localhost** — network-speak for "this same computer." `http://localhost:11434` on the main computer means "my own door 11434." Phones can't use `localhost` to reach *your* AI — they must use the main computer's IP address.

**Model** — the AI's "brain files." Downloaded once (several GB) and loaded into memory when needed. Examples in this guide: `llama3.1:8b` (family favorite), `phi3` (small-but-clever).

**Ollama** — the free program that runs models on your computer. The engine room.

**OLLAMA_HOST** — a setting controlling which doors Ollama listens behind. `0.0.0.0:11434` means "all of them, family, knock away."

**OLLAMA_ORIGINS** — a setting controlling which web apps may talk to Ollama. `*` means "any app on our network."

**Parameters (in a model name like `8b`)** — a rough measure of brain size. `8b` = 8 billion parameters — the household sweet spot of capable-but-fits-in-RAM.

**Port** — a numbered "door" on a computer that network traffic can knock on. Ollama's is **11434**.

**Private network (two senses)** — (1) an address starting `192.168.`, `10.`, or `172.16`–`172.31` — only real inside your home; (2) on Windows, its label for "a network you trust, like your home Wi-Fi" — as opposed to *Public*, for coffee shops. Windows won't let family traffic through until your home Wi-Fi is marked Private, a top-3 silent failure.

**RAM** — a computer's short-term working memory. The AI model lives here while chatting. 16 GB comfortable, 8 GB cozy-small.

**Reins** — a free iPhone app for chatting with an Ollama server. Our iOS pick.

**Router** — the box that hands out IP addresses in your home and keeps the outside world from wandering in. The building's front desk and lock, in one.

**Server** — in this manual: any computer that *answers knocks* rather than only making them. Your main computer becomes a small, home-only server. It doesn't need to be fancy.

**Static lease** — a router setting that permanently ties a name (or a fixed address) to your main computer, so its IP never changes after a restart. The cure for troubleshooting-row 4. Later-upgrade material.

**Tailscale** — a free private-network service that makes remote devices act as if they're home. Mentioned on [page 6](06-when-this-is-a-bad-idea.html) as the adult upgrade path — a fine separate project, deliberately not part of this one.

**WAN** — the internet side of your router. Everything "outside the building." This setup deliberately leaves the WAN door un-touched.

Updated by and for readers of the household AI project — *AI explained like a friend would*, by [Asdale Dynamics, LLC](https://dylanasdale.github.io).
