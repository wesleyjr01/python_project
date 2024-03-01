from bi_package.main import replace_commas_by_dots
from bi_package.dags.main import composite_function


def test_dummy_one():
    assert replace_commas_by_dots("1,000") == "1.000"


def test_composite_function():
    assert composite_function() == 5
