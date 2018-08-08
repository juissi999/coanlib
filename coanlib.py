import re

def read_codelines(filepath):
    """ Reads a source code file and returns all lines. """

    with open(filepath) as f:
        lines = f.readlines()
    
    return lines

def functions(lines): 
    """ Lists all the functions in the code. """

    functions = []

    for l in lines:

        fs = l
        # remove comments
        re.sub("#.*", "", fs)

        if re.match(" *def ", fs) is not None:

            # remove space before def and after
            fs = re.sub(" *def ", "", fs)

            # remove double-comma and things after that and EOL
            # assume no double-comma used in function definition
            fs = re.sub(":.*\n", "", fs)
            functions.append(fs)

    return functions

def remove_comments(codelines):

    for l in lines:

        # remove comments
        re.sub("#.*", "", l)

    return l