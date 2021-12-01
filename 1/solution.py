from utils.util import file2list


def count(l):
    sum = 0
    for i in range(1, len(l)):
        bigger = l[i-1] < l[i]
        sum += bigger
    return sum

def main():
    l = file2list("./1/input.txt")
    l = [int(x) for x in l]
    print(count(l))
    l2 = []
    for i in range(0,len(l)-2):
        l2.append(l[i] + l[i+1] + l[i+2])
    print(count(l2))

main()