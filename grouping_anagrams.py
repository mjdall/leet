def group_anagrams(strs):
        """
        Groups anagrams together into groups.
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_grouping = {}
        
        for anagram in strs:
            curr_ana = str(sorted(anagram))
            anagram_grouping.setdefault(curr_ana, [])
            
            anagram_grouping[curr_ana].append(anagram)
        
        return [ anagram_grouping[grouping] for grouping in anagram_grouping ]
