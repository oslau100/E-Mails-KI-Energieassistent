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

## savings_text compatibility
Across all locales, segment semantics must stay stable:
- spart = overpayment
- spart_nicht = positive status
- neueinzug = avoided cost

Required German base structures:
- spart: `Du zahlst aktuell {{ opportunity.savings_text }}` / `Das bedeutet für dich: {{ opportunity.savings_text }}`
- spart_nicht: `Du bist aktuell {{ opportunity.savings_text }}` / `Bei deinem {{ opportunity.energieart }}-Tarif bist du aktuell {{ opportunity.savings_text }}`
- neueinzug: `So vermeidest du {{ opportunity.savings_text }}` / `Beim Umzug vermeidest du {{ opportunity.savings_text }}`

## Subject and preheader quality
Across languages:
- subject must be concrete, clear, trustworthy
- preheader must complement subject and add context
- no misleading urgency
- no fake support-style phrasing
- no fake-transactional framing

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
