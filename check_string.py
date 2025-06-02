def derive_string(productions, target_string, start_symbol = "S"):
    def do_steps(current_string, deriv_steps, max_depth=50):
        if len(deriv_steps) > max_depth:
            return None
        
        if current_string == target_string:
            return deriv_steps
        
        if all(c not in productions for c in current_string):
            return None
        
        for i, symbol in enumerate(current_string):
            if symbol in productions:
                for prod in productions[symbol]:
                    aux = prod if prod != "@" else ""
                    string_aux = current_string[:i] + aux + current_string[i+1:]
                    result = do_steps(string_aux, deriv_steps + [string_aux])
                    if result:
                        return result
                break
        
        return None
    
    return do_steps(start_symbol, [start_symbol])