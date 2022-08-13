---
title: Display interactive plotly chart (.html file) on GitHub Pages
layout: post
post-image:  ../assets/images/heroku.png
description: 
tags: github plotly
category: github
permalink: "/blog/:title"
---


###### Source : [`stack overflow`](https://stackoverflow.com/questions/60513164/display-interactive-plotly-chart-html-file-on-github-pages)



## 1. Generate figure.html in _includes folder

<script src="https://gist.github.com/UC1973/7667a9c00b6f6f2e4edbd0b48e07eff9.js"></script>

## 2. Include html file in a markdown file

{% include figure.html %}