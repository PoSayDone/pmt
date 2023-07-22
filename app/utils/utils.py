def add_slash_if_needed(s):
    if s == "":
        return ""
    elif s[-1] != '/':
        s += '/'
    return s
