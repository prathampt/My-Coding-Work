# Co-Decoder...

# DataBase... Mixed up...

low_alfa = '''abcdefghijklmnop qrstuvwxyzabcdefghijklmnop qrstuvwxyzabcdefghijklmnop qrstuvwxyzabcdefghijklmnop qrstuvwxyzabcdefghijklmnop qrstuvwxyzabcdefghijklmnop qrstuvwxyz'''
high_alfa = '''ABCDEFGHI.JKLMNOPQRSTUVWXYZABCDEFGHI.JKLMNOPQRSTUVWXYZABCDEFGHI.JKLMNOPQRSTUVWXYZABCDEFGHI.JKLMNOPQRSTUVWXYZABCDEFGHI.JKLMNOPQRSTUVWXYZABCDEFGHI.JKLMNOPQRSTUVWXYZ'''
nums = '''123?4567890123?4567890123?4567890123?4567890123?4567890123?4567890123?4567890123?4567890'''
syms = '''`~^*-,#!@$%&()_=+[]{};:'"\|<>/`~^*-,#!@$%&()_=+[]{};:'"\|<>/`~^*-,#!@$%&()_=+[]{};:'"\|<>/`~^*-,#!@$%&()_=+[]{};:'"\|<>/`~^*-,#!@$%&()_=+[]{};:'"\|<>/`~^*-,#!@$%&()_=+[]{};:'"\|<>/'''

import random

# Coder...

def Coder():
    user_txt = input("\n\nEnter the text to be Coded...\n")
    key1 = random.randint(7,15)
    key2 = low_alfa[key1-1]

    the_code = f'''{key2}'''

    for i in range(len(user_txt)):
        j = user_txt[i]
        if j in low_alfa:
            k = low_alfa.find(j)
            j = low_alfa[k+((-1)**i)*key1]
        elif j in high_alfa:
            k = high_alfa.find(j)
            j = high_alfa[k+key1]
        elif j in nums:
            k = nums.find(j)
            j = nums[k+key1]
        elif j in syms:
            k = syms.find(j)
            j = syms[k+key1]
        else:
            j = j

        the_code = the_code + j

    print(f"Your code is below this line... ** Please copy the whole line... **\n\n{the_code}\n\nYou can also find the code in 'Coder.txt'")
    with open("D:\Programming\Python\Coder.txt", "a") as p:
        p.write(f"\nNew code is : \n{the_code}")

# Decoder...

def Decoder():
    print("\n\nEnter your code into a text file named 'Decoder.txt'...\n    ** Please paste the whole text... **")
    input("\tPress Enter\n")

    with open("D:\Programming\Python\Decoder.txt", "r") as x:
        d_code = x.read()
    
    with open("D:\Programming\Python\Decoder.txt", "w") as f:
        f.write("")

    d_key1 = d_code[0]
    d_key2 = low_alfa.find(d_key1) + 1

    decoded_code = ''''''

    for p in range(1,len(d_code)):
        q = d_code[p]
        if q in low_alfa:
            r = low_alfa.find(q)
            q = low_alfa[r-((-1)**(p-1))*d_key2]
        elif q in high_alfa:
            r = high_alfa.find(q)
            q = high_alfa[r-d_key2]
        elif q in nums:
            r= nums.find(q)
            q = nums[r-d_key2]
        elif q in syms:
            r = syms.find(q)
            q = syms[r-d_key2]
        else:
            q = q

        decoded_code = decoded_code + q

    print("Your code is successfully decoded and is as follows...\n\n\t", decoded_code, "\n\nOr you cand find it in 'Decoded_Text_Only.txt'...")
    with open("D:\Programming\Python\Decoded_Text_Only.txt", "a") as x:
        text_decoded = f"\n\nYour decoded text is:\n\n{decoded_code}"
        x.write(text_decoded)

# Other...
if __name__=="__main__":

    user = input("\n\nType 'C' to use Coder or 'D' to use Decoder...\n")
    if user == 'c' or user == 'C':
        Coder()
    elif user == 'd' or user == 'D':
        Decoder()
    else:
        print("Thanks...")
