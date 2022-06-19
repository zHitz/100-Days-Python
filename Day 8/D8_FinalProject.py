from D8_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
again = 1

def ceasar(plan_text, num_shift):
    cipher_text = ""
    num_shift = num_shift % 26 #if input > 26 (out of range)

    #choice direcion "decode" or "encode"
    if direction == "decode":
        num_shift *= -1 

    #    
    for letter in plan_text:
        #if leter(letter from plan_test user input) in alphabet  
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + num_shift
            if new_position > (int(len(alphabet))-1): #if new_position out of range in alphabet
                new_position = new_position - int(len(alphabet))
            cipher_text +=  alphabet[new_position]
        else:
            cipher_text += letter
    print(f"Here is the encoded result: {cipher_text}")    
 

while again == 1:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(plan_text=text, num_shift=shift)
    yes_no = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if yes_no == "no":
        again = 0
        print("Goodbye")


