from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        
        # Iterate through each word in the list of strings
        for word in strs:
            # Sort the characters of the word to create a key for the anagrams dictionary
            sorted_word = ''.join(sorted(word))
            # Append the word to the list of anagrams with the same sorted characters
            anagrams[sorted_word].append(word)
        
        # Return the values (lists of anagrams) from the dictionary as the result
        return list(anagrams.values())
