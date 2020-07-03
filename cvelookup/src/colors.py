class Color:
    """
    r = red, g = green
    y = yellow, b = blue
    m = magenta, c = cyan
    w = white, re = reset
    """
    r, g = "\u001b[31;1m", "\u001b[32;1m"
    y, b = "\u001b[33;1m", "\u001b[34;1m"
    m, c = "\u001b[35;1m", "\u001b[36;1m"
    w, re = "\u001b[37;1m", "\u001b[0m"