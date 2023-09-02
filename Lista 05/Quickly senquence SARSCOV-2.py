saida = []


def quicksort(vetor, inicio=0, fim=None):
    if fim is None:
        fim = len(vetor) - 1
    if inicio < fim:
        pivo = particionar(vetor, inicio, fim)
        quicksort(vetor, inicio, pivo - 1)
        quicksort(vetor, pivo + 1, fim)


def particionar(vetor, inicio, fim):
    index_pivo = inicio
    i = inicio + 1
    j = fim

    while i <= j:
        while i <= j and vetor[i] <= vetor[index_pivo]:
            i += 1
        while i <= j and vetor[j] >= vetor[index_pivo]:
            j -= 1
        if i <= j:
            trocar(vetor, i, j)
            i += 1
            j -= 1
    trocar(vetor, index_pivo, j)
    return j


def trocar(vetor, i, j):
    vetor[i], vetor[j] = vetor[j], vetor[i]
    if vetor[i] != vetor[j]:
        saida.append(str(vetor[j]) + " " + str(vetor[i]))


def main():
    array = []
    while True:
        try:
            entrada = input().split(" ")
            array.append(int(entrada[0]))
        except EOFError:
            break
    quicksort(array)
    for i in saida[0: -1]:
        print(i)
    print(saida[-1], end='')


if __name__ == '__main__':
    main()
