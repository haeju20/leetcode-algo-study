# baekjoon 4659
# 비밀번호 발음하기

# wrong answer
vowel = ['a', 'e', 'i', 'o', 'u']


# check 1st condition
def check1(word):
    # if the word includes at least one vowel
    for i in word:
        if i in vowel:
            return True
    return False


# check 2nd condition
def check2(word):
    # if there are continuous 3 vowels or consonants in the word
    for i in range(len(word)-2):
        cnt = 0
        for j in word[i:i+3]:
            if j in vowel:
                cnt += 1
        if cnt == 0 or cnt == 3:
            return False
    return True


# check 3rd condition
def check3(word):
    # if there are continuous same alphabets except for ee and oo
    for i in range(1, len(word)):
        if word[i] == word[i - 1] and word[i] != ('e' or 'o'):
            return False
    return True

while True:
    word = input()

    if word == "end":
        break

    if check1(word) and check2(word) and check3(word):
        print("<" + word + ">" + " is acceptable.")
    else:
        print("<" + word + ">" + " is not acceptable.")
