---
layout: revshort
title: "Ihr ändert am offenen Herzen"
description: "Freitag, 16:40 Uhr. Der Admin baut noch schnell eine Validierungsregel ins Produktivsystem, weil Vertriebsleitung das bis Montag wollte. Kein Test,..."
date: 2026-05-31
read_time: "2 Min Read"
category: "Data"
hero_icon: "database"
---

Freitag, 16:40 Uhr. Der Admin baut noch schnell eine Validierungsregel ins Produktivsystem, weil Vertriebsleitung das bis Montag wollte. Kein Test, keine Sandbox, kein zweites Augenpaar. Speichern, Feierabend.

Montag um 9 kann kein Außendienstler mehr Opportunities schließen, weil die Regel ein Feld verlangt, das die Hälfte der Datensätze nie hatte. Zwei Stunden Vertriebsstillstand bei 15 Leuten, rechnet das mal in Pipeline um. Und das Absurde daran: In der IT nebenan würde niemand auf die Idee kommen, ungetesteten Code freitags direkt auf den Produktionsserver zu schieben. Da gibt es Staging, Reviews, Deployment-Fenster. Drei Räume weiter, im CRM, gilt das alles plötzlich nicht.

Warum eigentlich? Weil Klicken sich harmloser anfühlt als Coden. Eine Validierungsregel, ein Flow, ein neues Pflichtfeld, das ist doch nur Konfiguration. Ist es nicht. Ein Flow, der bei jedem Lead-Update feuert, ist Software. Er hat Abhängigkeiten, Seiteneffekte, Grenzfälle. Dass man ihn zusammenklickt statt tippt, ändert daran exakt nichts. Das CRM ist das System, in dem euer Umsatz verwaltet wird, und ihr behandelt es mit weniger Sorgfalt als die Firmenwebsite.

Der Einwand kommt immer sofort: Sandbox-Prozesse machen uns langsam, wir sind doch kein Konzern. Stimmt so nicht. Der Prozess für eine 50-Personen-Firma ist keine Deployment-Pipeline mit vier Freigabestufen. Er ist drei Gewohnheiten. Erstens: Änderungen an Logik, die andere Datensätze anfasst, werden in der Sandbox gebaut und mit echten Fällen durchgespielt, und zwar auch mit den hässlichen, den Datensätzen von 2021 mit halb leeren Feldern. Zweitens: Deployments haben ein Zeitfenster, und Freitagnachmittag gehört nicht dazu, weil dann niemand mehr da ist, der den Fehler bemerkt, bevor er ein Wochenende lang Daten verbiegt. Drittens: Jede Änderung wird irgendwo notiert, ein Satz reicht. Was, warum, wer.

Das kostet pro Änderung vielleicht 20 Minuten mehr. Ein einziger verhinderter Montagmorgen-Ausfall zahlt das für ein Jahr zurück, von den stillen Schäden ganz zu schweigen, den Automatisierungen, die wochenlang leise falsche Daten schreiben, bis es jemand im Forecast merkt.

Deployment-Disziplin ist keine Frage der Firmengröße, sondern der Frage, wie wichtig euch das System ist, das eure Deals verwaltet. Wann war eure letzte Änderung direkt in Produktion, und wer hat sie getestet außer dem Zufall?
