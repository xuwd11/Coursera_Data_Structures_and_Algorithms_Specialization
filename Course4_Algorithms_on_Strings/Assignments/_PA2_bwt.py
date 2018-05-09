# python3
import sys

def BWT(text):
    return ''.join([m[-1] for m in sorted([text[i:] + text[0:i] for i in range(len(text))])])

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))