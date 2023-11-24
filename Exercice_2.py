from math import sqrt

def premier(n):
    list_premier = [2]
    counter = 3
    divisible = False
    while len(list_premier) < n:
        for premier in list_premier:
            if premier <= sqrt(counter) and counter%premier == 0:
                divisible = True

        if divisible == False:
            list_premier.append(counter)
        counter += 1
        divisible = False

    return list_premier


if __name__ == '__main__':
    print(premier(500))
