import pyzipper
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', ';', ':', '"', "'", '<', '>', '?', ',', '.', '/', '`', '~']
known_password_dict = {'n':1, '_':2, '^':3, '`':5, 'W':6,'5':8}


kn=list(known_password_dict)                                                 # kn for converting the given password (which is in dictionary) to lists
kn.insert(3,'')                                                              # for inserting a temperory charecter which is missing to the password list,
kn.insert(6,'')                                                              # and manipulating it while bruteforcing.

for i in characters:                                                         # two for loops brute forcing each charecters with every charecters
    kn[3]=i
    for j in  characters :
        kn[6]=j

        k= ''.join(kn)                                                       # to convert the brute forced list to string
        file_name = '/home/harinandanan/Desktop/C^3/The_secret.zip'             
        
        try:                                                                  # try-except for continuing the program even when an error has occured
            with pyzipper.AESZipFile(file_name) as zf:
                zf.extractall(path='/home/harinandanan/Desktop/C^3', pwd = bytes(k, 'utf-8'))   # to extract all files from the given path using password 'pwd (converted into bytes)'
                print("Correct password:",k)
        except :
            print("failed:",k)

          