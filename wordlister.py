import itertools
import os

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
def main():
    

    base_file = input("Arquivo com palavras base: ").strip()
    with open(base_file, "r", encoding="utf-8") as f:
        base_words = [line.strip() for line in f if line.strip()]

    min_comb = input("Mínimo de palavras combinadas (deixe vazio para sem limite): ").strip()
    max_comb = input("Máximo de palavras combinadas (deixe vazio para sem limite): ").strip()
    min_len = input("Tamanho mínimo da senha (deixe vazio para ignorar): ").strip()
    max_len = input("Tamanho máximo da senha (deixe vazio para ignorar): ").strip()
    use_upper = input("Gerar variações com maiúsculas? (s/n): ").strip().lower() == "s"
    use_leet = input("Gerar variações com l33t? (s/n): ").strip().lower() == "s"
    output_file = input("Nome do arquivo de saída: ").strip()

    if not output_file:
        print("Nome do arquivo de saída é obrigatório.")
        return

    min_comb = int(min_comb) if min_comb else 1
    max_comb = int(max_comb) if max_comb else len(base_words)
    min_len = int(min_len) if min_len else None
    max_len = int(max_len) if max_len else None

    leet_map = str.maketrans({
        'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'
    })

    def transform(word):
        variations = [word]
        if use_upper:
            variations.append(word.upper())
            variations.append(word.capitalize())
        if use_leet:
            variations += [w.translate(leet_map) for w in variations]
        return variations

    final_words = set()

    print("Gerando variações, aguarde...")

    for i in range(min_comb, max_comb + 1):
        for combo in itertools.permutations(base_words, i):
            combined = ''.join(combo)
            for var in transform(combined):
                if min_len and len(var) < min_len:
                    continue
                if max_len and len(var) > max_len:
                    continue
                final_words.add(var)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(final_words))

    print(f"Total de senhas geradas: {len(final_words)}")
    print(f"Arquivo salvo como: {output_file}")

if __name__ == "__main__":
    print(ascii_art)
    main()

