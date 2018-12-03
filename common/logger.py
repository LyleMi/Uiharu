#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

formatStr = '[%(asctime)s] [%(levelname)s] %(message)s'
formatter = logging.Formatter(formatStr)

logger = logging.getLogger("uiharu")
ch = logging.StreamHandler()
chformatter = logging.Formatter(formatStr)
ch.setLevel(logging.DEBUG)
ch.setFormatter(chformatter)
logger.addHandler(ch)
