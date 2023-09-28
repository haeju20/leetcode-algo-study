class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        cnt = []

        # list comprehension
        words = [words for words in re.sub(r'[^a-z]', ' ', paragraph.lower()).split()
        if words not in banned]

        for i in range(len(words)):
            cnt.append(words.count(words[i]))
            idx = cnt.index(max(cnt))

        return words[idx]

# class Solution2: # defaultdict 활용
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         cnt = collections.defaultdict(int)
#         words = [words for words in re.sub(r'[^a-z]', ' ', paragraph.lower()).split()
#         if words not in banned]
#         for i in words:
#             cnt[i] += 1
#         return max(cnt, key = cnt.get)

# class Solution3: # Counter 활용
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         words = [words for words in re.sub(r'[^a-z]', ' ', paragraph.lower()).split()
#         if words not in banned]
#         cnt = collections.Counter(words)
#         return cnt.most_common(1)[0][0]
