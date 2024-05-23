def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    # All words have the same length
    L = len(beginWord)
    
    # Dictionary to hold all combinations of words that can be formed
    # from any given word by changing one letter at a time.
    all_combo_dict = defaultdict(list)
    
    for word in wordList:
        for i in range(L):
            # Key is the generic word
            # Value is a list of words which have the same intermediate generic word
            generic_word = word[:i] + "*" + word[i+1:]
            all_combo_dict[generic_word].append(word)

    # Queue for BFS
    queue = deque([(beginWord, 1)])
    # Visited dictionary to make sure we don't repeat processing the same word
    visited = {beginWord: True}
    
    while queue:
        current_word, level = queue.popleft()
        
        for i in range(L):
            # Intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]
            
            # Next states are all the words which share the same intermediate state.
            for word in all_combo_dict[intermediate_word]:
                # If we find the end word, return the answer
                if word == endWord:
                    return level + 1
                # Otherwise, add it to the BFS queue
                if word not in visited:
                    visited[word] = True
                    queue.append((word, level + 1))
            
            # Clear the intermediate words to prevent loops
            all_combo_dict[intermediate_word] = []
    
    return 0