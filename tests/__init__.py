import unittest

class InitializationTests(unittest.TestCase):
    def test_initialization(self):
        """
        Check the test suite runs
        """
        self.assertEqual(2+2, 4)

    def test_import(self):
        """
        Ensure test suite can import module
        """
        try:
            import eyeoveryou
        except ImportError:
            self.fail("Could not import eyeoveryou")