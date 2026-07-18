---
layout: revshort
title: "Echtzeit ist ein Wunsch, keine Anforderung"
description: "'Das muss natürlich in Echtzeit laufen.' Der Satz fällt in fast jedem Integrationsworkshop, meist in den ersten zehn Minuten, und er wird fast nie..."
date: 2026-06-04
read_time: "2 Min Read"
category: "Integration"
hero_icon: "git-branch"
---

"Das muss natürlich in Echtzeit laufen." Der Satz fällt in fast jedem Integrationsworkshop, meist in den ersten zehn Minuten, und er wird fast nie hinterfragt. Klingt ja auch vernünftig. Wer will schon alte Daten?

Dann stellen wir die Gegenfrage: Welche Entscheidung wartet auf dieses Datum, und wie lange darf sie warten? Ab da wird es still im Raum. Der Zahlungsstatus aus dem Billing, der ins CRM zurückfließt, wird einmal am Tag von jemandem im Innendienst angeschaut. Das Management-Dashboard wird montags geöffnet. Die Anreicherung neuer Accounts mit Firmendaten muss fertig sein, bevor ein Mensch den Account anfasst, und das passiert frühestens Stunden später. Für gut 95 Prozent aller Datenflüsse ist ein Sync alle 15 Minuten kein Kompromiss. Er ist schlicht unsichtbar.

Der Unterschied im Aufwand ist dagegen sehr sichtbar. Echtzeit heißt eventgetrieben: Webhooks, die zuverlässig ankommen müssen, Retry-Logik für den Fall, dass die Gegenseite gerade nicht antwortet, Race Conditions, wenn zwei Events sich überholen, API-Limits, die bei Lastspitzen reißen. Alles lösbar. Alles teuer. Ein 15-Minuten-Batch ist demgegenüber langweilige, robuste Technik: alle Datensätze seit dem letzten Lauf holen, verarbeiten, wegschreiben, und was fehlschlägt, nimmt der nächste Lauf einfach nochmal mit. Testbar, nachvollziehbar, ein Zehntel der Komplexität. Und Komplexität ist bei Integrationen keine abstrakte Größe, sondern ziemlich exakt die Anzahl der Stellen, an denen es nachts um drei brechen kann.

Die Ausnahmen gibt es, und die soll man ernst nehmen. Speed-to-Lead ist echt: Liegt ein Demo-Request fünf Minuten unbearbeitet, sinkt die Erreichbarkeit messbar, dieser eine Fluss gehört eventgetrieben gebaut. Der Vertriebler, der beim Kunden im Termin sitzt und den aktuellen Vertragsstatus braucht, zählt auch. Nur sind das zwei, vielleicht drei Flüsse pro Firma. Nicht zwanzig.

Deshalb ein einfacher Vorschlag: Schreibt für jeden Datenfluss eine ehrliche Latenz-Anforderung auf. Keine Reflexantwort, sondern eine Zahl mit Begründung. "15 Minuten, weil der Report morgens um acht gezogen wird." "30 Sekunden, weil ein SDR anrufen soll, solange der Lead noch auf der Website ist." Wer diese Übung einmal durchzieht, stellt fest, dass die Liste fast komplett aus Viertelstunden besteht, und plötzlich schrumpft das Integrationsprojekt von sechs Monaten Event-Architektur auf drei Wochen solide Batch-Jobs.

"Sofort" ist keine Anforderung. Es ist die Abwesenheit einer Anforderung, und ihr bezahlt sie fünfstellig.
