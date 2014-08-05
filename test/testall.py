#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import coverage
    coverage.process_startup()
except ImportError:
    pass

import unittest
import sys, os, glob

test_root = os.path.dirname(os.path.abspath(__file__))
test_files = glob.glob(os.path.join(test_root, 'test_*.py'))

os.chdir(test_root)
sys.path.insert(0, os.path.dirname(test_root))
sys.path.insert(0, test_root)
test_names = [os.path.basename(name)[:-3] for name in test_files]
suite = unittest.defaultTestLoader.loadTestsFromNames(test_names)

def run():
    pass

if __name__ == '__main__':
    run()

