# Implement basic compression like 'aaabbbcc' → 'a3b3c2'

from itertools import groupby

# def compress_string(string):
#     return "".join(f"{k}{len(list(g))}" for k, g in groupby(string))

def compress_string(string):
    result, count = "", 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            result += f"{string[i-1]}{count}"
            count = 1
    result += f"{string[-1]}{count}"
    return result

print(compress_string("aaabbbcc"))  # a3b3c2
print(compress_string("aabbcccaaa"))  # a2b2c3a3
