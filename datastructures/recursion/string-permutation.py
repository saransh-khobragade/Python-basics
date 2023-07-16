def permute(s):
    out = []
    if len(s) == 1:
        return [s]
    else:
        for i,v in enumerate(s):
            for x in permute(s[:i]+s[i+1:]):
                out+=[v+x]
    return out
print((permute('abc')))
