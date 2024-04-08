class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        count = dict.fromkeys('QWER', 0)
        for c in s:
            count[c] += 1

        if count['Q'] == count['W'] == count['E'] == count['R']:
            return 0

        ans = n
        l = 0
        for r in range(n):
            count[s[r]] -= 1
            while l <= r:
                a = sorted(count, key=lambda x: count[x])
                needed = count[a[3]] * 3 - sum([count[x] for x in a[:3]])
                if r - l + 1 >= needed:
                    ans = min(ans, r-l+1)
                    count[s[l]] += 1
                    l += 1
                else:
                    break
        return ans
