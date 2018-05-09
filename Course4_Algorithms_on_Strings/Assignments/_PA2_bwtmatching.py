# python3
import sys

def PreprocessBWT(bwt, alphabet = ['$', 'A', 'C', 'G', 'T']):
    """
    Preprocess the Burrows-Wheeler Transform bwt of some text
    and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position 
        of this character in the sorted array of 
        all characters of the text.
    * counts - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
    """
    l = len(bwt)
    counts = dict()
    starts = dict()
    for char in alphabet:
        counts[char] = [0] * (l + 1)
    for i in range(l):
        currChar = bwt[i]
        for char, count in counts.items():
            counts[char][i+1] = counts[char][i]
        counts[currChar][i+1] += 1
    currIndex = 0
    for char in sorted(alphabet):
        starts[char] = currIndex
        currIndex += counts[char][l]
    return starts, counts

def CountOccurrences(pattern, bwt, starts, counts):
    """
    Compute the number of occurrences of string pattern in the text
    given only Burrows-Wheeler Transform bwt of the text and additional
    information we get from the preprocessing stage - starts and counts.
    """
    top = 0
    bottom = len(bwt) - 1
    currIndex = len(pattern) - 1
    while top <= bottom:
        if currIndex >= 0:
            symbol = pattern[currIndex]
            currIndex -= 1
            if counts[symbol][bottom+1] - counts[symbol][top] > 0:
                top = starts[symbol] + counts[symbol][top]
                bottom = starts[symbol] + counts[symbol][bottom+1] - 1
            else:
                return 0
        else:
            return bottom - top + 1
     


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    # Preprocess the BWT once to get starts and occ_count_before.
    # For each pattern, we will then use these precomputed values and
    # spend only O(|pattern|) to find all occurrences of the pattern
    # in the text instead of O(|pattern| + |text|).  
    starts, occ_counts_before = PreprocessBWT(bwt)
    occurrence_counts = []
    for pattern in patterns:
        occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
    print(' '.join(map(str, occurrence_counts)))