class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        # Initialize a variable to store the maximum number of words found
        max_words = 0

        # Iterate through each sentence in the list of sentences
        for sentence in sentences:
            # Split the sentence into words using whitespace as delimiter
            words = sentence.split()
            # Get the length of the list of words
            num_words = len(words)
            # Update max_words if the current sentence has more words
            max_words = max(max_words, num_words)

        # Return the maximum number of words found
        return max_words