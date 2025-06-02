def longest_palindrome_substring(s):
    result = ""
    resLen = 0
    for i in range(len(s)):
        # for odd length
        l, r = i, i
        while l>=0 and r<len(s) and (s[l] == s[r]):
            if resLen < r-l+1:
                result = s[l:r+1]
                resLen = r-l+1
                
            l -= 1
            r += 1
        
        # for even length
        l, r = i, i+1
        while l>=0 and r<len(s) and (s[l] == s[r]):
            if resLen < r-l+1:
                result = s[l:r+1]
                resLen = r-l+1
                
            l -= 1
            r += 1
    return result

print(longest_palindrome_substring("abcabbacd"))