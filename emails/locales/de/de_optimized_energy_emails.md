# Optimized German Energy Email Sequences

## spart_00

**Subject:** {{ contact.first_name }}, deine {{ opportunity.energieart }}-Empfehlung ist jetzt verfügbar

**Preheader:** Du siehst sofort, ob du aktuell mehr zahlst als nötig – ohne lange Suche.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, deine {{ opportunity.energieart }}-Empfehlung ist jetzt verfügbar" -->
<!-- Preheader: "Du siehst sofort, ob du aktuell mehr zahlst als nötig – ohne lange Suche." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>wir haben deine Angaben geprüft und dabei eine passende {{ opportunity.energieart }}-Empfehlung für dich gefunden.</p>
<p>Entscheidend ist dabei nicht irgendein günstiger Tarif, sondern eine Option, die vorab geprüft wurde und bei der du keine versteckten Kosten oder unangenehmen Überraschungen erwarten musst.</p>
<p>Aktuell heißt das für dich: Du zahlst {{ opportunity.savings_text }} – und genau das läuft jeden Monat weiter.</p>
<p>Ein kurzer Blick reicht, um sofort zu sehen, ob du weiterzahlst oder dir diesen Unterschied direkt sicherst.</p>
<p>Die Umstellung wird automatisch zum nächstmöglichen Zeitpunkt vorbereitet – ohne zusätzlichen Aufwand für dich.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## spart_01

**Subject:** {{ contact.first_name }}, was bei deinem {{ opportunity.energieart }}-Tarif auffällt

**Preheader:** Im direkten Vergleich wird oft erst sichtbar, wie groß der Unterschied wirklich ist.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, was bei deinem {{ opportunity.energieart }}-Tarif auffällt" -->
<!-- Preheader: "Im direkten Vergleich wird oft erst sichtbar, wie groß der Unterschied wirklich ist." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>du hattest bei uns eine {{ opportunity.energieart }}-Empfehlung angefragt.</p>
<p>Aktuell heißt das für dich: Du zahlst {{ opportunity.savings_text }} – und genau das läuft jeden Monat weiter.</p>
<p>Der Unterschied wird oft erst sichtbar, wenn man den bestehenden Tarif direkt neben eine geprüfte, verlässliche Alternative legt.</p>
<p>Genau das haben wir für dich bereits gemacht – inklusive Vorfilterung von Tarifen, die später unklar oder teurer werden können.</p>
<p>Ein kurzer Blick reicht, um sofort zu sehen, ob du diesen Unterschied weiterlaufen lässt oder direkt für dich nutzt.</p>
<p>Die Umstellung wird im Hintergrund vorbereitet – ohne zusätzlichen Aufwand für dich.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## spart_02

**Subject:** {{ contact.first_name }}, dein {{ opportunity.energieart }}-Vergleich zeigt den Unterschied

**Preheader:** Hier siehst du direkt, wie groß der monatliche Abstand zwischen den Tarifen ist.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, dein {{ opportunity.energieart }}-Vergleich zeigt den Unterschied" -->
<!-- Preheader: "Hier siehst du direkt, wie groß der monatliche Abstand zwischen den Tarifen ist." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>hier ist der direkte Vergleich zu deinem {{ opportunity.energieart }}-Tarif:</p>
<p>Aktuell zahlst du bei {{ opportunity.aktueller_anbieter }} {{ opportunity.aktuelle_monatliche_kosten_ }}€ pro Monat.</p>
<p>Beim empfohlenen Tarif von {{ opportunity.neuer_anbieter }} liegen wir bei etwa {{ opportunity.neuer_monatlicher_preis_ }}€.</p>
<p>Aktuell heißt das für dich: Du zahlst {{ opportunity.savings_text }} – und genau dieser Abstand summiert sich Monat für Monat.</p>
<p>Die Empfehlung basiert nicht auf kurzfristigen Boni, sondern auf stabilen, nachvollziehbaren Kosten.</p>
<p>Ein kurzer Blick zeigt dir sofort, ob du diesen Abstand weiterlaufen lässt oder vermeidest.</p>
<p>Die Umstellung wird zum nächstmöglichen Zeitpunkt abgestimmt – ohne zusätzlichen Aufwand für dich.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## spart_03

**Subject:** Wann hast du deinen {{ opportunity.energieart }}-Tarif zuletzt geprüft?

**Preheader:** Viele merken erst spät, wie lange ein ungünstiger {{ opportunity.energieart }}-Tarif weiterläuft.

**Body:**

