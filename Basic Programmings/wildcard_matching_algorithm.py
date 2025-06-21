import re

def wildcard_match(string, pattern):
    pattern = pattern.replace('*', '.*').replace('?', '.')
    print(pattern)
    return re.fullmatch(pattern, string)

print(wildcard_match('aa1aabbc', 'a*b?c'))
