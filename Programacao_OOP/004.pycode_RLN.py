def fact(n):
    if n<= 1:
        return 1
    return n * fact(n - 1)

def main():
    numb = 998
    result = fact(numb)
    # A partir do numb2 == 999, gera um exception
    numb2 = 998
    print(f"Fatorial de {numb} é {result}")
    print(f"Fatorial de {numb2} é {fact(numb2)}")

if __name__ == "__main__":
    main()