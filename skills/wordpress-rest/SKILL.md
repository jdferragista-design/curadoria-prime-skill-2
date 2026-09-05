---
name: wordpress-rest
description: "WordPress REST: media uploads, post updates, scheduling."
version: 1.0.0
author: Hermes (curator)
license: MIT
metadata:
  hermes:
    tags: [wordpress, rest-api, cms, publishing]
    related_skills: [curadoria-prime]
---

# WordPress REST — media, posts, scheduling

Operate a WordPress site programmatically via `wp-json/wp/v2` with Basic auth
(app password). Validated 03/09/2026 on curadoriaprime.com (image uploads,
featured images, draft rewrites, cluster scheduling).

## Auth

- `Authorization: Basic base64(user:app_password)`; app passwords contain
  SPACES — never `source .env` in bash (shell splits the line, exit 127).
  Parse the `.env` in Python (`line.split('=', 1)`) and build the header there.
- A freshly UI-created draft can have an empty slug (`//`) — fix with
  `POST /posts/{id} {"slug": ...}`.

## Media upload (the pitfall that costs a 400)

`POST /wp-json/wp/v2/media` with raw bytes as the body requires BOTH:
- `Content-Type: image/jpeg` (or webp/png)
- `Content-Disposition: attachment; filename="name.jpg"` — **without this
  header WP returns HTTP 400 Bad Request** (it derives the mime from the
  filename, not just Content-Type).

The filename becomes the library slug: avoid double extensions (`x.webp.jpg` →
ugly slug; if wrong, `DELETE /media/{id}?force=true` and re-upload).
Set `alt_text`/`title` afterwards with `POST /media/{id}` (JSON body).

## Featured image + post content

- Featured: `POST /posts/{id}` with `{"featured_media": <media_id>}` — then
  VERIFY by re-reading the post; a silent NENHUMA/NONE means the set didn't stick.
- Updating an existing post the editor may have touched in the UI: GET
  `?context=edit` → back up `content.raw` to disk → PUT new content → re-read
  and compare **byte a byte** with the local file before claiming success.

## Scheduling

- `POST /posts/{id}` with `{"status": "future", "date": "YYYY-MM-DDT08:00:00"}`.
  `date` is in the SITE timezone — read it from `GET /wp-json/`
  (`timezone_string`/`gmt_offset`); verification shows `date_gmt` shifted
  (11:00 GMT = 08:00 BRT). Don't misread the shift as a wrong schedule.
- Structured data in the post body (JSON-LD `datePublished`) should be updated
  to the publish date BEFORE the PUT, or schema and reality diverge.
- Acceptance check per post: `status == "future"`, `date_gmt` correct,
  `featured_media != 0`, `content.raw == local file`.

## Discovery

- `GET /posts?status=draft&per_page=100&_fields=id,slug,title,status,date,featured_media`
  to find posts; sites with <100 posts 400 on page=2 — page 1 covers all.
- `GET /media?search=<term>` to reuse existing library images instead of
  re-uploading.

## PITFALL: `?include=` silently returns [] for non-published posts

The posts collection defaults to `status=publish`, so `?include=5084,5090,...`
against scheduled/draft posts returns **HTTP 200 with an empty array** — no
error, easy to misread as "posts deleted" or "auth broken". And a single
request with `status=future,draft,publish` (comma list) also returns nothing
useful. Working pattern: loop one request per status
(`status=publish`, `status=future`, `status=draft`, `status=pending`,
`per_page=100&orderby=date`) and build an id→post map from the union. Use
this to verify a schedule actually landed on the WP side.

- Related WAF quirk (curadoriaprime.com): single-post endpoint `/posts/{id}`
  returns 401 even with valid auth; the collection endpoints with Basic auth
  work. Detect "published" as presence in `?include=` (publish-only) results.

## Rank Math SEO meta (title/description) — validated 04/09/2026

The `<title>` and meta description rendered on the page come from Rank Math
postmeta, NOT from the post content or `POST /posts/{id} {"meta": ...}`
(that silently no-ops — `context=edit` shows the keys absent). Working
endpoint:

```
POST /wp-json/rankmath/v1/updateMeta
{"objectType": "post", "objectID": <id>,
 "meta": {"rank_math_title": "...", "rank_math_description": "..."}}
```

- Wrong shapes fail loudly: missing `objectType`/`objectID` → 400
  `rest_missing_callback_param` (the error message lists the required params —
  read it, it reveals the schema).
- Verify by fetching the public page with a cache-buster (`?cb=123` +
  `Cache-Control: no-cache`): full-page cache serves stale HTML for seconds
  after the write, so an immediate re-check can show the OLD title and fool
  you into re-writing.
- When re-titling a post, update BOTH: `POST /posts/{id} {"title": ...}`
  (H1 + JSON-LD headline live in content) AND rank_math_title (the `<title>`
  tag). They drift otherwise.
