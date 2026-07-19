# RevShorts #3 bis #22

---

## RevShort #3: Daten sind nicht höflich

Fragt zehn Leute in eurem Vertrieb, wie euer Lead-Prozess läuft, und ihr bekommt zehn plausible Antworten. Alle klingen vernünftig. Alle widersprechen sich. Und keine davon erklärt, warum der Forecast schon wieder um 30 Prozent daneben lag.

Genau darauf baut das klassische Beratungsmodell: sechs Wochen Stakeholder-Interviews, Workshops, ein Zielbild. Klingt gründlich. Ist aber vor allem eins, nämlich eine Sammlung von Meinungen. Der Vertriebsleiter erzählt den Prozess, wie er sein sollte. Der AE erzählt ihn, wie er ihn erlebt. Der Geschäftsführer erzählt die Version, die er vor zwei Jahren mal abgenickt hat. Alle sind ehrlich. Trotzdem stimmt nichts davon.

Das System lügt nicht. Es kann gar nicht.

Fünf Tage mit Admin-Zugang im CRM finden mehr Wahrheit als sechs Wochen Interviews, weil Daten nicht höflich sind. Da steht die Automatisierung, die seit 14 Monaten in einen Fehler läuft und die niemand bemerkt hat, weil die Fehlermails an einen Ex-Mitarbeiter gehen. Da steht das Pflichtfeld, das in 80 Prozent der Fälle mit "tbd" gefüllt wird, weil es beim Speichern im Weg ist. Da steht der Forecast, der auf Close Dates basiert, die seit drei Quartalen niemand angefasst hat. Kein Interview der Welt fördert das zutage, weil es niemand weiß. Oder niemand zugeben will.

Ein Interview liefert, was Menschen glauben. Ein Audit liefert Befunde. Timestamp, Feldhistorie, Ausführungslog. Darüber kann man nicht diskutieren, man kann es nur reparieren.

Und ja, natürlich reden wir auch mit Leuten. Aber erst nachdem wir im System waren, und dann mit ganz anderen Fragen. Nicht "wie läuft euer Prozess", sondern "hier sind 340 Opportunities ohne nächsten Schritt, was ist da passiert". Das erste Gespräch dauert eine Stunde und produziert ein Organigramm der Wunschvorstellungen. Das zweite dauert zwanzig Minuten und produziert eine Entscheidung.

Warum verkaufen dann so viele Beratungen die Interview-Strecke? Folgt der Rechnung. Sechs Wochen Discovery sind sechs Wochen Tagessätze, und Interviews lassen sich wunderbar an Juniors delegieren, die noch nie einen Flow debuggt haben. Ein Fünf-Tage-Audit zum Festpreis lässt sich nicht strecken. Es muss liefern, sonst gibt es kein Folgegeschäft.

Wer Interviews verkauft, verkauft Zeit. Wer ins System geht, verkauft Befunde. Fragt beim nächsten Angebot einfach, ab welchem Tag sich jemand einloggt.

---

## RevShort #4: Die Schicht, die keine Suite je bauen wird

Salesforce kann inzwischen fast alles. HubSpot auch. Sequencing, Routing, Forecasting, Quoting, alles nativ, alles in der Edition, die ihr sowieso bezahlt. Wir predigen selbst laufend, dass die Hälfte eurer Point Solutions deswegen rausfliegen kann.

Aber eine Sache wird keine Suite je können, und zwar aus Prinzip: sich selbst mit dem Rest eurer Welt verbinden.

Jede Suite automatisiert nach innen. Ein Workflow in HubSpot bewegt HubSpot-Daten. Ein Flow in Salesforce bewegt Salesforce-Daten. Das ist kein Versäumnis, das ist Geschäftsmodell, denn jede Suite will die Welt sein, nicht Teil einer Welt. Systemübergreifend war nie nativ und wird es nie sein. Sobald der Auftrag gewonnen ist und die Rechnung in Stripe oder billwerk+ entstehen soll, sobald der Zahlungsstatus zurück ins CRM muss, damit der CSM sieht, dass der Kunde seit 60 Tagen nicht gezahlt hat, bevor er ihm fröhlich das Upsell pitcht: ab da seid ihr in der Glue-Schicht. Integration, Datenmodell über Systemgrenzen, die Logik dazwischen.

Genau dieses Stück ist der wertvollste Teil eures Stacks. Nicht das CRM. Nicht das Billing-Tool. Das Bindegewebe.

Warum? Weil dort die Wahrheit entsteht. Ob eine Zahl im Reporting stimmt, entscheidet sich nicht im Dashboard, sondern an der Stelle, wo drei Systeme sich einigen müssen, was ein Kunde ist. Wer die Integrationsschicht besitzt und versteht, kontrolliert den ganzen Stack. Der kann Tools tauschen wie Reifen, weil die Logik nicht im Tool wohnt. Der andere, bei dem die Verbindungen aus fünf Zapier-Zaps bestehen, die ein Praktikant 2023 gebaut hat, der ist Gefangener seiner eigenen Landschaft. Jeder Tool-Wechsel wird zur Operation am offenen Herzen.

Kleiner Test. Fragt in eurem Team, wer genau weiß, wie der Bezahlt-Status vom Billing zurück ins CRM kommt. Welches System, welcher Trigger, was passiert bei einem Fehler. Wenn die Antwort "das läuft irgendwie über Make, glaube ich" lautet, wisst ihr, wo euer Risiko sitzt. Nicht in den Tools mit den großen Logos. In den Fäden dazwischen.

Point Solutions kommen und gehen, Suiten fressen Features, die Preise verschieben sich jedes Jahr. Die Glue-Schicht bleibt, egal welcher Stack darunter liegt. Deshalb investiert man dort zuerst, mit Engineering statt mit Lizenzen.

Euer Stack ist so gut wie seine schwächste Integration. Kennt ihr eure?

---

## RevShort #5: Freitag, 16:20 Uhr

Ein Lead füllt euer Formular aus. Freitag, 16:20 Uhr, konkretes Projekt, Budget vorhanden, drei Anbieter im Blick. Eure Website sagt "Danke für Ihre Anfrage, wir melden uns zeitnah". Montag um 11 ruft jemand aus eurem Vertrieb an.

Der Wettbewerber hat Freitag um 16:25 angerufen.

Das Meeting stand, bevor euer CRM den Lead überhaupt einem Owner zugewiesen hatte. Montag um 11 wart ihr nicht mehr der mögliche Partner, ihr wart die Vergleichsofferte für den Einkauf.

Die Zahlen dazu sind seit Jahren bekannt und werden trotzdem konsequent ignoriert. Wer innerhalb von fünf Minuten reagiert, erreicht den Lead um ein Vielfaches häufiger als wer eine Stunde wartet. Nach einem Wochenende ist der Vorsprung weg, das Interesse abgekühlt, der Kalender des Wettbewerbers gefüllt. Antwortgeschwindigkeit schlägt Lead-Qualität. Ein mittelmäßiger Lead, der in fünf Minuten ein Gespräch bekommt, konvertiert besser als der perfekte ICP-Treffer, der drei Tage in einer Queue liegt.

Und jetzt der Teil, der wehtut: Das ist fast nie ein Tool-Problem.

Der Reflex geht trotzdem sofort Richtung Einkauf. Chili Piper evaluieren, Demo anschauen, noch eine Lizenz. Dabei können Salesforce, HubSpot und Dynamics Routing und Scheduling längst nativ. Lead kommt rein, wird nach Region oder Segment zugewiesen, der Interessent bucht sich direkt einen Termin in den Kalender des zuständigen AE. Alles vorhanden. Alles konfigurierbar. In der Edition, die ihr bezahlt.

