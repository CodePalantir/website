---
layout: revshort
title: "Eure Support-Tickets wissen vom Churn, bevor CS es tut"
description: "Rekonstruieren wir mal eine Kündigung, die angeblich aus dem Nichts kam. Sechs Wochen vorher: erstes Ticket, Exportfunktion liefert falsche Zahlen...."
date: 2026-05-17
read_time: "2 Min Read"
category: "Data"
hero_icon: "database"
---

Rekonstruieren wir mal eine Kündigung, die angeblich aus dem Nichts kam. Sechs Wochen vorher: erstes Ticket, Exportfunktion liefert falsche Zahlen. Zwei Tage später das nächste, gleiche Ecke des Produkts. Dann eines mit dem Satz "das hatten wir doch letzten Monat schon mal gemeldet". Woche vier: ein neuer Name taucht in den Tickets auf, der Abteilungsleiter schreibt jetzt selbst. Ton wird knapper. Woche fünf: Eskalation, CC an die Geschäftsführung. Woche sieben: Kündigung. Im CRM stand der Account die ganze Zeit auf grün.

Das Muster war komplett sichtbar. Häufung, wiederkehrende Themen, Tonalitätswechsel, neue Absender mit mehr Hierarchie, Eskalation. Jeder Support-Mitarbeiter, der die Tickets nacheinander gelesen hätte, hätte gesagt: Da brennt es. Nur liest niemand Tickets nacheinander pro Account. Der Support arbeitet die Queue ab, Ticket für Ticket, gemessen an Antwortzeit und Lösungsquote. Sein System belohnt schnelles Schließen, nicht Mustererkennung. Und der CSM, der das Muster erkennen müsste, lebt in einem anderen Werkzeug und sieht von alledem nichts.

Genau da liegt der Fehler, und er ist kein Prozessfehler, sondern ein Datenfehler. Zendesk oder Freshdesk kennen jedes einzelne Ticket, das CRM kennt den Vertrag, und dazwischen existiert keine Leitung, die aus Einzelfällen ein Account-Bild macht. Dabei ist die Verbindung technisch unspektakulär. Tickets pro Account aggregieren, rollierend über 30 und 90 Tage, dazu Eskalationen und Wiederöffnungen zählen. Wer mag, legt eine Sentiment-Bewertung über die Texte, das ist 2026 ein gelöstes Problem. Daraus entstehen drei, vier Felder am Account: Ticketfrequenz gegen den eigenen Normalwert, offene Eskalationen, Tendenz. Springt die Frequenz auf das Dreifache, bekommt der CSM eine Aufgabe, keinen Report zum Selbersuchen.

Der Einwand kommt verlässlich: Viele Tickets heißen doch nicht automatisch Unzufriedenheit, engagierte Kunden melden auch viel. Stimmt. Deshalb zählt nicht die absolute Zahl, sondern die Abweichung vom eigenen Muster plus die Begleitsignale. Ein Kunde, der immer fünf Tickets im Monat schreibt, ist bei fünf Tickets gesund. Einer, der nie schreibt und plötzlich viermal pro Woche, hat ein Thema.

Die bittere Pointe: Die meisten Firmen bezahlen bereits für jedes System, das dafür nötig ist. Es fehlt nur die Strecke dazwischen. Wie viele eurer letzten zehn Kündigungen hätte ein simpler Blick in die Tickethistorie angekündigt?
