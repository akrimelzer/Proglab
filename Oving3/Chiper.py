from Oving3 import crypto_utils

class Chiper:

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

    def __init__(self, key, chiper):
        key = self.key
        chiper = self.chiper


    def set_key(self,key):
        self.key = key

    def get_key(self):
        return self.key

    def operate_chiper(self,text):
        return


#SUBKLASSE AV PERSON
class Sender(Person):

# ----------- Krypterer tekst ut i fra tilhørende chiper og key ----------------
    def operate_chiper(self,text):
        self.decoded_text = text
        self.encoded_text = self.chiper.encode(text,self.key)
        return self.encoded_text

# ----------- Dekrypterer tekst ut i fra tilhørende chiper og key ---------------

def send_chiper(self,reciever,text):





# SUBKLASSE AV PERSON
class Reciever(Person):



#SUBKLASSE AV CHIPER
class Caesar(Chiper):

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



class Multiplikativ(Chiper):

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


class Affine(Chiper):

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



class Unbreakable(Chiper):


