Was fehlt, ist etwas viel Banaleres. Ownership. Wer ist verantwortlich, wenn ein Lead 20 Minuten unberührt liegt? Nicht das Team, eine Person. Und ein SLA, das den Namen verdient: jeder Inbound-Lead bekommt innerhalb von zehn Minuten eine echte Reaktion, auch freitags um 16:20, und wenn das niemand schafft, bucht sich der Lead eben selbst ein Meeting, dafür gibt es die Scheduling-Links. Dazu ein Eskalationspfad und ein Report, der die Reaktionszeit pro Woche sichtbar macht. Das ist ein Nachmittag Konfiguration plus eine unbequeme Prozessentscheidung.

Die Prozessentscheidung ist der Grund, warum es meist nicht passiert. Ein Tool kaufen fühlt sich nach Handeln an und tut niemandem weh. Einen SLA durchsetzen heißt, jemandem sagen, dass Freitag 16:20 zum Job gehört.

Zieht mal die Timestamps eurer letzten 50 Inbound-Leads. Erstellt bis erste echte Reaktion. Die Zahl, die da rauskommt, ist euer eigentlicher Wettbewerber.

---

## RevShort #6: Bauchgefühl mit Dashboard

Der Forecast-Call am Montagmorgen. Jeder AE geht seine Deals durch, sagt Commit oder Best Case, der Vertriebsleiter nickt, korrigiert nach Gefühl um 15 Prozent nach unten, und die Zahl geht an die Geschäftsführung. Am Quartalsende liegt sie um ein Drittel daneben. Wie immer.

Die reflexhafte Diagnose lautet dann: Wir brauchen ein Forecasting-Tool. Clari, BoostUp, irgendwas mit AI. Und die reflexhafte Diagnose ist falsch.

Schaut in die Daten unter eurem Forecast, bevor ihr über Tools redet. Da liegen Opportunities in der Commit-Kategorie, deren Close Date seit zwei Quartalen der 31. März ist, obwohl wir Juli haben. Da fehlt bei der Hälfte der offenen Deals ein nächster Schritt, was übersetzt heißt: Niemand weiß, was als Nächstes passiert, aber im Forecast steht der Deal trotzdem mit 60 Prozent. Und diese 60 Prozent, woher kommen die eigentlich? Aus der Stage-Definition, die irgendwann mal jemand mit Standardwerten angelegt hat. Eure Weighted Pipeline multipliziert echte Beträge mit Fantasie-Wahrscheinlichkeiten. Das Ergebnis hat zwei Nachkommastellen und null Aussagekraft.

Ein Forecast ist keine Zahl, die ein Tool ausspuckt. Ein Forecast ist eine Kette von Datenfeldern, die jemand pflegt, mal ehrlich, mal nicht. Close Date, Stage, Betrag, nächster Schritt, letztes Kundensignal. Wenn diese Felder Müll enthalten, aggregiert jedes Tool der Welt Müll. Clari kaufen löst das nicht. Clari macht aus leeren Feldern nur schneller ein schönes Diagramm. Bauchgefühl mit Dashboard eben, jetzt für 60.000 Euro im Jahr extra.

Forecast-Qualität ist Datenmodell-Qualität. Das ist die ganze These, und sie ist unbequem, weil sie Arbeit bedeutet statt Einkauf. Stages, die an beobachtbaren Kundenhandlungen hängen und nicht an AE-Optimismus. Ein Close Date, das automatisch hinterfragt wird, wenn es zum dritten Mal verschoben wird. Validierungen, die einen Commit ohne nächsten Schritt schlicht nicht zulassen. Wahrscheinlichkeiten aus eurer eigenen Win-Rate-Historie statt aus Werkseinstellungen. Alles baubar, in Salesforce wie in HubSpot, nativ, ohne eine einzige neue Lizenz.

Ab 300 Vertrieblern sieht die Rechnung anders aus, da spielt Clari seine Stärken aus. Ihr habt keine 300 Vertriebler.

Macht den Test: Nehmt euren aktuellen Commit und prüft bei jedem Deal nur zwei Felder, Close Date und nächster Schritt. Zählt, wie viele beide sauber gepflegt haben. Diese Quote ist euer echter Forecast. Der Rest ist Deko.

---

## RevShort #7: Das teuerste Datenproblem hat keinen Besitzer

Zwei AEs rufen in derselben Woche denselben Geschäftsführer an. Beide haben einen Account im CRM, einmal "Müller GmbH", einmal "Mueller GmbH & Co. KG", beide mit offener Opportunity. Der Geschäftsführer fragt beim zweiten Anruf trocken, ob die Kollegen bei euch eigentlich miteinander reden. Der Deal ist ab da Bergaufarbeit.

Das ist die sichtbare Version des Problems. Die unsichtbare ist teurer.

Eure Attribution zerfällt, weil der Marketing-Kontakt auf Dublette A hängt und der gewonnene Deal auf Dublette B, womit die Kampagne, die den Kunden gebracht hat, im Report als Kostenstelle ohne Ergebnis steht. Euer Bestandskunde bekommt die Neukunden-Mail mit "Lernen Sie uns kennen", weil sein zweiter Datensatz nie den Kunden-Status bekommen hat, und antwortet mit einem Screenshot seiner letzten drei Rechnungen. Euer Scoring, euer Routing, eure Segmentierung: alles rechnet auf einer Datenbasis, in der dieselbe Firma zwei, drei, manchmal fünfmal existiert. Jede Automatisierung wird zum Glücksspiel.

Warum ist ausgerechnet das das teuerste Datenproblem? Nicht weil es das größte wäre. Sondern weil es keinen Besitzer hat. Der Vertrieb sagt, Datenpflege sei Sache vom Marketing. Marketing sagt, die Accounts gehören dem Vertrieb. Der Admin, falls es einen gibt, hat 40 andere Tickets. Also passiert nichts, jahrelang, und alle gewöhnen sich daran, vor jedem Anruf erstmal drei Suchvarianten durchzuprobieren.

Irgendwann kommt dann der Frühjahrsputz. Ein Praktikant, eine Excel-Liste, zwei Wochen Merging. Danach ist es besser. Sechs Monate später ist alles wieder da, weil die Quellen weiterlaufen: das Webformular ohne Abgleich, der Import aus der Messe-Liste, das Enrichment-Tool, das fröhlich neue Records anlegt, die manuelle Anlage ohne Pflichtprüfung. Dubletten sind kein Bestand, den man einmal wegräumt. Dubletten sind ein Zufluss.

Deshalb ist Dedupe keine Aufräumaktion, sondern laufende Governance. Matching-Regeln, die zu euren Daten passen, deutsche Rechtsformen inklusive, GmbH gegen GmbH & Co. KG matcht kein Standardregelwerk sauber. Abgleich an jeder Eingangstür, nicht nachträglich. Klare Merge-Logik, welcher Datensatz überlebt und welche Felder gewinnen. Und vor allem: ein Name. Eine Person, die verantwortlich ist, mit einem Report, der die Dublettenquote pro Monat zeigt.

Sucht doch mal euren größten Kunden im CRM. Einmal ausgeschrieben, einmal abgekürzt, einmal mit Umlaut. Wie viele Treffer?

---

