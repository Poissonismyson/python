def getRettangolo(b,h):
    if b <= 0 or h <= 0:
        return ''
    else:
        return b*'+' + '\n' + getRettangolo(b,h-1).rstrip()


