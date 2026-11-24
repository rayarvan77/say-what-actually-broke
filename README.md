[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/rayarvan77/say-what-actually-broke/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/rayarvan77/say-what-actually-broke/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

# Say What Actually Broke

A [make.fun](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5) bounty entry: one line of software error copy, at most 200 characters, that tells the user the brutal truth about what went wrong — and makes them laugh on the way.

## The line

> This deploy failed because someone pushed straight to main on a Friday afternoon. We're rolling it back now, and yes, it was us, not you.

137 characters, one line.

## Why it meets the brief

- **Names the real failure.** No vague "something went wrong": a bad push straight to `main` on a Friday afternoon took the deploy down. The user knows exactly what happened.
- **Funny on a single read.** The Friday-afternoon deploy is every engineer's nightmare, and the deadpan "it was us, not you" lands the joke in one breath.
- **Shippable in a dialog.** It is honest without being rude, it tells the user what happens next (rollback in progress), and it apologises by owning the fault — the kind of copy a real team could actually put in front of users.

## Run it

```sh
python3 main.py
# or, to choose the output directory:
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

`main.py` (Python 3.13 standard library only, no network, deterministic) validates the line — 1–200 characters, a single line, no leading/trailing whitespace, no control characters, no double spaces — then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and prints what it wrote.
