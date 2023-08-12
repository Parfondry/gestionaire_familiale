def add_user():
    name = input("Veuillez entrer votre nom :")
    if not type(name) is str:
        raise TypeError("Pas une chaine de caractere")
    role = str(input("Veuillez entrer le role :"))
    if not type(name) is str:
        raise TypeError("Pas une chaine de caractere")
    point = 0
    print(type(name))
    users = []
    users = [name, role, point]

    return users

print(add_user())