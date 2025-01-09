import static org.junit.jupiter.api.Assertions.*;

class CountingWordsWithAGivenPrefixTest {

    private final CountingWordsWithAGivenPrefix solution = new CountingWordsWithAGivenPrefix();

    @org.junit.jupiter.api.Test
    void prefixCountWithValidInput() {
        String[] words = {"pay","attention","practice","attend"};
        String prefix = "at";
        int expected = 2;

        assertEquals(expected, solution.prefixCount(words, prefix));
    }
}