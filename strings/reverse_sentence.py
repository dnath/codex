def reverse_word(word, start, length):
    for i in xrange(0, length/2):
        tmp = word[start + i]
        word[start + i] = word[start + length - 1 - i]
        word[start + length - 1 - i] = tmp

def reverse_sentence(sentence):
    sentence = list(sentence)
    start = 0
    for i in xrange(len(sentence)):
        if sentence[i] == ' ':
            reverse_word(sentence, start, i-start)
            start = i+1

    reverse_word(sentence, start, len(sentence)-start)
    reverse_word(sentence, 0, len(sentence))
    return ''.join(sentence)


print reverse_sentence('I wish you a merry Christmas')
