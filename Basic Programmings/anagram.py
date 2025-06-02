def anagram(first_str, sec_str):
    return sorted(first_str)==sorted(sec_str)

print(anagram("cba", "absc"))