import pytest


# тест на определение первого элемента кортежа
@pytest.mark.parametrize("tpl, expected_res", [(("some_string", 0, set()), "some_string"),
                                               ((), IndexError)])
def test_return_first_element(tpl, expected_res):
    try:
        assert tpl[0] == expected_res
    except expected_res:
        print("Probably length of the tuple is 0")


# тест на подсчет количества элементов
@pytest.mark.parametrize("tpl, expected_res", [((1.5, -3, [], (), {}, "some_string"), 6),
                                               ((), 0)])
def test_count_elements(tpl, expected_res):
    assert len(tpl) == expected_res


# тест на добавление элемента с помощью метода append
@pytest.mark.parametrize("tpl", [()])
def test_append_element(tpl):
    try:
        assert tpl.append()
    except AttributeError:
        print("Method '.append()' is not acceptable for type tuple")
