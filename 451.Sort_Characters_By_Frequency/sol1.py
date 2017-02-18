class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Firstly, we count frequencies
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
                
        # Sort by frequency
        freq_sorted = sorted(freq.keys(), key=lambda c: -freq[c])
        
        # Now we ensure the freq of characters in the result string
        result = []
        for c in freq_sorted:
            result += c * freq[c]
            
        return ''.join(result)
