# Evolve — letting the style mature

A painter's style is not designed once; it accumulates. Moves that keep surviving become signature. Moves that keep getting cut disappear. Periods emerge. This mode makes that accumulation explicit so the person can see — and steer — what their style is becoming.

## After every finished piece: journal entry

Offer this at the end of any Apply or Blend session. Keep it to two minutes for the person. Use `templates/journal-entry.md` and prepend to `~/.design-atelier/profiles/<slug>/journal.md` (newest first).

Ask only:
1. What did you keep from what I proposed, unchanged?
2. What did you change, and why? (Their words, verbatim where possible.)
3. What did you reject outright?
4. Anything new you did by instinct that wasn't in the style?

Record which laws and genes were in play, so the entry can be counted later.

## Updating the DNA

After writing the entry, adjust the profile — slowly. A style that lurches with every project is not a style.

- **Axes:** move an axis by at most ±1 per entry, and only when the person's own changes clearly pushed in that direction. Note the change and the reason in the profile's changelog.
- **Signature moves:** a move that appears in **3 or more** entries (kept or added by the person) is promoted to the profile's "Signature moves" list. These are the most valuable lines in the profile — they are the person's handwriting.
- **Dead genes:** a gene rejected in **2** entries is moved to "Tried and rejected" with the reason. Don't propose it again unless asked.
- **Instinct moves (Q4):** collect separately. Instinct repeated is how new signature appears.
- **Never rules:** add any new strong rejection.

## Drift check

Every update, run:

```bash
python3 <skill-dir>/scripts/atlas_match.py --profile ~/.design-atelier/profiles/<slug>/dna.md --include-trends
```

If the profile has moved toward a saturated trend, say so plainly: "The last three projects pulled you toward [trend]; that's where your work will start looking like everyone else's. Intended?" The person may choose it — but it should be a choice.

## Style review (every 5 entries, or on request)

Compare the first and current profile:
1. **Vector change** — which axes moved, by how much, and which projects moved them.
2. **Signature emergence** — the moves that became signature, in order of appearance.
3. **Period** — name the current period if it is distinct from the start ("the ledger period: dense, warm, type-led"). Painters' periods help a person talk about their own evolution.
4. **Next frontier** — one TENSION source from the atlas the person has never used, suggested as an experiment for the next project. Growth comes from deliberate friction.

When a style has changed enough that its laws no longer describe the work (2+ laws routinely broken by the person), propose a new version of the style spec (`<style-slug>-v2.md`), keeping the old one. Never overwrite history.
