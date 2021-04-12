import unittest

from translator import english_to_french

class test_translator(unittest.TestCase):
    def english_to_french(self):
        self.assertEqual(english_to_french(text = 'Hi, What made you laugh today?'), "Salut, qu'est-ce qui t'a fait rire aujurd'hui?")
        self.assertEqual(english_to_french(text = '00000'), "Qu'est-ce qui t'a fait rire aujurd'hui?")
        self.assertEqual(english_to_french(text = 'Hello'), "Bonjour")

if __name__ == '__main__':
    unittest.main()
