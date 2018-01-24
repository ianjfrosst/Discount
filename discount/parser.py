
import re
import sys

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


def line_format_from_token(token, count):
    if token == ">":
        return "blockquote"
    if token == "*" or token == "-":
        return "li"
    if token == "#":
        return "h" + str(count)


def tag(name, close=False):
    return '<{1}{0}>'.format(name, '/' if close else '')

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
                file_out.write(tag(form, True))
                formats.remove(form)
            for form in lineFormats:
                file_out.write(tag(form, True))
                lineFormats.remove(form)
            #file_out.write("<br>")


        header = re.match(r'#+ ', line)
        if header:
            start, end = header.span()
            line = line[end:]
            lineFormats.append(line_format_from_token("#", end-1))

        if line.startswith("- ") or line.startswith("* "):
            lineFormats.append(line_format_from_token("-", 1))
            line = line[2:]
            if "ul" not in formats:
                formats.append("ul")
                file_out.write(tag("ul"))


        if line.startswith("> "):
            lineFormats.append(line_format_from_token(">", 1))
            line = line[2:]
            for form in formats:
                file_out.write(tag(form, True))
                formats.remove(form)


        for form in lineFormats:
            file_out.write(tag(form))

        escape = 0
        for c in line:
            if escape > 0:
                escape -= 1
                file_out.write(c)
                continue

            if c == token:
                count += 1
            else:
                if token != "\0":
                    form = format_from_token(token, count)
                    if form in formats:
                        file_out.write(tag(form, True))
                        formats.remove(form)
                    else:
                        file_out.write(tag(form))
                        formats.append(form)

                    token = "\0"

                if c == "\\":
                    escape += 1
                elif c == "*" or c == "_":
                    token = c
                    count = 1
                else:
                    file_out.write(c)

        for form in lineFormats:
            file_out.write(tag(form, True))
            lineFormats.remove(form)
