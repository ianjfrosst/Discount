
import sys

def parse(file_in, file_out):
    for line in file_in:
        parseLine(line)
    
def parseLine (line) :
    print(line, end="")
    if (line.startswith("-") or line.startswith("*")) :
        print ("BULLET")
    if (line.startswith("#")) :
        rank = 0
        for a in line:
            if (a == "#") :
                rank += 1
            else:
                break
        print ("Heading, rank " + str(rank))        
    if (line.startswith("\\")):
        print ("COMMENT: Print this exactly as shown!")
    pass
