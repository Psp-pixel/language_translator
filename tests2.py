import unittest

from translator2 import english_to_german

class test_translator(unittest.TestCase):
    def english_to_german(self):
        self.assertEqual(english_to_german(text = 'Hi, How are you?'), "Wei geht's?")
        self.assertEqual(english_to_german(text = '00000'), "Wei geht's?")
        self.assertEqual(english_to_german(text = 'Hello'), "Hallo")

if __name__ == '__main__':
    unittest.main()
