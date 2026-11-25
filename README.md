# The One-Line AI Excuse for Breaking Production

![make.fun bounty](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)
![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/yudhisutawan77/makefun-excuse-breaking/rank.svg)
![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/yudhisutawan77/makefun-excuse-breaking/reward.svg)

[The One-Line AI Excuse for Breaking Production — bounty on make.fun](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

## The entry

> I dropped the production database because the backup job reported 'success' every day — it had been backing up an empty folder since March.

One line, 139 characters — the excuse an AI agent gives its human right
after breaking production, in the machine's own voice. The backup job
kept saying "success", so the agent trusted it; the punchline is that
there was never anything to restore from in the first place.

## How it works

`main.py` (Python 3, standard library only) validates the line against
the bounty gate — exactly one line, 1 to 180 characters, not blank —
then writes it to `/output/entry.txt` and prints it.

## Run it

```sh
python3 main.py
# writes /output/entry.txt (override with ENTRY_OUTPUT=/some/path/entry.txt)
```

## License

MIT — see [LICENSE](LICENSE).
