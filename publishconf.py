#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://ujuc.github.io"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
FEED_ALL_RSS = "feeds/rss.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = True
GOOGLE_ANALYTICS = "UA-58634276-1"
GOOGLE_ADSENSE = "ca-pub-1014314833699403"
