# APX Lumos v2.1 — Backend Ingest Spec

## Endpoint

```
POST /api/ingest
Content-Type: application/json
```

Override the endpoint by setting `window.AP_ENDPOINT` before the script loads.

### Delivery method

The client uses the **Beacon API** (`navigator.sendBeacon`) as the primary send mechanism.
This fires on `beforeunload` — i.e. when the user navigates away or closes the tab.
Fallback is `fetch` with `keepalive: true`.

**The backend must return `200 OK` (or `204`). The client ignores the response body entirely.**
There is no retry logic. If the request fails, the data is lost.

---

## Top-level payload

```json
{
  "_e": [ ...events ],
  "_m": { ...metadata }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `_e` | `array` | Batch of events collected during the page session. Always at least 2 events (`pv` on load + `ex` on exit). |
| `_m` | `object` | Session-level metadata, same for all events in the batch. |

---

## Metadata object (`_m`)

```json
{
  "v":  "2.1",
  "sr": "1920x1080",
  "vp": "1280x900",
  "tz": "Europe/Berlin",
  "lg": "en-GB"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `v` | `string` | SDK version |
| `sr` | `string` | Screen resolution (`widthxheight`) |
| `vp` | `string` | Viewport size at time of flush (`widthxheight`) |
| `tz` | `string` | IANA timezone string |
| `lg` | `string` | Browser language (`navigator.language`) |

---

## Event envelope (fields present on every event)

```json
{
  "t":  "pv",
  "i":  "550e8400-e29b-41d4-a716-446655440000",
  "s":  "3-1718000000000",
  "n":  3,
  "q":  7,
  "x":  1718000000000,
  "dk": "2024-06-10",
  "u":  "/services",
  "r":  "google.com"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `t` | `string` | Event type. See event types below. |
| `i` | `string` | Visitor UUID (UUIDv4). Persisted in localStorage + cookie `_ax` for 2 years. |
| `s` | `string` | Session ID. Format: `{sessionNumber}-{timestamp}`. Resets after 30 min of inactivity or a new day. |
| `n` | `integer` | Session number for this visitor (1 = first ever visit, 2 = second, etc.) |
| `q` | `integer` | Days since last visit. `0` on first visit or same-day return. |
| `x` | `integer` | Unix timestamp in milliseconds when the event was queued. |
| `dk` | `string` | Date key `YYYY-MM-DD` in the visitor's local time. |
| `u` | `string` | Page pathname at time of event (e.g. `/services/audit`). |
| `r` | `string\|null` | Referrer hostname only (e.g. `google.com`). `null` if direct or same-site. |

---

## Event types

### `pv` — Page view

Fired once on page load.

```json
{
  "t":   "pv",
  "ti":  "Apex Palantir — Salesforce Consulting",
  "pv":  2,
  "rv":  true,
  "sc":  3,
  "dv":  2,
  "utm": { "source": "linkedin", "medium": "cpc", "campaign": "sf-audit" }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `ti` | `string` | Page `<title>` |
| `pv` | `integer` | How many times this visitor has visited this specific path (cumulative, from localStorage) |
| `rv` | `boolean` | `true` if returning visitor (has a prior session) |
| `sc` | `integer` | Total session count for this visitor (same as `n`) |
| `dv` | `integer` | Device type: `0` = mobile (<768px), `1` = tablet (768–1023px), `2` = desktop (≥1024px) |
| `utm` | `object\|null` | UTM params if present. Keys: `source`, `medium`, `campaign`, `term`, `content`. `null` if none. |

---

### `sc` — Scroll depth milestone

Fired at 25%, 50%, 75%, and 100% scroll depth. Each milestone fires only once per page session.

```json
{
  "t":  "sc",
  "dp": 50,
  "tm": 23
}
```

| Field | Type | Description |
|-------|------|-------------|
| `dp` | `integer` | Scroll depth percentage reached (`25`, `50`, `75`, or `100`) |
| `tm` | `integer` | Seconds since page load when the milestone was hit |

---

### `sv` — Section visibility

Fired when a `section[id]` or `[data-ap-section]` element has been visible for more than 2 continuous seconds (50% threshold via IntersectionObserver).

```json
{
  "t":  "sv",
  "id": "c2VydmljZXM",
  "dr": 8
}
```

| Field | Type | Description |
|-------|------|-------------|
| `id` | `string` | The element's `id` or `data-ap-section` value, **base64-encoded** (standard btoa, `=` stripped). Decode with `atob()` to get the original ID. |
| `dr` | `integer` | Seconds the section was continuously visible |

---

### `cp` — Copy event

Fired when the visitor copies text on the page.

```json
{
  "t":  "cp",
  "ln": 142,
  "pw": "Enterprise-grade Salesforce implementation starting"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `ln` | `integer` | Character length of copied text |
| `pw` | `string` | First 50 characters of the copied text (preview) |

---

### `ct` — CTA click

Fired when the visitor clicks any element with a `data-ap-track` attribute.

```json
{
  "t":  "ct",
  "nm": "book-audit-cta",
  "cg": "audit",
  "vl": null
}
```

| Field | Type | Description |
|-------|------|-------------|
| `nm` | `string` | Value of `data-ap-track` attribute |
| `cg` | `string\|null` | Value of `data-ap-category` attribute, or `null` |
| `vl` | `string\|null` | Value of `data-ap-value` attribute, or `null` |

**HTML usage:**
```html
<a href="/contact" data-ap-track="book-audit-cta" data-ap-category="audit">Book an Audit</a>
```

---

### `dl` — Download click

Fired when the visitor clicks a link pointing to a tracked file extension:
`pdf, doc, docx, xls, xlsx, ppt, pptx, zip, csv`

```json
{
  "t":  "dl",
  "hr": "/assets/docs/apex-palantir-capabilities.pdf",
  "ex": "pdf"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `hr` | `string` | The `href` of the link (truncated to 200 chars) |
| `ex` | `string` | File extension |

---

### `ex` — Page exit

Fired on `beforeunload`. Always the last event in the `_e` array. Sent together with all other queued events in the same Beacon request.

```json
{
  "t":  "ex",
  "at": 94,
  "sd": 75
}
```

| Field | Type | Description |
|-------|------|-------------|
| `at` | `integer` | Active time on page in seconds. Only counts time when the tab was visible AND the visitor was not idle (idle = no interaction for 5s). |
| `sd` | `integer` | Maximum scroll depth reached on this page (0–100) |

---

### `cu` — Custom event

Fired manually via `ApexPalantir.track('event-name', { key: 'value' })`.

```json
{
  "t":  "cu",
  "nm": "pricing-tab-switch",
  "pp": { "tab": "enterprise" }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `nm` | `string` | Event name passed to `track()` |
| `pp` | `object` | Properties object passed to `track()`. Empty object `{}` if none. |

---

## Full example payload

```json
{
  "_e": [
    {
      "t": "pv", "ti": "Services — Apex Palantir",
      "pv": 1, "rv": false, "sc": 1, "dv": 2, "utm": null,
      "i": "550e8400-e29b-41d4-a716-446655440000",
      "s": "1-1718000000000", "n": 1, "q": 0,
      "x": 1718000000000, "dk": "2024-06-10",
      "u": "/services", "r": "linkedin.com"
    },
    {
      "t": "sc", "dp": 25, "tm": 8,
      "i": "550e8400-e29b-41d4-a716-446655440000",
      "s": "1-1718000000000", "n": 1, "q": 0,
      "x": 1718000008000, "dk": "2024-06-10",
      "u": "/services", "r": "linkedin.com"
    },
    {
      "t": "sv", "id": "c2VydmljZXM", "dr": 11,
      "i": "550e8400-e29b-41d4-a716-446655440000",
      "s": "1-1718000000000", "n": 1, "q": 0,
      "x": 1718000019000, "dk": "2024-06-10",
      "u": "/services", "r": "linkedin.com"
    },
    {
      "t": "ct", "nm": "book-audit-cta", "cg": "audit", "vl": null,
      "i": "550e8400-e29b-41d4-a716-446655440000",
      "s": "1-1718000000000", "n": 1, "q": 0,
      "x": 1718000045000, "dk": "2024-06-10",
      "u": "/services", "r": "linkedin.com"
    },
    {
      "t": "ex", "at": 94, "sd": 75,
      "i": "550e8400-e29b-41d4-a716-446655440000",
      "s": "1-1718000000000", "n": 1, "q": 0,
      "x": 1718000094000, "dk": "2024-06-10",
      "u": "/services", "r": "linkedin.com"
    }
  ],
  "_m": {
    "v": "2.1",
    "sr": "1920x1080",
    "vp": "1280x900",
    "tz": "Europe/Amsterdam",
    "lg": "nl-NL"
  }
}
```

---

## Notes

- **No authentication** on the ingest endpoint by design — treat all incoming data as untrusted. Validate types before writing to a store.
- **Idempotency**: there is no deduplication on the client side. If `beforeunload` fires multiple times in quick succession (rare), you may receive duplicate batches. Use `s` (session ID) + `x` (timestamp) as a composite key for dedup if needed.
- **Section IDs** in `sv` events are base64-encoded. Decode with `atob(id)` on the backend. Padding (`=`) was stripped on the client, add it back before decoding if your base64 decoder requires it: pad to a multiple of 4.
- **Active time** (`at` in `ex` events) only counts periods where the tab was in the foreground and the visitor interacted within the last 5 seconds. It will always be ≤ wall-clock time on page.
