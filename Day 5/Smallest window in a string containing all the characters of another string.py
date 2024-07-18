
class Solution:
    def smallestWindow(self, s: str, p: str) -> str:
        from collections import defaultdict

        n = len(s)
        s_map, p_map = defaultdict(int), defaultdict(int)

        for char in p:
            p_map[char] += 1
        v = len(p_map)

        need = 0
        mini = float('inf')
        l = 0
        ind1, ind2 = -1, -1

        for i in range(n):
            s_map[s[i]] += 1

            if s[i] in p_map and s_map[s[i]] == p_map[s[i]]:
                need += 1

            while need == v:
                if mini > i - l + 1:
                    ind1 = l
                    ind2 = i
                    mini = i - l + 1

                s_map[s[l]] -= 1
                if s[l] in p_map and s_map[s[l]] < p_map[s[l]]:
                    need -= 1
                l += 1

        return s[ind1:ind1 + mini] if mini != float('inf') else "-1"
