import string
chars = list(string.ascii_lowercase + string.digits)

def grammar_parser(infile):
    non_terminals = set()
    terminals = set()
    start_symbol = "S"
    product = {}

    while line := infile.readline().strip():
        frm, results = line.split("->")
        frm = frm.strip()
        for res in results.split("|"):
            for char in res.strip():
                if char in chars:
                    terminals.add(char)
                elif char in string.ascii_uppercase:
                    non_terminals.add(char)
                
            if frm not in product:
                product[frm] = [res.strip()]
            else:
                product[frm] += [res.strip()]

    return [non_terminals, terminals, start_symbol, product]