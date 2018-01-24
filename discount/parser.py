
import sys
import re

def parse(file_in, file_out):
    for line in file_in:
        parse_line(line)

def parse_line (line):
    # let's match beginning-of-line elements
    head = re.match(r'#+\ ?', line) # look for headings
    quote = re.match(r'(>\ *)+', line) # look for quotes
    if head: print(head)
    if quote: print(quote)

    heading_depth = 0

    if line.startswith("-") or line.startswith("*"):
        print("BULLET")

    elif line.startswith("#"):
        heading_depth = 0
        for a in line:
            if a == "#":
                heading_depth += 1
            else:
                break
        print("Heading, rank", heading_depth)
        line = line[heading_depth+1:]

    lToken = "\0"
    tCount = 0

    isComment = False

    def get_tag(token,count):
        if token == "*" or token == "_":
            if count == 2:
                return "<b>"


    for c in line:
        # Found a *; we're either
        
        if c == lToken:
            tCount += 1
        else:
            tCount = 0
        
        if c == "\\":
            isComment = not isComment
            lToken = "\0"
            tCount = 0
        
        if not isComment:
            if c == "*":
                if lToken == c:
                    tCount += 1
                else:
                    tCount = 0
                lToken = c
            elif c == "_":
                if lToken == c:
                    tCount += 1
                else:
                    tCount = 0
                lToken = c
            
            if lToken == "*" or lToken == "_":
                if tCount == 1:
                    print("<b>")
                if tCount == 2:
                    print("<i>")

    print(line, end="")
