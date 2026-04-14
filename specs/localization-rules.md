# Localization Rules

## Current state
Phase 1 builds German master emails only.

## Future localization principle
Future languages are for people living in the DACH region who prefer another language.

This means:
- market context stays German / DACH-specific
- language changes
- product logic does not change
- mission stays the same
- plain-email style stays the same

## Rules
- translate persuasively, not literally
- preserve all placeholders exactly
- keep structure aligned across languages
- maintain equivalent scenario psychology
- keep CTA intent equivalent
- do not adapt to a foreign energy market
- do not invent region-specific claims outside DACH

## Performance consistency across locales
- optimize subject lines for open rate in each language
- preheaders must add value beyond the subject
- do not force every email to be ultra-short; keep a natural length mix
- keep selective mission references (not every email)
- keep objection handling natural and localized
- use `{{ opportunity.energieart }}` where it improves relevance

## CTA rule
Every email in every language must contain exactly one CTA destination link.

### Default
Most CTAs point to:
- {{ opportunity.offer_url }}

### Referral exception
Only selected loop emails may use referral-oriented CTAs:
- {{ contact.empfehlungslink }}

## Reward variable rule
`{{custom_values.empfehlungsprmie}}` is amount-only and must remain language-neutral.
Examples:
- 30€
- 50€

## Referral rule
Referral messaging must remain trust-based and mission-led across languages.

Should feel like:
- helping loved ones
- sharing clarity
- helping more households
- contributing to something useful

Must not become:
- aggressive affiliate language
- spammy recruiting language
- money-first messaging

## QA checklist
- no broken placeholders
- no mixed-language leftovers
- no broken CTA labels
- one CTA destination link per email
- no loss of persuasion
- plain style preserved (no buttons/images/layout marketing)