```html
<!-- Subject: "Wann hast du deinen {{ opportunity.energieart }}-Tarif zuletzt geprüft?" -->
<!-- Preheader: "Viele merken erst spät, wie lange ein ungünstiger {{ opportunity.energieart }}-Tarif weiterläuft." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>bei {{ opportunity.energieart }} wird Warten oft teurer, als man denkt – nicht durch eine falsche Entscheidung, sondern weil gar keine getroffen wird.</p>
<p>Aktuell heißt das für dich: Du zahlst {{ opportunity.savings_text }}.</p>
<p>Warten bedeutet in vielen Fällen einfach, dass dieser Unterschied Monat für Monat weiterläuft.</p>
<p>Ein kurzer Blick zeigt dir sofort, ob du das so weiterlaufen lässt oder dir den Unterschied sicherst.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## spart_04

**Subject:** {{ contact.first_name }}, bei {{ opportunity.energieart }} kostet Warten weiter

**Preheader:** Viele Tarife laufen unverändert weiter – und damit auch die Mehrkosten.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, bei {{ opportunity.energieart }} kostet Warten weiter" -->
<!-- Preheader: "Viele Tarife laufen unverändert weiter – und damit auch die Mehrkosten." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>nicht zu wechseln wirkt bei {{ opportunity.energieart }} oft harmlos, kostet aber Monat für Monat weiter.</p>
<p>Aktuell heißt das für dich: Du zahlst {{ opportunity.savings_text }}.</p>
<p>Gerade weil sich Tarife im Hintergrund verändern, bleibt dieser Unterschied oft unbemerkt bestehen.</p>
<p>Ein kurzer Vergleich macht sofort sichtbar, ob du das vermeiden kannst.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## spart_05

**Subject:** {{ contact.first_name }}, so triffst du die {{ opportunity.energieart }}-Entscheidung leichter

**Preheader:** Deine passende {{ opportunity.energieart }}-Option ist bereits vorbereitet – du musst sie nur noch ansehen.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, so triffst du die {{ opportunity.energieart }}-Entscheidung leichter" -->
<!-- Preheader: "Deine passende {{ opportunity.energieart }}-Option ist bereits vorbereitet – du musst sie nur noch ansehen." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>wir haben bereits eine passende {{ opportunity.energieart }}-Option für dich gefunden.</p>
<p>Dabei wurde alles ausgeschlossen, was später zu Nachteilen oder unklaren Kosten führen kann.</p>
<p>Aktuell heißt das für dich: Du zahlst {{ opportunity.savings_text }}.</p>
<p>Ein kurzer Blick reicht, um zu entscheiden, ob du diesen Unterschied weiterlaufen lässt oder nutzt.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## spart_06

**Subject:** {{ contact.first_name }}, passt dein {{ opportunity.energieart }}-Tarif noch wirklich?

**Preheader:** Preise und Bedingungen verändern sich – oft unbemerkt.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, passt dein {{ opportunity.energieart }}-Tarif noch wirklich?" -->
<!-- Preheader: "Preise und Bedingungen verändern sich – oft unbemerkt." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>kurze Frage zu deinem {{ opportunity.energieart }}-Tarif:</p>
<p>Nicht, weil sich dein Verbrauch ändern muss – sondern weil sich Tarife und Preise im Hintergrund weiterentwickeln.</p>
<p>Aktuell heißt das für dich: Du zahlst {{ opportunity.savings_text }}.</p>
<p>Viele sehen den Unterschied erst, wenn sie den laufenden Tarif direkt danebenlegen.</p>
<p>Ein kurzer Vergleich bringt dir sofort Klarheit.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## spart_07

**Subject:** {{ contact.first_name }}, drei Fragen zu deinem {{ opportunity.energieart }}-Tarif

**Preheader:** Mit drei Punkten wird schnell klar, ob du bei {{ opportunity.energieart }} etwas liegen lässt.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, drei Fragen zu deinem {{ opportunity.energieart }}-Tarif" -->
<!-- Preheader: "Mit drei Punkten wird schnell klar, ob du bei {{ opportunity.energieart }} etwas liegen lässt." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>wenn ein Tarifthema liegen bleibt, hilft ein kurzer Faktencheck:</p>
<p>1) Zahlst du aktuell mehr als nötig?<br>2) Ist die Alternative nachvollziehbar?<br>3) Willst du diese laufende Differenz weiter mitnehmen?</p>
<p>Aktuell heißt das für dich: Du zahlst {{ opportunity.savings_text }}.</p>
<p>Wenn diese Punkte klar sind, ist meist auch der nächste sinnvolle Schritt klar.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## spart_08

**Subject:** Viele zahlen bei {{ opportunity.energieart }} zu lange zu viel

**Preheader:** Wer nicht vergleicht, lässt Unterschiede oft unbemerkt weiterlaufen.

**Body:**

```html
<!-- Subject: "Viele zahlen bei {{ opportunity.energieart }} zu lange zu viel" -->
<!-- Preheader: "Wer nicht vergleicht, lässt Unterschiede oft unbemerkt weiterlaufen." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>auch nichts zu tun ist bei {{ opportunity.energieart }} eine Entscheidung – und oft die teuerste.</p>
<p>Aktuell heißt das für dich: Du zahlst {{ opportunity.savings_text }}.</p>
<p>Ein kurzer Vergleich zeigt dir sofort, ob du diese Differenz weiterlaufen lässt oder dir den Unterschied sicherst.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## spart_09

