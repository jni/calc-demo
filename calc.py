import sys

if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == "add":
        nums = map(float, sys.argv[2:])
        print(sum(nums))
    elif cmd == "mult":
        nums = map(float, sys.argv[2:])
        print(reduce(lambda a,b:a*b, nums))

