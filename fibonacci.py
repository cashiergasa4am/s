import pandas as pd

def fibonacci_pandas():

    try:
        adim_sayisi = int(input("Kaç adım Fibonacci dizisi üretilsin?: "))
    except ValueError:
        print("Lütfen geçerli bir tam sayı girin.")
        return


    if adim_sayisi <= 0:
        print("Lütfen 0'dan büyük bir değer girin.")
        return


    fib_listesi = []
    

    for i in range(adim_sayisi):
        if i == 0:
            fib_listesi.append(0)
        elif i == 1:
            fib_listesi.append(1)
        else:
            fib_listesi.append(fib_listesi[-1] + fib_listesi[-2])
            

    df = pd.DataFrame({
        'Adım': range(1, adim_sayisi + 1),
        'Fibonacci Değeri': fib_listesi
    })
    

    return df


fibonacci_pandas()
