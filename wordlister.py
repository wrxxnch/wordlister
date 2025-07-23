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
def leet_variations(word):
    leet_map = {
        'a': ['4', '@'],
        'e': ['3'],
        'i': ['1', '!'],
        'o': ['0'],
        's': ['5', '$'],
        't': ['7'],
        'g': ['9']
    }
    variations = set([word])
    for i, c in enumerate(word):
        if c.lower() in leet_map:
            for sub in leet_map[c.lower()]:
                for variant in list(variations):
                    new_variant = variant[:i] + sub + variant[i+1:]
                    variations.add(new_variant)
    return variations

# Inputs
wordlist_file = input("Arquivo com palavras base: ").strip()
try:
    with open(wordlist_file, "r", encoding="utf-8") as f:
        base_words = [line.strip() for line in f if line.strip()]
except:
    print("Erro ao abrir o arquivo.")
    exit()

min_words = input("Mínimo de palavras combinadas (deixe vazio para sem limite): ").strip()
max_words = input("Máximo de palavras combinadas (deixe vazio para sem limite): ").strip()
min_words = int(min_words) if min_words.isdigit() else 1
max_words = int(max_words) if max_words.isdigit() else len(base_words)

min_len = input("Tamanho mínimo da senha (deixe vazio para ignorar): ").strip()
max_len = input("Tamanho máximo da senha (deixe vazio para ignorar): ").strip()
min_len = int(min_len) if min_len.isdigit() else 0
max_len = int(max_len) if max_len.isdigit() else float('inf')

use_upper = input("Gerar variações com maiúsculas? (s/n): ").lower() == 's'
use_leet = input("Gerar variações com l33t? (s/n): ").lower() == 's'

output_file = input("Nome do arquivo de saída: ").strip()
if not output_file:
    output_file = "senhas.txt"

# Geração
print("Gerando variações, aguarde...")

final_passwords = set()

for n in range(min_words, max_words + 1):
    for combo in itertools.permutations(base_words, n):
        base = ''.join(combo)
        if min_len <= len(base) <= max_len:
            variations = set([base])
            if use_upper:
                variations.update([base.upper(), base.capitalize()])
            if use_leet:
                for var in list(variations):
                    variations.update(leet_variations(var))
            for pw in variations:
                if min_len <= len(pw) <= max_len:
                    final_passwords.add(pw)

# Salvar
with open(output_file, "w", encoding="utf-8") as f:
    for pw in sorted(final_passwords):
        f.write(pw + "\n")

print(f"Total de senhas geradas: {len(final_passwords)}")
print(f"Arquivo salvo como: {output_file}")

if __name__ == "__main__":
    print(ascii_art)
    main()

