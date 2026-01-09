# 1. Definindo a função (equivalente ao lengthOfList no Nix)
def length_of_list(lista):
    return len(lista)

# 2. Criando o dicionário/objeto (equivalente ao { description = ... } no Nix)
resultado = {
    "description": f"Tamanho da lista: {length_of_list(['a', 'b', 'c'])}"
}

print(resultado["description"])

