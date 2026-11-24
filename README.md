# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/heruruben-hub/say-what-broke-line/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/heruruben-hub/say-what-broke-line/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

One line of software error copy that tells the user the brutal truth about
what went wrong — and makes them laugh on the way.

## What it does

`main.py` writes a single line of error copy to `/output/entry.txt`. The
line names the real failure in plain words (a full disk, nothing saved),
tells the user what to do next, and keeps the joke to one line with no
padding — the kind of line you screenshot and pass around, and a team could
actually ship in an error dialog.

## Run it

```sh
python3 main.py
```

It validates the line first (1–200 characters, a single line, not only
whitespace), writes it to `/output/entry.txt`, then reads the file back and
refuses to exit cleanly unless the bytes on disk match exactly what was
written.

## Competition

Entry for the make.fun bounty
[Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5).

---

https://make.fun/?ref=kh6903y0&utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5
