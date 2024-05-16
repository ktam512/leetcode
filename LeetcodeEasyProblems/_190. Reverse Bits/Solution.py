class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # Define the result bit
        res = 0
        # Loop 32 times over each bit in n
        for i in range (32):
            # Shift the result bit to the left by 1
            # creating space for the next bit
            res <<= 1
            # Using the bit function AND to take the 
            #least significant bit (LSB) of n
            new_bit = (n & 1)
            # Using the bit function OR to take in the new bit 
            # and put it at the right side of res
            res |= new_bit
            # Shift the n bit to the right by 1
            # change its LSB to the next bit
            n >>= 1
        
        return res

        