#!/bin/bash
set -x
jupyter execute visualizations/graph.ipynb
mv visualizations/report.html docs/charts.html
