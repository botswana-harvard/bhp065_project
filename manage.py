#!/usr/bin/env python
import os
import sys
from unipath import Path

SOURCE_ROOT = Path(os.path.dirname(os.path.realpath(__file__))).ancestor(1)
EDC_DIR = SOURCE_ROOT.child('edc_project')
LIS_DIR = SOURCE_ROOT.child('lis_project')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bhp065.config.settings")
    sys.path.insert(0, EDC_DIR)
    sys.path.insert(0, LIS_DIR)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
