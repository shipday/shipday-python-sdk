from shipday.exeptions import ShipdayException


def verify_none_or_instance_of(obj_type, variable, error_message):
    if type(obj_type) is not list:
        obj_type = [obj_type]
    if variable is None:
        return
    if type(variable) not in obj_type:
        raise ShipdayException(error_message)


def verify_instance_of(obj_type, variable, error_message):
    if type(obj_type) is not list:
        obj_type = [obj_type]
    if type(variable) not in obj_type:
        raise ShipdayException(error_message)


def verify_not_negative(number, error_message):
    verify_instance_of([int, float], number, error_message)
    if number < 0:
        raise ShipdayException(error_message)


def verify_none_or_not_negative(number, error_message):
    verify_none_or_instance_of([int, float], number, error_message)

    if number is not None and number < 0:
        raise ShipdayException(error_message)
