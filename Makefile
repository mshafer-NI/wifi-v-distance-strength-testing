REPORTS := \
   docs/charts.html \
   docs/notebook.html \

all: $(REPORTS) docs/index.html


docs:
	mkdir -p docs

docs/index.html: docs
	python tools/markdown_to_html.py README.md -o docs/index.html

$(REPORTS): docs/%.html: export_%.sh | docs
	sh $<

clean:
	rm -rf docs
