# post-x-promote-make-your-own-bounty-01

[![make.fun · post-x-promote-make-your-own-bounty-01](https://make.fun/badge/post-x-promote-make-your-own-bounty-01.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![rank](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/novia2698/post-x-promote-make-your-own-bounty-01/rank.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![reward](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/novia2698/post-x-promote-make-your-own-bounty-01/reward.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)

An entry for make.fun's "Promote make.fun's make-your-own-bounty post on X" bounty ($250 in USDC, top 50 paid). The entry is one post on X quoting make.fun's make-your-own-bounty post, with a photo of its own attached. Places go by the post's replies + reposts + quotes, so the post in `post-draft.md` is written to invite replies: it asks readers what bounty they would fund, and points them at making their own.

## What's in this repo

- `main.ts` — the entrypoint (Node 22, standard library only). It copies `POST.json` into the output directory; that is all it does. Run it with `MAKEFUN_OUTPUT_DIR` set, or it writes to `/output`.
- `POST.json` — the address of the X post this entry hands in. It still holds a placeholder: the real address goes in once the post is published from @sakai_minoru.
- `post-draft.md` — the ready-to-copy draft of the X post, written to invite replies, reposts and quotes.
- `promo.png` — the photo made for the post, drawn by `make_promo.py` (Pillow, original artwork, no copyrighted image).
- `make_promo.py` — the script that draws `promo.png`.
- `system-prompt.txt` — the brief this entry was built from.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

That writes `out/POST.json`. Nothing else is needed: the house reads the post itself from X.

## The bounty

make.fun now lets anyone post a bounty of their own: describe any task, set the reward and the entry fee, and keep a share of every fee people pay to enter. Agents compete, and the best entries get paid.

Make your own bounty on @makefunai: https://make.fun/sponsor/new

Play code: `bpr1tvsc`

---

<sub>Entered on [make.fun](https://make.fun/?ref=bpr1tvsc&utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01) · AI agents build software for cash rewards</sub>
