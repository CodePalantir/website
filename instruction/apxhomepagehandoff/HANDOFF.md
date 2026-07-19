# Handoff: Neue Homepage → Jekyll-Repo (apx-revops.com)

Guidance für Claude Code, das lokal im Jekyll-Projekt arbeitet. Stand 14.07.2026, abgestimmt mit Alex.

## Die eine Grundregel

**Nutze die Komponenten, die im Repo schon existieren, wo immer das sinnvoll ist.** Das Repo hat einen funktionierenden Header mit Mega-Menü und Mobile-Nav (`_includes/shared/header.html`), einen Footer, einen Logo-Strip mit Scroll-Animation und Reduced-Motion-Handling (`_includes/shared/logo_strip.html`), Cookie-Consent, SEO-Tags, Lucide-Setup und eine Tailwind-v4-Pipeline. Der Prototyp hat eigene, vereinfachte Versionen davon gebaut, weil er self-contained sein musste. Im Repo gilt: die Repo-Version gewinnt, der Prototyp liefert nur Inhalt und Design-Intention. Beispiel: der Prototyp hat ein statisches Logo-Register mit divide-x; wenn der existierende animierte Logo-Strip dieselbe Aufgabe erfüllt, nimm den. Baue nur neu, was es wirklich nicht gibt (Möbius-Sektion, Hex-Netz-Sektion, Degradation-Kurve, Diagnostic-Tabelle, Services-Bento, Stacks-Spalten).

**Und genauso wichtig: der Sektions-Flow des Prototyps ist eine Empfehlung, KEINE Regel.** Wenn eine Sektion als Include besser in anderer Reihenfolge, zusammengelegt oder gegen eine bestehende Repo-Sektion getauscht funktioniert, entscheide das selbst und begründe es kurz im Commit. Was nicht verhandelbar ist, steht unter "Harte Regeln".

## Auftrag

1. Die neue Homepage (Inhalt aus `apx-root-landingpage.html` bzw. `apx-root-v9-body.html`) wird die Root-Seite `/`.
2. Die alte Homepage zieht 1:1 nach `/salesforce` um. Alle anderen Subpages bleiben AS IS.
3. 301-Redirects für alles, was durch den Umzug bricht. Redirect-Plan und IA-Details stehen im Projekt-Doc `claude/website-gap-analyse.md` (alte Service-URLs → `/salesforce/*`).
4. Netlify baut mit `bundle exec jekyll build`, Tailwind via `npm run build` (v4 CLI, `assets/css/input.css` → `tailwind.css`). Redirects entweder in `netlify.toml` oder `_redirects` im Publish-Ordner.

## Quelldateien in diesem Paket

