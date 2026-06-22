class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        elif numRows == 2:
            r1 = []
            r2 = []
            for i in range(0, len(s), 2):
                if i + 1 == len(s):
                    r1.append(s[i])
                else:
                    r1.append(s[i])
                    r2.append(s[i + 1])
            r1.extend(r2)
            return ''.join(r1)

        dist = 2 * (numRows - 1)

        all_rows = {i: [] for i in range(numRows)}

        for i in range(0, len(s), dist):
            all_rows[0].append(s[i])
            if (i + (dist // 2)) < len(s):
                all_rows[numRows - 1].append(s[i + (dist // 2)])
            for j in range(1, numRows - 1):
                if i + j < len(s):
                    all_rows[j].append(s[i + j])
                if i + dist - j < len(s):
                    all_rows[j].append(s[i + dist - j])

        result = []

        for k in range(len(all_rows)):
            result.extend(all_rows[k])

        return ''.join(result)


            
                