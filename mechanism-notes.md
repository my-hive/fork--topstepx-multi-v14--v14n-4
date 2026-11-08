# v14n-4 — research complete

Nine recorded attempts, including one self-check failure. Best dev_score = 0, first reached e1. No improvement in e2–e9: mandatory stagnation stop. No eligible finalists; no 20/200-seed runs or sealed submissions. Development alone rejects these hypotheses. No new data purchases, OOS access, external trading, or other identities used.

## Mechanisms and coverage

Read program.md before research. Read v14n-3 feed; did not adopt or rely on their source scores. Claimed lead-lag initially, replaced claim with overnight inventory-premium work before evaluation. Shared development outcomes and final stop.

Inspected development cache and session/time coverage across supplied markets: equities ES/MES, NQ/MNQ, YM/MYM, RTY/M2K, NKD; energy CL/MCL/QM, NG/MNG/QG, HO/RB; metals GC/MGC, SI/SIL, HG/MHG, PL; FX 6E/M6E, 6B/M6B, 6A/M6A, 6C, 6J, 6S, 6N, 6M; rates ZB/UB/ZT/ZF/ZN/TN; agriculture ZC/ZS/ZW/ZL/HE/LE; crypto MBT/MET. Used broad descriptive clock-block returns to assess gross economic plausibility, not optimized parameter sweeps. All account screens selected manageable single-market subsets except baseline MES/MGC. Traded only program-authorized equity/energy roots after baseline inherited optional MGC.

Overnight equity hypothesis: investors bear inventory/news risk while cash market closed; reopening inventory premium could exceed costs. Gross returns positive more often across equity roots than commodities/FX. Sparse older ES daytime data and micro missing bars made continuous exposure unreliable. e2 repeatedly reopened after evaluator gap liquidation; causal gap-abandonment added e3, but costs still dominated. e4 Europe-window ES and e5 MYM transferred same economics without improvement.

Small-cap hypothesis: RTY daytime weakness versus overnight strength might reflect cash hedging/selling pressure. e6 failed self-check before simulation; e7 fixed typo, e8 tested micro sizing. Natural-gas overnight short e9 tested producer hedge pressure; also negative under stress.

## Frozen diagnostic candidate, NOT eligible finalist

Restored exact e7/e8 source SHA256 `64d729d32877720f1f1d72e0518f4a12294221cde8b0a00ea41fa3dbbbc3cdb2`, committed at `39cc07ea`. All completed candidates tied dev_score zero; e7 ranks first only on secondary fold_score and year fraction. Retention not claim of edge.

RTY e7: dev_score 0; fold_score 0.019280205655526992; positive_year_fraction 0.2857142857142857; knobs 5; folds 0.09487179487179487 / 0.012853470437017995 / 0.09511568123393316 / 0.02570694087403599; stressed PnL -36812.50. p unrun. M2K same source e8: dev_score 0, year fraction .2, all fold rates zero.

Entry gates: clock window 09:30–15:09 CT, one attempt per session, no reentry after observed missing minute/contract change. Fixed short position; stop declared before entry at $250 aggregate, anchored to actual next-bar open once observed. Stop trigger uses completed-bar high; exit next open, so gaps can exceed declared amount. No claim of intrabar stop fill. Five free numeric choices in PARAMS (start/end/risk/size/side); point values are exchange specifications, nanoseconds/minute unit constant. No optimized calendar or symbol gates. Built-in assert checks normal signals and missing-minute abandonment.

Every attempt logged in experiments.jsonl, raw screen summary retained excluding huge daily/attempt ledgers. Failure metrics null, not invented zeros. Every completed run submitted using printed dev_score, not eligibility score. Failed e6 submitted without score.
