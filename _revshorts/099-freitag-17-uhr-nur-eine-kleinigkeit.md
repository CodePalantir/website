---
layout: revshort
title: "Freitag, 17 Uhr, nur eine Kleinigkeit"
description: "Die Nachricht kommt immer zur gleichen Zeit. Freitag, kurz vor fünf: 'Kannst du noch schnell eine Validierungsregel auf die Opportunity setzen? Nur..."
date: 2026-06-20
read_time: "2 Min Read"
category: "Integration"
hero_icon: "git-branch"
---

Die Nachricht kommt immer zur gleichen Zeit. Freitag, kurz vor fünf: "Kannst du noch schnell eine Validierungsregel auf die Opportunity setzen? Nur eine Kleinigkeit, Montag ist Pipeline-Review." Der Admin will ins Wochenende, klickt die Regel zusammen, aktiviert sie, Feierabend.

Was die Regel am Wochenende macht, sieht niemand. Der nächtliche Import aus dem Webshop scheitert an ihr, still, 600 Datensätze bleiben liegen. Die Marketing-Automation versucht, Leads zu konvertieren, und läuft gegen dieselbe Wand. Montagmorgen ist die Pipeline fürs Review zwar formal sauberer, dafür fehlen ihr zwei Tage Daten, und drei Leute verbringen den Vormittag mit Fehlersuche statt mit dem Review, für das die Regel gedacht war.

Die Kleinigkeit gibt es im CRM nicht. Jede Validierungsregel, jeder neue Pflichtstatus, jede geänderte Automatisierung greift in ein System ein, an dem Integrationen, Imports und andere Automatisierungen hängen, und die halten sich nicht an Büroarbeitszeiten. Nachts läuft mehr in eurem CRM als tagsüber. Genau dann ist niemand da, der es merkt.

Software-Teams haben das vor zwanzig Jahren gelernt und Regeln daraus gemacht. Deployment-Fenster: Änderungen gehen Dienstag bis Donnerstag vormittags live, wenn Leute da sind, die reagieren können. Freeze-Zeiten: kein Deployment vor Wochenenden, keins in der letzten Woche des Quartals, wenn der Forecast steht und jede Statusänderung Zahlen verschiebt, über die am Montag der Beirat spricht. Und nichts geht direkt in Produktion, was nicht vorher in der Sandbox gegen die laufenden Integrationen getestet wurde.

Klingt nach Konzern-Bürokratie für eine Firma mit 60 Leuten? Ist das Gegenteil. Die Regeln passen auf eine halbe Seite und kosten nichts außer der Bereitschaft, einmal Nein zu sagen. "Gerne, geht Dienstagvormittag live" ist ein vollständiger Satz. Wer wirklich einen Notfall hat, kann eskalieren, aber dann heißt es auch Notfall und jemand bleibt dran, bis die Nachtläufe durch sind.

Der eigentliche Gewinn ist nicht das gerettete Wochenende des Admins, obwohl auch das zählt. Es ist die Datenqualität. Fast jede Datenleiche, die wir in Audits finden, hat einen Zeitstempel, und auffällig viele davon liegen zwischen Freitagabend und Montagfrüh.

Euer Fertigungsleiter würde nie freitags um fünf eine Maschine umbauen lassen und dann abschließen. Warum darf das im System passieren, in dem euer gesamter Umsatz entsteht?
