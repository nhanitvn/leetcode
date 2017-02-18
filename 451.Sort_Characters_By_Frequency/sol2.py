class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Firstly, we count frequencies
        freq = {}
        freq_to_chars = {}
        result = []
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        
        for c, f in freq.iteritems():
            if f in freq_to_chars:
                freq_to_chars[f] = ''.join([freq_to_chars[f], c * f])
            else:
                freq_to_chars[f] = c * f
        
        for i in range(len(s), 0, -1):
            if i in freq_to_chars:
                result.extend(freq_to_chars[i])
            
        return ''.join(result)
