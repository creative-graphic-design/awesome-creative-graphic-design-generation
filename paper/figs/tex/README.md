# Figure sources

`overview.tex`, `edit_protocol.tex`, and `research_map.tex` are self-contained standalone TikZ figures. Their manuscript float wrappers (`*_figure.tex`) store captions and labels, and include the generated PDFs in `../pdf/`. Run `make figures` to render all three vector PDFs.

The research map's 67 labels are linked to their cited bibliography entries in `research_map_sources.csv`. `paper/scripts/check_manuscript.py` checks this correspondence and each citation year. See `paper/RESEARCH_MAP_AUDIT.md` for selection, known preprint-versus-venue year differences, and limits of evidence.

`research_map_narrative.tex` is a second standalone, original, **26-study illustrated map** with task lanes, technique-colored borders and conceptual output sketches. Its exact nodes and citation years are checked against `research_map_narrative_sources.csv` by `check_manuscript.py`. The 67-node `research_map.tex` remains the complete, separately generated atlas; the narrative diagram does not replace the original audited crosswalk. Small institutional labels are source-grounded **text, not official logos**.
