# Localization Rules

## Current state
Phase 1 builds German master emails only.

## Core principle
Future languages must keep DACH market logic and mission.

## Must preserve
- placeholders exactly
- same scenario psychology
- same CTA intent
- plain personal email style

## Subject and preheader quality
Across languages:
- subject must be concrete, clear, trustworthy
- preheader must complement subject and add context
- no misleading urgency
- no fake support-style phrasing
- no fake-transactional framing (e.g. "request open", "waiting for your reply")

## Forbidden ambiguous wording (carry over by meaning)
Do not translate into equivalents of:
- "dein aktueller Stand"
- "dein Tarif-Status"
- "deine Situation"
- "deine Daten"

## CTA rule (global)
Every email in every language must contain exactly one CTA link in the body.

## CTA business logic (global)
In non-referral mails, CTA language should reflect:
- recommendation already determined from provided user information
- recommendation framed as safe/clear option
- user can directly view that recommendation now

## Variable usage
- In non-referral mails, {{ opportunity.energieart }} is mandatory:
  - in subject or preheader
  - and in body
- In referral mails, {{ opportunity.energieart }} is optional (only if natural)
- do not overuse other dynamic variables

## Selective bridge-line rule
- Keep original structure and add 1–2 extra lines only when needed for context + objection handling.
- Do not apply this globally to every email.

## Signature localization rule
- Keep one consistent lightweight HTML signature in localized emails.
- Signature may include brand name, small logo, address, impressum/privacy links.
- Signature formatting should remain subtle and personal-mail compatible.

## QA for localization
- no broken placeholders
- no mixed-language leftovers
- no fake urgency
- no fake-transactional framing
- no ambiguous wording
- exactly one CTA link in body
