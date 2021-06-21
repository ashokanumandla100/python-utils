import sys
import os

# Note: We should remove the quote escape character while setting the User level System Environment Variable
# ALL_CHARS = '0123456789 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~'
# ENCODED_CHARS can be get using ''.join(random.sample(ALL_CHARS, len(ALL_CHARS)))

ALL_CHARS = os.environ['ALL_CHARS']
ENCODED_CHARS = os.environ['ENCODED_CHARS']
ENCODING_MAP = dict(zip(ALL_CHARS, ENCODED_CHARS))
DECODING_MAP = dict(zip(ENCODED_CHARS, ALL_CHARS))

def encode(original_text=''):
    encoded_text = ''
    encoded_chars = [ENCODING_MAP.get(char) for char in original_text]
    encoded_text = ''.join(encoded_chars)
    
    return encoded_text


def decode(encoded_text=''):
    original_text = ''
    original_chars = [DECODING_MAP.get(char) for char in encoded_text]
    original_text = ''.join(original_chars)

    return original_text



if __name__ == '__main__':
    if len(sys.argv) > 2:
        if (sys.argv[1][0]).lower() == 'e':
            print(encode(sys.argv[2].strip()))
        elif (sys.argv[1][0]).lower() == 'd':
            print(decode(sys.argv[2].strip()))
        else:
            print("Encode or decode option not passed correctly")
    
    elif len(sys.argv) > 1:
        print('Runtime arguments not passed correctly')

    else:
        encode_or_decode = input("Encode or Decode? Enter 'e' for encode or 'd' for decode: ").strip()
        input_value = input( "Enter your text: ").strip()
        if encode_or_decode == 'e':
            print(encode(input_value))
        elif encode_or_decode == 'd':
            print(decode(input_value))
        else:
            print("Encode or decode option not passed correctly")