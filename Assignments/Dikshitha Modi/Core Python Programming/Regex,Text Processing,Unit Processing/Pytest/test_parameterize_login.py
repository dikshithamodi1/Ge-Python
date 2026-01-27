import pytest
from parametreize_login_validation import login_validation
@pytest.mark.parametrize(
    "email,expected",
    [
         ("user@test.com",True),
         ("bad.email", False),
    ]
)
def test_login_validation(email,expected):
    assert login_validation(email)==expected