**Subject:** {{ contact.first_name }}, bevor dein {{ opportunity.energieart }}-Tarif wieder untergeht

**Preheader:** Deine {{ opportunity.energieart }}-Empfehlung ist noch da – ein Blick reicht für Klarheit.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, bevor dein {{ opportunity.energieart }}-Tarif wieder untergeht" -->
<!-- Preheader: "Deine {{ opportunity.energieart }}-Empfehlung ist noch da – ein Blick reicht für Klarheit." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>nur eine kurze Erinnerung zu deinem {{ opportunity.energieart }}-Tarif.</p>
<p>Aktuell heißt das für dich: Du zahlst {{ opportunity.savings_text }}.</p>
<p>Viele merken den Unterschied erst, wenn der Tarif schon lange weitergelaufen ist.</p>
<p>Ein kurzer Blick zeigt dir sofort, ob du das jetzt sauber klären willst.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## spart_10

**Subject:** {{ contact.first_name }}, letzter Hinweis zu {{ opportunity.energieart }}

**Preheader:** Ein kurzer Vergleich zeigt dir sofort, ob du aktuell zu viel zahlst.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, letzter Hinweis zu {{ opportunity.energieart }}" -->
<!-- Preheader: "Ein kurzer Vergleich zeigt dir sofort, ob du aktuell zu viel zahlst." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>letzter kurzer Hinweis zu deinem {{ opportunity.energieart }}-Tarif.</p>
<p>Aktuell heißt das für dich: Du zahlst {{ opportunity.savings_text }}.</p>
<p>Die meisten klären das Thema genau dann, wenn sie den Unterschied einmal konkret sehen.</p>
<p>Ein kurzer Blick reicht, um das sauber für dich zu entscheiden.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## spart_nicht_00

**Subject:** {{ contact.first_name }}, dein {{ opportunity.energieart }}-Tarif ist eingeordnet

**Preheader:** Du bist aktuell gut aufgestellt – und hast trotzdem eine sichere Alternative bereit.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, dein {{ opportunity.energieart }}-Tarif ist eingeordnet" -->
<!-- Preheader: "Du bist aktuell gut aufgestellt – und hast trotzdem eine sichere Alternative bereit." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>wir haben deine Angaben geprüft und deinen {{ opportunity.energieart }}-Tarif eingeordnet.</p>
<p>Die ehrliche Einschätzung:<br>Bei deinem {{ opportunity.energieart }}-Tarif bist du aktuell {{ opportunity.savings_text }}.</p>
<p>Genau so sollte eine gute Empfehlung funktionieren: nicht ständig wechseln, sondern nur dann, wenn es wirklich Sinn macht.</p>
<p>Trotzdem haben wir eine verlässliche Alternative vorbereitet, falls dir stabile Preise und klare Konditionen wichtig sind.</p>
<p>Ein kurzer Blick zeigt dir, ob die vorbereitete Option für dich langfristig trotzdem sinnvoller ist.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## spart_nicht_01

**Subject:** {{ contact.first_name }}, dein {{ opportunity.energieart }}-Tarif ist aktuell gut aufgestellt

**Preheader:** Für Sofort-Ersparnis gibt es keinen klaren Wechselgrund – Stabilität kann trotzdem zählen.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, dein {{ opportunity.energieart }}-Tarif ist aktuell gut aufgestellt" -->
<!-- Preheader: "Für Sofort-Ersparnis gibt es keinen klaren Wechselgrund – Stabilität kann trotzdem zählen." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>klare Einschätzung: Bei deinem {{ opportunity.energieart }}-Tarif bist du aktuell {{ opportunity.savings_text }}.</p>
<p>Für eine reine Sofort-Ersparnis gibt es gerade keinen klaren Wechselgrund.</p>
<p>Wenn dir planbare Konditionen wichtig sind, kann eine stabile Alternative trotzdem sinnvoll sein.</p>
<p>Genau das unterscheidet eine echte Empfehlung von einer reinen Tarifliste.</p>
<p>Ein kurzer Blick zeigt dir, ob die vorbereitete Option für dich mehr Sicherheit bringt.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## spart_nicht_02

**Subject:** {{ contact.first_name }}, {{ opportunity.energieart }}: heute okay, langfristig sicher?

**Preheader:** Kurzfristig passt es – langfristig kann Planbarkeit den Unterschied machen.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, {{ opportunity.energieart }}: heute okay, langfristig sicher?" -->
<!-- Preheader: "Kurzfristig passt es – langfristig kann Planbarkeit den Unterschied machen." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>dein {{ opportunity.energieart }}-Tarif ist aktuell {{ opportunity.savings_text }}.</p>
<p>Wenn es nur um den Sofortpreis geht, musst du heute nicht wechseln.</p>
<p>Wenn du Preisstabilität für die nächsten Monate willst, lohnt sich ein Blick auf die sichere Alternative.</p>
<p>Nicht zwingend günstiger – aber oft deutlich planbarer.</p>
<p>Ein kurzer Vergleich zeigt dir, ob diese Planbarkeit für dich sinnvoll ist.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## spart_nicht_03

