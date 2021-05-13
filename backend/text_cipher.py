
import  sys
from itertools import  permutations
#encrypy  => byte to ascii             -> ascii_byte xor secret_key
#dycrypt  => ascii_byte xor secret_key -> ascii to byte

key_letters = 'abcdefghijklmnopqrstuvwxyz'

def xor_decrypt(encrypted_text, key): 
    text = ''.join([ chr(d ^ ord(p)) for d, p in zip(encrypted_text, key * (len(key) + 1))])
    return text
    #return sum(x^y for x, y in zip(encrypted_text, key*(len(encrypted_text)//len(key)+1)))
    



def guess_key(encrypted_text, key_size):
    key = None
    data_length = (len(encrypted_text) // key_size) + 1
    #a = []
    for possible_keys in permutations('ab', key_size):
        possible_text = ''.join([ chr(d ^ ord(p)) for d, p in zip(encrypted_text, possible_keys * data_length)])
        key = sum([ord(c) for c in possible_text])
        print(possible_text)
        print(key)
        
  
    return key

   

if __name__ == '__main__':
    text = list(map(int, open('backend/encrypted.txt', 'r').read().split(',')))
    #key = guess_key(text, 3)
    print(xor_decrypt(text,'god'))
    