# sort_odd_even([5, 3, 2, 8, 1, 4]) // would return [1, 3, 8, 4, 5, 2]
# odd numbers ascending: [1, 3,    5, ] ( Odds number in the index 0, 1, and 4)
# even numbers descending: [    8, 4,  2] (Evens number in the index 2,3, and 5)

def sort_odd_even (num):

    indexEven = []  # membuat list kosong untuk diisi dgn index dari angka genap
    even = []       # membuat list kosong untuk diisi dgn angka genap
    indexOdd = []   # membuat list kosong untuk diisi dgn index dari angka ganjil
    odd = []        # membuat list kosong untuk diisi dgn angka ganjil

    for i in range(len(num)):  
      if num[i]%2 == 1:         # mencari angka ganjil 
        indexOdd.append(i)      # 0 1 4 (index dari angka ganjil dimasukkan ke list indexOdd)
        odd.append(num[i])      # 5 3 1 (angka ganjil dimasukkan ke list odd)

    odd.sort(reverse=False)     # 1 3 5 (angka ganjil diurutkan dari angka paling kecil)

    for i in range(len(indexOdd)): 
      num[indexOdd[i]] = odd[i] # memasukkan angka ganjil yg sudah berurut ke dlm index tertentu

    for i in range(len(num)):
      if num[i]%2 ==0:          # mencari angka genap
        indexEven.append(i)     # 2 3 5 (index dari angka genap dimasukkan ke list indexEven)
        even.append(num[i])     # 2 8 4 (angka genap dimasukkan ke list even)

    even.sort(reverse=True)     # 8 4 2 (angka genap diurutkan dari angka paling besar)

    for i in range(len(indexEven)):
      num[indexEven[i]] = even[i] # memasukkan angka genap yg sudah berurut ke dlm index tertentu
    
    return print(num) # mengembalikan nilai fungsinya berupa print num yg sudah berubah

sort_odd_even([5, 3, 2, 8, 1, 4])


