class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis ={'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in parenthesis:
                stack.append(parenthesis[char])
            elif not stack or stack.pop() != char:
                return False
        
        if not stack:
            return True
        return False


