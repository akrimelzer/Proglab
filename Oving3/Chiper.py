__author__ = "Andreas Melzer"
import random

from Oving3 import crypto_utils

class Cipher:

    def __init__(self):
        self.alphabet = [chr(x) for x in range(32,127)]

    def encode(self,text, key):
        return

    def decode(self, text, key):
        return

    def verify(self,text, key):
        encode_text = self.encode(text, key)
        decode_text = self.decode(encode_text,key)
        return text == decode_text




# SUPERKLASSE PERON
class Person:

    def __init__(self, key, cipher):
        key = self.key
        cipher = self.cipher


    def set_key(self,key):
        self.key = key

    def get_key(self):
        return self.key

    def operate_cipher(self,text):
        return


#SUBKLASSE AV PERSON
class Sender(Person):

# ----------- Krypterer tekst ut i fra tilhørende cipher og key ----------------
    def operate_cipher(self,text):
        self.decoded_text = text
        self.encoded_text = self.cipher.encode(text,self.key)
        return self.encoded_text

# ----------- Dekrypterer tekst ut i fra tilhørende cipher og key ---------------

    def send_cipher(self,reciever,text):
        if isinstance(self.cipher,RSA):
            reciever.generate_keypairs()
            self.key = self.get_recievers_publickey(reciever)



    def get_recievers_publickey(self,reciever):
        return reciever.get_publickey()


    def get_encoded_text(self,text):
        return self.operate_cipher(text)


    def print_input(self):
        print("Sender:\nInput: " + str(self.decoded_text) + "\nEncoded text: " + str(self.encoded_text) + "\n")




#SUBKLASSE AV PERSON
class Reciever(Person):


    def operate_cipher(self,encoded_text):
        self.encoded_text = encoded_text
        self.decoded_text = self.cipher.decode(encoded_text, self.key)

        return self.decoded_text

    def recieve_cipher(self, encoded_text):
        self.operate_cipher(encoded_text)

    def get_publickey(self):
        return self.public_key

    def generate_keypairs(self):
        p, q = 0,0
        gcd_value = 2

        while p == q or gcd_value != 1:

            p = crypto_utils.generate_random_prime(8)
            q = crypto_utils.generate_random_prime(8)
            phi = (p-1)(q-1)
            e = random.randint(3,phi-1)

        n = p * q
        d = crypto_utils.modular_inverse(e, phi)


        #offentlig nøkkel
        self.public_key = (n,e)

        #privat nøkkel
        self.key = (n,d)

    def print_output(self):
        print("Reciever:\nEncoded text: "+ str(self.encoded_text)+ "\nDecoded text: "+str(self.decoded_text))







#SUBKLASSE AV CIPHER
class Caesar(Cipher):

    def encode(self,text, key):
        encode_text = ""

        for character in text:
            new_index = (self.alphabet.index(character)+key) % 95
            encode_text += self.alphabet[new_index]

        return encode_text

    def decode(self, text, key):

        decode_text = ""

        for character in text:
            new_index = (self.alphabet.index(character)-key) % 95
            decode_text = self.alphabet[new_index]

        return decode_text



class Multiplikativ(Cipher):

    def encode(self,text, key):
        encode_text = ""

        for character in text:
            new_index = (self.alphabet.index(character)*key) % 95
            encode_text += self.alphabet[new_index]

        return encode_text

    def decode(self, text, key):
        new_key = self.generate_inverted_key(key)
        decoded_text = self.encode(text, new_key)
        return decoded_text


    def generate_inverted_key(self, key):
        return crypto_utils.modular_inverse(key, 95)


class Affine(Cipher):

    def encode(self,text, key):
        multiplikativ = Multiplikativ()
        encoded_text_mult = multiplikativ.encode(text,key[0])


        caesar = Caesar()
        encodet_text = caesar.encode(encoded_text_mult, key[1])

        return encodet_text

    def decode(self, text, key):
        caesar = Caesar()
        decoded_text_caesar = caesar.decode(text,key[1])

        multiplikativ = Multiplikativ()
        decoded_text = multiplikativ.decode(decoded_text_caesar,key[0])
        return decoded_text



class Unbreakable(Cipher):

    def encode(self,text, key):

        i = 0
        encoded_text = ""

        for character in text:

            new_index = (self.alphabet.index(key[i % len(key)]) + self.alphabet.index(character)) % 95
            encoded_text += self.alphabet[new_index]
            i += 1

        return encoded_text

    def decode(self, text, key):

        new_key = self.generate_inverted_key(key)


        return self.encode(text, new_key)


    def generate_inverted_key(self,key):
        new_key = ""

        for character in key:
            new_key += self.alphabet[(95- self.alphabet.index(character)) % 95]

        return new_key




class RSA(Cipher):

    def encode(self,text, key):

        n, public_key = key

        blocks = crypto_utils.blocks_from_text(text,2)


        cipher = [pow(t, public_key, n) for t in blocks]
        return cipher


    def decode(self, text, key):
        n, private_key = key

        blocks = [pow(t,e,n) for t in text]
        decoded_text = crypto_utils.text_from_blocks(blocks,2)

        return decoded_text


    def check_gcd_previous_remainder(self,_a,_b):
        previous_remainder, remainder = _a,_b
        current_x, previous_x, current_y,previous_y = 0,1,1,0

        while remainder > 0:
            previous_remainder, (quotient, remainder) = remainder, divmod(previous_remainder, remainder)
            current_x, previous_x = previous_x - quotient * current_x, current_x
            current_y, previous_y = previous_y - quotient * current_y, current_y
        return previous_remainder




class Hacker(Person):

    def __init__(self, cipher):
        self.cipher = cipher
        self.create_wordbook()

    def create_wordbook(self):
        self.wordbook = [line.rstrip('\n') for line in open('english_words.txt')]


    def get_possibleKeys(self):
        if isinstance(self.cipher,Caesar):
            print("Decoding Caesar-cryptation\n")

            self.count = [0]*95

            return [x for x in range(0,95)]

        elif isinstance(self.cipher,Multiplikativ):
            print("Decoding Multiplicative-cryptation\n")

            self.count = [0]*9025


            return [(x,y) for x in range(0,95) for y in range(0,95)]


        elif isinstance(self.cipher,Unbreakable):
            print("Decoing Unbreakable-cryptation\n")

            self.count = [0]*len(self.wordbook)

            return "wordbook"


    def decode_text(self,text):































