---
layout: revshort
title: "MRR aus Excel ist eine Meinung, keine Zahl"
description: "Monatsanfang. Jemand aus Finance exportiert die Rechnungen, öffnet die Excel-Vorlage vom Vormonat, passt drei Formeln an, zieht den einen Jahresvertrag..."
date: 2026-05-12
read_time: "2 Min Read"
category: "RevOps"
hero_icon: "zap"
---

Monatsanfang. Jemand aus Finance exportiert die Rechnungen, öffnet die Excel-Vorlage vom Vormonat, passt drei Formeln an, zieht den einen Jahresvertrag ab, der sonst alles verzerrt, und schickt die MRR-Zahl ans Management. Dauer: ein halber Tag. Ergebnis: eine Zahl, die jeden Monat leicht anders entsteht.

Genau das ist das Problem. Nicht der halbe Tag. Die wacklige Definition.

MRR klingt trivial und ist es nicht. Was passiert mit dem Kunden, der am 15. upgradet? Zählt der Rabatt im ersten Jahr? Ist der pausierte Vertrag Churn oder nicht? Wie geht ihr mit Setup-Fees um, mit Gutschriften, mit dem Kunden, der in Dollar zahlt? Jede dieser Fragen hat mehrere vertretbare Antworten. Solange die Antwort im Kopf der Person liegt, die gerade die Excel baut, ändert sie sich mit der Person, der Tagesform und dem Zeitdruck. Zwei Leute, dieselben Rohdaten, zwei verschiedene Churn-Raten. Beide können ihre Version begründen. Keine ist die Wahrheit.

Deshalb die harte Regel: Subscription-Metriken kommen definiert und automatisiert aus dem Billing-System, oder sie sind Meinung. Stripe Billing und Chargebee rechnen MRR, Churn und NRR von Haus aus, mit dokumentierten, stabilen Definitionen. Wer Sonderfälle hat oder es genauer will, zieht die Rohdaten ins Warehouse und schreibt die Logik einmal als Code, versioniert, nachlesbar, für immer gleich. Beides ist eine Sache von Tagen, nicht von Quartalen.

Der eigentliche Gewinn ist dabei nicht die gesparte Zeit. Es ist die Belastbarkeit der Zahl. Wenn die NRR im nächsten Bankgespräch oder in einer Due Diligence auseinandergenommen wird, schafft "das rechnet Kollegin Meier immer in Excel" kein Vertrauen. Eine Metrik, deren Herleitung im Billing-System oder im dbt-Modell steht, überlebt jede Nachfrage. Eine Excel mit 14 Tabs überlebt nicht mal die Frage, warum Zelle G47 hart überschrieben wurde. War bestimmt ein guter Grund. Weiß nur keiner mehr.

Und ja, die Excel fühlt sich flexibel an, das ist ihr ganzer Charme. Man kann eben schnell mal den Sonderfall rausrechnen. Aber diese Flexibilität ist exakt die Eigenschaft, die eine Metrik entwertet: Eine Zahl, die sich der Situation anpassen lässt, misst nichts mehr.

Die Diagnose kostet euch fünf Minuten. Fragt zwei Leute in der Firma nach der aktuellen MRR und nach der Definition von Churn. Kommen zwei verschiedene Antworten zurück, habt ihr keine Metriken. Ihr habt Folklore.
