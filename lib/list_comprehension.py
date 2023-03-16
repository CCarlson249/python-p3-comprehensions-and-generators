#!/usr/bin/env python3

def return_evens(num_list):
    return [x for x in num_list if x % 2 == 0]
    pass

def make_exclamation(sentences):
    return [sentence.strip() + "!" for sentence in sentences]

    pass