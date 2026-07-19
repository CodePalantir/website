---
layout: revshort
title: "Hört auf, die Single Source of Truth zu jagen"
description: "Drei Leute, ein Meeting, eine Frage: wie viele aktive Kunden haben wir? Vertrieb sagt 214, Finance sagt 189, das CS-Tool sagt 240. Der Reflex darauf..."
date: 2026-07-12
read_time: "2 Min. Lesezeit"
category: "Integration"
hero_icon: "git-branch"
lang: de
translation: /revshorts/121-hoert-auf-die-single-source-of-truth-zu-jagen/
---

Drei Leute, ein Meeting, eine Frage: wie viele aktive Kunden haben wir? Vertrieb sagt 214, Finance sagt 189, das CS-Tool sagt 240. Der Reflex darauf ist der Satz, der in jedem zweiten RevOps-Zielbild steht: wir brauchen endlich eine Single Source of Truth.

Nur gibt es die nicht. Hat noch niemand gebaut, wird niemand bauen, und die Gründe sind strukturell, nicht handwerklich. Euer Billing weiß über Zahlungen mehr, als das CRM je wissen wird. Produkt-Analytics kennt die Nutzung, das CRM kennt die Beziehung, der Support kennt die Schmerzen. Jedes dieser Systeme hat seine Datenhoheit aus gutem Grund, weil dort der Prozess lebt, der die Daten erzeugt. Wer trotzdem alles an einen Ort zwingen will, landet entweder in einem Warehouse-Projekt, das nach 18 Monaten immer noch nicht fertig ist, oder bei einem CRM mit 900 Feldern, von denen zwei Drittel leer sind.

Das erreichbare Ziel ist bescheidener und deutlich wertvoller: pro Domäne ein definiertes Führungssystem, und Konsistenz dazwischen. Kundenstammdaten führt das CRM, Punkt. Zahlungsstatus führt das Billing, und das CRM zeigt eine synchronisierte Kopie, die als Kopie erkennbar ist. Nutzungsdaten führt die Produkt-Analytics. Für jede wichtige Entität steht schriftlich fest, welches System bei Widerspruch gewinnt, in welche Richtung synchronisiert wird und wie schnell. Am Ende ist das ein Dokument von zwei Seiten plus die Integrationen, die es durchsetzen.

Im Alltag ändert das alles. Die Frage nach 214 gegen 189 gegen 240 ist keine Vertrauenskrise mehr, sondern hat eine Antwort: 189, weil Finance zahlende Verträge zählt und genau das die vereinbarte Definition von aktivem Kunden ist. Die anderen Zahlen messen etwas anderes, und das steht auch dran. Streit über Zahlen ist fast nie ein Datenproblem. Meistens fehlt schlicht die Einigung, welche Definition gilt und wer sie führt.

Kleiner Einschub, bevor der Einwand kommt: ein Warehouse kann später trotzdem sinnvoll sein, als Ort, an dem die Domänen fürs Reporting zusammenlaufen. Aber als Reporting-Schicht über sauberen Führungssystemen. Nicht als magischer Ort, an dem Wahrheit von selbst entsteht.

Die Single Source of Truth ist ein Poster an der Wand. Führungssysteme mit Konfliktregeln sind ein Freitagnachmittag Arbeit pro Domäne. Welche der beiden Varianten hat euer letztes Zielbild versprochen?
