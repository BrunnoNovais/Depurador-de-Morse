def lin():
    print('-' * 40)


def continuar(frase):
    texto1 = frase
    texto = f'  {texto1}  '
    texto = texto.replace(" .- ", "a")
    texto = texto.replace(" -... ", "b")
    texto = texto.replace(" -.-. ", "c")
    texto = texto.replace(" -.. ", "d")
    texto = texto.replace(" . ", "e")
    texto = texto.replace(" ..-. ", "f")
    texto = texto.replace(" --. ", "g")
    texto = texto.replace(" .... ", "h")
    texto = texto.replace(" .. ", "i")
    texto = texto.replace(" .--- ", "j")
    texto = texto.replace(" -.- ", "k")
    texto = texto.replace(" .-.. ", "l")
    texto = texto.replace(" -- ", "m")
    texto = texto.replace(" -. ", "n")
    texto = texto.replace(" --- ", "o")
    texto = texto.replace(" .--. ", "p")
    texto = texto.replace(" --.- ", "q")
    texto = texto.replace(" .-. ", "r")
    texto = texto.replace(" ... ", "s")
    texto = texto.replace(" - ", "t")
    texto = texto.replace("..- ", "u")
    texto = texto.replace(" ...- ", "v")
    texto = texto.replace(" .-- ", "w")
    texto = texto.replace(" -..- ", "x")
    texto = texto.replace(" -.-- ", "y")
    texto = texto.replace(" --.. ", "z")
    texto = texto.replace(" / ", " ")
    texto.strip()
    print(texto)


def codificar():
    texto = input('Texto para morse: ')
    texto = texto.lower()
    texto = texto.replace(" ", " / ")
    texto = texto.replace("a", " .- ")
    texto = texto.replace("b", " -... ")
    texto = texto.replace("c", " -.-. ")
    texto = texto.replace("d", " -.. ")
    texto = texto.replace("e", " . ")
    texto = texto.replace("f", " ..-. ")
    texto = texto.replace("g", " --. ")
    texto = texto.replace("h", " .... ")
    texto = texto.replace("i", " .. ")
    texto = texto.replace("j", " .--- ")
    texto = texto.replace("k", " -.- ")
    texto = texto.replace("l", " .-.. ")
    texto = texto.replace("m", " -- ")
    texto = texto.replace("n", " -. ")
    texto = texto.replace("o", " --- ")
    texto = texto.replace("p", " .--. ")
    texto = texto.replace("q", " --.- ")
    texto = texto.replace("r", " .-. ")
    texto = texto.replace("s", " ... ")
    texto = texto.replace("t", " - ")
    texto = texto.replace("u", " ..- ")
    texto = texto.replace("v", " ...- ")
    texto = texto.replace("w", ".-- ")
    texto = texto.replace("x", " -..- ")
    texto = texto.replace("y", " -.-- ")
    texto = texto.replace("z", " --.. ")
    texto = texto.strip()
    print(texto)
    return texto


def decodificar():
    texto1 = str(input('Texto para morse: ')).lower().strip()
    texto = f'  {texto1}  '
    texto = texto.replace(" .- ", "a")
    texto = texto.replace(" -... ", "b")
    texto = texto.replace(" -.-. ", "c")
    texto = texto.replace(" -.. ", "d")
    texto = texto.replace(" . ", "e")
    texto = texto.replace(" ..-. ", "f")
    texto = texto.replace(" --. ", "g")
    texto = texto.replace(" .... ", "h")
    texto = texto.replace(" .. ", "i")
    texto = texto.replace(" .--- ", "j")
    texto = texto.replace(" -.- ", "k")
    texto = texto.replace(" .-.. ", "l")
    texto = texto.replace(" -- ", "m")
    texto = texto.replace(" -. ", "n")
    texto = texto.replace(" --- ", "o")
    texto = texto.replace(" .--. ", "p")
    texto = texto.replace(" --.- ", "q")
    texto = texto.replace(" .-. ", "r")
    texto = texto.replace(" ... ", "s")
    texto = texto.replace(" - ", "t")
    texto = texto.replace("..- ", "u")
    texto = texto.replace(" ...- ", "v")
    texto = texto.replace(" .-- ", "w")
    texto = texto.replace(" -..- ", "x")
    texto = texto.replace(" -.-- ", "y")
    texto = texto.replace(" --.. ", "z")
    texto = texto.replace(" / ", " ")
    texto.strip()
    print(texto)


lin()
print('''Codifique ou Decodifique Para Morse!!!
1 - Codificar
2 - Decodificar
3 - Sair''')
while True:
    x = int(input('>> '))
    lin()

    if x == 1:
        frase = codificar()
        while True:
            escolha = str(input('Deseja Decodificar o Código? [S / N] \n> ')).lower().strip()[0]
            if escolha in 's':
                continuar(frase=frase)
                break
            elif escolha in 'n':
                break
        break
    elif x == 2:
        decodificar()
        break
    elif x == 3:
        break
    print('Digite Um dos Numeros Acima!')
    lin()
