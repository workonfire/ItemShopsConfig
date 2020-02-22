def color_text(color, format, text):
    colors = {'black': 0, 'red': 1, 'green': 2, 'yellow': 3, 'blue': 4, 'purple': 5, 'cyan': 6, 'white': 7}
    if format == 'back':
        format = "\033[4"
    elif format == 'underline':
        format =  "\033[4;3"
    elif format == 'bright':
        format =  "\033[0;9"
    else:
        format = "\033[0;3"
    return format + str(colors[color]) + 'm' + text + "\033[00m"