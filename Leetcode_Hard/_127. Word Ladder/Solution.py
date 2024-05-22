class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # The middle sequence 
        # (aside from the beginWord and endWord)
        # must be inside the wordList 

        # We also know that each word
        # that differ only by 1 will be each other's 
        # neighbor, we can then create a graph of 
        # nodes with its adjacent nodes as neighbors

        # 

