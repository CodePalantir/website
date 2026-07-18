---
layout: revshort
title: "Der Sync, der 3.000 Telefonnummern gelöscht hat"
description: "Montagmorgen, halb neun. Das SDR-Team öffnet die Anruflisten und das Feld Telefonnummer ist leer. Nicht bei einem Kontakt. Bei 3.000."
date: 2026-06-06
read_time: "2 Min Read"
category: "Integration"
hero_icon: "git-branch"
---

Montagmorgen, halb neun. Das SDR-Team öffnet die Anruflisten und das Feld Telefonnummer ist leer. Nicht bei einem Kontakt. Bei 3.000.

Was war passiert? Freitagabend ging der neue Sync live, Marketing-Tool und CRM, bidirektional, sauber gemappt, alle Felder verbunden. Im Marketing-Tool war das Telefonfeld bei fast allen Kontakten leer, weil es dort nie gepflegt wurde. Der Sync stand auf "Quellsystem gewinnt". Also hat er in der Nacht getan, was man ihm gesagt hat: 3.000 mühsam recherchierte, verifizierte, über Jahre gepflegte Nummern mit nichts überschrieben. Drei Jahre Datenarbeit, wegsynchronisiert in 40 Minuten.

Der Fehler ist nicht exotisch. Er ist der häufigste Integrationsfehler überhaupt, und er entsteht, weil bidirektionale Syncs als Mapping-Übung behandelt werden. Feld A auf Feld B, Haken dran, nächstes Feld. Die eigentliche Frage stellt niemand: Wem gehört dieses Feld? Ownership auf Feldebene heißt, für jedes synchronisierte Feld ein Master-System zu benennen. Telefonnummer gehört dem CRM, dort wird sie gepflegt, das Marketing-Tool darf lesen, nie schreiben. E-Mail-Opt-in gehört dem Marketing-Tool, aus rechtlichen Gründen sogar zwingend. Firmenname gehört vielleicht dem Enrichment-Tool. Das ist pro Feld eine Zeile in einer Tabelle und eine Entscheidung, die zehn Sekunden dauert. Bei 60 Feldern ein Vormittag.

Dazu kommen Konfliktregeln für die Fälle, in denen beide Seiten schreiben dürfen. Die wichtigste ist banal und wird trotzdem ständig verletzt: Leer überschreibt niemals gefüllt. Ein fehlender Wert ist keine Information, er ist die Abwesenheit einer Information, und Abwesenheit darf keine Daten töten. Zweite Regel: Neuer gewinnt nur mit echtem Zeitstempelvergleich auf Feldebene, nicht auf Datensatzebene, sonst zieht ein geändertes Anrede-Feld die alte Adresse gleich mit.

Und vor dem Go-Live gehört der Sync gegen eine Sandbox-Kopie gefahren, mit einem Diff-Report: Diese 4.200 Feldwerte würden sich ändern, hier die Stichprobe. Wer den Report liest, sieht die 3.000 leeren Telefonnummern, bevor sie passieren. Dazu ein voller Export als Backup, direkt vor dem Schalter. Gesamtaufwand für all das: ein bis zwei Tage. Der Schaden im echten Fall: drei Wochen Rekonstruktion aus Telefonanlagen-Logs und alten CSV-Exporten, plus ein SDR-Team, das eine Woche lang nicht wählen konnte.

Wenn zwei eurer Systeme sich widersprechen, wer gewinnt? Falls ihr die Antwort nicht kennt: Euer Sync kennt sie auch nicht. Er entscheidet trotzdem. Jede Nacht.
