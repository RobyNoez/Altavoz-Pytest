from altavoz import Altavoz


def main() -> None:
    altavoz = Altavoz("Salón", 30)

    print(altavoz.nombre)
    print(altavoz.volumen)
    print(altavoz.estado)

    print(altavoz.nombre)
    print(altavoz.volumen)
    print(altavoz.estado)


if __name__ == "__main__":
    main()
