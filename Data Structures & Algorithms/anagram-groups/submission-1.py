class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        #{act: [act, cat], stop: [stop, pots, tops]}

        for word in strs:

            w = ''.join(sorted(word))

            if w in strs_dict:
                strs_dict[w].append(word)
            else:
                strs_dict[w] = [word]
        
        return strs_dict.values()