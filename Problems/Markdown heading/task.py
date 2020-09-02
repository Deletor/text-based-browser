def heading(name, level=1):
    hash = "#"
    if level <= 1:
        r = hash + " " + name
        return r
    elif level >= 2 and level <= 6:
        r = hash * level + " " + name
        return r
    elif level > 6:
        r = hash * 6 + " " + name
        return r
