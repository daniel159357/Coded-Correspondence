letters="abcdefghijklmnopqrstuvwxyz"

#1 To decode
def caesar_decode(encrypted_message,offset):
  decrypted_message = ""
  for i in encrypted_message:
    if i in letters: #To check if the item is in the letters string
      position = letters.find(i) # To locate the index
      new_pos = (position + int(offset)) % 26 # for reverse-offset
      new_char = letters[new_pos] # To change back to string
      decrypted_message += new_char
    else: #To add i direct if it is not character
      decrypted_message += i 
  print("Your decrypted message is:\n")
  print(decrypted_message)
  print("***")

encrypted_message_1 = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
caesar_decode(encrypted_message_1,10)

#2 To encode
def caesar_encode(ori_message,offset):
  encrypted_message = ""
  for i in ori_message:
    if i in letters: #To check if the item is in the letters string
      position = letters.find(i) #finds the first index
      new_pos = (position - int(offset)) % 26 # for offset 
      new_char = letters[new_pos]
      encrypted_message += new_char
    else: #To add i direct if it is not character
      encrypted_message += i 
  print("Your encrypted message is:\n")
  print(encrypted_message)
  print("***")

ori_message_1 = "hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!"
caesar_encode(ori_message_1,8)

#3 two more coded messages
encrypted_message_2 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
caesar_decode(encrypted_message_2,10)

encrypted_message_3 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
caesar_decode(encrypted_message_3,14)


#4 Brute Force
encrypted_message_4 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
caesar_decode(encrypted_message_4,1)
caesar_decode(encrypted_message_4,2)
caesar_decode(encrypted_message_4,3)
caesar_decode(encrypted_message_4,4)
caesar_decode(encrypted_message_4,5)
caesar_decode(encrypted_message_4,6)
caesar_decode(encrypted_message_4,7) # the offset is 7

#5 Vigenere decode
#need to creat a key with space that align with encryped text
encrypted_message_5 = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"
keyword = "friends"



def vigenere_encrypt(plaintext, key):
    key = key.lower() # To use lowercase for key
    key_length = len(key) # To cal the key length
    key_as_int = [letters.find(i) for i in key] # To change key from str to int in a list
    plaintext = plaintext.lower() # To use lowercase for message
    ciphertext = ""
    
    j = 0 # The index of key
    for i in plaintext:
        if i.isalpha():
            shift = key_as_int[j % key_length] # To limit the key index within the length of key
            encrypted_int = (letters.find(i) - shift + 26) % 26 # the +26 is to avoid negative number
            encrypted_letter = letters[encrypted_int] # To change int back to str
            ciphertext += encrypted_letter
            j += 1 # To move to the next key character
        else:
            ciphertext += i
    return ciphertext


def vigenere_decrypt(plaintext, key):
    key = key.lower() 
    key_length = len(key) 
    key_as_int = [letters.find(i) for i in key] 
    plaintext = plaintext.lower() 
    ciphertext = ""
    
    j = 0
    for i in plaintext:
        if i.isalpha():
            shift = key_as_int[j % key_length] 
            decrypted_int = (letters.find(i) + shift + 26) % 26
            decrypted_letter = letters[decrypted_int]
            ciphertext += decrypted_letter
            j += 1
        else:
            ciphertext += i
    return ciphertext

print(vigenere_decrypt("txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!","friends"))






