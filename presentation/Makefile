serve:
	ipython nbconvert human_control_param_id.ipynb --to slides --template slides_reveal.tpl --post serve
build:
	ipython nbconvert human_control_param_id.ipynb --to slides --template slides_reveal.tpl
fix-pdf:
	pdftk A="human_control_param_id slides.pdf" B=fixed-page.pdf cat A1-18 B1 A20 output tmp.pdf
	mv tmp.pdf "human_control_param_id slides.pdf"
