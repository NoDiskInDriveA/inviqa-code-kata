from hamcrest import assert_that, calling, equal_to, raises
from example.example import do_nothing


def test_do_nothing_raises_value_error():
    assert_that(calling(do_nothing).with_args(dict()), raises(ValueError))


def test_binary_search_returns_negative_if_item_not_present():
    input = {
        1: ['A', 'B'],
        2: ['C']
    }
    assert_that(do_nothing(input), equal_to(42))
