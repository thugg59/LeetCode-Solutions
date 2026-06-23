class Solution:
    def myAtoi(self, s: str) -> int:

        positive = True
        digits = []

        for i in range(len(s)):
            if s[i].isdigit():
                if i + 1 >= len(s) or not s[i + 1].isdigit():
                    digits.append(s[i])
                    solution = int(''.join(digits))
                    if positive:
                        if solution > 2147483647:
                            return 2147483647
                        else:
                            return solution
                    else:
                        if -solution < -2147483648:
                            return -2147483648
                        else:
                            return -solution
                else:
                    if s[i] == 0:
                        continue
                    else:
                        while i < len(s) and s[i].isdigit():
                            digits.append(s[i])
                            i += 1
                        solution = int(''.join(digits))
                        if positive:
                            if solution > 2147483647:
                                return 2147483647
                            else:
                                return solution
                        else:
                            if -solution < -2147483648:
                                return -2147483648
                            else:
                                return -solution
            elif s[i] == ' ':
                continue
            elif s[i] == '-' or s[i] == '+':
                if i + 1 >= len(s) or not s[i + 1].isdigit():
                    return 0
                if s[i] == '-':
                    positive = False
            else:
                return 0
        return 0

            