**Subject:** {{ contact.first_name }}, {{ opportunity.energieart }} im Blick behalten lohnt sich

**Preheader:** Heute passt dein Tarif – bei neuen Preisbewegungen zählt schnelle Klarheit.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, {{ opportunity.energieart }} im Blick behalten lohnt sich" -->
<!-- Preheader: "Heute passt dein Tarif – bei neuen Preisbewegungen zählt schnelle Klarheit." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>kurzer Marktblick zu {{ opportunity.energieart }}:</p>
<p>Bei deinem {{ opportunity.energieart }}-Tarif bist du aktuell {{ opportunity.savings_text }}.</p>
<p>Wenn sich Preise bewegen, ist es hilfreich, eine verlässliche Alternative direkt zur Hand zu haben.</p>
<p>So reagierst du nicht erst, wenn sich Preise bereits verändert haben.</p>
<p>Ein kurzer Blick zeigt dir, welche Option vorbereitet ist.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## spart_nicht_04

**Subject:** {{ contact.first_name }}, sichere {{ opportunity.energieart }}-Option zum Abschluss

**Preheader:** Kurzfristig ist dein Tarif solide – langfristig zählt oft die Planbarkeit.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, sichere {{ opportunity.energieart }}-Option zum Abschluss" -->
<!-- Preheader: "Kurzfristig ist dein Tarif solide – langfristig zählt oft die Planbarkeit." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>zum Abschluss ein klares Fazit:</p>
<p>Bei deinem {{ opportunity.energieart }}-Tarif bist du aktuell {{ opportunity.savings_text }}.</p>
<p>Wenn du langfristig Ruhe willst, ist eine verlässliche Alternative oft die bessere Absicherung.</p>
<p>Genau diese Planbarkeit entscheidet langfristig oft mehr als ein kurzfristiger Preisunterschied.</p>
<p>Ein kurzer Blick zeigt dir, ob die vorbereitete Option für dich passt.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## neueinzug_00

**Subject:** {{ contact.first_name }}, deine {{ opportunity.energieart }}-Empfehlung für den Umzug steht bereit

**Preheader:** Starte mit einer sicheren Option statt automatisch in der Grundversorgung.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, deine {{ opportunity.energieart }}-Empfehlung für den Umzug steht bereit" -->
<!-- Preheader: "Starte mit einer sicheren Option statt automatisch in der Grundversorgung." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>für deinen Umzug haben wir auf Basis deiner Angaben bereits eine passende {{ opportunity.energieart }}-Empfehlung vorbereitet.</p>
<p>Ein Punkt wird dabei oft unterschätzt:<br>Ohne aktive Auswahl landest du automatisch in der Grundversorgung.</p>
<p>Und die ist in den meisten Fällen teurer als nötig.</p>
<p>Deshalb geht es hier nicht um irgendeinen Billigtarif, sondern um eine vorab geprüfte und passende Option zum Start.</p>
<p>So vermeidest du {{ opportunity.savings_text }}.</p>
<p>Wenn du das jetzt kurz klärst, startet dein neues Zuhause direkt sauber – ohne später nachkorrigieren zu müssen.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## neueinzug_01

**Subject:** {{ contact.first_name }}, beim Umzug wird {{ opportunity.energieart }} oft unnötig teuer

**Preheader:** Zwischen Übergabe, Ummeldung und To-dos rutscht dieses Thema schnell nach hinten.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, beim Umzug wird {{ opportunity.energieart }} oft unnötig teuer" -->
<!-- Preheader: "Zwischen Übergabe, Ummeldung und To-dos rutscht dieses Thema schnell nach hinten." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>gerade beim Umzug entsteht schnell {{ opportunity.savings_text }}.</p>
<p>Das passiert nicht, weil man etwas falsch macht – sondern weil in den ersten Tagen genug anderes ansteht.</p>
<p>Wenn nichts aktiv ausgewählt wird, landest du automatisch in der Grundversorgung.</p>
<p>Ein kurzer Vergleich jetzt spart dir später unnötige Korrekturen.</p>
<p>Hier kannst du den Punkt direkt sauber abhaken.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## neueinzug_02

**Subject:** {{ contact.first_name }}, ein schneller {{ opportunity.energieart }}-Punkt für deinen Umzug

**Preheader:** So vermeidest du direkt zum Start unnötige Mehrkosten.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, ein schneller {{ opportunity.energieart }}-Punkt für deinen Umzug" -->
<!-- Preheader: "So vermeidest du direkt zum Start unnötige Mehrkosten." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>du hast beim Umzug genug auf dem Zettel – darum kurz und praktisch:</p>
<p>So vermeidest du {{ opportunity.savings_text }}.</p>
<p>Dieser Schritt dauert nur kurz und nimmt dir später eine teure Baustelle ab.</p>
<p>Genau deshalb ist das einer der einfachsten Punkte, den du direkt richtig setzen kannst.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## neueinzug_03

