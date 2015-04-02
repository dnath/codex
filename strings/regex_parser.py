def regex_match(regex, string):
    return __regex_match(regex, 0, string, 0)

def __regex_match(regex, r_idx, string, s_idx):
    if r_idx == len(regex) and s_idx == len(string):
        return True

    if r_idx >= len(regex) or s_idx >= len(string):
        return False

    r_char = regex[r_idx]
    s_char = string[s_idx]

    if r_char != '*' and (r_char == s_char or r_char == '.'):
        if r_idx < len(regex)-1:
            next_r_char = regex[r_idx + 1]
            if next_r_char == '*':
                return __regex_match(regex, r_idx, string, s_idx+1) or \
                       __regex_match(regex, r_idx+2, string, s_idx+1)

        return  __regex_match(regex, r_idx+1, string, s_idx+1)

    return False


print regex_match('ab', 'ab')
print regex_match('a.', 'ab')
print regex_match('.', '')
print regex_match('a.*', 'absbjkbskj')
print regex_match('ab*', 'abb')
print regex_match('ab*', 'aba')
print regex_match('aa*b', 'aaab')