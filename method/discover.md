# Discover, building a Style DNA profile

Goal: a profile that predicts what this person will love, reject, and grow toward, precise enough that a blend made from it feels like *theirs* on first sight.

A painter finds a style by noticing what their hand keeps doing. We speed that up by gathering four kinds of evidence, then reconciling them. Use whatever the person can give; more sources → sharper profile.

| Evidence | What it reveals | Weight |
|---|---|---|
| Their own work | Revealed taste, what they actually do | Highest |
| Visual taste test | Instinctive preference, before words | High |
| References they collect | Aspiration, where they want to go | Medium |
| Interview | Stated taste, values, life material | Medium (people describe themselves imprecisely) |

The **gap between stated and revealed taste** is the most useful finding. If someone says "minimal" but every piece they're proud of is dense and warm, the style should be built on the work and the gap named out loud, it often marks where they are trying to grow.

## 1. Interview

Ask in rounds of 3 to 4 questions, never all at once. Adapt follow-ups to answers. Skip what earlier evidence already answers.

**Interview rules** (after Rob Fitzpatrick, *The Mom Test*, `atlas/ux/the-mom-test.md`): people describe the designer they want to be, so collect evidence, not self-description.
- Ask about what they have done, never what they like in general or would do. Follow every generic answer ("I always…", "I'm a minimalist") with "When was the last time? Show me."
- Name no styles, masters or blends until their own evidence is in. A label you offer first gets agreement, not information.
- Praise and agreement ("love it", "that's me") are not data. Ask what they would change, or where they would actually use it.
- Dig into every strong reaction, wince or delight, until you know the concrete cause (colour, spacing, tone, a memory). Record it verbatim.
- Let them do most of the talking.

**Round A, instinct**
1. Name three things you own and love the look of. Not famous design objects, things from your actual life. When did you get each, and what did you pick it over?
2. Think of the last time a design made you wince. What was it, where did you see it, and what exactly was wrong, the type, the colour, the spacing, the tone?
3. A place where you felt completely calm, and one where you felt electrified.

**Round B, influences**
4. Which designers, artists, films, records, games or books have you gone back to on purpose lately? When, and what did you go back for?
5. Three pieces of your own work you are proud of, and one you dislike. (Ask for images or links.)
6. Look at the last few things you chose for your home, desk or wardrobe. What are they made of, and what did you pass over? (If the person offers a material metaphor instead, record it as aspiration, not evidence.)

**Round C, voice**
7. The best thing anyone has said about a piece of yours, and the remark that stung most, who said each, about which piece? Then: three words you'd never want said about your work.
8. Open your last finished piece. Where does the eye land first, and what did you do to slow it down or speed it up?
9. The last brief where a striking option and a clearer one competed, which did you ship, and what happened after?

**Round D, roots** (optional; personal life, not nationality unless they bring it up)
10. Hobbies, crafts, places you have lived, things your hands do outside design.
11. Any culture, craft or tradition you would like your work to carry? (Only if they say yes do cultural genes enter later blends.)

Rejections (Q2, Q7 "never") are often more defining than likes. Record them verbatim.

### Quick version (when someone wants to start fast)

Q1, Q2, Q5 (or Q4 if they have no portfolio), Q7. Then score a provisional vector and mark the profile `confidence: low`.

## 2. Visual taste test

`assets/taste-test.html` is a self-contained page: 24 A/B pairs, two per axis, each a small abstract composition that differs mainly on one axis. The person picks instinctively (or "both / neither"), and the page outputs the `axes: {…}` line plus the raw choices.

How to run it:
- **Claude Code / desktop:** copy the file somewhere the person can open (or publish it as an artifact if that tool is available) and ask them to paste the result line back.
- **Claude.ai:** render the HTML as an artifact.
- **No HTML possible:** ask the pairs in text from `assets/taste-test.html`'s `PAIRS` list, one axis at a time.

Treat the test result as instinct, not truth. It catches what people can't articulate; it can also be noisy. Where it disagrees with their own work, trust the work and note the disagreement.

## 3. Work analysis

For each piece of their work they share (images, Figma links, URLs):
1. Score it on the 12 axes using the anchors in `discovery/dna-axes.md`.
2. Note recurring moves: the same corner treatment, the same way of placing a headline, a color they always reach for. Recurring moves are proto-signatures.
3. Note what they avoid. Absence is information.

Average the scores of the pieces they're proud of → **revealed vector**. Score the piece they dislike separately, it shows the direction to steer away from.

For references they collect (moodboards, saved posts): score the same way → **aspiration vector**.

## 4. Reconcile

1. Start from the revealed vector (work). If no work exists, start from the taste test.
2. Pull each axis toward the taste test and aspiration by at most ±2, enough to leave room to grow, not enough to erase who they are now.
3. Where interview and evidence disagree by 3+ points on an axis, keep the evidence value and record the gap in the profile.
4. Run `python3 <skill-dir>/scripts/atlas_match.py --vector "<vector>"` to find **kin** (masters they already resemble), **tension** sources and **far** sources. Read the top 3 kin cards; check them against the person's influences from Q4. Overlap confirms the vector; no overlap means re-check the scoring.
5. Write the profile with `templates/dna-profile.md` to `~/.design-atelier/profiles/<slug>/dna.md`.

## 5. Read the profile back

Present it to the person in plain language, not a vector dump:
- "Your work is strongly ordered and quiet (order 8, energy 3), warmer than you describe it, and type carries the voice."
- Their 3 kin masters, and one sentence on what they share with each.
- The stated-vs-revealed gap, framed as a choice: lean into it or close it.
- Their rejections, as the style's first "never" rules.

Ask what feels wrong. People recognise a mis-portrait instantly; adjust and save. If they only praise it, ask which line they would cut, approval of a portrait is not confirmation; using the style on a real brief is. Then offer Mode 3 (Blend).
