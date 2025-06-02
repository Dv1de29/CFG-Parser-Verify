# -*- coding: utf-8 -*-

import sys
import parser as ps
import string_generator as sg
import check_string as check
import checkanbncn as abc

non_terminals = set()
terminals = set()
start_symbol = "S"
product = {}

if __name__ == "__main__":
    file = sys.argv[1].strip()
    grammar_file = open(file, "r")
    
    non_terminals, terminals, start_symbol, product = ps.grammar_parser(grammar_file)

    print("This is the machine configuration:")
    print(f"Non-terminals values: {non_terminals}")
    print(f"Terminals values: {terminals}")
    print(f"Start simbol: {start_symbol}")
    print(f"productions: {product}")
    print("\nThis is some string from the CFG language:")

    tries = 0
    max_tries = 1000
    count = 0
    strings = set()
    while count < 10 and tries <= max_tries:
        tries += 1
        result = sg.generate_string(product, 10, start_symbol)
        if result == "":
                result = "@"
        if result is not None and result not in strings:
            strings.add(result)
            count += 1
            print(f"{count}: {result}")

    if count < 10:
        print(f"Only generated {count} strings from {max_tries} attempts\n")

    if len(sys.argv) == 3:
        print("Verfication of the words:\n")
        words_f = sys.argv[2].strip()
        words_file = open(words_f, "r")

        while word := words_file.readline( ).strip():
            print(f"Verifing {word}:")
            resulted_steps = check.derive_string(product, word)
            if resulted_steps:
                print( f"{" -> ".join(resulted_steps)} \n[True]")
            else:
                print("The string is not derived from the CFG \n[False]")

            print("Verifing for a^n b^n c^n:")
            print(f"Word '{word}' is {abc.check_word(word)}\n")

#ε