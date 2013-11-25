import sys

if __name__ == '__main__':
    cmd = sys.argv[1]
    nums = map(float, sys.argv[2:])
    if cmd == "add":
        print(sum(nums))
    elif cmd == "mult":
        print(reduce(lambda a,b:a*b, nums))

