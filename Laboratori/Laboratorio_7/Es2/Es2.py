def topDJ(djs):
    hscore = 0
    top = ''
    for i in djs:
        if djs[i] >= hscore:
            hscore = djs[i]
            top = i
    return top
