# 6. When This Is a Bad Idea

Most guides talk up their setup until the last paragraph. Let's do the opposite, because the plain truth is: this setup is *great* for some things and *actively wrong* for a few. Knowing the difference is the most useful skill on these ten pages.

## The one-line character of this setup

<blockquote style="border-left:4px solid #C8A24B;padding:0.5rem 1rem;margin:1rem 0;font-style:italic;">Fast, private answers for family members, inside one house, on one machine, over one Wi-Fi — as long as every device that wants it is under that same roof.</blockquote>

Everything on the "bad idea" list falls out of that sentence.

## When it's the wrong shape

**Anyone needs to use it away from home.** The address `192.168.1.42` only means something under your roof. On cellular data or the cabin's Wi-Fi, the phone can't reach it. Options, in order of sanity:

1. Don't solve this yet — a shared cloud-chat or a laptop that travels covers rare cases.
2. If it's now a *real* recurring need, learn about **Tailscale** — a free, reputable private-network tool that makes each family device act "at home" from anywhere, with no router fiddling and no exposed doors. That's a proper project for another day, with its own checklist; it's the adult version of this setup, not a loophole to sneak an open port onto the internet.

**The model needs to be top-tier.** A household computer runs friendly-and-smart, not frontier-genius. If a task genuinely needs the very best reasoning a company can train, this won't be it. Treat the family AI as the daily driver — for drafting, homework sanity checks, recipe swaps, "who's Oppenheimer" — and keep a cloud service in your back pocket for heavy-lift occasions.

**Big, fast household.** If three people hammer questions *while a fourth runs the main computer for gaming*, the machine will feel slow. One main computer serves a small household well; it is not a server farm.

**It's the family secret-keeper.** Please read this twice: **local means stored-at-home, not "truth serum."** An AI on your network still answers questions about medical symptoms with *general information* — it is never a doctor, and never a substitute for one. Dylan's nursing years put it plainly: general information about "when to worry about a fever" is fine and helpful; "should Uncle Chuck skip his meds" is a phone call to a pharmacist. Education, never advice — the model agrees eagerly, which is exactly why you must be the adult in that room.

## When the *neighborhood* is the risk

Private-address physics protect you from the internet, **not from your own Wi-Fi**. Anyone with your Wi-Fi password can reach the family AI's door:

- A guest Willy with your Wi-Fi password could chat to it (usually harmless — but it's *your* machine that computes, and conversations sit in the main computer's files where family reads them).
- A snooping kid could look through past chats of the whole family. Fine for recipes; uncomfortable for someone's health questions.

Practical guidance: chats on your own machine are roughly as private as *drawings on the family corkboard*. Anyone inside the house can peek; nobody outside can even see the corkboard. Set household norms accordingly — ask family members to keep truly private stuff out of the shared corkboard on a shared machine, exactly like everybody already does at home.

**Shared apartments/dorms:** if your "network" is a landlord's or university's network, it isn't *your* building — pause and read this section again. Some shared networks quarantine devices; in others every tenant is a "family member" you didn't choose. Bad fit; keep Ollama to `localhost` there.

## When the *skill level* outgrows it

A good rule: **things that worked during setup week will go on working, until something changes.** Change comes from router replacement, a new device you didn't set up, a "helpful" security app, or Windows updates that re-mark your Wi-Fi as Public. When the family reports it broke overnight, the [troubleshooting table](troubleshooting.html) first row is the answer 80% of the time.

Grow-up-the-stack moment: if you find yourself wanting user accounts with separate chat histories, access from genuinely remote locations, or *several* main computers, you've outgrown a beginner household setup. That's the moment to graduate to the *homelab* style of guide — with proper accounts, networks segmented off, and a weekend or two of tinkering budget. This manual's job is to be good enough that *not* being that is a calm, informed choice.

## A short honest list

| Situation | Verdict |
|---|---|
| Family at home, wants privacy-first AI on several devices | ✅ This setup, exactly |
| Occasional away-from-home use, low stakes | ⚠️ Fine to just know it won't work then |
| Regular away-from-home use | ⚠️ Learn Tailscale (separate project), or don't |
| College/dorm, apartment-shared Wi-Fi | ❌ Keep to localhost on one machine |
| Kids unsupervised on family Wi-Fi + shared corkboard | ⚠️ Household norms first; then it's fine |
| Need separate accounts and private histories per person | ❌ Outgrows this; homelab territory |
| Medical, legal, financial decisions | ❌ Never; that's professionals' terrain |

If your situation matches the first row — congratulations, you're exactly who this guide was written for. Finish strong with the [setup day checklist](setup-day-checklist.html).
