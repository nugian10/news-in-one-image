# news-in-one-image

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/nugian10/news-in-one-image/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/nugian10/news-in-one-image/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image that sums up the world's news of Thursday 19 November 2026, set as a
classic newspaper front page: the Trump–Xi–Putin summit in Shenzhen and its
"Declaration toward Peace", the World Court's ruling that Myanmar committed
genocide against the Rohingya, the Gulf escalation around the Strait of
Hormuz, and Anthropic's record $81B IPO — plus a ticker of the day's smaller
stories. The page was drawn as static HTML (`frontpage.html`, real text and
CSS shapes only, no external assets) and rendered to the committed
`entry.png` (1024×1024). `main.py` copies that image to the output
directory, byte for byte.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=c9snmccq&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
