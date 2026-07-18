---
layout: revshort
title: "Euer CRM hat technische Schulden, ihr nennt sie nur nicht so"
description: "Entwickler haben für ein bestimmtes Phänomen ein Wort: technische Schulden. Der schnelle Fix, der eigentlich ein Provisorium war und jetzt seit drei..."
date: 2026-07-04
read_time: "2 Min Read"
category: "Integration"
hero_icon: "git-branch"
---

Entwickler haben für ein bestimmtes Phänomen ein Wort: technische Schulden. Der schnelle Fix, der eigentlich ein Provisorium war und jetzt seit drei Jahren in Produktion läuft. Jeder kennt das Konzept aus Software. Fast niemand wendet es auf sein CRM an.

Dabei ist euer CRM eine Codebase. Schaut rein. Das Pflichtfeld, das 2022 für eine Kampagne angelegt wurde und seitdem mit "n/a" befüllt wird, weil sonst der Speichern-Button streikt. Der Flow, der einen anderen Flow triggert, der ein Feld setzt, das ein dritter Flow wieder überschreibt, und keiner weiß mehr, in welcher Reihenfolge. Die Validierungsregel, die jemand deaktiviert hat, "nur kurz", vor vierzehn Monaten. Workarounds auf Workarounds, jeder einzelne damals vernünftig, in Summe ein Minenfeld.

Und wie bei Code zahlt ihr Zinsen. Nicht irgendwann, sondern jeden Monat. Die Zinsen heißen: Reports, denen niemand traut. Ein Onboarding, in dem der neue Rep lernt, welche Felder man ignorieren muss. Und die teuerste Form von allen, die Angst vor Änderungen. Wenn eure Admins bei der Frage "können wir das Stage-Modell anpassen?" den Blick senken, weil niemand weiß, was dann alles bricht, dann ist das keine Vorsicht. Das ist Zahlungsunfähigkeit in Zeitlupe.

Der Unterschied zu einer echten Codebase: Dort gibt es wenigstens die Idee eines Refactoring-Budgets. Gute Engineering-Teams reservieren einen festen Anteil ihrer Kapazität, um Altlasten abzubauen, bevor sie neue Features bauen. Im CRM? Null. Jedes Quartal kommt ein neues Feld dazu, eine neue Automatisierung, ein neues Tool mit eigener Integration. Es wird nur eingezahlt, nie getilgt. Kein Wunder, dass die Orgs nach fünf Jahren aussehen wie ein Legacy-Monolith, den keiner mehr anfassen will.

Wir haben mal eine Org auditiert mit 340 Reports. Zwölf davon wurden im letzten Quartal geöffnet. 340 gebaut, zwölf genutzt, und trotzdem traute sich niemand zu löschen, denn was, wenn Report Nummer 218 doch irgendwo gebraucht wird? Genau so klingt Zinslast.

Die Tilgung ist übrigens kein Hexenwerk. Feld-Inventur, tote Automatisierungen abschalten, Abhängigkeiten dokumentieren, dann in Schichten aufräumen. Unbequem, ja. Aber messbar, endlich, und danach kann man wieder ändern, ohne zu beten.

Fragt euer Team mal, welche Änderung im CRM sie seit über einem Jahr aufschieben, weil sie sich nicht trauen. Diese eine Antwort sagt euch mehr über euren Zinssatz als jedes Dashboard.
