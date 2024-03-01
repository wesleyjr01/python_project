from bi_package.main import replace_commas_by_dots


def test_dummy_one():
    assert replace_commas_by_dots("1,000") == "1.000"
