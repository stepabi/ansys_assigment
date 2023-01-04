import unittest
import sys
import os
import xmlrunner


loader = unittest.TestLoader()

def runtest():
    suite = unittest.TestSuite()
    test_cases = unittest.defaultTestLoader.discover('./tests/','*.py')
    for cases in test_cases:
        suite.addTests(cases)
    runner = xmlrunner.XMLTestRunner(output='reports')
    runner.run(suite)

if __name__=='__main__':
    runtest()