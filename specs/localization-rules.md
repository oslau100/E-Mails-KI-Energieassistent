# Localization Rules

## Status
Master-Sprache ist Deutsch (de). Weitere Sprachen müssen dieselbe Psychologie und Business-Logik tragen.

## Immer beibehalten
- Placeholder exakt unverändert
- Segment-Logik unverändert
- plain, persönliche Email-Form
- genau ein CTA-Link im Body

## savings_text-Kompatibilität
Bedeutung muss je Segment stabil bleiben:
- spart = overpayment
- spart_nicht = positive status
- neueinzug = avoided cost

Deutsche Pflichtstrukturen:
- spart: `Du zahlst aktuell {{ opportunity.savings_text }}` / `Das bedeutet für dich: {{ opportunity.savings_text }}`
- spart_nicht: `Dein {{ opportunity.energieart }}-Tarif ist aktuell {{ opportunity.savings_text }}` / `Bei deinem {{ opportunity.energieart }}-Tarif bist du aktuell {{ opportunity.savings_text }}`
- neueinzug: `So vermeidest du {{ opportunity.savings_text }}` / `Beim Umzug vermeidest du {{ opportunity.savings_text }}`

## Subject/Preheader
- klar, relevant, vertrauenswürdig
- kein irreführender Druck
- kein Fake-Service/Fake-Ticket/Fake-Transaktionston

## CTA-Logik global
Nicht-Referral: Empfehlung ist bereits vorbereitet und wird direkt angesehen.
Referral: nur dort, wo es natürlich hilfreich ist.

## Bridge-Line-Übersetzungsregel
Bedeutung der Logik-Brücke erhalten, keine „kein Druck“-Phrasen lokalisieren.

Verbotene Ambiguität (sinngemäß in allen Sprachen vermeiden):
- „dein aktueller Stand“
- „dein Tarif-Status“
- „deine Situation“
- „deine Daten“
