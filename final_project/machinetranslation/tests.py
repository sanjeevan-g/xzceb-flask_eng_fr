import unittest

# from translator import english_to_french, french_to_english
from translator import english_to_french, french_to_english

# English to French Test
class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        # test when 'Hello' is given as input the output is "Bonjour". 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') 
        # test when 'Hello' is given as input the output is not "Hello".
        self.assertNotEqual(english_to_french('Hello'), 'Hello') 
        # test when null is given as input the output is null.
        self.assertEqual(english_to_french(None), None) 

#French to English Test     
class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        # test when 'Bonjour' is given as input the output is "Hello".
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        # test when 'Bonjour' is given as input the output is not "Bonjour". 
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour') 
        # test when null is given as input the output is null.
        self.assertEqual(french_to_english(None), None) 

unittest.main()