## RevShort #8: Euer Pipeline-Meeting ist ein Übersetzungsproblem

Freitag, zehn Uhr, Pipeline-Review. Marketing präsentiert 340 MQLs für das Quartal, Zielerreichung 112 Prozent, Folie mit grünem Haken. Sales schaut auf die eigene Liste und findet davon ungefähr 60, die den Namen verdient haben. Der Rest: Whitepaper-Downloads von Studenten, Wettbewerber mit Wegwerfadressen, ein Praktikant, der dreimal dasselbe Formular ausgefüllt hat. Und dann fällt der Satz, der in jedem zweiten Mittelständler fällt. Eure Leads sind Müll. Worauf die Antwort kommt, die genauso alt ist: Ihr fasst sie ja nicht mal an, im Schnitt erst nach vier Tagen.

Beide haben recht. Das ist das Problem.

Marketing zählt als MQL, was einen Score über 50 hat. Sales meint mit MQL einen Kontakt, der Budget und ein konkretes Projekt hat. Und wenn ihr eine CS-Abteilung habt, benutzt die das Wort vermutlich für etwas Drittes. Drei Abteilungen, drei Funnel-Definitionen, ein Begriff. Solange das so ist, redet ihr in jedem Meeting über Zahlen, die nicht dasselbe messen, und streitet folgerichtig über die Zahlen statt über Maßnahmen. Das Meeting fühlt sich an wie Arbeit. Es ist Simultandolmetschen ohne Dolmetscher.

Der Reflex ist dann oft, ein Tool zu kaufen. Besseres Scoring, neues Attributionsmodell, ein Dashboard, das endlich die Wahrheit zeigt. Funktioniert nicht, weil das Problem gar kein Datenproblem ist. Einheitliche Funnel-Definitionen sind eine Entscheidung, keine Software. Jemand mit Autorität über beide Abteilungen muss festlegen: Ein MQL ist ein Kontakt aus dem ICP mit Verhalten X, ein SQL entsteht, wenn Sales Kriterium Y bestätigt hat, und die Übergabe gilt erst nach dokumentiertem Erstkontakt. Das ist ein Nachmittag Arbeit plus ein unangenehmes Gespräch. Kein Lizenzvertrag der Welt nimmt euch das ab.

Danach, und erst danach, lohnt sich das Dashboard. Denn ein Dashboard auf uneinheitlichen Definitionen ist kein Reporting, sondern ein Streitbeschleuniger mit Diagrammen. Dieselbe Conversion-Rate, dreimal anders berechnet, dreimal anders interpretiert. Wir haben Firmen gesehen, die 40.000 Euro in BI-Tooling gesteckt haben, bevor irgendjemand aufgeschrieben hatte, was ein Lead eigentlich ist.

Der Test ist simpel. Fragt drei Leute aus drei Abteilungen, was bei euch ein MQL ist, und zwar schriftlich, ohne dass sie sich absprechen können. Wenn drei verschiedene Antworten kommen, wisst ihr, warum euer Forecast wackelt. Und ihr wisst auch, dass die Lösung nichts kostet außer einer Entscheidung, die bisher niemand treffen wollte.

---

## RevShort #9: Garbage in, Agent out

Der Vorstand hat auf einer Konferenz Agentforce gesehen, jetzt soll AI ins CRM. Verständlicher Wunsch. Nur: Ein AI-Agent auf einem kaputten Datenmodell produziert denselben Unsinn wie vorher eure Prozesse, bloß schneller, rund um die Uhr und mit selbstbewusster Formulierung.

Konkretes Beispiel aus der Praxis. Ein Agent soll eingehende Anfragen automatisch dem richtigen Account-Owner zuweisen. Klingt nach zwei Tagen Projekt. In der Org existiert die Müller GmbH aber viermal: einmal als Müller GmbH, einmal als Mueller GmbH & Co. KG, einmal als MÜLLER (Import aus dem alten System) und einmal als Testaccount, den 2022 jemand angelegt und nie gelöscht hat. Der Agent routet die Anfrage an den Owner der falschen Dublette, der Kollege ist seit einem Jahr raus, die Anfrage liegt zwölf Tage in einer verwaisten Queue. Vorher wäre das einem Menschen aufgefallen. Der Agent macht es fehlerfrei falsch.

Oder die Kundenhistorie. Fragst du einen Copilot nach der Historie eines Accounts, dessen Aktivitäten über vier Dubletten und zwei alte Systeme verstreut sind, bekommst du eine flüssig formulierte Zusammenfassung von einem Viertel der Wahrheit. Das Modell halluziniert nicht mal im technischen Sinn. Es fasst korrekt zusammen, was da ist. Da ist nur fast nichts.

Gleiche Mechanik beim Scoring. Ein AI-Scoring auf Feldern, die zu 60 Prozent leer sind, weil sie nie Pflichtfeld waren und niemand sie pflegt, lernt vor allem eines: welche Vertriebler ordentlich dokumentieren. Das korreliert mit Abschlusswahrscheinlichkeit ungefähr so gut wie die Schriftgröße im Angebot.

Die unbequeme Wahrheit ist, dass die unsexy Vorarbeit ungefähr 80 Prozent eines ernsthaften AI-Projekts ausmacht. Dubletten zusammenführen. Pflichtfelder definieren und durchsetzen. Festlegen, was ein aktiver Kunde ist und wann eine Opportunity tot ist. Prozesse so bauen, dass Daten beim Arbeiten entstehen statt als Zusatzaufgabe. Erst dann lohnen sich Agentforce, Breeze oder der Dynamics Copilot, und dann lohnen sie sich tatsächlich, weil sie auf einem Modell arbeiten, das die Realität abbildet.

Die Anbieter erzählen euch das übrigens nicht, weil sich Datenhygiene schlecht auf einer Keynote-Bühne demonstrieren lässt. Ein Agent, der live eine E-Mail schreibt, sieht besser aus als ein Dedupe-Job, der über Nacht 3.000 Accounts zusammenführt. Wertvoller ist trotzdem der Dedupe-Job.

Wer euch ein AI-Projekt verkauft, ohne vorher euer Datenmodell gesehen zu haben, verkauft euch einen Turbo für ein Auto mit plattem Reifen. Fährt schneller. Nur nicht dahin, wo ihr wollt.

---

## RevShort #10: Der eine Kollege, der alles weiß

Jede Firma zwischen 20 und 200 Leuten hat ihn. Den einen Admin, den einen Kollegen aus dem Vertrieb mit Faible fürs System, der als Einziger weiß, wie das CRM wirklich funktioniert. Warum das Feld heißt, wie es heißt. Welche Automatisierung man auf keinen Fall anfassen darf. Wo die Leiche im Prozess liegt. Im Management gilt er als Asset. Er ist ein Klumpenrisiko mit Gleitzeit.

Die Szene läuft immer gleich ab. Der Kollege kündigt, Übergabe in zwei Wochen, man notiert ein paar Passwörter, alle sind zuversichtlich. Drei Monate später bricht die Lead-Zuweisung. Neue Anfragen landen nirgends, der Vertrieb merkt es erst, als ein Interessent anruft und fragt, warum sich seit zehn Tagen niemand meldet. Jetzt sucht jemand im System nach der Ursache und findet einen Flow namens Test_Final_v2_NICHT_LOESCHEN, der von einem Workflow aus 2021 getriggert wird, der wiederum auf ein Feld schaut, das seit dem letzten Formular-Relaunch nicht mehr befüllt wird. Keine Beschreibung, kein Kommentar, kein Dokument. Der Mensch, der das erklären könnte, arbeitet inzwischen woanders.

