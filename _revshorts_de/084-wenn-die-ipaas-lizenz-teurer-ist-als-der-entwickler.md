---
layout: revshort
title: "Wenn die iPaaS-Lizenz teurer ist als der Entwickler"
description: "Der Pitch von iPaaS war mal bestechend: klicken statt coden, jeder Admin baut Integrationen, keine teuren Entwickler nötig. Zehn Jahre später ist die..."
date: 2026-06-05
read_time: "2 Min. Lesezeit"
category: "AI"
hero_icon: "sparkles"
lang: de
translation: /revshorts/084-wenn-die-ipaas-lizenz-teurer-ist-als-der-entwickler/
---

Der Pitch von iPaaS war mal bestechend: klicken statt coden, jeder Admin baut Integrationen, keine teuren Entwickler nötig. Zehn Jahre später ist die Rechnung gekippt. Nachgerechnet hat sie kaum jemand, weil die Lizenz still im Hintergrund mitwächst und der Vergleichswert fehlt.

Also rechnen wir. Fall aus einem Audit letztes Jahr: Firma mit 80 Leuten, Workato-Vertrag über 46.000 Euro im Jahr. Darauf laufen 14 Rezepte, die im Kern drei Dinge tun: CRM mit dem Billing abgleichen, Leads anreichern und routen, Bestandsdaten in ein Reporting schieben. Die Preislogik ist aufgabenbasiert, jeder verarbeitete Datensatz zählt, und weil das Geschäft wächst, wächst die Rechnung mit. Erfolg wird hier direkt besteuert.

Die Alternative: ein Senior-Entwickler baut dieselben Flüsse als Custom-Middleware. Sagen wir großzügig 25 Projekttage, macht rund 30.000 Euro einmalig, danach Hosting und ein Wartungsbudget von vielleicht 400 Euro im Monat. Nach 14 Monaten ist der Break-even durch, ab Jahr zwei spart die Firma jährlich 40.000 Euro, und die Kostenkurve ist flach statt volumengekoppelt. Das ist die ganze Rechnung. Kein Glaubenskrieg nötig.

Geld ist dabei nur das halbe Argument. Custom-Code lebt in Git, hat Tests, Code Review, eine Deploy-Pipeline und einen Rollback, wenn etwas schiefgeht. Und das Rezept im iPaaS? Wird live editiert, am offenen Herzen, von der einen Person, die das Tool versteht. Versionierung heißt dort oft: Kopie anlegen und hoffen. Wer schon mal um 17 Uhr eine Mapping-Änderung in einem Produktiv-Rezept gemacht hat, kennt das Gefühl im Magen.

Jetzt die ehrliche Einschränkung, denn ohne die wäre das Reseller-Logik mit umgekehrtem Vorzeichen. iPaaS hat seinen Platz. Drei simple Flüsse, Standardkonnektoren reichen, kein Entwickler im Haus und keiner buchbar: nehmt Make oder Zapier für ein paar hundert Euro im Monat und seid zufrieden. Der Kipppunkt kommt mit der Komplexität. Eigene Fehlerbehandlung, Mapping-Tabellen, Bedingungen über fünf Systeme hinweg, Logik, die jemand testen können muss. Ab da kämpft ihr gegen das Tool statt mit ihm, und ihr zahlt für den Kampf auch noch Enterprise-Preise.

Die Faustregel ist unbequem einfach. Sobald eure iPaaS-Jahresrechnung die Kosten eines soliden Entwicklerprojekts übersteigt, finanziert ihr ein Abo für etwas, das ihr einmal hättet bauen können. Holt euch die Rechnung. Legt sie neben ein Angebot. Der Rest ergibt sich.
