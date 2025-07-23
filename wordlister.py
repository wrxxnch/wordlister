import itertools

ascii_art = r"""
 /$$$$$$$  /$$$$$$$$ /$$$$$$$   /$$$$$$  /$$$$$$$$  /$$$$$$ 
| $$__  $$| $$_____/| $$__  $$ /$$__  $$| $$_____/ /$$__  $$
| $$  \ $$| $$      | $$  \ $$| $$  \__/| $$      | $$  \__/
| $$  | $$| $$$$$   | $$  | $$|  $$$$$$ | $$$$$   | $$      
| $$  | $$| $$__/   | $$  | $$ \____  $$| $$__/   | $$      
| $$  | $$| $$      | $$  | $$ /$$  \ $$| $$      | $$    $$
| $$$$$$$/| $$$$$$$$| $$$$$$$/|  $$$$$$/| $$$$$$$$|  $$$$$$/
|_______/ |________/|_______/  \______/ |________/ \______/ 
                                                            
                                                            """
# Leet map
leet_map = {
    'a': ['a', '@', '4'],
    'e': ['e', '3'],
    'i': ['i', '1', '!'],
    'o': ['o', '0'],
    's': ['s', '$', '5'],
    't': ['t', '7']
}

def to_leet(word):
    """Gera variações em leet speak para uma palavra."""
    options = []
    for char in word:
        if char.lower() in leet_map:
            options.append(leet_map[char.lower()])
        else:
            options.append([char])
    return [''.join(x) for x in itertools.product(*options)]

def gerar_combinacoes(palavras, min_palavras, max_palavras, to_upper, use_leet, min_len, max_len):
    for n in range(min_palavras, max_palavras + 1):
        for combinacao in itertools.permutations(palavras, n):
            base = ''.join(combinacao)
            if to_upper:
                base = base.upper()
            if min_len <= len(base) <= max_len:
                if use_leet:
                    for variante in to_leet(base):
                        if min_len <= len(variante) <= max_len:
                            yield variante
                else:
                    yield base

def main():
    print("=== GERADOR DE SENHAS COM LISTA E COMBINAÇÕES ===")
    usar_lista = input("Deseja usar uma lista de palavras? (S/N): ").lower() == 's'

    if usar_lista:
        caminho = input("Caminho do arquivo com palavras (uma por linha): ").strip()
        try:
            with open(caminho, 'r', encoding='utf-8') as f:
                palavras = [linha.strip() for linha in f if linha.strip()]
        except FileNotFoundError:
            print("Arquivo não encontrado.")
            return
    else:
        palavras = []
        min_len = int(input("Comprimento mínimo da senha: "))
        max_len = int(input("Comprimento máximo da senha: "))
        use_uppercase = input("Incluir maiúsculas? (S/N): ").lower() == 's'
        use_lowercase = input("Incluir minúsculas? (S/N): ").lower() == 's'
        use_numbers = input("Incluir números? (S/N): ").lower() == 's'
        use_special = input("Incluir caracteres especiais? (S/N): ").lower() == 's'

        chars = ''
        if use_uppercase:
            chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if use_lowercase:
            chars += 'abcdefghijklmnopqrstuvwxyz'
        if use_numbers:
            chars += '0123456789'
        if use_special:
            chars += '!@#$%^&*()_-+=~`[]{}|\\:;"\'<>,.?/'

        nome_arquivo = input("Nome do arquivo de saída (.txt será adicionado): ").strip() + '.txt'
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            print("Gerando senhas...")
            for length in range(min_len, max_len + 1):
                for combination in itertools.product(chars, repeat=length):
                    senha = ''.join(combination)
                    arquivo.write(senha + '\n')
                    print(senha)
        print(f"\nTodas as senhas foram salvas em '{nome_arquivo}'")
        return

    to_upper = input("Deseja transformar as senhas em maiúsculas? (S/N): ").lower() == 's'
    use_leet = input("Deseja aplicar variações em Leet Speak? (S/N): ").lower() == 's'
    min_palavras = int(input("Quantidade mínima de palavras por senha: "))
    max_palavras = int(input("Quantidade máxima de palavras por senha: "))
    min_len = int(input("Comprimento mínimo da senha final: "))
    max_len = int(input("Comprimento máximo da senha final: "))

    nome_arquivo = input("Nome do arquivo de saída (.txt será adicionado): ").strip() + '.txt'
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        print("\nSenhas geradas:")
        for senha in gerar_combinacoes(palavras, min_palavras, max_palavras, to_upper, use_leet, min_len, max_len):
            arquivo.write(senha + '\n')
            print(senha)

    print(f"\nTodas as senhas foram salvas em '{nome_arquivo}'")

if __name__ == "__main__":
    print(ascii_art)
    main()