Das ist kein Pech. Das ist die planbare Folge davon, dass Wissen im Kopf statt im System lag.

Dokumentation, Naming Conventions, Metadaten-Hygiene: klingt nach Bürokratie, nach dem Zeug, das man macht, wenn gerade nichts Wichtiges ansteht. Tatsächlich ist es eine Versicherung, und zwar eine billige. Ein Flow, der Lead_Routing_Region_DACH heißt und eine Beschreibung mit Zweck, Trigger und Ansprechpartner trägt, kostet beim Anlegen zwei Minuten mehr. Ein Flow, der Test_Final_v2 heißt, kostet drei Jahre später zwei Wochen Forensik plus die Deals, die in der Zwischenzeit versickert sind. Rechnet das gegen.

Der Bus-Faktor, also die Frage, wie viele Leute von einem Bus erfasst werden müssten, bis niemand mehr das System versteht, liegt in den meisten Orgs, die wir auditieren, bei exakt eins. Manchmal bei null, wenn der Kollege schon weg ist und die Firma auf einem System fährt, das keiner mehr versteht, das aber noch läuft. Noch.

Ein Audit deckt so etwas übrigens gnadenlos auf, weil man die Frage nur einmal stellen muss: Erklär mir, was dieser Flow tut. Wenn die Antwort mit "das hat damals der Markus gebaut" beginnt, weiß man genug.

Wie viele eurer Automatisierungen könnte morgen jemand anderes erklären? Zählt ehrlich. Die Zahl ist euer eigentlicher Wartungsvertrag.

---

## RevShort #11: Cold Outbound gehört nicht in eure Suite

Wir sagen sonst ständig, dass eure Suite mehr kann, als ihr denkt, und dass die meisten Point Solutions rausfliegen können. Heute die Ausnahme, und die ist wichtig: Kaltakquise per E-Mail läuft niemals über HubSpot, Salesforce oder euren Firmen-Mailserver. Nicht weil die Tools es nicht könnten. Sondern weil ihr es nicht wollen dürft.

Der Grund heißt Deliverability, und die Mechanik ist unerbittlich. Google und Microsoft bewerten die Reputation eurer Sending-Domain. Jede Spam-Markierung, jede Zustellung an eine tote Adresse, jede Massenmail an Leute, die euch nicht kennen, drückt diesen Score. Kaltakquise produziert all das zwangsläufig, selbst wenn sie handwerklich sauber ist. Bounce-Raten von drei, vier Prozent sind bei gekauften oder angereicherten Listen normal. Bei Bestandskunden wären sie ein Alarmsignal.

Und jetzt der Teil, der wehtut. Wer Cold Outbound über die Hauptdomain schickt, verbrennt die Reputation für alle Mails dieser Domain. Nicht nur für die nächste Sequenz. Für alles. Die Rechnung aus dem Billing-System landet im Spam. Die Antwort eures Supports an einen zahlenden Kunden landet im Spam. Das Angebot, auf das ein heißer Deal wartet, landet im Spam, und ihr wundert euch, warum er kalt wird. Wir haben eine Firma gesehen, bei der nach einer übermotivierten Outbound-Kampagne über die Hauptdomain wochenlang selbst interne Kalendereinladungen bei externen Partnern im Junk-Ordner lagen. Der Schaden ist schleichend, schwer messbar und dauert Monate in der Reparatur.

Deshalb ist das Setup für ernsthaftes Outbound immer getrennt. Eigene Domains, die der Hauptdomain ähneln, aber nichts mit ihr teilen, sagen wir firma-gmbh.de statt firma.de, davon mehrere. Pro Domain zwei bis drei Postfächer, jedes über Wochen aufgewärmt, bevor die erste echte Mail rausgeht. Volumen gedeckelt, 20 bis 30 Mails pro Postfach und Tag, nicht 500. Und eine Sending-Infrastruktur wie Smartlead oder Instantly, die Rotation, Warmup und Bounce-Handling übernimmt. Fliegt eine Domain in eine Blacklist, wird sie abgeklemmt und ersetzt. Eure Hauptdomain merkt davon nichts.

Das ist einer der wenigen Fälle im ganzen RevOps-Stack, wo das separate Tool keine Bequemlichkeit ist, sondern Pflicht. Die Trennung ist der Punkt, nicht das Feature-Set.

Falls bei euch gerade jemand Sequenzen an kalte Listen direkt aus dem CRM schickt: schaut heute noch in eure Domain-Reputation. Nicht nächste Woche. Der Score, den ihr da rettet, gehört euren Rechnungen.

---

## RevShort #12: Warum wir an der Rechnung aufhören

Es gibt eine Frage, die in fast jedem Erstgespräch kommt, meistens vom Geschäftsführer: Und das ERP, macht ihr das auch? Unsere Antwort ist nein, und wir halten diese Antwort für eines unserer besten Qualitätsmerkmale.

Die Grenze verläuft exakt an der Rechnungsauslösung. Alles bis dahin gehört zu RevOps und damit zu uns: Auftrag gewonnen, Billing getriggert, Rechnung raus, und der Zahlungsstatus fließt zurück ins CRM, damit der Vertrieb sieht, ob der Kunde zahlt, bevor er ihm das nächste Upgrade verkauft. Diese Strecke bauen wir komplett, inklusive der Integration zu Stripe, Chargebee oder was auch immer bei euch fakturiert. Alles ab dem Buchungssatz ist Nachbargebiet. Buchhaltung, Kontenrahmen, Steuerlogik, Warenwirtschaft, Lagerbestände: anderes Land, andere Sprache, andere Spezialisten.

Warum wir darauf bestehen? Weil ERP eine eigene Welt ist, mit eigener Regulatorik, eigenen Release-Zyklen und Fehlern, die nicht ein Dashboard verhageln, sondern einen Jahresabschluss. Wer SAP Business One oder ein gewachsenes Navision ernsthaft beherrschen will, macht wenig anderes. Das ist ein Vollzeitgebiet. Kein Nebenfach.

Und jetzt die unbequeme Beobachtung: Der Dienstleister, der euch CRM, Marketing Automation, BI, AI und das ERP aus einer Hand verspricht, beherrscht davon in der Regel eines gut, zwei mittel und den Rest gar nicht. Das Vollversprechen ist ein Vertriebsargument, kein Kompetenzprofil. Gemerkt wird das immer erst im Projekt, wenn beim ERP-Teil plötzlich ein Subunternehmer auftaucht, den niemand gebrieft hat, oder ein Junior, der das Modul zum ersten Mal sieht. Bezahlt habt ihr trotzdem den Alles-Könner-Tagessatz.

Eine sauber gezogene Grenze ist das Gegenteil davon. Im Audit benennen wir, was jenseits der Rechnungsauslösung im Argen liegt, das sehen wir ja trotzdem. Dann definieren wir die Schnittstelle so präzise, dass euer ERP-Partner sie umsetzen kann, ohne dreimal nachzufragen: welche Felder, welche Trigger, welches Format, wer ist Master für welche Daten. Genau an dieser undefinierten Übergabe zwischen CRM und ERP sterben nämlich die meisten Integrationsprojekte im Mittelstand. Nicht an der Technik. An der Frage, wem welcher Datensatz gehört, die vorher niemand gestellt hat.

