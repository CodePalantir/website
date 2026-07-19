---
layout: revshort
title: "Erst das Datenmodell, dann die Flows"
description: "Der Wunsch klingt immer gleich. Mehr automatisieren, weniger Handarbeit, am besten noch diesen Monat. Verständlich, und ein Flow ist ja auch schnell..."
date: 2026-05-29
read_time: "2 Min. Lesezeit"
category: "Data"
hero_icon: "database"
lang: de
translation: /revshorts/077-erst-das-datenmodell-dann-die-flows/
---

Der Wunsch klingt immer gleich. Mehr automatisieren, weniger Handarbeit, am besten noch diesen Monat. Verständlich, und ein Flow ist ja auch schnell gebaut. Nur automatisiert ihr damit auf dem Datenmodell, das ihr habt. Wenn das schief ist, macht Automatisierung den Fehler nicht behebbar, sondern permanent.

Eine Szene aus einem Audit letztes Jahr. Ein Softwareunternehmen führt Verträge als Freitextfelder auf dem Account: Laufzeit, Volumen, Kündigungsfrist, alles in Textspalten, weil vor vier Jahren niemand ein eigenes Vertragsobjekt anlegen wollte. Ging ja auch erstmal. Inzwischen hängen 19 Automatisierungen an diesen Feldern: Renewal-Erinnerungen, eine Provisionslogik, zwei Board-Reports, eine Schnittstelle zum Billing. Jetzt soll ein sauberes Vertragsobjekt her, mehrere Verträge pro Kunde, Historie, das Übliche. Der Umbau kostet nicht die zwei Stunden von damals. Er kostet sechs Wochen, weil jede der 19 Automatisierungen angefasst, umgebaut und getestet werden muss. Das ist der Zinseszins auf ein schiefes Fundament.

Jeder Flow ist eine Wette darauf, dass die Struktur darunter stimmt. Objekte, Felder, Beziehungen: Das ist die Statik. Automatisierung ist der Beton, den man drumherum gießt. Beton um ein gerades Fundament trägt. Beton um ein schiefes Fundament sorgt dafür, dass man es nie wieder geradeziehen kann, jedenfalls nicht ohne Presslufthammer.

Die richtige Reihenfolge ist unspektakulär. Erst die Objekte: Was sind eure Dinge? Kunden, Standorte, Verträge, Abos, Geräte, was auch immer euer Geschäft strukturiert. Dann die Felder: Was müsst ihr über diese Dinge wissen, und in welchem Format? Dann die Beziehungen: Hängt der Vertrag am Account oder an der Opportunity, kann ein Kontakt zu mehreren Firmen gehören? Erst wenn das steht, kommen Flows. Klingt nach Lehrbuch, wird trotzdem in neun von zehn Orgs andersherum gemacht, weil ein Flow in der Demo glänzt und ein Datenmodell auf keinem Screenshot gut aussieht.

Der Test ist einfach. Malt euer Datenmodell auf ein Whiteboard, mit Kästen und Linien. Wenn dabei Streit entsteht, was ein Account ist oder wo Verträge leben: kein einziger neuer Flow, bis das geklärt ist. Jede Automatisierung, die vorher live geht, gießt den Streit in Beton.

Ist das langsamer? Am Anfang, ja. Zwei Wochen Modellarbeit fühlen sich zäh an neben einem Flow, der Freitag deployt wird. Aber ihr baut nur einmal. Die Alternative baut dreimal und reißt zweimal ab.

Was in eurem System würdet ihr heute anders modellieren, und wie viele Automatisierungen halten euch genau davon ab?
