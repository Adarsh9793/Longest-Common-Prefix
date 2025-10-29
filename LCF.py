# Longest Common Prefix


from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

# --- User Input Section ---
if __name__ == "__main__":
    # Input: comma-separated strings
    user_input = input("Enter strings separated by commas: ")
    strs = [s.strip() for s in user_input.split(",")]

    sol = Solution()
    result = sol.longestCommonPrefix(strs)
    print("Longest Common Prefix:", result)
