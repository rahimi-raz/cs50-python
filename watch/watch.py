import re
import sys
def main():
    print(parse(input("HTML: ")))

def parse(s):
    maches=re.search(r"(src=\"https?://(www.)?youtube.com/embed/)(\w*)(\")",s)
    if maches:
        return (f"https://youtu.be/{maches.group(3)}")
    # else:
    #     return (maches.group(3))
if __name__ == "__main__":
    main()