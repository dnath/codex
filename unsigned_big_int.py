import re


class UnsignedBigInt(object):
    WORD_SIZE = 9
    WORD_BASE = 1000000000

    def __init__(self, string=None):
        if string == None:
            self.__words = []
        else:
            self.__words = self.__parse(string)

    def __parse(self, string):
        string = string.strip().lstrip('0')
        if string == '':
            string = '0'

        if re.match('[0-9]*', string) == None:
            raise Exception('Invalid string "{0}", cannot be parsed into UnsignedBigInt!'.format(string))

        return [int(string[max(len(string) - pos - UnsignedBigInt.WORD_SIZE, 0): len(string) - pos]) \
                for pos in xrange(0, len(string), UnsignedBigInt.WORD_SIZE)]


    def __add__(self, other):
        result = UnsignedBigInt()
        carry = 0
        for i in xrange(max(len(self.__words), len(other.__words))):
            sum = carry
            if i < len(self.__words):
                sum += self.__words[i]
            if i < len(other.__words):
                sum += other.__words[i]

            carry, res_word = divmod(sum, UnsignedBigInt.WORD_BASE)
            result.__words.append(res_word)

        if carry > 0:
            result.__words.append(carry)

        return result

    def __sub__(self, other):
        result = UnsignedBigInt()
        carry = 0
        for i in xrange(max(len(self.__words), len(other.__words))):
            sum = carry
            if i < len(self.__words):
                sum += self.__words[i]
            if i < len(other.__words):
                sum -= other.__words[i]

            carry, res_word = divmod(sum, UnsignedBigInt.WORD_BASE)
            result.__words.append(res_word)

        if carry < 0:
            result.__words.append(carry % UnsignedBigInt.WORD_BASE)

        length = len(result.__words)
        for i in xrange(length):
            if result.__words[length - 1 - i] != 0:
                break
            elif i < length - 1:
                del result.__words[length - 1 - i]

        return result

    def __eq__(self, other):
        if len(self.__words) != len(other.__words):
            return False

        for i in xrange(len(self.__words)):
            if self.__words[i] != other.__words[i]:
                return False
        return True

    def __str__(self):
        if not hasattr(self, '__string'):
            self.__string = str(self.__words[-1]) + ''.join(reversed(map(lambda x: str(x).zfill(9), self.__words[:-1])))
        return self.__string

    # TODO: div, mod, cmp


x = ['99999999999999999999', '0', '999999999', '1111111111111111', '111111111111',    '111111111111111111111111']
y = ['11111111111111111111', '1', '100',       '9999999999999',    '999999999999999', '111111111111111111111111']
for i in xrange(len(x)):
    a, b = UnsignedBigInt(x[i]), UnsignedBigInt(y[i])
    print '{0} + {1} = {2} : {3}'.format(a, b, a+b, int(str(a+b)) == (int(x[i]) + int(y[i])))
    print '{0} - {1} = {2} : {3}'.format(a, b, a-b, int(str(a-b)) == (int(x[i]) - int(y[i])))

print (UnsignedBigInt('11111111111') == UnsignedBigInt('11111111111'))
print (UnsignedBigInt('11111111111') == UnsignedBigInt('11111111110'))