
def strtobool (val):
    val = val.lower()
    if val in ('true'):
        return True
    elif val in ('false'):
        return False
    else:
        raise ValueError("invalid truth value %r" % (val,))