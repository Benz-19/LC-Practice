class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        result = []

        for i in range(n):
            if k == 0:
                result.append(0)
            elif k > 0:
                total = 0
                for j in range(1, k + 1):
                    total += code[(i + j) % n] 
                result.append(total)
            else:  # k < 0
                total = 0
                for j in range(1, -k + 1):
                    total += code[(i - j + n) % n] 
                result.append(total)

        return result


# Test
code = [5, 7, 1, 4]
k = 3
decode = Solution()
print(decode.decrypt(code, k))
