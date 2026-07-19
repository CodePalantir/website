---
layout: revshort
title: "Der Zahlungsstatus gehört ins CRM"
description: "Szene aus einem normalen Dienstag: Der Account Executive ruft beim Kunden an, gut gelaunt, das Renewal steht an. Was er nicht weiß: Die Buchhaltung hat..."
date: 2026-05-10
read_time: "2 Min. Lesezeit"
category: "Integration"
hero_icon: "git-branch"
lang: de
translation: /revshorts/058-der-zahlungsstatus-gehoert-ins-crm/
---

Szene aus einem normalen Dienstag: Der Account Executive ruft beim Kunden an, gut gelaunt, das Renewal steht an. Was er nicht weiß: Die Buchhaltung hat derselben Firma gestern die zweite Mahnung geschickt. Zwei Abteilungen, ein Kunde, null gemeinsame Information.

Das ist kein Kommunikationsproblem, das man mit einem wöchentlichen Sync löst. Es ist ein Datenproblem. Der Zahlungsstatus lebt im Billing-System oder im ERP, das CRM weiß nichts davon, und der Mensch, der den Kunden anruft, arbeitet nun mal im CRM. Zwei Systeme, die nicht miteinander reden, und die Menschen dahinter deshalb auch nicht.

Dabei ist die Schnittstelle, die genau das behebt, die vielleicht dankbarste im ganzen RevOps-Feld. Rechnung erstellt, Rechnung bezahlt, Rechnung überfällig: drei Statuswerte, ein Feld auf dem Account, ein Sync pro Nacht reicht in den meisten Fällen völlig. Kein Echtzeit-Streaming, keine Middleware-Kathedrale. Stripe, Chargebee, billwerk, selbst ein zugenageltes altes ERP gibt diese Information irgendwie her, notfalls als Export, den ein Skript einsammelt.

Warum hat sie trotzdem kaum jemand? Weil sie zwischen zwei Zuständigkeiten fällt. Die Buchhaltung denkt in ihrem System und hält das CRM für Vertriebsspielzeug. Der Vertrieb will mit Rechnungen nichts zu tun haben, solange die Provision stimmt. Und der IT ist das Ding zu klein, um dafür ein Projekt aufzumachen. Also bleibt es ungebaut. Jahrelang.

Die Gegenrechnung ist schnell gemacht. Ein AE, der vor dem Anruf sieht, dass der Kunde überfällig ist, führt ein anderes Gespräch. Ein CSM, der den offenen Posten kennt, eskaliert intern, bevor die dritte Mahnung rausgeht und die Beziehung ruiniert. Und wer im Dashboard sieht, welche Accounts gleichzeitig offene Pipeline und offene Posten haben, priorisiert anders. Das sind keine Nice-to-haves. Das ist der Unterschied zwischen einer Firma, die mit ihrem Kunden spricht, und drei Abteilungen, die es unabhängig voneinander tun.

Nebenbei: Genau hier verläuft eine Grenze, die wir bewusst ziehen. Buchungssätze, Kontenrahmen, Steuerlogik, alles ab dem ERP gehört den Steuerleuten und bleibt dort. Aber Auftrag gewonnen, Billing getriggert, Zahlungsstatus zurück ins CRM: das ist Revenue-Prozess, kein Rechnungswesen.

Wenn ihr dieses Jahr nur eine einzige Integration baut, baut diese. Sie ist klein, sie ist billig, und sie verhindert die teuersten Telefonate eures Vertriebs. Welche andere Schnittstelle kann das von sich behaupten?
