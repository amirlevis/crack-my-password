
import  sys
from itertools import  permutations
#encrypy  => byte to ascii             -> ascii_byte xor secret_key
#dycrypt  => ascii_byte xor secret_key -> ascii to byte

eng_letters = range(97, 123)


def xor_decrypt(encrypted_text, key) -> str: 
    return ''.join([ chr(d ^ ord(p)) for d, p in zip(encrypted_text, key * ((len(encrypted_text) // len(key)) + 1))])
    
def guess_key(encrypted_text, key_size):
    for possible_key in permutations(eng_letters, key_size):
        key =  ''.join(map(chr, possible_key))
        text = xor_decrypt(encrypted_text,key)
        yield key, text
  

if __name__ == '__main__':
    text = list(map(int, open('backend/encrypted.txt', 'r').read().split(',')))
    #key = guess_key(text, 3)
    print(xor_decrypt(text,'god'))
    