---
layout: revshort
title: "Ein Feld, drei Bedeutungen, kein Report stimmt"
description: "Fragt drei Abteilungen, was im Feld 'Region' steht, und ihr bekommt drei Antworten. Marketing meint die Sprachregion der Kampagne, DACH als ein Block...."
date: 2026-05-23
read_time: "2 Min Read"
category: "Data"
hero_icon: "database"
---

Fragt drei Abteilungen, was im Feld "Region" steht, und ihr bekommt drei Antworten. Marketing meint die Sprachregion der Kampagne, DACH als ein Block. Sales meint das Vertriebsgebiet, also die Territory-Logik mit Nord, Süd und dem seltsamen Sonderfall Österreich, der historisch bei einem bestimmten AE liegt. Finance meint das Land der Rechnungsadresse, weil daran die Umsatzsteuer hängt.

Ein Feld. Drei Wahrheiten. Und jeder Report, der "Region" gruppiert, ist für zwei von drei Abteilungen falsch, ohne dass es jemand merkt.

Das Tückische daran: Alle Beteiligten handeln korrekt. Der Marketing-Kollege pflegt das Feld nach seiner Definition, der Sales-Kollege überschreibt es nach seiner, und Finance zieht sich die Daten und wundert sich, warum die Schweiz mal auftaucht und mal nicht. Es gibt keinen Schuldigen. Es gibt nur ein Feld, das nie definiert wurde, und ein Datenmodell, das drei Konzepte in eine Spalte quetscht, weil beim Anlegen vor fünf Jahren niemand nachgefragt hat.

Dasselbe Spiel läuft bei "Lead Source", wo Kampagne, Kanal und Erstkontakt durcheinandergehen. Bei "Kunde seit", wo keiner weiß, ob das Datum die erste Opportunity, den ersten Vertrag oder die erste Rechnung meint. Bei "MRR", das in einem Dashboard mit und im anderen ohne Rabatte gerechnet wird. Jedes Meeting, in dem zwei Teams mit unterschiedlichen Zahlen zum selben Thema aufschlagen, ist am Ende ein Semantik-Meeting. Man einigt sich mühsam, und beim nächsten Quartalsreview geht die Debatte von vorn los, weil die Einigung nirgendwo steht.

Die Lösung ist fast beleidigend simpel: ein Feld-Glossar. Pro kritischem Feld eine Definition, ein Owner, die erlaubten Werte, die Quelle der Befüllung und wer es ändern darf. Zwanzig Felder reichen für den Anfang, die anderen dreihundert sind es meist nicht wert. Das Dokument kostet zwei Workshops und lebt danach dort, wo eure Doku lebt. Kein Tool zu kaufen, keine Lizenz, keine Migration.

Und wenn das Glossar eine echte Kollision aufdeckt, wie bei "Region", dann ist die Antwort nicht die bessere Definition, sondern die Trennung: drei Felder für drei Konzepte, sauber benannt, automatisch befüllt, wo es geht. Ländercode aus der Rechnungsadresse ableiten kann jedes CRM.

Der ROI dieses Dokuments ist schwer zu bilanzieren und leicht zu spüren. Jede Zahlendebatte, die nicht stattfindet, weil man einfach nachschlagen kann, ist gewonnene Zeit. Wie viele eurer Meetings letzte Woche waren eigentlich Streit über Felddefinitionen?