Ein Dienstleister, der laut sagt, was er nicht macht, sagt euch damit auch, dass der Rest ernst gemeint ist. Fragt beim nächsten Angebot mal nach der Grenze. Wenn keine kommt, ist das die Antwort.

---

## RevShort #13: Attribution ist eine Entscheidung, kein Feature

Die Szene kennt jeder: Marketing präsentiert im Monatsreport den Deal für 80.000 Euro, gewonnen über die Demo-Anfrage vom Landingpage-Formular. Applaus für die Kampagne. Was im Report nicht steht: Vor diesem Formular lagen acht Touchpoints. Ein Podcast, zwei Webinare, ein Kollege des Käufers auf einer Messe, drei Newsletter, ein LinkedIn-Post vom Gründer. Der letzte Klick hat gewonnen. Alle anderen haben verloren, obwohl sie den Deal getragen haben.

Last Click lügt. First Touch lügt genauso, nur in die andere Richtung, dann bekommt eben der Podcast von vor 14 Monaten die gesamte Ehre und die Sales-Sequenz, die den Deal tatsächlich geschlossen hat, taucht nirgends auf. Beide Modelle sind bequem. Beide sind falsch.

Und jetzt der Teil, den euch kein Anbieter erzählt: Das ist kein Tool-Problem. Dreamdata, HockeyStack, das Attributionsmodul in eurer Suite, die können alle Touchpoints sammeln und nach jedem beliebigen Modell verrechnen. Was keins davon kann: entscheiden, welches Modell für euer Geschäft stimmt. Verkauft ihr in drei Wochen an Einzelentscheider oder in neun Monaten an Buying Committees mit fünf Leuten? Kommt die Hälfte eurer Pipeline über Empfehlungen, die nie einen Klick hinterlassen? Das sind Definitionsfragen. Ein Tool beantwortet sie nicht. Es rechnet nur aus, was ihr ihm sagt.

Die Reihenfolge ist deshalb nicht verhandelbar. Erst die Attributionslogik festlegen, und zwar nicht Marketing alleine im stillen Kämmerlein, sondern zusammen mit Sales und Geschäftsführung, weil alle drei nachher mit der Zahl arbeiten müssen. Welche Touchpoints zählen, wie wird gewichtet, was passiert mit Offline-Kontakten, ab wann gilt ein Deal als beeinflusst. Das ist ein Nachmittag Streit im Konferenzraum. Unangenehm, aber billig.

Wer die Reihenfolge umdreht, kauft erst das Tool, misst dann irgendwas und optimiert am Ende auf eine Zahl, die im Vertrieb keiner glaubt. Genau das passiert dauernd. Marketing steuert Budget nach einem Modell, das Sales für Fantasie hält, und in jedem Quartalsmeeting läuft dieselbe Debatte, ob die Kampagne den Deal gebracht hat oder der Kollege mit dem guten Draht zum Kunden. Die Debatte kostet mehr als jede Attributionslizenz.

Ein Modell, auf das sich alle geeinigt haben, schlägt ein präzises Modell, das nur Marketing versteht. Immer.

Also, bevor ihr das nächste Attributions-Tool testet: Habt ihr die Logik schon aufgeschrieben, die es rechnen soll?

---

## RevShort #14: "Wir kaufen Gong" ist keine Strategie

Der Satz fällt meistens im Q4-Planning. Die Win-Rate stagniert, das Coaching kommt zu kurz, irgendwer hat auf LinkedIn ein Video gesehen. Wir kaufen Gong. Beschlossen, budgetiert, abgehakt. Fühlt sich an wie eine Entscheidung.

Ist aber keine. Es ist eine vertagte.

Denn die eigentlichen Fragen sind nach dem Kauf exakt so offen wie davor. Wer hört sich die Calls an? Der Sales Lead hat 30 Direct Reports an der Pipeline und keine vier Stunden pro Woche für Call-Reviews. Was passiert mit dem, was auffällt? Gibt es ein Coaching-Format, einen Rhythmus, jemanden, der Einwandbehandlung wirklich trainiert, oder wird die Erkenntnis im Weekly kurz erwähnt und verdampft? Wer pflegt die Tracker, die Keywords, die Scorecards? Software beantwortet nichts davon. Software zeichnet auf.

Und so läuft es dann auch. Das Tool schneidet brav jeden Call mit, die Bibliothek wächst auf 2.000 Aufnahmen, reingeschaut hat seit Monat drei niemand mehr. Nach zwölf Monaten geht der CFO durch die SaaS-Liste, findet 15.000 Euro für ein Tool ohne erkennbaren Nutzer und kündigt. Zu Recht. Das Tool war nie das Problem. Es gab nur nie einen Prozess, den es hätte unterstützen können.

Die Reihenfolge, die funktioniert, ist unspektakulär. Erst den Prozess definieren: Wer reviewt wie viele Calls pro Woche, nach welchen Kriterien, was ist der Loop zurück ins Team, wer trägt das als Owner. Auf ein Blatt Papier passt das. Dann, zweiter Schritt, prüfen, was ihr schon bezahlt. Salesforce und HubSpot haben Gesprächsaufzeichnung und Auswertung inzwischen nativ an Bord, in den Editions, die bei vielen längst laufen. Nicht auf Gong-Niveau, das stimmt. Aber für ein Team mit acht Vertrieblern und einem sauber definierten Review-Prozess reicht nativ meistens locker. Und erst wenn der Prozess steht und die Suite nachweislich nicht kann, was er braucht, erst dann wird gekauft.

Klingt banal. Wird trotzdem fast immer andersrum gemacht, weil ein Kauf sich nach Fortschritt anfühlt und eine Prozessdefinition nach Arbeit. Der Kauf dauert eine Woche. Der Prozess zwingt euch, unbequeme Fragen zu klären, Zuständigkeiten festzunageln, Zeit im Kalender zu blocken.

Genau deshalb ist er das Einzige, was den Unterschied macht.

Welches Tool in eurem Stack war so eine vertagte Prozessentscheidung? Ihr wisst es vermutlich sofort.

---

## RevShort #15: Renewals in Excel sind Überraschungs-Churn

Dienstagvormittag, die Kündigung liegt im Postfach. Ein Kunde, 40.000 Euro Jahresvertrag, seit vier Jahren dabei. Im Vertrieb sind alle ehrlich überrascht, der Geschäftsführer fragt, wie das passieren konnte, der Account Manager sagt, der Kunde habe sich doch nie beschwert. Dann schaut jemand nach: Die Verlängerung stand seit 90 Tagen an. Es gab keinen Task, keinen Termin, kein Gespräch. Es gab eine Zeile in einer Excel-Liste, Reiter "Verträge 2026", zuletzt geändert im Februar.

Das ist kein Einzelfall, das ist der Normalzustand. Renewals leben in einer Tabelle, die eine Person pflegt, wenn sie dran denkt. Neben der Spalte mit dem Vertragsende steht ein Datum, das beim letzten Upsell nicht aktualisiert wurde. Ob jemand 90 Tage vorher zum Hörer greift, hängt davon ab, ob diese eine Person die Liste zufällig offen hat. Das ist kein Prozess. Das ist Hoffnung mit Zellbezügen.

Dabei ist die Mechanik lächerlich einfach. Drei Dinge gehören ins System: das Renewal-Datum als Pflichtfeld am Vertrag oder an der Opportunity, ein Owner, der namentlich dranhängt, und ein Playbook, das automatisch anläuft. 120 Tage vorher Health-Check, 90 Tage vorher Gespräch, 60 Tage vorher Angebot, bei Funkstille Eskalation an den Vertriebsleiter. Kein Mensch muss sich daran erinnern, das System erinnert. Genau dafür wurde es gebaut.

