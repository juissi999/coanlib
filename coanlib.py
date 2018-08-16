import re

def read_codelines(filepath):
    """ Reads a source code file and returns all lines. """

    with open(filepath) as f:
        lines = f.readlines()
    
    return lines

def functions(lines): 
    """ Lists all the functions in codelines. """

    functions = []

    lines_stripped = remove_strings(lines)
    lines_nocom = remove_comments(lines_stripped)
    one_line = concatenate_codelines(lines_nocom)

    functions = re.findall("def [^\:]*", one_line)

    return functions

def remove_comments(codelines):
    """ Removes all comments from codelines. """

    lines_removed = []
    for l in codelines:

        # remove comments
        lines_removed.append(re.sub("#.*", "", l))

    return lines_removed

def concatenate_codelines(codelines):
    """ Compresses a list of strings into one string. """

    codeline = ""

    for l in codelines:
        codeline = codeline + l

    return codeline

def calculate_count(expr, codelines):
    """ Calculates occurrences of expr in codelines. (max 1/line) """

    count = 0
    for l in codelines:
        if re.match(expr, l) is not None:
            count +=1

    return count

def remove_strings(codelines):
    """ Removes strings from the code. """

    reg = re.compile("\"[^\"]*\"")
    
    newlines = []
    for l in codelines:
        l = re.sub("\"[^\"]*\"", "", l)
        newlines.append(l)

    return newlines

def imports(codelines):
    
    imps = []
    for l in codelines:
        if re.search("import [^\s]*", l) is not None:
            imps.append(l)

    return imps

def remove_eols(string):

    if isinstance(string, str):
        return(re.sub("\n", " ", string))
    else:
        newlist = []
        for s in string:
            newlist.append(re.sub("\n", " ", s))
        return newlist

def function_calls(lines):
    """ Return all function calls from codelines. """

    # remove strings    
    # remove comments
    # remove function definitions

#    lines_stripped = remove_strings(lines)
    lines_nocom = remove_comments(lines) #_stripped
    one_line = concatenate_codelines(lines_nocom)

    one_line = re.sub("def [^\:]*", "", one_line)

    calls = re.findall("[a-zA-Z]*[a-zA-Z0-9]*\([^\)]*\)", one_line)

    return calls



def code_statistics(filepath):
    """ Print statistics about the code. [more coming] """

    c = read_codelines(filepath)

    c_stripped = remove_strings(c)
    commentlinec = calculate_count(" *#", c_stripped)
    trailing_commentc = calculate_count("(.*)#", c_stripped) - commentlinec

    print("Source code contains %d commentlines" % commentlinec)
    print("Source code contains %d trailing comments" % trailing_commentc)

#    c_no_str_no_coms = remove_comments(c_stripped)
    no_coms = remove_comments(c)
    fcs = functions(no_coms)

    print("\nSource code contains %d functions" % len(fcs))
    print("Function definitions listed:")
    for i in fcs:
        print(" " + i)

    imps = imports(remove_eols(no_coms))
    print("\nSource code contains %d imports" % len(imps))
    print("Imports listed:")
    for i in imps:
        print(" " + i)

    calls = function_calls(c)
    print("\nFunction calls:")
#
    for i in calls:
        print(" " + i)
