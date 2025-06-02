# CFG Parser, String Generator and Verifier

This Python script reads a context-free grammar (CFG) from a file, generates strings from that grammar, and optionally checks if specific strings can be derived from it. It also checks whether given strings are in the form of `aⁿbⁿcⁿ`.

The script parses a CFG from a user-provided file, generates up to 10 unique strings using the production rules, verifies whether specific words can be derived from the grammar, and checks if the strings conform to the format `aⁿbⁿcⁿ`. It relies on several helper modules: `parser.py` (for parsing the grammar), `string_generator.py` (for generating strings), `check_string.py` (for checking derivations), and `checkanbncn.py` (for `aⁿbⁿcⁿ` validation).

## Requirements

- Python 3.x

## Project Structure

```
.
├── main_script.py # Main script
├── parser.py # Contains grammar_parser()
├── string_generator.py # Contains generate_string()
├── check_string.py # Contains derive_string()
├── checkanbncn.py # Contains check_word()
├── grammar.txt # Input CFG file (user-provided)
└── words.txt # Optional file with words to check

```


## Usage

### Generate strings from a grammar file:

```bash
py CFG.py grammar.txt
```

### Generate strings from grammar files and verify words from a words text file if they are from that CFG
```bash
py CFG.py grammar.txt words.txt
```

## Grammar File Format (`grammar.txt`)

The grammar file should follow a format readable by `parser.py`, and it must include:

- A list of **non-terminals**
- A list of **terminals**
- A **start symbol**
- A set of **production rules**

### Example Format

Each production rule should follow the form:
```
S -> aSb | @
```
where @ is the lambda symbol (ε)


