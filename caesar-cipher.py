def cipher(text,number,direction):
     alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
     cp=""
     number=int(number)
     
     for l in text:
         if l in alphabet:  
            if direction == "encode":
                sp = (alphabet.index(l) + number) % len(alphabet) 
                cp += alphabet[sp]
            elif direction == "decode":
                sp = (alphabet.index(l) - number) % len(alphabet)  
                cp += alphabet[sp]
         else:
            cp += l
     print(cp)
def intro():
    direction=input("Enter you want to encode or decode?\n")
    text=input("Enter the text\n")
    number=input("Enter the shift number\n")
    cipher(text,number,direction)
    peel=input("Enter yes if you want to repeat the process else enter no\n")
    if peel=="yes":
        intro()
intro()
