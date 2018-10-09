import unittest
import capitalize


class TextPractice(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = capitalize.cap(text)
        self.assertEqual(result, "Python")

    def test_multiple_word(self):
        text = 'monty python'
        result = capitalize.cap(text)
        self.assertEqual(result, "Monty python")

    def test_upper(self):
        text = "python"
        result = capitalize.upper(text)
        self.assertEqual(result, "PYTHON")

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
