def numDecodings(s: str) -> int:
    # Check if the input string is empty or starts with '0',
    # in which case it can't be decoded.
    if not s or s[0] == '0':
        return 0
    
    n = len(s)
    # Create a list to store the number of ways to decode
    # the string up to the current index.
    dp = [0] * (n + 1)
    
    # Initialize the first two elements of dp based on the
    # first digit of the input string.
    dp[0] = 1  # Empty string has one way to decode
    dp[1] = 1 if s[0] != '0' else 0  # First digit can be decoded if it's not '0'
    
    # Iterate through the string starting from the second index.
    for i in range(2, n + 1):
        # Check if the current single digit can be decoded
        # (i.e., it's between '1' and '9').
        if 1 <= int(s[i-1:i]) <= 9:
            dp[i] += dp[i - 1]  # Add the number of ways to decode the previous digit
        
        # Check if the current two digits can be decoded
        # (i.e., they form a number between 10 and 26).
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i - 2]  # Add the number of ways to decode the two previous digits
    
    # The last element of dp contains the total number of ways


