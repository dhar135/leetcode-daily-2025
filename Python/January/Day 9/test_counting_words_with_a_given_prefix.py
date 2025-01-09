from counting_words_with_a_given_prefix import CountingWordsWithAGivenPrefix

class TestCountingWordsWithAGivenPrefix:

    def setup_method(self):
        self.solution = CountingWordsWithAGivenPrefix()


    def test_valid_list_of_words_with_prefix(self):
        words = ["pay","attention","practice","attend"]
        prefix = "at"
        expected = 2
        assert self.solution.count_words_with_a_given_prefix(words, prefix) == expected

    def test_invalid_list_of_words_with_prefix(self):
        words = ["leetcode", "win", "loops", "success"]
        prefix = "code"
        expected = 0
        assert self.solution.count_words_with_a_given_prefix(words, prefix) == expected





