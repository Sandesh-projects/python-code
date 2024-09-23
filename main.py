# Function to compute the LPS (Longest Prefix Suffix) array
def compute_LPS(pattern):
    lps = [0] * len(pattern)  # LPS array to hold the longest prefix suffix values
    length = 0  # Length of the previous longest prefix suffix
    i = 1

    # Build the LPS array
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Use the previously computed LPS value
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

# KMP search function
def KMP_search(text, pattern):
    n = len(text)     # Length of the text
    m = len(pattern)  # Length of the pattern
    lps = compute_LPS(pattern)  # Compute the LPS array for the pattern
    i = 0  # Index for text
    j = 0  # Index for pattern

    # Loop through the text
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            # Found the pattern at index i - j
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]

        # Mismatch after j matches
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

# Example usage
text = "BACBABABABACAAB"
pattern = "ABABACA"
KMP_search(text, pattern)
