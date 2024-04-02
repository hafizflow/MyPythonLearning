haystack = "butsad"
needle = "sad"

if needle in haystack:
    ind = haystack.index(needle)
    print(ind)
else:
    print(-1)