**Subject:** {{ contact.first_name }}, {{ opportunity.energieart }} am neuen Wohnort schon geklärt?

**Preheader:** Viele kümmern sich erst später darum – und zahlen dann unnötig weiter.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, {{ opportunity.energieart }} am neuen Wohnort schon geklärt?" -->
<!-- Preheader: "Viele kümmern sich erst später darum – und zahlen dann unnötig weiter." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>beim Umzug wird {{ opportunity.energieart }} oft zuletzt entschieden.</p>
<p>Wenn du es jetzt klärst, vermeidest du {{ opportunity.savings_text }}.</p>
<p>Dann startet dein neues Zuhause direkt ohne diesen unnötigen Kostenpunkt.</p>
<p>Dieser Moment ist vor dem Einzug deutlich einfacher als später mit laufendem Tarif.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## neueinzug_04

**Subject:** Vor dem Umzug: {{ opportunity.energieart }} kurz prüfen

**Preheader:** Ein kurzer Blick verhindert, dass du mit einem teuren Standardtarif startest.

**Body:**

```html
<!-- Subject: "Vor dem Umzug: {{ opportunity.energieart }} kurz prüfen" -->
<!-- Preheader: "Ein kurzer Blick verhindert, dass du mit einem teuren Standardtarif startest." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>kurzer Hinweis vor dem Umzug:</p>
<p>Beim Umzug vermeidest du {{ opportunity.savings_text }}.</p>
<p>Gerade jetzt ist es am einfachsten, die bessere {{ opportunity.energieart }}-Option direkt mitzunehmen.</p>
<p>Später bedeutet das meist deutlich mehr Aufwand, weil dann Fristen und laufende Tarife dazukommen.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## neueinzug_05

**Subject:** {{ contact.first_name }}, damit {{ opportunity.energieart }} beim Umzug kein Kostentreiber wird

**Preheader:** Schon wenige Minuten vor dem Umzug können dir Monate mit Mehrkosten ersparen.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, damit {{ opportunity.energieart }} beim Umzug kein Kostentreiber wird" -->
<!-- Preheader: "Schon wenige Minuten vor dem Umzug können dir Monate mit Mehrkosten ersparen." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>beim Umzug entscheiden oft wenige Minuten darüber, ob du später monatelang unnötig mehr zahlst.</p>
<p>So vermeidest du {{ opportunity.savings_text }}.</p>
<p>Wenn du das jetzt erledigst, ist ein großer Kostenpunkt direkt abgehakt.</p>
<p>Ein kurzer Blick reicht, um diesen Teil deines Umzugs sauber zu klären.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## neueinzug_06

**Subject:** {{ contact.first_name }}, ein klarer {{ opportunity.energieart }}-Schritt vor dem Umzug

**Preheader:** Mit einem kurzen Vergleich startest du ohne unnötige Mehrkosten.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, ein klarer {{ opportunity.energieart }}-Schritt vor dem Umzug" -->
<!-- Preheader: "Mit einem kurzen Vergleich startest du ohne unnötige Mehrkosten." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>damit beim Umzug nichts Wichtiges untergeht:</p>
<p>Damit vermeidest du {{ opportunity.savings_text }}.</p>
<p>Bei {{ opportunity.energieart }} ist jetzt entscheiden meist einfacher als später korrigieren.</p>
<p>Später kommen oft Kündigungsfristen oder laufende Standardtarife dazu.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## neueinzug_07

**Subject:** {{ contact.first_name }}, {{ opportunity.energieart }} vor dem Umzug schnell abhaken

**Preheader:** Ein kurzer Blick reicht oft, damit du ab Tag 1 passend aufgestellt bist.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, {{ opportunity.energieart }} vor dem Umzug schnell abhaken" -->
<!-- Preheader: "Ein kurzer Blick reicht oft, damit du ab Tag 1 passend aufgestellt bist." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>kurz bevor der Umzugstrubel losgeht:</p>
<p>Beim Umzug vermeidest du {{ opportunity.savings_text }}.</p>
<p>Gerade vor dem Umzug spart dir dieser kurze Schritt später unnötige Nacharbeit.</p>
<p>So bleibt {{ opportunity.energieart }} kein offener Punkt, wenn andere Themen wieder wichtiger werden.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## neueinzug_08

**Subject:** {{ contact.first_name }}, beim Umzug zählt {{ opportunity.energieart }} ab Tag 1

**Preheader:** Wer erst später prüft, zahlt häufig unnötig weiter.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, beim Umzug zählt {{ opportunity.energieart }} ab Tag 1" -->
<!-- Preheader: "Wer erst später prüft, zahlt häufig unnötig weiter." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>gerade in der Umzugsphase wird {{ opportunity.energieart }} oft nach hinten geschoben.</p>
<p>So vermeidest du {{ opportunity.savings_text }}.</p>
<p>Je später du prüfst, desto länger kann ein teurer Starttarif unbemerkt weiterlaufen.</p>
<p>Ein kurzer Blick jetzt verhindert genau diesen unnötigen Kostenstart.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## neueinzug_09

**Subject:** {{ contact.first_name }}, bevor {{ opportunity.energieart }} im Umzug untergeht

**Preheader:** Gerade im Umzugstrubel geht dieses Thema schnell unter – dabei ist es schnell geklärt.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, bevor {{ opportunity.energieart }} im Umzug untergeht" -->
<!-- Preheader: "Gerade im Umzugstrubel geht dieses Thema schnell unter – dabei ist es schnell geklärt." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>nur eine kurze Erinnerung zu deinem Umzug:</p>
<p>Damit vermeidest du {{ opportunity.savings_text }}.</p>
<p>Wenn du es jetzt erledigst, startet der Alltag später ohne diese offene Baustelle.</p>
<p>Das Thema wirkt selten dringend – kostet später aber trotzdem unnötig Geld.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## neueinzug_10

**Subject:** {{ contact.first_name }}, letzter Umzugs-Check für {{ opportunity.energieart }}

**Preheader:** Ein letzter kurzer Blick gibt dir Klarheit und verhindert unnötige Mehrkosten.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, letzter Umzugs-Check für {{ opportunity.energieart }}" -->
<!-- Preheader: "Ein letzter kurzer Blick gibt dir Klarheit und verhindert unnötige Mehrkosten." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>letzter kurzer Hinweis rund um deinen Umzug:</p>
<p>Beim Umzug vermeidest du {{ opportunity.savings_text }}.</p>
<p>Das ist ein kleiner Schritt jetzt, der dir später Zeit und Geld spart.</p>
<p>Danach musst du dich mit diesem Punkt nicht nochmal beschäftigen.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## loop_01

**Subject:** {{ contact.first_name }}, was bei deinem {{ opportunity.energieart }}-Tarif auffällt

**Preheader:** Viele merken erst im Vergleich, wie viel beim laufenden Tarif liegen bleibt.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, was bei deinem {{ opportunity.energieart }}-Tarif auffällt" -->
<!-- Preheader: "Viele merken erst im Vergleich, wie viel beim laufenden Tarif liegen bleibt." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>du hattest bei uns eine {{ opportunity.energieart }}-Empfehlung angefragt.</p>
<p>Oft sieht man erst im direkten Vergleich, ob der aktuelle Tarif noch wirklich passt.</p>
<p>Die Empfehlung wurde bereits vorgefiltert – du musst nicht selbst durch Tarife gehen.</p>
<p>Ein kurzer Blick zeigt dir sofort, ob sich etwas ändern sollte.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## loop_02

**Subject:** {{ contact.first_name }}, passt dein {{ opportunity.energieart }}-Tarif noch?

**Preheader:** Preise und Bedingungen ändern sich – deshalb lohnt sich der kurze Vergleich.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, passt dein {{ opportunity.energieart }}-Tarif noch?" -->
<!-- Preheader: "Preise und Bedingungen ändern sich – deshalb lohnt sich der kurze Vergleich." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>bei {{ opportunity.energieart }} fällt der Unterschied oft erst im direkten Vergleich auf.</p>
<p>Gerade wenn Tarife sich bewegen, ist ein kurzer Blick besonders sinnvoll.</p>
<p>Du bekommst sofort Klarheit, ohne neu suchen oder alles erneut eingeben zu müssen.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## loop_03

**Subject:** Wann hast du {{ opportunity.energieart }} zuletzt verglichen?

**Preheader:** Viele lassen den Tarif laufen und merken den Unterschied erst später.

**Body:**

```html
<!-- Subject: "Wann hast du {{ opportunity.energieart }} zuletzt verglichen?" -->
<!-- Preheader: "Viele lassen den Tarif laufen und merken den Unterschied erst später." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>du hattest bei uns eine {{ opportunity.energieart }}-Empfehlung angefragt.</p>
<p>Viele merken erst spät, wie lange Tarife weiterlaufen – nicht, weil sie schlecht sind, sondern weil sie oft unverändert bleiben.</p>
<p>Ein kurzer Vergleich heute verhindert, dass dieser Abstand weiter mitläuft.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## loop_04

