import json

dico_test = {"Fleur": 3, "Prénom": "Charles"}

# lis un fichier json et stock tout dans un dico d'objet data
def readFileData(filename):
    data = {}
    try:
        with open(filename) as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Fichier introuvable.")
    except IOError:
        print("Erreur IO.")
    return data


def writeFileData(filename, dico):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(json.dumps(dico))
            file.close()
    except FileNotFoundError:
        print("Fichier introuvable.")
    except IOError:
        print("Erreur IO.")


writeFileData("test.txt", dico_test)

print(readFileData("test.txt"))
