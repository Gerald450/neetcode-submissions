class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in hashmap_s:
                hashmap_s[i] += 1
            else:
                hashmap_s[i] = 1
        # {key, value
        #     r: 2, a:2, c:2, e:1
        #     }
        for y in t:
            if y in hashmap_t:
                hashmap_t[y] += 1
            else:
                hashmap_t[y] = 1
        #{c:2, a:2, r:2, e:1}

        for key, value in hashmap_s.items():
            if key in hashmap_t:
                if hashmap_t[key] != hashmap_s[key]:
                    return False
            else:
                return False
        return True