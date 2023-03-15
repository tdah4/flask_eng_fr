import unittest
from translator import english_to_french, french_to_english

class TestenglishtoFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(""), "Try a different phrase.")
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestfrenchtoEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(''), 'Try a different phrase.')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')        

unittest.main()