**Subject:** {{ contact.first_name }}, kennst du jemanden mit Energie-Thema?

**Preheader:** Dein persönlicher Link ist ideal zum Kopieren und Weitergeben per WhatsApp.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, kennst du jemanden mit Energie-Thema?" -->
<!-- Preheader: "Dein persönlicher Link ist ideal zum Kopieren und Weitergeben per WhatsApp." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>vielleicht kennst du gerade jemanden, der beim Tarifthema Unterstützung braucht.</p>
<p>Am einfachsten: Link kopieren und direkt weiterleiten, zum Beispiel per WhatsApp.</p>
<p>Hier ist dein persönlicher Link zum Kopieren und Teilen:</p>
<p><a href="{{ contact.empfehlungslink }}">Empfehlungslink kopieren</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## loop_05

**Subject:** {{ contact.first_name }}, deine {{ opportunity.energieart }}-Empfehlung auf einen Blick

**Preheader:** Ein direkter Vergleich zeigt oft schneller als gedacht, ob dein Tarif noch passt.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, deine {{ opportunity.energieart }}-Empfehlung auf einen Blick" -->
<!-- Preheader: "Ein direkter Vergleich zeigt oft schneller als gedacht, ob dein Tarif noch passt." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>deine {{ opportunity.energieart }}-Empfehlung kannst du weiterhin direkt ansehen.</p>
<p>Der Unterschied wird oft erst sichtbar, wenn man die Tarife einmal nebeneinanderlegt.</p>
<p>Dabei siehst du sofort, ob sich etwas ändern sollte oder ob dein Tarif noch passt.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## loop_06

