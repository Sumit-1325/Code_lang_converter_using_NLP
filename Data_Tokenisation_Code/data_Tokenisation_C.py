import os
import ply.lex as lex

def build_lexer():
    tokens = (
        'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
        'LPAREN', 'RPAREN', 'SEMI', 'LBRACE', 'RBRACE', 'STRING', 'NEWLINE', 'COMMENT',
    )

    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_SEMI = r';'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_STRING = r'".*?"'
    t_NEWLINE = r'\n+'
    t_COMMENT = r'//.*|/\*.*?\*/'

    def t_ID(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        return t

    def t_NUMBER(t):
        r'\d+'
        t.value = int(t.value)
        return t

    t_ignore = ' \t'

    def t_error(t):
        print(f"Illegal character '{t.value}'")
        t.lexer.skip(1)

    lexer = lex.lex()
    return lexer

def tokenize_c_file(filepath):
    lexer = build_lexer()

    with open(filepath, 'r', encoding='utf-8') as file:
        code = file.read()

    lexer.input(code)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    return tokens

def tokenize_files_in_folder(input_folder_path, output_folder_path):
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    for filename in os.listdir(input_folder_path):
        if filename.endswith('.c'):
            filepath = os.path.join(input_folder_path, filename)
            tokens = tokenize_c_file(filepath)
            
            output_filepath = os.path.join(output_folder_path, f"{filename}_tokens.txt")
            with open(output_filepath, 'w', encoding='utf-8') as output_file:
                for token in tokens:
                    output_file.write(f"{token.type}: {token.value}\n")
            print(f'Processed file: {filename}')

input_folder_path = r"E:\codes\sumit\SEM_PROJ_4\Mini_Project_CodeNet\data\p04030\C"
output_folder_path = r"E:\codes\sumit\SEM_PROJ_4\Token_output\C_tokenise_data\C7"
tokenize_files_in_folder(input_folder_path, output_folder_path)
print(f"Tokenized files are saved in: {output_folder_path}")
