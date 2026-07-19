---
layout: revshort
title: "Bidirektional heißt doppelte Wahrheit"
description: "'Der Sync soll bidirektional sein, alle Felder, beide Richtungen.' Dieser Satz fällt in fast jedem Integrationsprojekt, meistens früh, meistens..."
date: 2026-06-02
read_time: "2 Min. Lesezeit"
category: "Integration"
hero_icon: "git-branch"
lang: de
translation: /revshorts/081-bidirektional-heisst-doppelte-wahrheit/
---

"Der Sync soll bidirektional sein, alle Felder, beide Richtungen." Dieser Satz fällt in fast jedem Integrationsprojekt, meistens früh, meistens beiläufig. Er klingt nach Vollständigkeit. Bestellt wird damit Datenchaos mit Lieferzeit.

Denn bidirektional über alle Felder heißt: Es gibt keine führende Quelle mehr. Zwei Systeme dürfen dieselbe Information ändern, und irgendein Mechanismus muss entscheiden, wer gewinnt. Meistens gewinnt der letzte Schreibzugriff. Klingt fair, ist aber Roulette. Marketing korrigiert im MAP die Branche, drei Minuten später überschreibt ein CRM-Workflow sie mit dem alten Wert, weil er aus einem ganz anderen Grund den Datensatz angefasst hat. Niemand sieht das. Es gibt keinen Fehler, keinen Alert, nur zwei Systeme, die sich gegenseitig leise die Daten kaputtschreiben. Der Klassiker ist die Sync-Schleife: System A updated, B synct zurück, A wertet das als Änderung, synct wieder, und plötzlich fragt ihr euch, warum das API-Kontingent um 3 Uhr nachts leer ist.

Der Schmerz ist doppelt, weil auch die Wahrheit doppelt ist. Wenn im CRM eine andere Telefonnummer steht als im Support-Tool, welche stimmt? Ohne definierte Führung ist die Antwort: keine Ahnung, kommt drauf an, wer zuletzt gespeichert hat. Das ist der Moment, in dem der Vertrieb aufhört, den Daten zu trauen, und anfängt, wieder Excel-Listen zu pflegen. Dann habt ihr drei Wahrheiten.

Die Lösung ist unspektakulär und funktioniert seit Jahrzehnten: Ein System führt, das andere folgt, und zwar pro Feld entschieden, nicht pauschal pro Objekt. Firmenname und Branche führt das CRM, weil dort angereichert und geprüft wird. Consent-Status führt das Marketing-Tool, weil dort die Opt-ins entstehen. Ticketvolumen führt das Support-System, das CRM zeigt es nur an. Das ergibt eine Tabelle, vielleicht 40 Zeilen, Feld, Owner, Richtung, Konfliktregel. Eine langweilige Tabelle, zugegeben. Sie ist das wertvollste Dokument der ganzen Integration, und sie zu erarbeiten dauert einen Nachmittag mit den richtigen Leuten am Tisch.

Echte Zwei-Wege-Fälle bleiben übrig, klar, ein Opportunity-Status, den beide Seiten fortschreiben müssen. Die behandelt man einzeln, mit Zeitstempeln und expliziter Konfliktlogik, und man hält die Liste so kurz wie irgend möglich.

Wer euch "beide Richtungen, alle Felder" als Feature verkauft, hat entweder die Konfliktfälle nie durchdacht oder rechnet fest damit, dass ihr ihn fürs Aufräumen nochmal bucht. Welches eurer Felder hat heute eigentlich einen Owner?