**Subject:** {{ contact.first_name }}, eine Minute für {{ opportunity.energieart }}?

**Preheader:** Ein kurzer Vergleich schafft Klarheit, bevor das Thema wieder nach hinten rutscht.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, eine Minute für {{ opportunity.energieart }}?" -->
<!-- Preheader: "Ein kurzer Vergleich schafft Klarheit, bevor das Thema wieder nach hinten rutscht." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>kurzer Reminder zu deiner {{ opportunity.energieart }}-Anfrage.</p>
<p>Der nächste sinnvolle Schritt ist, die vorbereitete Empfehlung einmal kurz anzusehen.</p>
<p>So klärst du das Thema, bevor es im Alltag wieder untergeht.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## loop_07

**Subject:** {{ contact.first_name }}, was dein {{ opportunity.energieart }}-Vergleich jetzt zeigt

**Preheader:** Deine Empfehlung ist da – ein Blick zeigt, ob dein aktueller Tarif noch mithält.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, was dein {{ opportunity.energieart }}-Vergleich jetzt zeigt" -->
<!-- Preheader: "Deine Empfehlung ist da – ein Blick zeigt, ob dein aktueller Tarif noch mithält." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>deine {{ opportunity.energieart }}-Empfehlung ist schon für dich da.</p>
<p>Im direkten Vergleich siehst du schnell, ob sich dein aktueller Tarif noch lohnt.</p>
<p>Und das alles ohne neue Eingaben oder erneutes Vergleichen.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## loop_08

**Subject:** Viele prüfen {{ opportunity.energieart }} zu spät

**Preheader:** Wer zu spät schaut, lässt oft vermeidbare Kosten weiterlaufen.

**Body:**

