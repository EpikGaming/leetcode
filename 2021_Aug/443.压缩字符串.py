class Solution:
    def compress(self, chars: list):
        def revers(char: list, left: int, right: int):
            while left < right:
                char[left], char[right] = char[right], char[left]
                left += 1
                right -= 1

        n = len(chars)
        write = start = 0
        for read in range(n):
            if read == n - 1 or chars[read] != chars[read + 1]:
                chars[write] = chars[read]
                write += 1
                num = read - start + 1
                if num > 1:
                    temp = write
                    while num > 0:
                        chars[write] = str(num % 10)
                        write += 1
                        num //= 10
                    revers(chars, temp, write - 1)
                start = read + 1
        return write, chars[:write]

s = Solution()
test = "aaaaaaaaaaaabbbbbbcccccccccc"
print(s.compress(list(test)))