Und ihr müsst dafür nichts kaufen. Salesforce kann das mit Flows und Renewal-Opportunities, HubSpot mit Deal-Pipelines und Workflows, jedes CS-Tool sowieso. Die Funktionalität liegt in der Lizenz, die ihr seit Jahren bezahlt, unbenutzt. Der Aufbau ist ein paar Tage Konfiguration, keine Rocket Science, kein Projekt mit Lenkungsausschuss.

Warum existiert die Excel dann trotzdem überall? Weil sie nie eine Lösung war, sondern ein Symptom. Sie entsteht, wenn im CRM die Vertragsdaten fehlen oder falsch sind, wenn niemand für Bestandskunden zuständig ist, wenn Renewal als Verwaltungsakt gilt statt als Umsatz. Die Tabelle ist der sichtbare Beweis, dass der Prozess fehlt. Man erkennt es auch an der Sprache: Firmen mit Prozess reden über Net Revenue Retention. Firmen mit Excel reden über den Kunden, der letzte Woche überraschend gekündigt hat.

Rechnet kurz mit: Bei 2 Millionen Bestandsumsatz kostet jeder Prozentpunkt vermeidbarer Churn 20.000 Euro. Jedes Jahr. Wie viele Zeilen hat eure Liste?

---

## RevShort #16: Euer Lead-Score misst Fleiß, nicht Kaufabsicht

Zehn Punkte für eine geöffnete Mail. Fünf für den Klick, fünfzehn fürs Whitepaper, zwanzig für den Webinar-Besuch. Ab achtzig Punkten gilt der Lead als heiß und wandert an Sales. Klingt nach System. Ist aber nur Arithmetik über Aktivität, und Aktivität sagt nichts über Budget, nichts über Timing, nichts über die Frage, ob dieser Mensch überhaupt etwas entscheiden darf.

Das Ergebnis kennt jeder Vertriebler: der Dauerklicker. Ein Werkstudent bei einem Konzern, der jeden Newsletter öffnet, jedes Whitepaper zieht, jedes Webinar bucht, weil er eine Seminararbeit über euer Themenfeld schreibt. Score: 240. Kaufwahrscheinlichkeit: null. Daneben der Geschäftsführer eines 80-Mann-Maschinenbauers, der einmal die Preisseite besucht hat und drei Minuten auf dem Case Study geblieben ist. Score: 25. Der Score sortiert den Werkstudenten nach oben und den echten Deal nach unten, und zwar systematisch, weil er Fleiß belohnt statt Absicht.

Dazu kommt die Inflation. Jede neue Kampagne verteilt Punkte, keine nimmt welche weg, und nach zwei Jahren hat die halbe Datenbank Scores jenseits der Schwelle. Gepflegt wird das Modell von der Person, die gerade Zeit hat, oft genug der Praktikant im Marketing, der die Punktwerte nach Gefühl setzt, weil ihm niemand eine Logik mitgegeben hat. Sales merkt das nach der dritten toten Übergabe und hört auf, den Score anzuschauen. Völlig zu Recht. Ab da ist das Scoring nicht nur nutzlos, sondern Fassade: Es suggeriert Priorisierung, wo keine stattfindet.

Was fehlt, ist keine Software. HubSpot, Salesforce, jedes MAP kann Scoring nativ, das Rechenwerk ist das kleinste Problem. Was fehlt, ist eine Hypothese. Wer kauft bei euch wirklich, und woran erkennt man das früh? Vielleicht ist es die Firmengröße plus Branche plus Preisseiten-Besuch. Vielleicht ist es die zweite Person aus demselben Unternehmen innerhalb einer Woche. Das steht in euren gewonnenen Deals der letzten zwei Jahre, man muss nur reinschauen. Und dann braucht die Hypothese einen Feedback-Loop: Sales bewertet jede Übergabe, die Punktlogik wird quartalsweise gegen echte Abschlüsse geprüft und nachjustiert.

Ohne diese beiden Dinge, Hypothese und Loop, ist Lead-Scoring Nummerologie. Man addiert Zahlen, die jemand mal ausgedacht hat, und behandelt die Summe wie eine Wahrheit.

Kleiner Test für euer Modell: Zieht die Scores eurer letzten zehn gewonnenen Deals am Tag der Übergabe. Wenn ihr jetzt zögert, kennt ihr die Antwort schon.

---

## RevShort #17: Der Zapier-Friedhof

Bestandsaufnahme bei einem Kunden, 60 Leute, solide gewachsen: 47 Zaps. Gebaut über vier Jahre von vier verschiedenen Leuten, von denen zwei nicht mehr in der Firma sind. Dokumentation existiert nicht, Namenskonventionen auch nicht, ein Zap heißt "Test Kopie 2 FINAL". Und einer davon, der die Deals ans Rechnungstool übergibt, schlägt seit drei Wochen still fehl, weil irgendwer im CRM ein Feld umbenannt hat. Gemerkt hat es niemand. Aufgefallen ist es erst, als ein Kunde anrief und fragte, wo seine Rechnung bleibt.

Das ist kein Zapier-Problem. Zapier und Make sind völlig legitime Werkzeuge, für Prototypen sogar die besten: In einer Stunde steht ein Workflow, den man erst mal beobachten kann, bevor man ihn richtig baut. Für Low-Volume-Kram, der beim Ausfall niemandem wehtut, die Slack-Nachricht bei neuen Deals, der Export in ein Sheet, spricht auch dauerhaft nichts dagegen.

Das Problem beginnt an einer klar benennbaren Grenze, und die heißt geschäftskritisch. Sobald ein Workflow Umsatz berührt, Leads routet, Rechnungen auslöst, Verträge anstößt, ändert sich die Anforderung fundamental. Nicht die Funktion ändert sich. Die Fehlerbehandlung.

Genau da liegt der Unterschied zwischen Automatisierungs-Kleber und Integrationsarchitektur. Kleber führt aus, solange alles gut geht. Architektur geht davon aus, dass Dinge schiefgehen, weil sie das tun. APIs haben Timeouts, Systeme haben Wartungsfenster, Kollegen benennen Felder um. Eine Integration, die das ignoriert, ist keine kleinere Version einer richtigen Integration. Sie ist eine tickende, nur weiß keiner, wie laut es knallt und wann.

Konkret heißt Architektur drei Dinge. Monitoring: Wenn etwas fehlschlägt, geht innerhalb von Minuten ein Alert an einen Menschen, nicht in einen Log, den keiner liest. Retry-Logik: Ein Timeout um 3 Uhr nachts wird automatisch wiederholt statt kommentarlos verworfen, und was nach drei Versuchen noch failt, landet in einer Queue zur manuellen Klärung, damit kein Datensatz einfach verschwindet. Und Ownership: Ein Mensch mit Namen ist zuständig, kennt die Strecken, wird informiert, bevor jemand ein Feld anfasst. Ob darunter dann Make läuft, n8n, Workato oder Custom Code, ist ehrlich gesagt zweitrangig.

Die Frage an euren Stack ist deshalb nicht, welches Automatisierungstool ihr nutzt. Die Frage ist: Wenn heute Nacht eure wichtigste Strecke bricht, wer merkt es, und wann? Wenn die Antwort "der Kunde, nächste Woche" lautet, wisst ihr, was zu tun ist.

