import unittest
from http_load_tester.metrics import Metrics
from http_load_tester.core import load_test

class TestLoadTester(unittest.TestCase):
    # A unit test case for testing the load_test function
    def test_load_test(self):
        url = 'https://httpbin.org/get'
        qps = 10
        duration = 5

        # Calling the load_test function with the defined parameters
        load_test(url, qps, duration)

if __name__ == '__main__':
    unittest.main()