def join_list(lst):
    return ", ".join(lst)

def filter_list(condition, lst):
    return [x for x in lst if condition(x)]

# Lista original
lista = ["a", "b", "c", "d"]

# Filtrando (remover "b")
filtrada = filter_list(lambda x: x != "b", lista)

# Juntando em string
descricao = f"Filtro lista: {join_list(filtrada)}"

print(descricao)
