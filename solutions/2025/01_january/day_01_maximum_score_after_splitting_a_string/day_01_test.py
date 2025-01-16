import logging
from day_01_solution import Solution

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_max_score():
    solution = Solution()

    test_cases = [
        ("011101", 5),
        ("00111", 5),
        ("1111", 3),
        ("00", 1)
    ]

    for s, expected in test_cases:
        logger.info(f"Testing string: {s}, Expected score: {expected}")
        result = solution.maxScore(s)
        assert result == expected
        logger.info(f"Test passed: {s} -> {result}")