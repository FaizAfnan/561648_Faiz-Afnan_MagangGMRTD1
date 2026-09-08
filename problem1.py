#Program by : Faiz Afnan
#unfinished

k = int(input("k = "))
n = int(input("n = "))
m = int(input("m = "))
        
def langkah(n, m):
    # tidak mungkin
    if n == 0:
        return 0
    if m == 0:
        return None  
    #brp x robot membawa muatan ful
    q = n//m
    #sisa barang setelah dibawa muatan penuh
    r = n%m
    #apakah semua barang terbagi habis
    if r == 0:
        return 4*q
    elif 2 * r <= m:
        return 4*q+3
    else:
        return 4*q+4

def hitungan(n, m, k):
    if n % 3 != 0 or m % 3 != 0:
        return -1
    #biar sama rata
    a = n // 3
    b = m // 3
    #maks 2kg dan 1kg
    K2 = k // 2  
    K1 = k // 1   
    #L 2 kg dan 1 kg
    L2 = langkah(a, K2) 
    if L2 is None:
        return -1
    L1 = langkah(b, K1)
    if L1 is None:
        return -1
    return L2 + L1

print(hitungan(n, m, k))