# Copy

Words are part of the design. A distinctive layout with generated-sounding copy still reads as AI work. Every text this skill produces follows these rules: headlines, body copy, buttons, microcopy, alt text, meta descriptions, and the replies to the person.

When the `humanizer` skill is installed, run its process on all copy before delivery; it has the full catalogue of AI writing patterns. This file is the short version and the hard rules.

## Hard rules

1. **No dashes.** No em dash (—) and no en dash (–) anywhere: copy, alt text, titles, replies. Use a period, a comma, a colon or parentheses, or rewrite the sentence. No ` - ` or ` -- ` used as a dash either. Write number ranges in words ("2 ilə 3 saat", "two to three hours"). The only exception is a writing sample from the person that uses dashes; then match their habit.
2. **No invented facts.** Unknown details stay as `[bracketed placeholders]`.
3. **Run the checker** on every text file and page before showing it:
   ```bash
   python3 <skill-dir>/scripts/copy_check.py path/to/file.html
   ```
   Fix every hit. Zero hits on dashes is required; slop-word hits need a rewrite or a clear reason.

## Patterns to cut

| Pattern | Looks like | Write instead |
|---|---|---|
| AI vocabulary | unlock, seamless, elevate, effortless, curated, journey, vibrant, testament, delve, empower; *inqilabi, misilsiz, unikal təcrübə, möhtəşəm, heyrətamiz, sehrli, unudulmaz, dünyasına qərq olun, yeni səviyyəyə* | The plain word for what the thing does: "burns about 40 hours", "soya mumundan" |
| Negative parallelism | "not just X, it's Y"; *"təkcə … deyil, həm də"*, *"nəinki … həm də"* | Say Y directly |
| Rule of three | three adjectives or three clauses by reflex: "calm, cozy and elegant" | One precise word, or two if both carry information |
| Inflated significance | "a testament to", "more than a candle" | What it is and does |
| Copula avoidance | "serves as", "boasts", "features" | "is", "has" |
| Imperative stacks | "Kəşf edin. Hiss edin. Yaşayın." | One instruction that leads somewhere |
| Generic promise | "for every taste", *"hər zövqə uyğun"*, "high quality" | A specific, checkable claim, or nothing |
| Staccato drama | short punchy fragments for effect | Normal sentences |
| Filler signposting | "Here's the thing", "Let's dive in" | Start with the point |

## Voice

- Take the voice from the style spec and the brand's own words (a tagline, an existing caption). A brand that says *fait pour les soins* speaks quietly and concretely.
- Prefer concrete nouns and real numbers over adjectives. "Fitili 5 mm saxlayın" beats "mükəmməl yanma üçün".
- Short paragraphs, normal sentence rhythm, no exclamation marks unless the brand uses them.
- Read every headline aloud. If it could sit on any other brand's site, rewrite it with something only this brand can say.
- In Azerbaijani, write natural Azerbaijani, not translated English (no calques such as "səyahətə çıxın" for "embark on a journey").
