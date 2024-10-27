Title: Lessons Learned Setting up Pelican
Date: 2024-10-27 10:15
Category: Lessons-Learned

Pelican is a python website build & template library. Using it is fairly simple as all dependencies
are python libraries, so no complex environment management is necessary.

![Lessons-Learned-Setting-Up-Pelican-screenshot.png]({filename}/images/Lessons-Learned-Setting-Up-Pelican-screenshot.png)


A configuration file, `pelicanconf.py`, is used to specify details of site generation. Of particular interest to us
are the configuration variables `THEME_TEMPLATES_OVERRIDES` and `STATIC_PATHS`. This repository
used both to define a folder of override themes, particularly we override `base.html` to include
additional styles under `static/our-style.css` and remove templated footer content.

Detailed documentation is available at [https://docs.getpelican.com](https://docs.getpelican.com/en/latest/settings.html).


