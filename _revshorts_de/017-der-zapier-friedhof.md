---
layout: revshort
title: "Der Zapier-Friedhof"
description: "Bestandsaufnahme bei einem Kunden, 60 Leute, solide gewachsen: 47 Zaps. Gebaut über vier Jahre von vier verschiedenen Leuten, von denen zwei nicht mehr..."
date: 2026-03-30
read_time: "2 Min. Lesezeit"
category: "Integration"
hero_icon: "git-branch"
lang: de
translation: /revshorts/017-der-zapier-friedhof/
---

Bestandsaufnahme bei einem Kunden, 60 Leute, solide gewachsen: 47 Zaps. Gebaut über vier Jahre von vier verschiedenen Leuten, von denen zwei nicht mehr in der Firma sind. Dokumentation existiert nicht, Namenskonventionen auch nicht, ein Zap heißt "Test Kopie 2 FINAL". Und einer davon, der die Deals ans Rechnungstool übergibt, schlägt seit drei Wochen still fehl, weil irgendwer im CRM ein Feld umbenannt hat. Gemerkt hat es niemand. Aufgefallen ist es erst, als ein Kunde anrief und fragte, wo seine Rechnung bleibt.

Das ist kein Zapier-Problem. Zapier und Make sind völlig legitime Werkzeuge, für Prototypen sogar die besten: In einer Stunde steht ein Workflow, den man erst mal beobachten kann, bevor man ihn richtig baut. Für Low-Volume-Kram, der beim Ausfall niemandem wehtut, die Slack-Nachricht bei neuen Deals, der Export in ein Sheet, spricht auch dauerhaft nichts dagegen.

Das Problem beginnt an einer klar benennbaren Grenze, und die heißt geschäftskritisch. Sobald ein Workflow Umsatz berührt, Leads routet, Rechnungen auslöst, Verträge anstößt, ändert sich die Anforderung fundamental. Nicht die Funktion ändert sich. Die Fehlerbehandlung.

Genau da liegt der Unterschied zwischen Automatisierungs-Kleber und Integrationsarchitektur. Kleber führt aus, solange alles gut geht. Architektur geht davon aus, dass Dinge schiefgehen, weil sie das tun. APIs haben Timeouts, Systeme haben Wartungsfenster, Kollegen benennen Felder um. Eine Integration, die das ignoriert, ist keine kleinere Version einer richtigen Integration. Sie ist eine tickende, nur weiß keiner, wie laut es knallt und wann.

Konkret heißt Architektur drei Dinge. Monitoring: Wenn etwas fehlschlägt, geht innerhalb von Minuten ein Alert an einen Menschen, nicht in einen Log, den keiner liest. Retry-Logik: Ein Timeout um 3 Uhr nachts wird automatisch wiederholt statt kommentarlos verworfen, und was nach drei Versuchen noch failt, landet in einer Queue zur manuellen Klärung, damit kein Datensatz einfach verschwindet. Und Ownership: Ein Mensch mit Namen ist zuständig, kennt die Strecken, wird informiert, bevor jemand ein Feld anfasst. Ob darunter dann Make läuft, n8n, Workato oder Custom Code, ist ehrlich gesagt zweitrangig.

Die Frage an euren Stack ist deshalb nicht, welches Automatisierungstool ihr nutzt. Die Frage ist: Wenn heute Nacht eure wichtigste Strecke bricht, wer merkt es, und wann? Wenn die Antwort "der Kunde, nächste Woche" lautet, wisst ihr, was zu tun ist.