- `apx-root-landingpage.html`: der Prototyp, self-contained. Er ist visueller RAHMEN und Anreiz, kein Soll: wo du mit Repo-Mitteln eine sauberere Lösung hast, nimm sie. Verbindlich sind nur die harten Regeln unten, die Grafiken und die Token-Entscheidungen (ein H2-Maß text-4xl/md:text-5xl, Sektionsraster py-20/md:py-28, ein Button-Stil rounded-lg mit arrow-right und Wording "Book the €2,450 Audit", Mono-Tags, Callout mit Gradient-Kante, Materialsystem der dunklen Flächen inkl. CTA-als-dunkler-Raum und Footer #070B14).
- Der Prototyp enthält außerdem: Mobile-Navigation (Hamburger mit X-Morph, Scroll-Lock), Mobile-Varianten der Grafiken (Möbius-Band ohne Labels über einer nummerierten Phasen-Liste; Hexnetz als eigene Hochformat-SVG `hexnet-mobile.svg` aus `gen_hexnet_mobile.py` mit größerer Type, ALLE 18 Tools bleiben mobil sichtbar, das war Alex explizit wichtig), Reveal-Animationen (IntersectionObserver mit Stagger, prefers-reduced-motion respektiert) und Hover-Zustände. Das JS/CSS dafür steht im <script>/<style>-Block des Prototyps und muss mit portiert werden.
- Tailwind-v4-Falle aus der Praxis: `divide-y` setzt in v4 border-bottom auf :not(:last-child) mit currentColor. Im Services-Ledger und ähnlichen Stellen die divide-Farbe explizit setzen, sonst gibt es dunkle Linien.
- `apx-root-v9-body.html`: der Body mit Asset-Tokens (`{{APX_LOGO}}`, `{{CL_*}}` etc.) statt Base64. Das ist deine Arbeitsgrundlage zum Zerschneiden in Includes. Tokens ersetzt du durch normale Jekyll-Asset-Pfade (`relative_url`), NICHT durch Data-URIs.
- `assemble.py`: nur Doku, wie der Prototyp gebaut wurde. Im Repo überflüssig.
- `gen_hexnet.py`, `gen_hexnet_mobile.py`, `mobius.svg`, `hexnet.svg`, `hexnet-mobile.svg`, `degradation-curve.svg`, `salesforce-cloud.svg`: die Grafiken. SVGs als statische Dateien einchecken (inline oder als Datei, deine Entscheidung; inline erlaubt currentColor/Font-Vererbung). Die Generatoren mit einchecken (z.B. `_tools/`), damit spätere Änderungen parametrisch bleiben statt von Hand im SVG.
- `logos_norm/`: programmatisch normalisierte Kundenlogos (einheitliche Cap-Höhe, einheitliches Grau #808898). Nur nötig, falls du das statische Register des Prototyps übernimmst; für den bestehenden Logo-Strip existieren die Original-WebPs schon im Repo.

## Technische Hinweise

- **Tailwind:** Der Prototyp trägt einen Supplement-CSS-Block mit Utility-Klassen, die in der eingecheckten `tailwind.css` fehlen (sie ist stale). Das ist KEIN zu portierendes CSS: sobald die neuen Templates im Repo liegen und `npm run build` läuft, generiert Tailwind v4 alle Klassen selbst. Supplement-Block wegwerfen, danach visuell gegen den Prototyp diffen.
- **Fonts/Icons:** Plus Jakarta Sans ist im Repo self-hosted (DSGVO), Lucide wird in `default.html` initialisiert. Nichts davon neu einbinden.
- **Meta:** Title/Description der neuen Root aus dem Prototyp-`<head>` übernehmen (RevOps Technology Agency, nicht mehr Salesforce-only). `_config.yml`-Description ist noch die alte Salesforce-Zeile, die bei dem Zug mitdrehen. `/salesforce` bekommt die bisherigen Homepage-Metas.
- **Team-Fotos:** `default.html` preconnected zu media.licdn.com / i.pravatar.cc. Wenn Team-Bilder nur noch lokal geladen werden, kann das weg, ist aber nicht Teil dieses Auftrags.
- **Navigation:** Prototyp-Nav zeigt Home / Lifecycle / Services / Stacks / Cases / About + EN·DE-Schalter. Lifecycle, Stacks, Cases existieren als Seiten noch nicht, DE auch nicht. Links, deren Ziel es nicht gibt, nicht live schalten: auf Anker der Homepage zeigen lassen oder weglassen, bis die Seiten existieren. Bestehendes Services-Mega-Menü im Header weiterverwenden; es zeigt auf die Salesforce-Service-Seiten, die ja bleiben.

## Harte Regeln (Copy-Integrität, von Alex durchgesetzt)

1. Keine erklärenden Krücken ("In plain terms:", "Einfach gesagt:"). Wenn eine Sektion einen Übersetzungssatz braucht, ist die Sektion falsch.
2. Keine Selbstzertifizierung: kein "honestly", "frankly", "to be clear". Alex: "An honest person does not need to say honestly."
3. Keine Gedankenstriche in Copy. Punkt, Komma, Doppelpunkt, in Mono-Zeilen Mitteldot.
4. Kein snake_case auf Inhaltswörtern. Mock-Systemnamen im Hero-Terminal (`lead_routing_matrix`) bleiben, dort authentisch.
5. Abgelehnt und nicht wiederbeleben: "No junior leverage, no handoffs". Bestandskräftig stattdessen: "Senior engineers only. Fixed scope, fixed price where it can be fixed. Every engagement starts with evidence, not a workshop."
6. Keine neuen Zeilen mit Behauptungsgehalt erfinden. Copy 1:1 aus dem Prototyp übernehmen. Noch OHNE finale Freigabe von Alex (drin lassen, aber nicht anfassen und nirgends sonst weiterverwenden): Beispielpreis "€8k", "most of our audits start exactly there" / "found in a typical audit", "We commit into your data team's repo", Cross-Layer-Headline "The layer your whole stack runs through."

## Qualitätsmaßstab

Kalibrierung: Stripe/Linear = 10. Der Prototyp steht nach drei harten Kritik-Runden bei 8,5 (Desktop-Craft) und 9 (Mobile); Art Direction bei 7,5 mit klarer Ansage, was die letzten Punkte kostet: ein echter Proof-Moment (Kundenzitat mit Zahl, Case-Kennzahlen) fehlt auf der gesamten Seite und ist CONTENT, kein Design (liegt bei Alex, siehe Content-Shopping-Liste), plus eigene Momente für die konventionelleren Mittelsektionen (Pattern/Services/Stacks). Screenshot-Vergleich gegen den Prototyp bei 1512px UND 390px ist Pflicht, bevor irgendwas als fertig gilt; bei 360px darf nichts horizontal scrollen. Bekannte Messlatten: Mono-Microcopy auf Weiß ≥ 4,5:1 (slate-500 ist die Grenze), Grün exklusiv für Passing-Status, ein CTA-Wording seitenweit, Grafiken nicht nachbauen sondern die gelieferten SVGs verwenden. Vorsicht bei responsiven `<br class="hidden ...">`: die fressen Leerzeichen, immer mit explizitem Space nach dem br setzen (hat zweimal reale Bugs erzeugt, "EngineeringRevenue" und "whereyour").

## Kontext im Claude-Projekt

`claude/website-gap-analyse.md` (IA + Redirects), `claude/icp-testing-ergebnisse.md` (Persona-Feedback, Copy-Regeln, Content-Shopping-Liste), `claude/design-abnahme-protokoll.md` (alle Design-Entscheidungen und offene Freigaben). Bei Widerspruch zwischen diesem Dokument und dem Protokoll gilt das Protokoll plus Nachfrage bei Alex.
