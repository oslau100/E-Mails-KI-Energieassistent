# Localization Rules

## Current state
Phase 1 builds German master emails only.

## Core principle
Future languages keep DACH market logic and mission.

## Must preserve
- placeholders exactly
- same scenario psychology
- same CTA intent
- plain personal email style

## Subject and preheader quality
Across languages:
- subject must be concrete, clear, trustworthy
- preheader must complement subject
- no misleading urgency
- no fake support-style phrasing
- no fake-transactional framing (e.g. "request open", "waiting for your reply")

## Forbidden ambiguous wording (carry over by meaning)
Do not translate into equivalents of:
- "dein aktueller Stand"
- "dein Tarif-Status"
- "deine Situation"
- "deine Daten"

## CTA rule
Every email in every language must contain a CTA.
CTA should remain exactly one clear CTA link per email body.

## Variable usage
- {{ opportunity.energieart }} may be used selectively where relevance increases
- do not overuse dynamic variables in every email

## Selective bridge-line rule
- Keep original structure and add one extra line only where needed to smooth CTA transition.
- Allowed purposes: objection handling, trust, relevance.

## Signature localization rule
- Keep one consistent lightweight HTML signature in localized emails.
- Signature may include brand name, small logo, address, impressum/privacy links.
- Signature formatting should remain subtle and personal-mail compatible.

## QA for translation
- no broken placeholders
- no mixed-language leftovers
- no fake urgency
- no ambiguous wording
- CTA remains clear and unique
