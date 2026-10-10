class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_holder = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in anagram_holder:
                anagram_holder[sorted_word] = []

            anagram_holder[sorted_word].append(word)

            anagram_lst = list(anagram_holder.values())

        return anagram_lst
                

                
                    
                
                
                    
            