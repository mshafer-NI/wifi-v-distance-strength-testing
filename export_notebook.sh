#!/bin/bash
set -x
jupyter nbconvert visualizations/graph.ipynb --execute --to html --output-dir docs
mv docs/graph.html docs/notebook.html