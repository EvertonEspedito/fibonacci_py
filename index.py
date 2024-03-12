def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

def pertence_fibonacci(num, fib):
    return num in fib

def main():
    n = int(input("Digite o número de termos da sequência de Fibonacci a serem calculados: "))
    fib = fibonacci(n)

    num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

    if pertence_fibonacci(num, fib):
        print(f"{num} pertence à sequência de Fibonacci.")
    else:
        print(f"{num} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
