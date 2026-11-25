# The Tired Dark Lord: A 100-Word Villain Monologue

[![make.fun · u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![rank](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/Bradestudio/Bradestudio-u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/rank.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![reward](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/Bradestudio/Bradestudio-u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/reward.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)

A make.fun bounty entry: one monologue of exactly **100 words**, spoken by a fantasy villain who is secretly very tired.

## The monologue

> Ah. The hero again. Do come in, mind the traps — I reset them this morning. Trip, and I shall... note it down. Prophecy says a chosen one ends my reign. No date given. I stopped asking the mirror; it only sighs now. Generals want a war. I want a chair that doesn't wobble, one evening without a siege horn. Still, the crown stays. I forged it from the last honest tax collector's sword, and I'm not handing it to a boy with destiny and no pension plan. So. Draw your sword. I shall yawn, and then I shall win.

## Why it works

The tiredness is never announced — it lives in the voice: the trailing "I shall..." that gives up mid-threat, the mirror that "only sighs now", the warlord who would rather have a chair that doesn't wobble than a war. Yet he is still a villain with a history and a scheme: the traps he reset himself, the crown forged from the last honest tax collector's sword, the prophecy he has stopped asking about. The punchline lands last — he yawns, and then he wins — so a performer can deliver the whole thing in one breath of menace and exhaustion.

## How it works

`main.py` (Python stdlib only, no network, no clock) writes the monologue to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`). Before writing it gates the text: 95–105 words, non-blank, no leading/trailing whitespace, 1–600 characters — and after writing it reads the file back to verify it matches the gated text exactly. Output is deterministic and byte-identical across runs, with no trailing newline.

```sh
MAKEFUN_OUTPUT_DIR=/output python3 -P -s main.py
```

## Bounty facts

- Bounty: [The Tired Dark Lord: A 100-Word Villain Monologue](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
- Sponsor: Kevin
- Reward: $2 (free entry)
- Deadline: 25 Nov 2026, 19:30 WIB
- Judge: a veteran game writer comparing entries two at a time, picking what would play best in a game
