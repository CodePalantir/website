---
layout: revshort
title: "Freitextfelder sind der Ort, wo Reporting stirbt"
description: "Öffnet mal das Feld 'Region' in eurem CRM und schaut, was drinsteht. München. Muenchen. MUC. Munich, weil ein Kollege das englische Tastaturlayout..."
date: 2026-05-25
read_time: "2 Min Read"
category: "Data"
hero_icon: "database"
---

Öffnet mal das Feld "Region" in eurem CRM und schaut, was drinsteht. München. Muenchen. MUC. Munich, weil ein Kollege das englische Tastaturlayout hatte. Bayern, weil jemand großzügig dachte. Süd, aus der Zeit vor der Gebietsreform 2024. Sechs Schreibweisen, eine Stadt, null Auswertbarkeit.

Und dann wundert sich jemand, warum der Umsatz-nach-Region-Report nicht stimmt.

Das Muster ist immer dasselbe. Ein Feld wird angelegt, schnell, zwischen zwei Meetings, als Freitext, weil Freitext keine Diskussion braucht. Picklist hieße ja: jemand müsste entscheiden, welche Werte erlaubt sind. Also lieber offen lassen. Drei Jahre später hat das Feld 214 verschiedene Werte für 16 tatsächliche Regionen, und jede Auswertung beginnt mit einer Stunde Excel-Putzarbeit, die jedes Mal jemand anders macht, jedes Mal leicht anders.

Freitext fühlt sich nach Freiheit an. Stimmt auch, für den, der tippt. Für den, der auswertet, ist es Archäologie.

Die Lösung klingt banal und ist es nicht: Picklists mit Ownership. Nicht einfach Dropdowns, sondern Dropdowns, für die ein Mensch verantwortlich ist. Wer darf Werte hinzufügen? Was passiert mit alten Werten, wenn sich Gebiete ändern? Wie werden Bestandsdaten migriert? Das sind keine technischen Fragen, das sind Governance-Fragen, und genau deshalb drückt sich jeder davor.

Natürlich gibt es Felder, die Freitext sein müssen. Notizen. Kontext. Das, was der Kunde wörtlich gesagt hat. Alles, worüber ihr nie einen Report bauen werdet. Die Faustregel ist simpel: Wenn ein Feld jemals in einem Filter, einer Gruppierung oder einem Chart landen soll, ist Freitext die falsche Antwort. Und "jemals" kommt schneller, als man denkt.

Der eigentliche Punkt liegt eine Ebene tiefer. Jede Auswertung, die ihr in zwei Jahren fahren wollt, wird heute bei der Feldanlage entschieden. Das Dashboard ist nur das Ende der Kette. Wer bei der Anlage schludert, kann hinten polieren, so viel er will, die Daten geben es nicht her. Reporting-Probleme sind fast nie Reporting-Probleme. Es sind Feldanlage-Probleme mit zwei Jahren Verzögerung.

Deshalb: neues Feld, drei Fragen. Wird das jemals ausgewertet? Wer besitzt die Werteliste? Was passiert mit den Altdaten? Dauert zwei Minuten. Die Alternative kostet, konservativ geschätzt, eine Stunde pro Monat für jeden, der mit dem Feld arbeiten muss.

Wie viele eurer Freitextfelder wären heute Picklists, wenn bei der Anlage jemand zwei Minuten nachgedacht hätte?
