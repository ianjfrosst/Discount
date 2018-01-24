
import sys
import re

def parse(file_in, file_out):
    parse2(file_in, file_out)
    #for line in file_in:
    #    parse_line(line)


def format_from_token(token, count):
    if token == "*" or token == "_":
        if count == 2:
            return "b"
        if count == 1:
            return "i"
    if token == "#" :
        return "h"+str(count)
    return ""

def line_format_from_token(token, count):
    if token == ">" :
        return "blockquote"
    if token == "*" or token == "-":
        return "li"
    if token == "#" :
        return "h"+str(count)



def parse2(file_in, file_out):
    # List of all patterns currently enabled
    formats = []
    lineFormats = []


    for line in file_in:
        line.rstrip()
        token = "\0"
        count = 0

        if line.splitlines()[0] == "":
            # Remove all formatting
            for form in formats:
                print("</" + form + ">", end="")
                formats.remove(form)
            for form in lineFormats:
                print("</" + form + ">", end="")
                lineFormats.remove(form)
            #print("<br>",end="")


        header = re.match(r'#+ ', line)
        if (header) :
            start, end = header.span()
            line = line[end:]
            lineFormats.append(line_format_from_token("#", end-1))

        if line.startswith("- ") or line.startswith("* "):
            lineFormats.append(line_format_from_token("-",1))
            line = line[2:]
            if "ul" not in formats:
                formats.append("ul")
                print("<" + "ul" + ">", end="")


        if line.startswith("> "):
            lineFormats.append(line_format_from_token(">", 1))
            line = line[2:]
            for form in formats:
                print("</" + form + ">", end="")
                formats.remove(form)


        for form in lineFormats:
            print("<" + form + ">", end="")

        escape = 0
        #print (line)
        for c in line:
            if escape > 0:
                escape -= 1
                print(c, end="")
                continue

            if c == token:
                count += 1
            else :
                if token != "\0":
                    form = format_from_token(token, count)
                    if form in formats :
                        print ("</"+form+">", end="")
                        formats.remove(form)
                    else :
                        print ("<"+form+">", end="")
                        formats.append(form)

                    token = "\0"

                if c == "\\" :
                    escape += 1
                elif c == "*" or c == "_" :
                    token = c
                    count = 1
                else:
                    print (c, end="")

        for form in lineFormats:
            print("</" + form + ">", end="")
            lineFormats.remove(form)
