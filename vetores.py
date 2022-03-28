def search(vetor, elemento):
    for index, numero in enumerate(vetor):
        if numero == elemento:
            return index

    return -1


def insert(vetor, elemento, index):
    if index > len(vetor):
        to_insert = index - len(vetor)
        for index in range(to_insert):
            vetor.append(0)
        vetor.append(elemento)
    else:
        vetor.insert(index, elemento)


def remove(vetor, elemento):
    index = [index for index, _ in enumerate(vetor) if _ == elemento][0]

    if index:
        vetor.pop(index)
        return index
    else:
        return -1


if __name__ == "__main__":
    v = [0, -1, -2, -2, -4, -5]
    rs = search(v, 2)
    print(rs)
    insert(v, 2, 3)
    print(v)
    insert(v, 10, 10)
    print(v)
    rr = remove(v, -2)
    print(rr)
    print(v)
