# hollowTriangle(4)// would return  
# ___#___
# __#_#__
# _#___#_
# #######

def hollowTriangle(height):

    for i in range(1,height+1):        # (baris) 1 2 3 4 , misal height=4
        for j in range(1,2*height):    # (kolom) 1 2 3 4 5 6 7 

            if i+j == height+1 or j-i == height-1 or i == height:
            # jika i+j == height+1 : untuk print # pada kolom j (# yg pertama)
            # jika j-i == height-1 : untuk print # pada kolom j (# yg kedua)
            # jika i == height : untuk baris terakhir, print # sejumlah j
                print('#',end='') # end='' untuk print horizontal

            else:
                print('_',end='') # jika tidak memenuhi syarat di atas, maka print '_'

        print() # untuk pindah baris

hollowTriangle(1)
hollowTriangle(2)
hollowTriangle(3)
hollowTriangle(4)
hollowTriangle(5)
hollowTriangle(6)