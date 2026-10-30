while True:
    caracter = input("Introduce un caracter: ")

    if caracter == " ":
        break
    elif caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u" or caracter == "A" or caracter == "E" or caracter == "I" or caracter == "O" or caracter == "U":
        print("VOCAL")
    else:
        print("NO VOCAL")
