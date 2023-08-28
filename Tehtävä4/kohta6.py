import random

def likiarvo(luvut):
    x = random.uniform(1, -1)
    y = random.uniform(1, -1)

    i = 0

    if x**2 + y**2 <= 1:
        i += 1

    likiarvo = 4 * i / luvut
    return likiarvo

def main():
    luvut = int(input("Montako pistettä? "))

    if luvut <= 0:
        print("Virheellinen arvo")

    else:
        print("Piin likiarvo on", likiarvo(luvut))

if __name__ == "__main__":
    main()