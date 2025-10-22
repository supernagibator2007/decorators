from .constants import ADMIN_USERNAME, UNKNOWN_COMMAND


def control_access(func):
    def wrapper(class_object):
        if class_object.username == ADMIN_USERNAME:
            result = func(class_object)
            return result
        else:
            print(UNKNOWN_COMMAND)
    return wrapper
