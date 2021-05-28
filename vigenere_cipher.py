'''matrix creation'''
def matrix_creation():     
        alphabet='abcdefghijklmnopqrstuvwxyz'
        matrix=[]
        for i in range(26):
                row=[]
                for j in range(26):
                        x=i+j
                        if(x>=26):
                                x=x%26
                        row.append(alphabet[x])
                matrix.append(row)
        return matrix
    
'''display created matrix'''
def display(x):
        for i in range(len(x)):
                print(x[i])
                
'''encrypting plain text to cipher text'''
def encrypt(t,k,matrix):
        '''CONVERTING TO UPPERCASE'''
        t=t.upper()
        '''print(t)'''
        k=k.upper()
        '''print(k)'''
        to_encrypt=[]
        num_spaces=0
        key_arr=[]
        '''Array for plaintext with spaces incl'''
        for i in range(len(t)):
                to_encrypt.append(t[i])
        '''print(to_encrypt)'''
        '''COUNT NUM OF SPACES'''
        for j in range(len(t)):
                if(t[j]==' '):
                        num_spaces+=1
        ''' creating key matrix with appropriate repitions'''
        for i in range(len(t)-num_spaces):
                if(i >= len(k)):
                        i=i%len(k)
                key_arr.append(k[i])
        '''print(key_arr)'''
        '''print("Number of spaces in the plaintext entered:",num_spaces)'''
        match=[]
        match.append(to_encrypt)
        match.append(key_arr)
        '''print("How the plaintext and key are being matched:",match)'''
        '''print(match[0])
        print(match[1])'''
        encrypted=[]
        count=0
        for i in range(len(to_encrypt)):
                        if(to_encrypt[i]!=' '):
                                count+=1
                                row_i=to_encrypt[i]                                       
                                col_i=key_arr[count-1]
                                '''print(row_i)
                                print(col_i)'''
                                row_i=ord(row_i)-65
                                col_i=ord(col_i)-65
                                '''print(row_i)
                                print(col_i)'''
                                encrypted_char=matrix[row_i][col_i]
                                encrypted.append(encrypted_char)
                        else:
                                encrypted_char=' '
                                encrypted.append(encrypted_char)
        '''print(encrypted)'''
        encry=''
        for i in encrypted:
                encry+=i
        encry=encry.upper()
        '''print(encry)'''
        return encry

def encrypt_no_spaces1(t,k,matrix):
        '''CONVERTING TO UPPERCASE'''
        t=t.upper()
        '''print(t)'''
        k=k.upper()
        '''print(k)'''
        to_encrypt=[]
        num_spaces=0
        key_arr=[]
        '''Array for plaintext with spaces incl'''
        for i in range(len(t)):
                to_encrypt.append(t[i])
        '''print(to_encrypt)'''
        '''COUNT NUM OF SPACES'''
        for j in range(len(t)):
                if(t[j]==' '):
                        num_spaces+=1
        ''' creating key matrix with appropriate repitions'''
        for i in range(len(t)-num_spaces):
                if(i >= len(k)):
                        i=i%len(k)
                key_arr.append(k[i])
        '''print(key_arr)'''
        '''print("Number of spaces in the plaintext entered:",num_spaces)'''
        match=[]
        match.append(to_encrypt)
        match.append(key_arr)
        '''print("How the plaintext and key are being matched:",match)'''
        '''print(match[0])
        print(match[1])'''
        encrypted=[]
        count=0
        for i in range(len(to_encrypt)):
                        if(to_encrypt[i]!=' '):
                                count+=1
                                row_i=to_encrypt[i]                                       
                                col_i=key_arr[count-1]
                                '''print(row_i)
                                print(col_i)'''
                                row_i=ord(row_i)-65
                                col_i=ord(col_i)-65
                                '''print(row_i)
                                print(col_i)'''
                                encrypted_char=matrix[row_i][col_i]
                                encrypted.append(encrypted_char)
                                '''print(encrypted)'''
        encry=''
        for i in encrypted:
                encry+=i
        encry=encry.upper()
        '''print(encry)'''
        return encry

