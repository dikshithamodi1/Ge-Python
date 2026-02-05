import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import pytest
from student_reg_toolkit import validators
from student_reg_toolkit import streaming


@pytest.mark.parametrize("email, expected", [
    ("valid@univ.edu", True),
    ("another@college.edu", True),
    ("invalid@gmail.com", False),
    ("noatsign.edu", False),
    ("missingdomain@.edu", False),
    ("student@univ.org", False),
    ("", False),
    ("a@b.edu", True),
])
def test_validate_university_email(email, expected):
    assert validators.validate_university_email(email) == expected


@pytest.mark.parametrize("student_id, expected", [
    ("123456789", True),
    ("000000000", True),
    ("999999999", True),
    ("12345678", False),
    ("1234567890", False),
    ("abc123456", False),
    ("", False),
    (" 123456789", False),
])
def test_validate_student_id(student_id, expected):
    assert validators.validate_student_id(student_id) == expected


@pytest.mark.parametrize("password, expected", [
    ("StrongPass1", True),
    ("AnotherPass2024!", True),
    ("weakpass", False),
    ("NOPASSWORD", False),
    ("password123", False),
    ("P1", False),
    ("Passwd", False),
    ("PASS123", False),
    ("P@ssw0rd!", True),
])
def test_validate_password(password, expected):
    assert validators.validate_password(password) == expected


def test_batch_generator_basic():
    records = [f"item{i}" for i in range(10)]
    batches = list(streaming.batch_generator(records, batch_size=3))
    assert len(batches) == 4
    assert batches[0] == ["item0", "item1", "item2"]
    assert batches[1] == ["item3", "item4", "item5"]
    assert batches[2] == ["item6", "item7", "item8"]
    assert batches[3] == ["item9"]


def test_batch_generator_empty_list():
    records = []
    batches = list(streaming.batch_generator(records, batch_size=5))
    assert len(batches) == 0


def test_batch_generator_single_batch():
    records = [f"item{i}" for i in range(3)]
    batches = list(streaming.batch_generator(records, batch_size=5))
    assert len(batches) == 1
    assert batches[0] == ["item0", "item1", "item2"]


def test_batch_generator_invalid_batch_size():
    records = [f"item{i}" for i in range(5)]
    with pytest.raises(ValueError, match="Batch size must be a positive integer."):
        list(streaming.batch_generator(records, batch_size=0))
    with pytest.raises(ValueError, match="Batch size must be a positive integer."):
        list(streaming.batch_generator(records, batch_size=-1))


def test_batch_generator_non_list_records():
    with pytest.raises(TypeError, match="Records must be a list."):
        list(streaming.batch_generator("not a list", batch_size=5))
