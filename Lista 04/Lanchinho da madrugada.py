def merge_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if fim - inicio > 1:
        meio = (fim + inicio) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
        return lista


def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right += 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left += 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left += 1
        else:
            lista[k] = right[top_right]
            top_right += 1


def seletor(lista, qunt_rest_inf):
    menores_distancias = []

    for i in range(qunt_rest_inf):
        menores_distancias.append(lista[0])
        del lista[0]

    return menores_distancias


def main():
    restaurantes_informar = int(input())
    restaurantes_totais = int(input())

    lista_distancias = []

    dict = {}

    for i in range(restaurantes_totais):

        entrada = input().split(" ")

        for i in range(len(entrada)):
            entrada[i] = int(entrada[i])

        distancia = (entrada[0] ** 2 + entrada[1] ** 2) ** 1 / 2

        lista_distancias.append(distancia)

        dict[distancia] = entrada

    lista_distancias = merge_sort(lista_distancias)

    lista_rest_info = seletor(lista_distancias, restaurantes_informar)

    lista_rest_info = lista_rest_info[:: -1]

    for i in lista_rest_info:
        temp = dict[i]
        saida = str(temp[0]) + ", " + str(temp[1])
        print(saida)


if __name__ == '__main__':
    main()
