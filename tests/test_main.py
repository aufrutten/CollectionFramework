from main import counting_unique_characters
import pytest


def test_counting_unique_characters():
    assert counting_unique_characters('abbbccdf') == 3
    assert counting_unique_characters('aabcdfee') == 4

    with pytest.raises(TypeError):
        counting_unique_characters(123)




