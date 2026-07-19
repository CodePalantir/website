---
layout: revshort
title: "Wem gehört eigentlich die Middleware?"
description: "Fast jede Firma, die wir auditieren, hat sie: die Integration, die ein Freelancer 2022 gebaut hat. Läuft auf einem Server, dessen Zugangsdaten in einem..."
date: 2026-06-07
read_time: "2 Min. Lesezeit"
category: "Integration"
hero_icon: "git-branch"
lang: de
translation: /revshorts/086-wem-gehoert-eigentlich-die-middleware/
---

Fast jede Firma, die wir auditieren, hat sie: die Integration, die ein Freelancer 2022 gebaut hat. Läuft auf einem Server, dessen Zugangsdaten in einem alten Slack-Thread stehen, oder als Make-Szenario im persönlichen Account von jemandem, der letztes Jahr gegangen ist. Sie verbindet CRM und Billing, oder Shop und CRM, oder alle drei. Sie läuft. Bis sie nicht mehr läuft.

Und dann passiert etwas Interessantes, nämlich eine sehr vorhersagbare Reihenfolge. Der Kunde merkt es zuerst: Die Auftragsbestätigung kommt nicht, die Rechnung fehlt, der Onboarding-Termin wird nie gebucht. Als Nächstes merkt es der Vertrieb, weil Deals im Forecast fehlen oder Zahlungsstatus auf "offen" stehen, die längst bezahlt sind. Ihr selbst merkt es zuletzt, oft erst, wenn der dritte Kunde anruft. Diese Reihenfolge ist kein Pech. Sie ist die logische Folge davon, dass eine Integration ohne Monitoring nur über Symptome auffällt, und Symptome entstehen nun mal draußen, beim Geld und beim Kunden.

Das Ownership-Loch hat System. Fürs CRM gibt es einen Admin. Für die Website ist Marketing zuständig. Fürs Billing die Buchhaltung. Aber der Datenfluss dazwischen, also genau die Stelle, an der Umsatzinformationen von einem System ins nächste wandern, gehört niemandem. "Läuft doch" ist kein Betriebsmodell. Es ist die Abwesenheit von einem.

Was ein Datenfluss braucht, ist überschaubar. Erstens einen Namen im Org-Chart, eine Person, kein Team, denn "das Team" ruft nachts niemand an. Zweitens Monitoring, das den Fehler meldet, bevor der Kunde ihn meldet: eine Fehlerqueue, in die gescheiterte Datensätze fallen statt zu verschwinden, ein Heartbeat, der Alarm schlägt, wenn der Sync still steht, ein Alert in einen Kanal, den jemand liest. Drittens eine Seite Dokumentation. Welche Flüsse gibt es, wo laufen sie, wo liegen die Credentials, was ist bei Fehler X zu tun. Das ist für eine typische Firma unserer Größe ein Nachmittag Arbeit pro Integration. Kein Projekt, ein Nachmittag.

Der Test ist einfach und tut ein bisschen weh. Öffnet euer Org-Chart und zeigt auf die Person, die gerufen wird, wenn der Sync zwischen CRM und Billing heute Nacht um zwei stehen bleibt. Zeigt euer Finger ins Leere, dann wisst ihr jetzt, wer es als Erstes merken wird. Nicht ihr.
