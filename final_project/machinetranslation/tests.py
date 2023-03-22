import unittest
from translator import englishToFrench, frenchToEnglish

class TestenglishtoFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench(""), "Try a different phrase.")
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class TestfrenchtoEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish(''), 'Try a different phrase.')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')        

unittest.main()