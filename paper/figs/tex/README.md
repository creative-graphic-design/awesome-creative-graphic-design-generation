# Figure sources

`overview.tex`, `edit_protocol.tex`, and `research_map.tex` are self-contained standalone TikZ figures. Their manuscript float wrappers (`*_figure.tex`) store captions and labels, and include the generated PDFs in `../pdf/`. Run `make figures` to render all three vector PDFs.

The research map's 67 labels are linked to their cited bibliography entries in `research_map_sources.csv`. `paper/scripts/check_manuscript.py` checks this correspondence and each citation year. See `paper/RESEARCH_MAP_AUDIT.md` for selection, known preprint-versus-venue year differences, and limits of evidence.
