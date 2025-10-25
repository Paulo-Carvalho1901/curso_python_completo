# Fibonacci

def fibonacci(n):
    """Retorna o n-ésimo número da sequência de Fibonacci."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Primeiros 10 números de Fibonacci
for i in range(10):
    print(fibonacci(i), end=" ")  # Saída: 0 1 1 2 3 5 8 13 21 34