# python3

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def checkBrackets(text):
    brackets = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            brackets.append(Bracket(next, i))

        if next == ')' or next == ']' or next == '}':
            if not brackets:
                return i+1
            top = brackets.pop()
            if not top.Match(next):
                return i+1
    if not brackets:
        return 'Success'
    else:
        return brackets.pop().position+1

if __name__ == "__main__":
    text = input()
    print(checkBrackets(text))