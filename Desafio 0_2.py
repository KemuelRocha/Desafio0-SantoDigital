def fibonacci(N):
    ult = 1
    penul = 1

    if (N == 1) or (N == 2):
        return(1)
    else:
        for count in range(2,N):
            termo = ult + penul
            penul = ult
            ult = termo
            count += 1
        return(termo)

def get_dois_ultimos(fib):
    resultado = fib % 100
    return(resultado)


N = int(input())
fibo = fibonacci(N)
dois_ultimos = get_dois_ultimos(fibo)
print(dois_ultimos)