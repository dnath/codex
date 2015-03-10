class WordDictionary(object):
    WORDS = set(['abc', 'cba', 'cab', 'ba', 'a', 'ab'])
    @staticmethod
    def is_valid(word):
        return word in WordDictionary.WORDS

def gen_anagrams(word):
    anagrams = []
    __gen_anagrams(list(word), 0, anagrams)
    return anagrams

def __gen_anagrams(char_array, n, anagrams):
    if n == len(char_array):
        word = ''.join(char_array)
        if WordDictionary.is_valid(word):
            anagrams.append(word)
    else:
        for i in xrange(n, len(char_array)):
            char_array[i], char_array[n] = char_array[n], char_array[i]
            __gen_anagrams(char_array, n+1, anagrams)
            char_array[i], char_array[n] = char_array[n], char_array[i]


print gen_anagrams('abc')
print gen_anagrams('ab')