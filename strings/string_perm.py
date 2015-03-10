def permute(word):
    __permute(list(word), 0)

def __permute(word, n):
    if n == len(word):
        print ''.join(word)
        return

    for i in xrange(n, len(word)):
        word[n], word[i] = word[i], word[n]
        __permute(word, n+1)
        word[n], word[i] = word[i], word[n]

permute('abc')