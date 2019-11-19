import re


# validates the action input must be 0 or 1 or 2
def valid_action_input(action):
    try:
        action = int(action)
    except ValueError:
        return False
    if action in range(0, 3):
        return True
    return False


# validates path by using regular expression
def valid_path(path):
    try:
        assert isinstance(path, str)
        if re.match(r"^root\/(?:[^\"\']*)", path):
            return True
        else:
            return False
    except ValueError:
        return False
