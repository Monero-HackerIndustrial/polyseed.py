from polyseed.wordlists import wordlists
import unittest


class wordlistTest(unittest.TestCase):
    def test_loadList(self):
        words = wordlists()
        #returns the wordlists as a list
        # words.wordlist
        # self.assertEqual(type(words.wordlist), "list")
        self.assertIsInstance(words.wordlist, list)
        self.assertEqual(len(words.wordlist), 2048)
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')





if __name__ == '__main__':
    unittest.main()