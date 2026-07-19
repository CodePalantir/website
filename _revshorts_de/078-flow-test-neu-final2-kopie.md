---
layout: revshort
title: "Flow_Test_NEU_final2_KOPIE"
description: "Öffnet mal eure Automatisierungsliste. Nicht die Prozessdoku, die es sowieso nicht gibt. Die echte Liste im System."
date: 2026-05-30
read_time: "2 Min. Lesezeit"
category: "AI"
hero_icon: "sparkles"
lang: de
translation: /revshorts/078-flow-test-neu-final2-kopie/
---

Öffnet mal eure Automatisierungsliste. Nicht die Prozessdoku, die es sowieso nicht gibt. Die echte Liste im System.

Da steht dann sowas wie "Lead Update", "Lead Update 2", "Flow_Test_NEU_final2_KOPIE" und ein Workflow namens "Michael bitte nicht löschen". Michael hat die Firma 2023 verlassen. Niemand weiß, was das Ding tut, aber alle haben Angst, es anzufassen.

Das ist keine Anekdote, das ist der Normalzustand. In fast jeder Org, die wir auditieren, sind die Automatisierungen anonym. Sie haben Namen, klar, aber Namen, die nichts verraten: nicht welches Objekt sie anfassen, nicht was sie auslösen, nicht ob sie überhaupt noch aktiv gebraucht werden. Und dann passiert das, was immer passiert. Ein Feld wird plötzlich überschrieben, ein Lead landet beim falschen Team, eine E-Mail geht doppelt raus. Jetzt beginnt die Suche.

Mit sauberen Namen dauert die Suche zehn Minuten. Man filtert nach Objekt, liest die Namen, hat den Kandidaten. Ohne saubere Namen dauert sie drei Tage, weil man 47 Flows einzeln öffnen, durchklicken und im Kopf nachbauen muss, was sie tun. Drei Tage, in denen das Feld weiter überschrieben wird. Wir haben Debugging-Sessions erlebt, in denen die Hälfte der Zeit nicht ins Problem ging, sondern in die Archäologie: Was ist das hier überhaupt?

Naming Conventions sind Dokumentation zum Nulltarif. Das ist der eigentliche Punkt. Eine Prosa-Doku im Wiki veraltet in dem Moment, in dem sie geschrieben wird, weil sie neben dem System lebt und niemand sie nachzieht. Ein Name lebt im System selbst. "Lead_BeforeSave_SetRegion" sagt dir Objekt, Zeitpunkt und Zweck, ohne dass du den Flow öffnest. Kostet beim Anlegen fünf Sekunden Nachdenken. Spart bei jedem einzelnen Incident Stunden.

Die Convention selbst ist fast egal. Objekt zuerst oder Zweck zuerst, Unterstriche oder nicht, darüber kann man streiten, muss man aber nicht lange. Wichtig ist nur: eine Regel, konsequent, für alle. Auch für den Admin, der nur mal schnell was testet. Gerade für den, denn aus "mal schnell was testen" wird "final2_KOPIE", und aus "final2_KOPIE" wird Produktionslogik, auf der drei Jahre später euer Routing hängt.

Man erkennt am Zustand der Automatisierungsliste ziemlich genau, wie eine Org geführt wird. Nicht die Kultur-Slides, die Liste. Wie viele eurer Flows könntet ihr am Namen erkennen, ohne sie zu öffnen?
