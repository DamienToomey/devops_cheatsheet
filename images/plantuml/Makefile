all:
	find . -type f -name "*.pu" -exec sh -c 'plantuml -tsvg {}' sh {} \; # generate svg from plantuml
	#find . -type f -name "*.svg" -exec sh -c 'rsvg-convert -f pdf -o "$${1%.*}.pdf" "$$1"' sh {} \; # convert svg to pdf