---

## RevShort #18: Eine Pipeline, drei Wahrheiten

Montag, neun Uhr, Führungsrunde. Marketing legt das Dashboard auf den Screen: 2,4 Millionen Pipeline. Der Vertriebsleiter hat seinen Report dabei, da stehen 1,9. Und die Geschäftsführung bringt ihre Excel mit, sonntagabends gepflegt, die sagt 2,8. Zwanzig Minuten gehen dafür drauf, zu klären, welche Zahl stimmt. Für die Frage, was mit der Pipeline passieren soll, bleibt keine.

Der Reflex ist immer derselbe: Wir brauchen besseres Reporting. Ein neues Dashboard, vielleicht Power BI, vielleicht jemand, der die Reports vereinheitlicht. Klingt vernünftig. Löst nichts.

Denn die drei Zahlen sind alle korrekt. Das ist das Perfide daran. Marketing zählt jede Opportunity ab Stage 1, weil da die Kampagnen-Attribution dranhängt. Der Vertrieb zählt ab Qualifizierung, weil alles davor sowieso Rauschen ist. Und in der Excel stehen noch zwei Deals, die im CRM längst verschoben wurden, plus einer, den der Geschäftsführer selbst angebahnt hat und der nie eingetragen wurde. Drei Quellen, drei Definitionen, drei Wahrheiten. Jede in sich schlüssig.

Das ist kein Reporting-Problem. Das ist ein Datenschicht-Problem. Reporting zeigt nur an, was drunter liegt, und drunter liegt bei den meisten Firmen zwischen 20 und 200 Leuten keine gemeinsame Antwort auf die einfachsten Fragen. Ab welcher Stage zählt ein Deal als Pipeline? Gewichtet oder nominal? Wann fliegt eine tote Opportunity raus? Solange jede Abteilung das anders beantwortet, produziert jedes neue BI-Tool nur eine vierte Zahl. Schöner formatiert, genauso umstritten.

Die Lösung ist unspektakulär und genau deshalb so selten: eine Definition, eine Datenquelle, ein Report. Die Definition wird einmal entschieden, schriftlich, mit Geschäftsführung und Vertrieb am selben Tisch. Die Datenquelle ist das CRM, und zwar nur das CRM, was auch heißt, dass der Deal des Geschäftsführers da rein muss wie jeder andere. Und der Report wird aus dieser einen Quelle gebaut, für alle gleich. Marketing sieht dieselbe Zahl wie der CFO, ob sie ihnen gefällt oder nicht.

Das ist Architekturarbeit. Felder, Validierungen, Stage-Logik, ein paar Automatisierungen, die Altlasten wegräumen. Kein Tool-Kauf, kein sechsmonatiges BI-Projekt, eher eine Woche konzentriertes Aufräumen im System, das ihr längst bezahlt.

Danach ist das Montagsmeeting nicht kürzer. Aber die zwanzig Minuten gehen in Deals statt in Zahlenabgleich.

Rechnet mal aus, was euch die Frage, welche Zahl stimmt, pro Jahr an Führungszeit kostet. Und dann fragt euch, warum die Antwort ein weiteres Dashboard sein soll.

---

## RevShort #19: Der kaputte Prozess zieht mit um

Irgendwann ist der Frust groß genug. Die Reports stimmen nicht, das System ist voll mit Dubletten, der Vertrieb trägt nur noch das Nötigste ein, und dann fällt der Satz, der sechsstellige Projekte auslöst: Wir brauchen ein neues CRM.

Verständlicher Impuls. Meistens falsch.

Denn was genau soll das neue System besser machen? Die Dubletten entstehen, weil es keine sauberen Anlage-Regeln gibt und niemand dedupliziert. Die ziehen mit um, das Migrationsskript kopiert sie treu und brav rüber. Die Workflow-Ruinen, also die vierzig Automatisierungen, von denen keiner mehr weiß, welche noch was tut, werden im neuen System nachgebaut, weil ja irgendwas davon wichtig sein könnte. Und das Misstrauen des Vertriebs ins System, das über Jahre gewachsen ist, weil die Daten drin nie gestimmt haben, wandert gleich mit. Neue Oberfläche, alte Skepsis. Nach sechs Monaten und einem Projektpreis, für den man einen Senior ein Jahr hätte beschäftigen können, sitzt ihr vor demselben Zustand mit anderem Logo.

Wir haben Migrationen gesehen, bei denen 180.000 Kontakte umgezogen wurden, von denen 60.000 Dubletten oder tot waren. Das hat niemand vorher geprüft. Der Umzugskarton wurde nicht ausgepackt und aussortiert, er wurde versiegelt und teuer transportiert.

Die Reihenfolge muss andersrum sein. Erst das Datenmodell sanieren: Welche Objekte, welche Felder, welche Pflichtangaben braucht der Prozess wirklich? Dann die Prozesse geradeziehen: Lead-Anlage, Stage-Definitionen, Routing, Übergaben. Dann aufräumen, deduplizieren, Totes archivieren. Das alles geht im bestehenden System. Es ist unglamourös, es fühlt sich weniger nach Aufbruch an als ein Systemwechsel, und es kostet einen Bruchteil.

Und dann, erst dann, stellt sich die Frage nach dem Wechsel noch mal. Oft beantwortet sie sich von selbst, denn ein aufgeräumtes Salesforce oder HubSpot mit sauberem Datenmodell kann plötzlich erstaunlich viel von dem, wofür das neue System gekauft werden sollte. Die Featureliste des Wettbewerbers war nie das Problem. Das Problem war, dass niemand das vorhandene System je zu Ende konfiguriert hat.

Manchmal ist der Wechsel trotzdem richtig, klar. Wenn die Plattform strukturell nicht passt, wenn Lizenzkosten aus dem Ruder laufen, wenn ein Konzern-Carve-out ansteht. Aber das ist die Ausnahme, nicht der Reflex.

Bevor ihr die Umzugsfirma bestellt: Wer hat eigentlich mal geprüft, was in den Kartons ist?

---

## RevShort #20: Der Azubi macht bei euch die Elektrik

Stellt euch vor, ihr lasst euer Haus neu verkabeln. Der Meisterbetrieb kommt zum Erstgespräch, macht einen kompetenten Eindruck, ihr unterschreibt. Am Montag steht der Azubi allein vor eurem Sicherungskasten. Der Meister schaut Freitag mal drüber, remote.

Im Handwerk undenkbar. In der CRM-Beratung ist es das Geschäftsmodell.

Das Modell heißt Junior-Leverage und funktioniert so: Der Senior verkauft das Projekt und taucht danach in Lenkungskreisen auf. Die eigentliche Arbeit in eurem System machen Leute, die vor 18 Monaten ihren Abschluss gemacht haben und deren Tagessatz trotzdem vierstellig fakturiert wird. Die Marge lebt von genau dieser Differenz. Für die Beratung ist das rational. Für euer System ist es ein Risiko, das ihr auch noch bezahlt.

Denn ein Produktivsystem ist kein Übungsgelände. Wer noch nie eine Automation debuggt hat, die um drei Uhr nachts 4.000 falsche E-Mails rausgeschickt hat, baut anders. Wer noch nie erlebt hat, wie ein unbedachtes Feld-Update eine Integrationskette triggert, die Rechnungen dupliziert, denkt in Happy Paths. Diese Erfahrung steht in keinem Zertifikat. Sie entsteht nur auf eine Art: indem man Dinge kaputtgemacht und selbst wieder repariert hat. Nicht eskaliert, nicht ans nächste Ticket weitergereicht. Selbst repariert, mit schwitzigen Händen, während der Vertrieb nicht arbeiten kann.

