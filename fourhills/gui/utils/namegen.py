'''
This is a markov name generator based off the name generator from https://donjon.bin.sh/code/name/
and ported to python
'''

import math
import random


def generate_name(name_set):
    try:
        chain = markov_chain(name_set)
        if chain:
            name = markov_name(chain)
            if name == None:
                return generate_name(name_set)
            else:
                return name
        return 'Problem with name set'
    except:
        return generate_name(name_set)


def name_list(name_set, n_of):
    return [generate_name(name_set) for _ in range(n_of)]


def markov_chain(name_set):
    ls = name_set
    chain = construct_chain(ls)
    if chain:
        return chain
    return False
    

def construct_chain(ls):
    chain = {}

    for i in range(len(ls)):
        names = ls[i].split()
        chain = incr_chain(chain, "parts", len(names))

        for name in names:
            chain = incr_chain(chain, "name_len", len(name))

            c =  name[0:1]
            chain = incr_chain(chain, "initial", c)

            string = name[1:]
            last_c = c

            while len(string) > 0:
                c = string[0:1]
                chain = incr_chain(chain, last_c,c)

                string = string[1:]
                last_c = c
    return scale_chain(chain)


def incr_chain(chain, key, token):
    if key in chain: 
        if token in chain[key]:
            chain[key][token] += 1
        else:
            chain[key][token] = 1
    else:
        chain[key] = {}
        chain[key][token] = 1
    return chain

    
def scale_chain(chain):
    table_len = {}
    for key in chain:
        table_len[key] = 0

        for token in chain[key]:
            count = chain[key][token]
            weighted = math.floor(math.pow(count, 1.3))

            chain[key][token] = weighted
            table_len[key] += weighted
            
    chain['table_len'] = table_len
    return chain


#construct name from markov chain

def markov_name(chain):                                                      
    parts = select_link(chain, "parts")
    names = []
    for i in range(parts):
        name_len = select_link(chain, "name_len")
        c = select_link(chain, "initial")
        name = c
        last_c = c

        while len(name) < name_len:
            c = select_link(chain, last_c)
            name += c
            last_c = c;
        names.append(name)

    return " ".join(names)


def select_link(chain, key):
    if key in chain["table_len"]:
        length = chain["table_len"][key]
    else:
        length = 1
    idx = math.floor(random.random() * length)
    t = 0
    for token in chain[key]:
        t += chain[key][token]
        if idx < t:
            return token

    return "-"