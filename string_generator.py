import random

def generate_string(productions, max_lenght, start_symbol="S"):
    def expand(symbols, current_string):
        if len(current_string) > max_lenght:
            return None
        
        if not symbols:
            return current_string
        
        symbol = symbols[0]
        
        if symbol not in productions:
            return expand(symbols[1:], current_string + symbol)
        
        prod = productions[symbol]
        random.shuffle(prod)

        for product in prod:
            if product == "@":
                result = expand(symbols[1:], current_string)
            else:
                result = expand(list(product) + symbols[1:], current_string)

            if result is not None and len(result) <= max_lenght:
                return result
        
        return None
    
    return expand(list(start_symbol), "")

        
        