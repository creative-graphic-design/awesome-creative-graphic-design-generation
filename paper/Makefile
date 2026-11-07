.PHONY: check figures pdf clean
check:
	python3 scripts/check_sentence_lines.py
	python3 -m unittest discover -s scripts/tests -p 'test_*.py'
	python3 scripts/check_manuscript.py
	python3 scripts/check_bibliography.py
figures: check
	sh scripts/build_figures.sh
pdf: figures
	latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode main.tex
clean:
	latexmk -C main.tex
	rm -f figs/pdf/overview.pdf figs/pdf/edit_protocol.pdf
