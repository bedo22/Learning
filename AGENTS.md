# AGENTS.md — Learning ("Learn to Learn") shelf

Lessons + docs shelf: `lessons/NNNN-*.html` series + `reference/*.html` topic
docs (EN + `ar/` twins) + `reference/sources/` research digests.
shelf-pipeline 1.2.18 installed; transcript lane DORMANT — the 8 dumps in
`Trascriptions/` are raw YouTube text WITHOUT timestamps, so minute cites are
impossible until re-fetched with markers. Full `check` exits 2 (zero-corpus
refusal) until then — that is the gate working, not a bug.

**Hard rules:**

1. `reference/sources/` is the durable research cache (fetch → digest → doc).
   `.tmp/` = true scratch only.
2. `reference/CONVENTIONS.md` governs the doc shelf; this file governs the
   pipeline layer.
3. AR twins: EN canonical, twin sync gated on verification.
4. Verify before trusting: `python3 tools/shelf.py selftest` (26/26) →
   `doctor` → per-doc `check reference/<doc>.html` (doc lane runs today).
5. Re-fetch transcripts with `[MM:SS]` markers before enabling the transcript
   lane; then scaffold notes with `python3 tools/shelf.py scaffold NNNN`.

Version: `python3 tools/shelf.py --version` (1.2.18)
