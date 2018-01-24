
import sys

def parse(file_in, file_out):
    for line in file_in:
        parseLine(line)

def parseLine (line) :
    headingDepth = 0
    
    if (line.startswith("-") or line.startswith("*")) :
        print ("BULLET")
    if (line.startswith("#")) :
        headingDepth = 0
        for a in line:
            if (a == "#") :
                headingDepth += 1
            else:
                break
        print ("Heading, rank " + str(headingDepth))
        line = line[headingDepth+1:]
    if (line.startswith("\\")):
        print ("COMMENT: Print this exactly as shown!")
    
    
    lToken = "\0"
    tCount = 0
    
    isComment = False
    
    def getTag(token,count) :
        if (token == "*" or token == "_") :
            if (count == 2) :
                return "<b>"
                
    
    for c in line:
        # Found a *; we're either
        
        if (c == lToken) :
            tCount += 1
        else :
            tCount = 0
        
        if (c == "\\") :
            isComment = not isComment
            lToken = "\0"
            tCount = 0;
        
        if (not isComment) :        
            if (c == "*") :
                if (lToken == c) :
                    tCount += 1
                else :
                    tCount = 0
                lToken = c
            elif (c == "_") :
                if (lToken == c) :
                    tCount += 1
                else :
                    tCount = 0
                lToken = c
            
            if (lToken == "*" or lToken == "_") :
                if (tCount == 1) :
                    print ("<b>")
                if (tCount == 2) :
                    print ("<i>")
        
    
    print(line, end="")
    pass
