import pytest
from zero_division import divide
def test_divide():
    with pytest.raises(ValueError):
        divide(10,0)