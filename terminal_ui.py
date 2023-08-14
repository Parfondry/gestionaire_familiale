def another_function():
    try:
        user_input = int(input("Entrez un nombre : "))
        return user_input  # Retourne la valeur en cas de succès
    except ValueError:
        print("Erreur : l'entrée doit être un nombre entier")
        return another_function()  # Appel récursif en cas d'erreur

def recursive_function():
    value = another_function()  # Appelle la fonction "another_function"
    # Effectuez d'autres opérations ici si nécessaire
    return value  # Renvoie la valeur retournée par "another_function"

result = recursive_function()
print("Résultat :", result)