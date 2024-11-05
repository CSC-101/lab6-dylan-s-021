import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books_1(self):
        input = [data.Book(["Suzanne Collins"], "The Hunger Games"),
                         data.Book(["Lois Lowry"], "The Giver")]
        expected = [data.Book(["Lois Lowry"], "The Giver"),
                    data.Book(["Suzanne Collins"], "The Hunger Games")]
        lab6.selection_sort_books(input)
        self.assertEqual(expected, input)


    # Part 2
    def test_swap_case_1(self):
        string = "Hello"
        expected = "hELLO"
        actual = lab6.swap_case(string)
        self.assertEqual(expected, actual)

    def test_swap_case_2(self):
        string = "Hello & gOODBYE"
        expected = "hELLO & Goodbye"
        actual = lab6.swap_case(string)
        self.assertEqual(expected, actual)


    # Part 3
    def test_str_translate_1(self):
        string = "abcdcba"
        old = "a"
        new = "x"
        expected = "xbcdcbx"
        actual = lab6.str_translate(string, old, new)
        self.assertEqual(expected, actual)

    def test_str_translate_2(self):
        string = "test: string w/ characters?"
        old = "?"
        new = "!"
        expected = "test: string w/ characters!"
        actual = lab6.str_translate(string, old, new)
        self.assertEqual(expected, actual)


    # Part 4
    def test_histogram_1(self):
        string = "a string with some words"
        expected = {"a": 1, "string": 1, "with": 1, "some":1, "words":1}
        actual = lab6.histogram(string)
        self.assertEqual(expected, actual)

    def test_histogram_2(self):
        string = "a string with some words & some more words"
        expected = {"a": 1, "string": 1, "with": 1, "some":2, "words":2, "&":1, "more":1}
        actual = lab6.histogram(string)
        self.assertEqual(expected, actual)





if __name__ == '__main__':
    unittest.main()
