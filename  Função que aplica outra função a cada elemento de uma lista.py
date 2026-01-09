def join_list(lst, sep=", "):
    return sep.join(lst)

def map_list(func, lst):
    return [func(x) for x in lst]

# Lista inicial
lista = ["vim", "git", "htop"]

# Função para formatar os elementos da lista
formatted_list = map_list(lambda x: f"pkg-{x}", lista)

# Juntando a lista formatada em uma string
description = f"Mapa lista: {join_list(formatted_list)}"

# Estrutura final
result = {
    "description": description
}

print(result)