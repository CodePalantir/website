---
layout: revshort
title: "Agentur oder eigener Admin ist die falsche Frage"
description: "Die Frage kommt in fast jedem Erstgespräch: Sollen wir das CRM an eine Agentur geben oder jemanden einstellen? Als wäre das ein Entweder-oder. Beide..."
date: 2026-06-23
read_time: "2 Min Read"
category: "Integration"
hero_icon: "git-branch"
---

Die Frage kommt in fast jedem Erstgespräch: Sollen wir das CRM an eine Agentur geben oder jemanden einstellen? Als wäre das ein Entweder-oder. Beide Antworten sind falsch, wenn man sie pur nimmt.

Alles an die Agentur: Dann wird jedes neue Feld ein Ticket, jedes Ticket ein Dreitagesumlauf, und der Vertriebsleiter, der nur einen Statuswert umbenannt haben will, zahlt dafür anteilig einen Tagessatz. Nach einem Jahr kennt niemand im Haus das eigene System, und die Agentur wird vom Dienstleister zur Geisel-Situation mit Rechnungsstellung. Alles inhouse: Dann macht der eine Admin alles, vom Passwort-Reset bis zur Billing-Integration, und für die Integration fehlt ihm die Erfahrung, was aber erst auffällt, wenn sie in Produktion bricht. Beides schon oft gesehen. Beides teuer.

Die tragfähige Antwort ist eine Arbeitsteilung entlang einer klaren Linie. Intern gehört alles, was täglich anfällt und Nähe zum Geschäft braucht: Nutzerverwaltung, Reports, Feldanpassungen, Schulung, das Ohr an den Vertrieblern. Extern gehört alles, was selten, schwer und folgenreich ist: Datenmodell-Änderungen, Integrationen, Migrationen, größere Automatisierungslogik, alles, was man in fünf Jahren dreimal braucht und wofür sich internes Erfahrungsaufbauen schlicht nicht rechnet.

So weit, so vernünftig. Der Teil, der in der Praxis fehlt, ist ein anderer: Die Grenze muss vertraglich stehen, nicht nur im Kopf. Wer darf in Produktion deployen? Wer owned das Datenmodell, wer genehmigt Änderungen daran? Was passiert, wenn der interne Admin freitags eine Automatisierung anfasst, die die Agentur gebaut hat, und montags die Rechnungsübergabe steht? Ohne schriftliche Antwort auf diese Fragen bekommt ihr im Fehlerfall das übliche Theater: Die Agentur zeigt auf den Admin, der Admin auf die Agentur, und ihr zahlt die Fehlersuche, während beide Recht behalten.

Drei Sätze reichen oft. Datenmodell und Integrationen ändert nur der externe Partner, dokumentiert im System. Alles auf der Konfigurationsebene darüber gehört dem internen Admin, ohne Rückfrage. Übergaben passieren schriftlich mit Sandbox-Test, sonst gilt die Änderung als nicht abgenommen.

Klingt nach Vertragsprosa für etwas, das man doch auch kollegial regeln kann? Kollegial funktioniert genau bis zum ersten kaputten Quartalsabschluss.

Fragt euch nicht, ob Agentur oder Admin. Fragt, wo bei euch heute die Linie verläuft, und wer sie unterschrieben hat. Wenn die Antwort "nirgends" lautet, habt ihr keine Arbeitsteilung. Ihr habt Glück gehabt, bisher.
