import pytest

from shipday.exeptions.shipday_exeption import ShipdayException
from shipday.utils.verifiers import verify_instance_of, verify_none_or_instance_of, \
    verify_not_negative, verify_none_or_not_negative


class TestVerifiers:
    @pytest.mark.parametrize('object_type, instance, success', [
        *[(int, value, True) for value in (-1, 0, 1)],
        *[(int, value, False) for value in (0.0, 'abc', [1], {1: 1})],
        *[(float, value, True) for value in (-1.0, 0.0, 1.5, 2.1)],
        *[(float, value, False) for value in (1, -1, 0, 'abc', [1], {1: 1})],
        *[(str, value, True) for value in ('', "", '''x''', 'abcd')],
        *[(str, value, False) for value in (0, 1, -1.0, 2.3, [1], {1: 1})],
        *[(list, value, True) for value in (list(), [], [1, 2, 3], ['abcd', {}, 1])],
        *[(list, value, False) for value in (0, 1, -1.0, 2.3, 'abcd', {1: 1})],
        *[(dict, value, True) for value in ({}, {'a': 'a'}, {'value': [1, 2, 3]})],
        *[(dict, value, False) for value in (0, 1, -1.0, 2.3, 'a', [1], [])],
    ])
    def test_verify_instance_of(self, object_type, instance, success: bool):
        if success:
            verify_instance_of(object_type, instance, "Exception")
        else:
            with pytest.raises(ShipdayException):
                verify_instance_of(object_type, instance, "Exception")

    @pytest.mark.parametrize('object_type, instance, success', [
        *[(object_type, None, True) for object_type in (int, float, str, list, dict, ShipdayException)],
        *[(int, value, True) for value in (-1, 0, 1)],
        *[(int, value, False) for value in (0.0, 'abc', [1], {1: 1})],
        *[(float, value, True) for value in (-1.0, 0.0, 1.5, 2.1)],
        *[(float, value, False) for value in (1, -1, 0, 'abc', [1], {1: 1})],
        *[(str, value, True) for value in ('', "", '''x''', 'abcd')],
        *[(str, value, False) for value in (0, 1, -1.0, 2.3, [1], {1: 1})],
        *[(list, value, True) for value in (list(), [], [1, 2, 3], ['abcd', {}, 1])],
        *[(list, value, False) for value in (0, 1, -1.0, 2.3, 'abcd', {1: 1})],
        *[(dict, value, True) for value in ({}, {'a': 'a'}, {'value': [1, 2, 3]})],
        *[(dict, value, False) for value in (0, 1, -1.0, 2.3, 'a', [1], [])],
    ])
    def test_verify_none_or_instance_of(self, object_type, instance, success: bool):
        if success:
            verify_none_or_instance_of(object_type, instance, "Exception")
        else:
            with pytest.raises(ShipdayException):
                verify_none_or_instance_of(object_type, instance, "Exception")

    @pytest.mark.parametrize('value, success', [
        (1, True),
        (0, True),
        (1.5, True),
        (0.0, True),
        (-0, True),
        (1000, True),
        (-1, False),
        (-10.3, False)
    ])
    def test_verify_not_negative(self, value, success: bool):
        if success:
            verify_not_negative(value, "Exception")
        else:
            with pytest.raises(ShipdayException):
                verify_not_negative(value, "Exception")

    @pytest.mark.parametrize('value, success', [
        (None, True),
        (1, True),
        (0, True),
        (1.5, True),
        (0.0, True),
        (-0, True),
        (1000, True),
        (-1, False),
        (-10.3, False)
    ])
    def test_verify_none_or_not_negative(self, value, success: bool):
        if success:
            verify_none_or_not_negative(value, "Exception")
        else:
            with pytest.raises(ShipdayException):
                verify_none_or_not_negative(value, "Exception")
