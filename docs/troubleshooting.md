# Troubleshooting

When something goes sideways, start with the table. Eighty percent of shared-Ollama problems live in the first four rows.

## The table

| # | Symptom | Most likely cause | Fix |
|---|---|---|---|
| 1 | **Other device gets "connection refused" or times out** | Ollama still listening only to itself — `OLLAMA_HOST` not applied | Confirm the settings actually took: the `setx`/export lines exist, then **fully quit Ollama from the tray and start it again**. On Windows, open a **brand-new** terminal and run `echo %OLLAMA_HOST%` to see what *new* programs will actually receive. |
| 2 | **"Connection refused" but Ollama restart was done properly** | Firewall said no | Open the door again carefully ([page 4](04-firewall-basics.html)). Windows first check: home Wi-Fi marked **Private**? Then re-check the Ollama entry in "Allow an app through firewall" has its **Private** box ticked. |
| 3 | **Worked yesterday; nothing today** | Something changed on its own | Usual suspects, in order: (a) Ollama just isn't running — check the tray icon; (b) the main computer's IP address *changed* after a router restart — see next row; (c) Windows update re-marked your Wi-Fi as "Public." |
| 4 | **The address stopped working after a network hiccup** | IP address changed (routers re-lease addresses; `…42` can become `…57`) | Look up the address again ([step 1](03-open-it-to-your-network.html#step-1-find-the-main-computers-address)) and update it in each family device's app. One-time annoyance; you can *later* make it permanent with a "static lease" on your router — a friendly ten-minute project for another day. |
| 5 | **"Ollama is running" page loads, but the chat app errors** | Wrong URL shape in the app | Apps want the **plain http** base, no `/v1`, no trailing slash insisted upon by some: `http://192.168.1.42:11434`. If you typed the address wrong, retype it — leading `https://` (with the s) is the classic silent mistake. |
| 6 | **Answers crawl, minutes per reply** | Machine overloaded, or wrong machine for the job | Check RAM vs. model: 8 GB + an 8B model is tight. Try the smaller model: `ollama pull phi3`, then `ollama run phi3`. Also: is someone gaming on the main computer? One machine, one job at a time. |
| 7 | **Loads the *first* question, then blank / stalls on later ones** | The box is almost out of memory mid-conversation | Same as above but sneakier — reboot the main computer and try the smaller model; consider a RAM upgrade as the real fix. |
| 8 | **`ollama run` says "model not found" on a family device** | You typed the model name on a device *without* Ollama installed | Nothing's wrong. Family devices only need the **app + address** ([page 5](05-phone-access.html)) — the *model* runs on the main computer alone. Only the main computer runs `ollama` commands. |
| 9 | **Phone connects at home but "not found" on cellular data** | Working as designed | Local means local. Away-from-home use is the one thing this setup deliberately doesn't do — see [page 6](06-when-this-is-a-bad-idea.html) for what changes if you need it. |
| 10 | **Mac firewall pops "Do you want Ollama to accept incoming…?" again** | A new Ollama version re-introduced itself | Click **Allow**. Update jokes aside — this is normal after an app update, one click, done. |
| 11 | **Everything above checks out; still stubborn** | Order-of-operations drift | Walk the phases again from Phase 3 of the [checklist](setup-day-checklist.html) — nine times out of ten the failed box announces itself. |

## Two habits worth more than any single fix

1. **Change one thing, then re-test.** The fastest way to make troubleshooting into archaeology is changing three things between tests.
2. **Keep the failing test in mind as `A: from X to Y`.** "From the phone to `192.168.1.42:11434`" pins down which hop broke: phone→Wi-Fi, Wi-Fi→main computer, or main computer→Ollama. Each hop has exactly one fix; the sentence finds it.

## Last resort

The nuclear reset that fixes stale state more often than it should: on the main computer quit Ollama fully, restart the computer, reopen Ollama, test locally (`localhost:11434`), then remotely. Ten minutes, and it removes every "state nobody remembers changing" between you and the answer.