Das ist die eigentliche Qualifikationsfrage, und sie kommt in keinem Pitch vor. Referenzlogos sagen euch, wen die Firma als Kunde gewonnen hat. Sie sagen euch nicht, wer sich bei euch einloggt.

Seniorität im System schlägt Headcount im Deck. Ein Mensch mit zehn Jahren Schrauberfahrung löst in zwei Tagen, wofür zwei Juniors zwei Wochen brauchen, und hinterlässt dabei keine neuen Baustellen. Das rechnet sich sogar bei doppeltem Tagessatz, weil ihr nicht Zeit kauft, sondern die Abwesenheit von Folgeschäden. Die teuerste Beratung ist die, deren Fehler ihr zwei Jahre später von jemand anderem ausbauen lasst.

Beim nächsten Angebot also nicht fragen, wie viele Leute die Firma hat. Fragen, wer konkret in eurem System arbeiten wird, wie viele Jahre die Person schon Produktivsysteme anfasst, und was ihr größter selbstverschuldeter Ausfall war. Wer auf die letzte Frage keine Geschichte hat, hat entweder nie gebaut oder lügt.

Würdet ihr dem Azubi allein euren Sicherungskasten geben? Euer CRM hängt an mehr Umsatz als eure Elektrik.

---

## RevShort #21: Woran verdient euer Dienstleister?

Vergesst die Referenzliste für einen Moment. Vergesst die Zertifikate, die Case Studies, das Partnerlogo. Die aufschlussreichste Information über euer künftiges Projekt steht im Preismodell.

Anreize bestimmen Verhalten. Nicht Absichten, nicht Werte-Slides, Anreize. Ein Dienstleister, der nach Tagessätzen abrechnet, verdient an jedem Tag, den euer Projekt länger dauert. Das macht ihn nicht zum schlechten Menschen. Es macht ihn zu jemandem, dessen wirtschaftliches Interesse und euer Projektziel in entgegengesetzte Richtungen zeigen. Jede entdeckte Komplexität ist für ihn gute Nachricht. Jeder zusätzliche Workshop, jede Verlängerung der Discovery-Phase, jedes "da müssen wir noch mal tiefer rein" zahlt auf sein Quartal ein. Warum sollte er schnell fertig werden? Die ehrliche Antwort: Es gibt keinen Grund. Schnell fertig werden ist in diesem Modell ein Verlustgeschäft.

Festpreis dreht die Mechanik um. Wer ein Audit für einen festen Betrag in fünf Tagen anbietet, verliert Geld mit jedem Tag, den er trödelt, und verdient an Effizienz. Plötzlich lohnt es sich, Werkzeuge zu bauen, die die Analyse beschleunigen. Plötzlich lohnt Erfahrung, weil der 47. Blick in eine kaputte Salesforce-Org schneller geht als der dritte. Der Anreiz zeigt auf Ergebnis statt auf Dauer.

Und hier steckt die zweite Information, die im Preismodell mitgeliefert wird: Festpreis kann sich nur leisten, wer sein Handwerk kalkulieren kann. Wer nicht weiß, wie lange etwas dauert, weil er es noch nicht oft genug gemacht hat, muss nach Aufwand abrechnen, sonst ruiniert ihn die eigene Unsicherheit. Der Tagessatz ist auch eine Versicherung gegen die eigene Unerfahrenheit, die ihr als Kunde bezahlt. Ein fester Preis mit fester Frist ist dagegen eine Wette des Anbieters auf sich selbst. Die geht nur auf, wenn er das Problem schon dutzendfach gesehen hat.

Natürlich hat Festpreis Grenzen. Ein Sechs-Monats-Programm mit unklarem Scope kann seriös niemand pauschal bepreisen, und wer es trotzdem tut, hat den Puffer einfach versteckt. Aber abgrenzbare Bausteine, ein Audit, eine Migration, eine Integration mit definiertem Umfang: alles bepreisbar, wenn man weiß, was man tut.

Die Frage fürs nächste Angebotsgespräch ist also nicht, was der Tag kostet. Sondern: Was kostet das Ergebnis, und bis wann liegt es vor? An der Reaktion auf diese Frage erkennt ihr mehr als in drei Referenzcalls.

---

## RevShort #22: Best of Breed war 2015 richtig

Es gab eine Zeit, da war der Ratschlag goldrichtig: Kauf für jede Aufgabe das beste Spezialtool und verbinde alles per API. 2015 konnten die Suiten schlicht zu wenig. Salesforce ohne Zusatztools hieß Vertrieb ohne Sequencing, Forecasting auf Excel-Niveau, Angebote in Word. Wer damals Best of Breed baute, hatte einen echten Vorsprung.

Nur ist 2015 elf Jahre her, und der Ratschlag wird immer noch erteilt, als wäre nichts passiert.

Passiert ist eine Menge. Die Suiten haben nachgerüstet, teils gebaut, teils zugekauft: Sequencing, Meeting-Routing, Scheduling, Gesprächsaufzeichnung, Forecasting, Quoting, Ticketing. Alles nativ, alles in Editions, die viele Firmen ohnehin lizenziert haben. Der Funktionsabstand zur Point Solution ist von riesig auf klein geschrumpft, für ein Team mit 20 bis 200 Leuten meist auf null. Was nicht geschrumpft ist: der Preis der Trennung.

Denn jede Point Solution kostet dreimal. Die Lizenz sieht man. Die Integration sieht man erst, wenn sie bricht, und sie bricht, bei jedem API-Update, bei jedem Feldnamen, den jemand ändert. Und der Datenbruch, der Deal, der im Sequencing-Tool anders heißt als im CRM, der Anruf, der nie zurückgeschrieben wird, kostet still und dauerhaft. Zwölf Tools heißt elf Integrationen, die jemand pflegen muss, und ein Datenmodell, das über elf Nähte zusammengeflickt ist. Diesen Preis stellt niemand in Rechnung. Bezahlt wird er trotzdem.

Heißt das, alles in die Suite? Nein, und die Ausnahmen sind präzise benennbar, weil die Trennung dort strukturell ist und nicht historisch. Datenprodukte: Kontakt- und Firmendaten kann keine Suite erfinden, die kauft man. Cold-Email-Infrastruktur läuft aus Deliverability-Gründen absichtlich getrennt vom Hauptsystem, das ist Feature, nicht Schwäche. Billing und eSignature sind eigene, regulierte Welten mit eigener Logik. Und die Glue-Schicht, alles, was Systeme übergreifend verbindet und Daten konsistent hält, war nie Teil einer Suite und wird es nie sein.

Der Rest ist verhandelbar geworden. Das separate Sequencing-Tool, das Forecasting-Tool, das Routing-Tool, das Conversation-Intelligence-Tool: für die allermeisten Mittelständler Erinnerungen an eine Marktlage, die nicht mehr existiert. Die Suite kann es. Sie kann es nur nicht von allein, jemand muss es sauber konfigurieren, und genau daran scheitert es, nicht an der Featureliste.

Wann habt ihr eure Best-of-Breed-Entscheidungen zuletzt gegen den heutigen Stand der Suite geprüft? Wenn die Antwort "beim Kauf" lautet, prüft ihr gegen 2015.

