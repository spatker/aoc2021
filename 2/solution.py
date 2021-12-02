from utils.util import file2list


def main():
    l = file2list("./2/input.txt")
    depth = 0
    forward = 0
    for i in l:
        if (i.startswith("forward")):
            forward += int(i[len("forward ")])
        elif (i.startswith("up")):
            depth -= int(i[len("up ")])
        elif (i.startswith("down")):
            depth += int(i[len("down ")])
    print(depth*forward)


def main2():
    l = file2list("./2/input.txt")
    depth = 0
    forward = 0
    aim = 0
    for i in l:
        command, x = i.split(" ")
        x = int(x)
        if (command == "forward"):
            forward += x
            depth += x*aim
        elif (command == "up"):
            aim -= x
        elif (command == "down"):
            aim += x
    print(depth*forward)

main()
main2()