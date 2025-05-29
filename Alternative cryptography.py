def encrypt(text):  
 
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'  
    

    reverse_upper = alphabet_upper[::-1]  
    reverse_lower = alphabet_lower[::-1]  
    
    encrypted_text = ''  
    
    for char in text:  
        if char in alphabet_upper:  
     
            encrypted_text += reverse_upper[alphabet_upper.index(char)]  
        elif char in alphabet_lower:  
      
            encrypted_text += reverse_lower[alphabet_lower.index(char)]  
        else:  
           
            encrypted_text += char  
            
    return encrypted_text  

def decrypt(encrypted_text):  
   
    return encrypt(encrypted_text) 


input_text = input('Enter your text to encrypt: ')  
encrypted_output = encrypt(input_text)  
print('Encrypted output:', encrypted_output)  

decrypted_output = decrypt(encrypted_output)  
print('Decrypted output:', decrypted_output)   