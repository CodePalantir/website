---
layout: revshort
title: "Auch fehlerfreie Automatisierung kostet jeden Monat Geld"
description: "Der Flow läuft seit zwei Jahren ohne einen einzigen Fehler. Klingt nach einem abgeschlossenen Projekt. Ist es nicht."
date: 2026-07-11
read_time: "2 Min. Lesezeit"
category: "Integration"
hero_icon: "git-branch"
lang: de
translation: /revshorts/120-auch-fehlerfreie-automatisierung-kostet-jeden-monat-geld/
---

Der Flow läuft seit zwei Jahren ohne einen einzigen Fehler. Klingt nach einem abgeschlossenen Projekt. Ist es nicht.

Drei Kostenarten laufen weiter, unsichtbar, aber real. Verständnis: irgendjemand im Team muss wissen, was der Flow tut, warum er es tut und was passiert, wenn man ihn anfasst. Als die Kollegin ging, die ihn gebaut hat, ging dieses Wissen mit, und seitdem traut sich niemand an die Automatisierung, die den Opportunity-Status setzt. Wartung: die API, die der Flow aufruft, bekommt eine neue Version, das Feld, auf das er hört, wird umbenannt, das Tool am anderen Ende ändert nach einem Update sein Verhalten. Nichts davon ist ein Fehler im Flow, alles davon erzeugt Arbeit. Und die teuerste der drei, Abhängigkeiten: jeder neue Prozess muss um die bestehenden 40 Automatisierungen herumgebaut werden. Die Frage "können wir dieses Feld umbenennen" dauert in einer frischen Org fünf Minuten. In einer gewachsenen sind es zwei Tage Impact-Analyse.

Deshalb der Vorschlag: denkt in einem Komplexitätsbudget. Jede Automatisierung, jede Integration, jedes Custom-Feld gibt davon etwas aus, völlig unabhängig davon, ob es funktioniert. Das Budget ist endlich, es hängt an Größe und Seniorität eures Teams, und wenn es überzogen ist, merkt ihr das an einem klaren Symptom: einfache Änderungen dauern plötzlich Wochen, und niemand hat mehr das Gesamtsystem im Kopf.

Mit dieser Brille fallen Entscheidungen anders aus. Der Report, der einmal im Quartal gebraucht wird? Von Hand bauen, zwanzig Minuten, viermal im Jahr. Die Datenübergabe an ein Tool, das vielleicht nächstes Jahr rausfliegt? Ein CSV-Export reicht völlig. Der Genehmigungsschritt, bei dem sowieso ein Mensch draufschauen soll? Dann lasst den Menschen draufschauen, statt eine Logik zu bauen, die menschliches Urteil simuliert und dafür Sonderfälle produziert, die wieder jemand pflegen muss.

Manchmal ist der manuelle Schritt die richtige Architektur. Aus dem Mund einer Engineering-Firma klingt das vielleicht seltsam, aber es ist genau die Erfahrung aus den Orgs, die wir aufräumen: die schlimmsten sind nie die mit zu wenig Automatisierung. Es sind die mit 200 Flows, von denen 60 niemand mehr erklären kann.

Automatisiert wird, was häufig passiert, stabil definiert ist und nachweislich Zeit frisst. Der Rest bleibt manuell, bewusst und dokumentiert. Wie viel von eurem Komplexitätsbudget ist eigentlich schon ausgegeben, und wofür?
