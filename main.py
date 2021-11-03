def isPrime(x):
    '''
    determina daca un nr. este prim
    :param x: nr. intreg
    :return: True, daca x este prim sau False, in caz contrar
    '''

    if x < 2:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True

def is_palindrome(x):
    '''
    determina daca un nr. este palindrom
    :param x: nr. intreg
    :return: True daca nr. este palindrom sau False in caz contrar
    '''
    oglindit = 0
    copie_x = x
    while copie_x != 0:
        oglindit = oglindit * 10 + copie_x % 10
        copie_x = copie_x // 10
    if x == oglindit:
        return True
    return False

def all_are_palindrome(l):
    '''
    determina daca toate nr. din lista sunt palindroame
    :param l: lista de nr. intregi
    :return: True daca toate nr. din lista sunt palindroame sau False in caz contrar
    '''
    for x in l:
        if is_palindrome(x) is False:
            return False
    return True

def test_all_are_palindrome():
    assert all_are_palindrome([121,141,131]) is True
    assert all_are_palindrome([136,456,345]) is False

def get_longest_all_palindrome(l):
    '''
    determina cea mai lunga subsecventa de nr. care sunt palindroame
    :param l: lista de nr. intregi
    :return: cea mai lunga subsecventa de nr. care sunt palindroame
    '''
    subsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if all_are_palindrome(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventaMax):
                subsecventaMax = l[i:j + 1]
    return subsecventaMax

def test_get_longest_all_palindrome():
    assert get_longest_all_palindrome([145,121,131,234]) == [121,131]
    assert get_longest_all_palindrome([121,141,234,678]) == [121,141]

def all_digits_are_prime(l):
    '''
    determina daca toate nr. din lista au toate cifrele prime
    :param l: lista de nr. intregi
    :return: True daca toate nr. din l au toate cifrele prime sau False, in caz contrar
    '''
    ok=1
    for x in l:
        while x!=0:
            cifra=x%10
            if isPrime(cifra) is False:
                ok=0
            x=x//10
    if ok==1:
        return True
    return False


def test_all_digits_are_prime():
    assert all_digits_are_prime([33,77,55,53]) is True
    assert all_digits_are_prime([45,67,56,78]) is False



def get_longest_prime_digits(l):
    '''
    determina cea mai lunga subsecventa de nr. care au toate cifrele prime
    :param l: lista de nr. intregi
    :return: cea mai lunga subsecventa de nr. care au toate cifrele prime
    '''
    subsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if all_digits_are_prime(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventaMax):
                subsecventaMax = l[i:j + 1]
    return subsecventaMax

def test_get_longest_prime_digits():
    assert get_longest_prime_digits([33,77,56,90])==[33,77]
    assert get_longest_prime_digits([45,78,90])==[]
    assert get_longest_prime_digits([33,23,56,78,54,77])==[33,23]

def all_even(l):
    '''
    determina daca toate nr. din lista sunt pare
    :param l: lista de nr. intregi
    :return: True daca toate nr. din l sunt pare sau False, in caz contrar
    '''
    for x in l:
        if x % 2 != 0:
            return False
    return True

def test_all_even():
    assert all_even([2,4,6]) is True
    assert all_even([2,7,3]) is False


def get_longest_all_even(l):
    '''
    determina cea mai lunga subsecventa de nr. pare
    :param l: lista de nr. intregi
    :return: cea mai lunga subsecventa de nr. pare din l
    '''
    subsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if all_even(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventaMax):
                subsecventaMax = l[i:j + 1]
    return subsecventaMax

def test_get_longest_all_even():
    assert get_longest_all_even([2,4,7,8])==[2,4]
    assert get_longest_all_even([3,5,7,9])==[]
    assert get_longest_all_even([1,3,4,6,9])==[4,6]

def printMenu():
    print("1. Citire lista")
    print("2. Afisare cea mai lunga subsecventa de nr. pare")
    print("3. Afisare cea mai lunga subsecventa de nr. cu toate cifrele prime")
    print("4.Afisare cea mai lunga subsecventa de nr. care sunt palindroame")
    print("5. Iesire")

def citireLista():
    l = []
    givenString = input("Dati lista, cu elemente separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l

def main():
    test_all_even()
    test_get_longest_all_even()
    test_all_digits_are_prime()
    test_get_longest_prime_digits()
    test_all_are_palindrome()
    test_get_longest_all_palindrome()
    l = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(get_longest_all_even(l))
        elif optiune == "3":
            print(get_longest_prime_digits(l))
        elif optiune == "4":
            print(get_longest_all_palindrome(l))
        elif optiune == "5":
            break
        else:
            print("Optiune gresita! Reincercati!")

main()

