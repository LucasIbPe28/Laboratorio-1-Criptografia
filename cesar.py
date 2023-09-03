import sys

def cifrar_cesar(texto, corrimiento):
    texto_cifrado = ""
    for caracter in texto:
        if caracter.isalpha():
            mayuscula = caracter.isupper()
            caracter = caracter.lower()
            codigo = ord(caracter) - ord('a')
            codigo_cifrado = (codigo + corrimiento) % 26
            caracter_cifrado = chr(codigo_cifrado + ord('a'))
            if mayuscula:
                caracter_cifrado = caracter_cifrado.upper()
            texto_cifrado += caracter_cifrado
        else:
            texto_cifrado += caracter
    return texto_cifrado

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 cifrado_cesar.py <texto_a_cifrar> <corrimiento>")
        sys.exit(1)

    texto_a_cifrar = sys.argv[1]
    corrimiento = int(sys.argv[2])

    texto_cifrado = cifrar_cesar(texto_a_cifrar, corrimiento)
    print("Texto cifrado:", texto_cifrado)

