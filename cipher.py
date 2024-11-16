input_text = input("Please Enter a Sentence- ")


input_text = input_text.lower()


encrypted_text = "" #An empty string
shift_value = 5 #Shift value

for char in input_text:

  if('a'<= char <='z'):
    new_character = chr((ord(char) - ord('a') + shift_value) % 26 + ord('a'))
    encrypted_text=encrypted_text + new_character
  else:
    encrypted_text+=char


print("The entered sentence is:\n",input_text)
print("The encrypted sentence is:\n",encrypted_text)
