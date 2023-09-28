class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let, dig = [], []
        for i in logs:
            s = i.split()[1]
            if s.isdigit():
                dig.append(i) # 이미 입력순으로 정렬
            else:
                let.append(i)

        # 알파벳순으로 정렬해야 한다
        let.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return let + dig
