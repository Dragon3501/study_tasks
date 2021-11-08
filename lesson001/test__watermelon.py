from watermelon import watermelon
import pytest 




@pytest.mark.parametrize(
    "weight, etalon_answer",
    [
        pytest.param(6,"YES"),
        pytest.param(93,"NO"),
        pytest.param(2,"NO"),
        pytest.param(1,"NO"),
        pytest.param(44,"YES"),
        pytest.param(87,"NO"),
        pytest.param(96,"YES"),
    ]
)
def test_watermelon(weight, etalon_answer):
    assert watermelon(weight) == etalon_answer
    
