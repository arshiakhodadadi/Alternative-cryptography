# Alternative-cryptography
The code defines two functions: encrypt and decrypt.

Encryption (encrypt function):

It uses the Atbash cipher, a classical cipher that maps each letter of the alphabet to its reverse counterpart (e.g., 'A' ↔ 'Z', 'B' ↔ 'Y', ..., 'a' ↔ 'z').

The function iterates through each character in the input text:

If the character is an uppercase letter, it finds its index in the uppercase alphabet and replaces it with the corresponding letter from the reversed uppercase alphabet.

If the character is a lowercase letter, it performs a similar operation using the lowercase alphabets.

Non-alphabetic characters (like numbers, punctuation, spaces) are left unchanged.

Decryption (decrypt function):

Since the Atbash cipher is symmetric (applying it twice returns the original text), the decrypt function simply calls the encrypt function on the encrypted text.

User Interaction:

The program prompts the user to enter text to encrypt.

It then displays the encrypted output.

Subsequently, it decrypts the encrypted text and displays the original message.
