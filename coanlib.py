import re

def read_codelines(filepath):
    """ Reads a source code file and returns all lines. """

    with open(filepath) as f:
        lines = f.readlines()
    
    return lines

def functions(lines): 
    """ Lists all the functions in the code. """

    functions = []

    lines_nocom = remove_comments(lines)

    for l in lines_nocom:

        if re.match(" *def ", l) is not None:

            # remove space before def and after
            l = re.sub(" *def ", "", l)

            # remove double-comma and things after that and EOL
            # assume no double-comma used in function definition
            l = re.sub(":.*\n", "", l)
            functions.append(l)

    return functions

def remove_comments(codelines):

    lines_removed = []
    for l in codelines:

        # remove comments
        lines_removed.append(re.sub("#.*", "", l))

    return lines_removed

def concatenate_codelines(codelines):

    codeline = ""

    for l in codelines:
        codeline = codeline + l

    return codeline

def calculate_count(expr, codelines):

    count = 0
    for l in codelines:
        if re.match(expr, l) is not None:
            count +=1

    return count

def remove_strings(codelines):

    reg = re.compile("\"[^\"]*\"")
    
    newlines = []
    for l in codelines:
        l = re.sub("\"[^\"]*\"", "", l)
        newlines.append(l)

    return newlines

def code_statistics(filepath):

    c = read_codelines(filepath)

    c_stripped = remove_strings(c)
    commentlinec = calculate_count(" *#", c_stripped)
    trailing_commentc = calculate_count("(.*)#", c_stripped) - commentlinec
    fcs = functions(c)

    print("Source code contains %d commentlines" % commentlinec)
    print("Source code contains %d trailing comments" % trailing_commentc)
    print("Source code contains %d functions" % len(fcs))
    print("Functions listed:")

    for i in fcs:
        print(" " + i)
