---
layout: revshort
title: "Der Sync fiel aus, und keiner wusste warum"
description: "Dienstagmorgen, die Dashboards sind leer. Der Sync zwischen Shop und CRM lief nachts nicht durch, im Log steht sowas wie 'REQUEST_LIMIT_EXCEEDED', und..."
date: 2026-06-03
read_time: "2 Min. Lesezeit"
category: "Integration"
hero_icon: "git-branch"
lang: de
translation: /revshorts/082-der-sync-fiel-aus-und-keiner-wusste-warum/
---

Dienstagmorgen, die Dashboards sind leer. Der Sync zwischen Shop und CRM lief nachts nicht durch, im Log steht sowas wie "REQUEST_LIMIT_EXCEEDED", und der Kollege, der die Integration vor zwei Jahren gebaut hat, sagt den Satz, der alles erklärt: "Wusste gar nicht, dass es da ein Limit gibt."

Jede API hat Limits. Salesforce zählt Calls pro 24 Stunden, gestaffelt nach Edition und Lizenzen. HubSpot drosselt pro 10 Sekunden. Stripe, Shopify, jedes Marketing-Tool: überall Kontingente, Drosselungen, Concurrency-Grenzen. Das ist keine Schikane, das ist Physik geteilter Infrastruktur, und es steht in jeder Doku auf den ersten Seiten. Trotzdem werden Integrationen reihenweise so gebaut, als wäre die API ein unendlicher Wasserhahn. Ein Datensatz, ein Call, in der Schleife, 80.000 Mal. Läuft im Test mit 50 Datensätzen wunderbar. Läuft in Produktion drei Monate lang auch, bis die Datenmenge wächst, ein zweites Team eine eigene Automatisierung ans selbe Kontingent hängt und beide sich nachts gegenseitig das Budget wegfressen.

Das Ärgerliche daran: Die Lösungen sind Lehrbuchstoff. Batching, also 200 Datensätze pro Call statt einem, reduziert den Verbrauch um den Faktor 200, die meisten APIs bieten Bulk-Endpunkte genau dafür an. Backoff heißt, dass die Integration bei einer Drosselung nicht stur sofort nochmal anklopft, sondern wartet, mit wachsenden Abständen, und sich danach sauber weiterarbeitet statt den halben Import zu verlieren. Dazu ein Monitoring, das den Kontingentverbrauch anzeigt, bevor er bei 100 Prozent steht. Nichts davon ist exotisch. Es muss nur am Anfang eingeplant werden, nicht am Ende.

Und genau da verläuft die Linie zwischen Bastelei und Engineering. Der Bastler fragt: Kriege ich die Daten von A nach B? Der Ingenieur fragt: Was passiert bei 10-facher Datenmenge, was passiert, wenn die Gegenseite drosselt, was passiert, wenn der Job mittendrin stirbt, und woran merken wir es? Beide Integrationen sehen in der Demo identisch aus. Der Unterschied zeigt sich erst nachts um drei, Monate später, und dann steht er nicht im Angebot von damals, sondern im Postmortem von heute.

Limits, Batching und Backoff gehören ins Integrationsdesign, auf Seite eins, neben das Datenmapping. Wer sie erst im Incident kennenlernt, hat keine Integration gekauft, sondern einen Prototyp im Dauereinsatz. Wisst ihr eigentlich, wie viel von eurem API-Kontingent heute Nacht verbraucht wurde und wovon?
