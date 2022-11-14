class Solution:
    def countSubstrings(self, s):

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        palindromes = []
        for middle in range(len(s)):
            left = middle
            right = middle

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    palindromes.append(s[left:right + 1])
                else:
                    break

                left -= 1
                right += 1

        for middle_left in range(len(s)):
            left = middle_left
            right = middle_left + 1

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    palindromes.append(s[left:right + 1])
                    num_palindromes += 1
                else:
                    break

                left -= 1
                right += 1
                #pali=[]
                for k in palindromes:
                    for j in palindromes:
                        if j in k:
                            print("yes")
                            palindromes.remove(k)
        return palindromes


def main():
    sol = Solution()
    print(sol.countSubstrings("madamciviclevel"))


if __name__ == '__main__':
    main()
