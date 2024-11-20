"""
This script discovers and runs all unit tests in the specified directory, 
then generates XML reports for each test case. The results are saved in the 
'./test-reports' directory with a unique filename based on the test case and timestamp.
"""

import os
import time
import unittest
import xmlrunner

if __name__ == '__main__':
    # Directory where the tests are located
    TEST_DIR = '/eda/processor-ci-communication/tests'

    # Discover all test files within the directory
    test_suites = unittest.defaultTestLoader.discover(TEST_DIR, pattern='*.py')

    # Create the test reports directory if it does not exist
    os.makedirs('test-reports', exist_ok=True)

    # Iterate over each test suite
    for test_suite in test_suites:
        # For each suite of tests, iterate over the test cases
        for test_case in test_suite:
            # Generate a unique file name based on the test case name and timestamp
            test_case_name = test_case.__class__.__name__
            TIMESTAMP = str(int(time.time()))
            REPORT_FILE = f'test-reports/results_{test_case_name}_{TIMESTAMP}.xml'

            # Run the tests and save the results in separate files
            with open(REPORT_FILE, 'w', encoding='utf-8') as output:
                xmlrunner.XMLTestRunner(output=output).run(test_case)
