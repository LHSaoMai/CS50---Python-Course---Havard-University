from collections import Counter
def main():
    x = Counter(list())
    sort_x = dict(sorted(x.items()))
    for i in sort_x:
        print(sort_x[i], i.upper())

def list():
    grocery = []
    while True:
        try:
            item = input()
            grocery.append(item)
        except EOFError:
            return grocery

main()
