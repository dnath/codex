def anagram_sig(word):
    return ''.join(sorted(word))

def get_anagram_groups(words):
    anagram_dict = {}
    for word in words:
        word_sig = anagram_sig(word)
        if word_sig in anagram_dict:
            anagram_dict[word_sig].append(word)
        else:
            anagram_dict[word_sig] = [word]

    return anagram_dict.values()

print get_anagram_groups(['aba', 'aab', 'aa', 'a', 'Aa', 'bab', 'baa', 'aab'])