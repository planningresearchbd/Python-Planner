import re

def tokenize(file_loc):
    """Takes in a pddl file and processes its contents into word tokens, formatted according to pddl definitions

    Args:
        file_loc: The path to the pddl file

    Returns:
        tokens: Processed and formatted tokens

    """
    f = open(file_loc,'r')
    text = re.sub(r';.*$', '', f.read(), flags=re.MULTILINE).lower()
    f.close()
    text = text.replace('ï', '')
    text = text.replace('»', '')
    text = text.replace('¿', '')

    stack = []
    tokens = []
    for t in re.findall(r'[()]|[^\s()]+', text):
        if t == '(':
            stack.append(tokens)
            tokens = []
        elif t == ')':
            if stack:
                l = tokens
                tokens = stack.pop()
                tokens.append(l)
            else:
                raise Exception('Missing open parentheses')
        else:
            tokens.append(t)
    if stack:
        raise Exception('Missing close parentheses')

    return tokens[0]

#a = tokenize('maze_solver.pddl')
#for token in a:
#    print(token,'\n------\n')