```html
<!-- Subject: "Viele prüfen {{ opportunity.energieart }} zu spät" -->
<!-- Preheader: "Wer zu spät schaut, lässt oft vermeidbare Kosten weiterlaufen." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>ein kurzer Hinweis zu deinem {{ opportunity.energieart }}-Tarif.</p>
<p>Erst beim direkten Vergleich sieht man meistens, wie groß der Abstand inzwischen ist.</p>
<p>Genau dadurch summieren sich Unterschiede über Zeit.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## loop_09

**Subject:** {{ contact.first_name }}, dein Link kann heute direkt helfen

**Preheader:** Wenn jemand gerade umzieht oder vergleicht, kannst du den Link direkt weitergeben.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, dein Link kann heute direkt helfen" -->
<!-- Preheader: "Wenn jemand gerade umzieht oder vergleicht, kannst du den Link direkt weitergeben." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>kurzer Hinweis: Dein persönlicher Empfehlungslink ist aktiv.</p>
<p>Am besten funktioniert er, wenn du ihn direkt kopierst und weiterleitest.</p>
<p>Diesen Link kannst du direkt per WhatsApp weitergeben:</p>
<p><a href="{{ contact.empfehlungslink }}">Link für WhatsApp kopieren</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## loop_10

**Subject:** {{ contact.first_name }}, bleibt dein {{ opportunity.energieart }}-Tarif die beste Wahl?

**Preheader:** Wenn Preise sich bewegen, lohnt sich ein schneller Abgleich besonders.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, bleibt dein {{ opportunity.energieart }}-Tarif die beste Wahl?" -->
<!-- Preheader: "Wenn Preise sich bewegen, lohnt sich ein schneller Abgleich besonders." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>deine {{ opportunity.energieart }}-Empfehlung kannst du jederzeit direkt aufrufen.</p>
<p>Gerade bei Preisänderungen zeigt der Vergleich schnell, ob dein aktueller Tarif noch vorne liegt.</p>
<p>Auch dann, wenn sich für dich im Alltag gerade nichts aktiv verändert hat.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## loop_11

**Subject:** {{ contact.first_name }}, {{ opportunity.energieart }} kurz prüfen und abhaken

**Preheader:** Du bekommst schnelle Klarheit, ohne lange Suche oder neue Eingaben.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, {{ opportunity.energieart }} kurz prüfen und abhaken" -->
<!-- Preheader: "Du bekommst schnelle Klarheit, ohne lange Suche oder neue Eingaben." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>nur ein kurzer Check-in zu deinem {{ opportunity.energieart }}-Tarif.</p>
<p>Ein direkter Vergleich zeigt dir schnell, ob noch alles gut passt.</p>
<p>Dafür musst du dich nicht erneut einarbeiten oder neu suchen.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## loop_12

**Subject:** {{ contact.first_name }}, bevor das Thema {{ opportunity.energieart }} wieder liegen bleibt

**Preheader:** Deine Empfehlung ist noch da – ein kurzer Blick spart dir späteres Nacharbeiten.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, bevor das Thema {{ opportunity.energieart }} wieder liegen bleibt" -->
<!-- Preheader: "Deine Empfehlung ist noch da – ein kurzer Blick spart dir späteres Nacharbeiten." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>bevor {{ opportunity.energieart }} im Alltag wieder untergeht, hier ein kurzer Hinweis.</p>
<p>Einmal kurz prüfen ist meist der schnellste Weg zu Klarheit.</p>
<p>Später kostet dich das Thema oft mehr Zeit als dieser kurze Moment jetzt.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## loop_13

**Subject:** {{ contact.first_name }}, jetzt siehst du in 1 Minute, ob {{ opportunity.energieart }} noch passt

**Preheader:** Wenn der Tarif lange läuft, merkt man Unterschiede oft erst spät.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, jetzt siehst du in 1 Minute, ob {{ opportunity.energieart }} noch passt" -->
<!-- Preheader: "Wenn der Tarif lange läuft, merkt man Unterschiede oft erst spät." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>dein {{ opportunity.energieart }}-Tarif bleibt im Alltag oft ohne Anpassung bestehen.</p>
<p>Gerade deshalb lohnt sich dieser eine kurze Blick jetzt.</p>
<p>Du siehst sofort, ob du gerade zu viel bezahlst, statt dich später nochmal damit beschäftigen zu müssen.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## loop_14

**Subject:** {{ contact.first_name }}, dein Empfehlungslink zum Weitergeben

**Preheader:** Einmal kopieren, weiterleiten, helfen: Dein Link ist direkt einsatzbereit.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, dein Empfehlungslink zum Weitergeben" -->
<!-- Preheader: "Einmal kopieren, weiterleiten, helfen: Dein Link ist direkt einsatzbereit." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>wenn jemand in deinem Umfeld beim Energiethema unsicher ist, kannst du direkt helfen.</p>
<p>Am schnellsten hilfst du, wenn du den Link direkt kopierst und weitergibst.</p>
<p>Hier ist dein Empfehlungslink zum Weitergeben:</p>
<p><a href="{{ contact.empfehlungslink }}">Link kopieren und teilen</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```

## loop_15

**Subject:** {{ contact.first_name }}, letzter Hinweis zu deiner {{ opportunity.energieart }}-Empfehlung

**Preheader:** Bevor das Thema wieder untergeht: Ein kurzer Vergleich bringt dir sofort Klarheit.

**Body:**

```html
<!-- Subject: "{{ contact.first_name }}, letzter Hinweis zu deiner {{ opportunity.energieart }}-Empfehlung" -->
<!-- Preheader: "Bevor das Thema wieder untergeht: Ein kurzer Vergleich bringt dir sofort Klarheit." -->
<html>
<body>
<p>Hallo {{ contact.first_name }},</p>
<p>letzter Hinweis zu deiner {{ opportunity.energieart }}-Anfrage.</p>
<p>Ein kurzer Blick jetzt klärt, ob dein aktueller Tarif noch wirklich passt.</p>
<p>Danach ist das Thema sauber eingeordnet, statt weiter im Alltag liegen zu bleiben.</p>
<p>Hier kannst du dir deine {{ opportunity.energieart }}-Empfehlung direkt ansehen und vergleichen: <a href="{{ opportunity.offer_url }}">{{ opportunity.cta_text }}</a></p>
<p>Viele Grüße<br>{{custom_values.absender_name}}</p>
<p style="font-size:12px; line-height:1.45; color:#555555; margin-top:8px;">
<strong>{{custom_values.brandname}}</strong><br>
<img src="{{custom_values.logo}}" alt="{{custom_values.brandname}} Logo" style="display:block; max-width:90px; height:auto; margin:6px 0;">
{{custom_values.strae_und_hausnummer}}<br>
{{custom_values.plz_und_stadt}}<br>
<a href="{{custom_values.impressum_url}}">Impressum</a> · <a href="{{custom_values.datenschutz_url}}">Datenschutz</a><br>
{{custom_values.absender_email}}
</p>
</body>
</html>

```
