# Hashtag("Hello there how are you doing")// would return "#HelloThereHowAreYouDoing"
# Hashtag("     Hello     World   ")// would return "#HelloWorld"
# Hashtag("") // would return False

def Hashtag (string):

    if string == '': # jika isinya kosong/'' maka False 
        print(False)
    elif len(string) > 140: # jika isinya >140 karakter maka False
        print(False)
    else:
        string1 = string.title() # mengubah huruf pertama setiap kata menjadi huruf capital
        string2 = string1.replace(' ','') # menghapus spasi
        
        return print('#'+string2) # jika selain itu maka kembalikan berupa print string nya dengan tambahan '#' di depan 

Hashtag("Hello there how are you doing")
Hashtag("     Hello     World   ")
Hashtag("")
