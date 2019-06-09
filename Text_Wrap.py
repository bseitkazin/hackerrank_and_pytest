def wrap(string, max_width):
    s = str()
    for i in range(0, len(string), max_width):
        s += string[i:(min([len(string), i + max_width]))]
        s += '\n'
    return s

