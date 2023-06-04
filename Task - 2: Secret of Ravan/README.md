# Task - 2: Secret of Ravan

## Challenge Description
Ram discovers that Ravan has a single weakness, and to defeat him, Ram needs to know this weakness.<br />
Ram learns that the secret to Ravan's weakness is hidden in a locked box, which can only be opened with a special password.<br />
Vibhishan knows that the password is a combination of 8 characters that include numbers, letters and special characters, but he only knows 6 of them.<br />
Can you find the password through brute force so that Ram can open the box?<br />
Write a Python program for brute-forcing.

## Solution 
- Downloaded the zipped folder `The_secret.zip` from the repository.
- Installed pyzipper in linux
```
pip install pyzipper
```
-Downloaded the given python file `Task - 02.py` and from the file we can see the known password with missing charecters to be found using bruteforce , for extracting the contents of the zip file.
```
n_^{*}`W{*}5
```
#### Code:

Given below is the updated code of the python file `Task - 02.py` capable of bruteforcing and extracting file from the zipped foler using pyzipper

```
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
                zf.extractall(path='/home/harinandanan/Desktop/C^3', pwd = bytes(k, 'utf-8'))   # to extract all files from the given path using password 'pwd (converted                                                                                                                                                              into bytes)'
                print("Correct password:",k)                                   
        except :
            print("failed:",k)
```


- `import pyzipper` is used for adding the pyzipper library to the code.
- We can see in the code a set of charecters given as list named charecters (these are the charecters used for brute forcing) and also a dictionary that contains the incomplete password pass.
- The dictionary *known_password* is converted to a list *kn* as list it is more familiar and ordered.`kn=list(known_password_dict)`
- As two letters are missing in the list there is only 6 elements in the list so we are adding 2 temporary space to thes list in the 3rd and 6th index of the list
- two for loops for brute forcing each charecters with every charecters so it can check every possiblities, and the brute forced result is converted from list to strings using `''join.(kn)`
- try-except for continuing the program even when an error has occured
- `zf.extractall(path='/home/harinandanan/Desktop/C^3', pwd = bytes(k, 'utf-8'))` extracts all files from the given path using password *pwd* (converted into bytes)

#### Result
After running the above bruteforcing code, 
The extracted folder can be seen in the directory where the python file is saved.

![Screenshot from 2023-06-04 13-59-06](https://github.com/HarinandanAM/C-Cube-Recruitment-23/assets/116416113/55b719a3-0e21-4479-93e5-b0665ef28cc6)

Now we can get into the *password* directory and open the file named *Hint.txt* that contains secret information.

![Screenshot from 2023-06-04 14-00-23](https://github.com/HarinandanAM/C-Cube-Recruitment-23/assets/116416113/44b76661-999d-4d7e-baa4-385cf1f98965) 

To find which was the correct we can grep the correct password from the output of python file.

![Uploading Screenshot from 2023-06-04 14-12-05.png…]()

**Correct password: n_^1`Wa5**