def encryption_addition(t,k,matrix):
        '''CONVERTING TO UPPERCASE'''
        t=t.upper()
        '''print(t)'''
        k=k.upper()
        '''print(k)'''
        to_encrypt=[]
        num_spaces=0
        key_arr=[]
        '''Array for plaintext with spaces incl'''
        for i in range(len(t)):
                to_encrypt.append(t[i])
        '''print(to_encrypt)'''
        '''COUNT NUM OF SPACES'''
        for j in range(len(t)):
                if(t[j]==' '):
                        num_spaces+=1
        ''' creating key matrix with appropriate repitions'''
        for i in range(len(t)-num_spaces):
                if(i >= len(k)):
                        i=i%len(k)
                key_arr.append(k[i])
        '''print(key_arr)'''
        '''print("Number of spaces in the plaintext entered:",num_spaces)'''
        match=[]
        match.append(to_encrypt)
        match.append(key_arr)
        '''print("How the plaintext and key are being matched:",match)'''
        '''print(match[0])
        print(match[1])'''
        encrypted=[]
        count=0
        for i in range(len(to_encrypt)):
                        if(to_encrypt[i]!=' '):
                                count+=1
                                row_i=to_encrypt[i]                                       
                                col_i=key_arr[count-1]
                                '''print(row_i)
                                print(col_i)'''
                                row_i=ord(row_i)-65
                                col_i=ord(col_i)-65
                                encrypted_char= row_i + col_i
                                if(encrypted_char>25):
                                        encrypted_char=encrypted_char%26
                                encrypted_char=encrypted_char+65
                                encrypted_char=chr(encrypted_char)
                                encrypted.append(encrypted_char)
                        else:
                                encrypted_char=' '
                                encrypted.append(encrypted_char)
        '''print(encrypted)'''
        encry=''
        for i in encrypted:
                encry+=i
        encry=encry.upper()
        '''print(encry)'''
        return encry

def decryption(t, k):
        '''CONVERTING TO UPPERCASE'''
        t=t.upper()
        '''print(t)'''
        k=k.upper()
        '''print(k)'''
        to_decrypt=[]
        num_spaces=0
        key_arr=[]
        '''Array for plaintext with spaces incl'''
        for i in range(len(t)):
                to_decrypt.append(t[i])
        '''print(to_encrypt)'''
        '''COUNT NUM OF SPACES'''
        for j in range(len(t)):
                if(t[j]==' '):
                        num_spaces+=1
        ''' creating key matrix with appropriate repitions'''
        for i in range(len(t)-num_spaces):
                if(i >= len(k)):
                        i=i%len(k)
                key_arr.append(k[i])
        '''print(key_arr)'''
        '''print("Number of spaces in the plaintext entered:",num_spaces)'''
        match=[]
        match.append(to_decrypt)
        match.append(key_arr)
        '''print("How the plaintext and key are being matched:",match)'''
        '''print(match[0])
        print(match[1])'''
        #print(match)
        decrypted=[]
        count=0
        for i in range(len(to_decrypt)):
                        if(to_decrypt[i]!=' '):
                                count+=1
                                row_i=to_decrypt[i]                                       
                                col_i=key_arr[count-1]
                                '''print(row_i)
                                print(col_i)'''
                                row_i=ord(row_i)
                                col_i=ord(col_i)
                                decrypted_char = row_i - col_i
                                if(decrypted_char<0):
                                        decrypted_char=decrypted_char+91
                                else:
                                        decrypted_char=decrypted_char+65
                                #print(decrypted_char)
                                decrypted_char=chr(decrypted_char)
                                decrypted.append(decrypted_char)
                        else:
                                decrypted_char=' '
                                decrypted.append(decrypted_char)
        '''print(encrypted)'''
        decry=''
        for i in decrypted:
                decry+=i
        decry=decry.upper()
        '''print(encry)'''
        return decry

matrix=matrix_creation()
'''display(matrix)'''
select=input("Press E to encrypt or D to decrypt: ")
if select=="e":
    plaintext=input("Enter plain text:")
    key=input("Enter key: ")
    ciphertext1=encryption_addition(plaintext,key,matrix)
    print("\nEncrypted text:",ciphertext1)
elif select=="d":
    ciphertext=input("Enter cipher text:")
    key=input("Enter key: ")
    plaintext1=decryption(ciphertext,key)
    print("\nDecrypted text:",plaintext1)
'''ciphertext2=encrypt_no_spaces1(plaintext,key,matrix)
ciphertext3=encryption_addition(plaintext,key,matrix)
print(ciphertext1)
print(ciphertext2)
print(ciphertext3)'''
