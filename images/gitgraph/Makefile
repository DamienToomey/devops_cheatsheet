all:
	find . -type f -name "*.html" -exec sh -c 'wkhtmltoimage "$$1" "$${1%.*}.svg"' sh {} \; # convert html to svg
	#find . -type f -name "*.svg" -exec sh -c 'rsvg-convert -f pdf -o "$${1%.*}.pdf" "$$1"' sh {} \; # convert svg to pdf

