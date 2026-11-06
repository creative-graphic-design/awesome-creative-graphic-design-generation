# The default acro occurrence-page index and CVPR backrefs require
# more than latexmk's default five LaTeX/BibTeX convergence passes.
# Keep a finite cap; never silently accept a non-convergent manuscript.
$max_repeat = 8;
