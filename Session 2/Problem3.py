def check_anagram(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if sorted(s1) == sorted(s2):
        return True
    return False

str1 = input("Enter First String: ")
str2 = input("Enter Second String: ")

if check_anagram(str1,str2):
    print(f"{str1} and {str2} are anagrams")
else:
    print(f"{str1} and {str2} are NOT anagrams")