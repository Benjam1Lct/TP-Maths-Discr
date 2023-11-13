from math import sqrt

def premier(n):
    list_premier = [2]
    counter = 3
    while len(list_premier) < n:
        for premier in list_premier:
            if premier <= sqrt(counter) and counter%premier != 0:
                list_premier.append(premier)
        counter += 1

    return list_premier


if __name__ == '__main__':
    print(premier(5))
