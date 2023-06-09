def toBinary(s):                                          # Function for converting the strings to binary for doing XOR
    res = ''.join(format(ord(i), '08b') for i in s)         
    return res
def xor(a, b, n):                                         # Function for decrypting OTP by doing XOR
    
    ans = ""
    repetitions = 1 + (len(a) // len(b))                  # To do XOR both the strings should be of equal length
    b = b * repetitions                                   #  but the length of key is less than enc text,so repetioin is done to the key 

    for i in range(n):                                    # this for loop does the main task: bitwise XORing
        if (a[i] == b[i]):
            ans += "0"
        else:
            ans += "1"
    
    bytes_= []
    for i in range(0, len(ans), 8):                       # Converting the result which is binary into bytes for converting to ascii  charecters
        bytes_.append(ans[i:i+8])
        
    ascii_chars = ""                                      
    for i in bytes_:                                      # Converting to ASCII and joining the the charecters to get the coordinates
        ascii_chars += chr(int(i, 2))    
    
    return ascii_chars

enc_text=toBinary("|OP`Z<E]|Y\$")
key=toBinary("Jai Shree Ram!")

n = len(enc_text)
c = xor(enc_text, key, n)
print(c)