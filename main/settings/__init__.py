# -*- coding: utf-8 -*-

import os.path

try:
    from .local import *
except Exception as err:
    print(err)
    print("You are using the base settings file.")
    print("You are advised to create or check local.py file (based on local_sample.py) with your personal settings.")
    from .base import *
