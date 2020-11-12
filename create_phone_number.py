# create_phone_number([1,2,3,4,5,6,7,8,9,0])// would return "(123) 456-7890"

def create_phone_number(number):

    head = number[0:3] # slicing bagian kepala
    head = [str(i) for i in head] # membuat seluruh elemen menjadi string
    head = ''.join(head) # menggabungkan semua elemen dalam list menjadi 1
    
    body = number[3:6] # slicing bagian tengah 
    body = [str(i) for i in body] # membuat seluruh elemen menjadi string
    body = ''.join(body) # menggabungkan semua elemen dalam list menjadi 1

    tail = number[6:10] # slicing bagian belakang
    tail = [str(i) for i in tail] # membuat seluruh elemen menjadi string
    tail = ''.join(tail) # menggabungkan semua elemen dalam list menjadi 1

    return print('('+head+')',body+'-'+tail) # print dgn plus agar tidak ada spasi, dgn koma agar ada spasi

create_phone_number([1,2,3,4,5,6,7,8,9,0])

 