---
layout: revshort
title: "Cold Outbound gehört nicht in eure Suite"
description: "Wir sagen sonst ständig, dass eure Suite mehr kann, als ihr denkt, und dass die meisten Point Solutions rausfliegen können. Heute die Ausnahme, und die..."
date: 2026-03-24
read_time: "2 Min Read"
category: "Outbound"
hero_icon: "send"
---

Wir sagen sonst ständig, dass eure Suite mehr kann, als ihr denkt, und dass die meisten Point Solutions rausfliegen können. Heute die Ausnahme, und die ist wichtig: Kaltakquise per E-Mail läuft niemals über HubSpot, Salesforce oder euren Firmen-Mailserver. Nicht weil die Tools es nicht könnten. Sondern weil ihr es nicht wollen dürft.

Der Grund heißt Deliverability, und die Mechanik ist unerbittlich. Google und Microsoft bewerten die Reputation eurer Sending-Domain. Jede Spam-Markierung, jede Zustellung an eine tote Adresse, jede Massenmail an Leute, die euch nicht kennen, drückt diesen Score. Kaltakquise produziert all das zwangsläufig, selbst wenn sie handwerklich sauber ist. Bounce-Raten von drei, vier Prozent sind bei gekauften oder angereicherten Listen normal. Bei Bestandskunden wären sie ein Alarmsignal.

Und jetzt der Teil, der wehtut. Wer Cold Outbound über die Hauptdomain schickt, verbrennt die Reputation für alle Mails dieser Domain. Nicht nur für die nächste Sequenz. Für alles. Die Rechnung aus dem Billing-System landet im Spam. Die Antwort eures Supports an einen zahlenden Kunden landet im Spam. Das Angebot, auf das ein heißer Deal wartet, landet im Spam, und ihr wundert euch, warum er kalt wird. Wir haben eine Firma gesehen, bei der nach einer übermotivierten Outbound-Kampagne über die Hauptdomain wochenlang selbst interne Kalendereinladungen bei externen Partnern im Junk-Ordner lagen. Der Schaden ist schleichend, schwer messbar und dauert Monate in der Reparatur.

Deshalb ist das Setup für ernsthaftes Outbound immer getrennt. Eigene Domains, die der Hauptdomain ähneln, aber nichts mit ihr teilen, sagen wir firma-gmbh.de statt firma.de, davon mehrere. Pro Domain zwei bis drei Postfächer, jedes über Wochen aufgewärmt, bevor die erste echte Mail rausgeht. Volumen gedeckelt, 20 bis 30 Mails pro Postfach und Tag, nicht 500. Und eine Sending-Infrastruktur wie Smartlead oder Instantly, die Rotation, Warmup und Bounce-Handling übernimmt. Fliegt eine Domain in eine Blacklist, wird sie abgeklemmt und ersetzt. Eure Hauptdomain merkt davon nichts.

Das ist einer der wenigen Fälle im ganzen RevOps-Stack, wo das separate Tool keine Bequemlichkeit ist, sondern Pflicht. Die Trennung ist der Punkt, nicht das Feature-Set.

Falls bei euch gerade jemand Sequenzen an kalte Listen direkt aus dem CRM schickt: schaut heute noch in eure Domain-Reputation. Nicht nächste Woche. Der Score, den ihr da rettet, gehört euren Rechnungen.
