import pytest


# тест на сложение двух целых чисел
@pytest.mark.parametrize("x, y, expected_res", [(1, 3, 4),
                                                (1, 0, 1),
                                                (-1, 1, 0),
                                                (-1, -3, -4)])
def test_sum_two_int(x, y, expected_res):
    assert x + y == expected_res


# тест на преобразование строки в целое число
@pytest.mark.parametrize("x, expected_res", [("0", 0),
                                             ("-1", -1),
                                             ("0257", 257),
                                             ("-000", 0),
                                             ("", ValueError),
                                             ("1.2", ValueError)])
def test_convert_str_to_int(x, expected_res):
    try:
        assert int(x) == expected_res
    except expected_res:
        print("This string cannot be converted to the int type")


# тест на обращение к последней цифре числа по индексу
@pytest.mark.parametrize("x", [-1002, 0, 1])
def test_call_last_number_via_index(x):
    try:
        assert x[-1]
    except TypeError:
        print("Indices are not acceptable for type int")
