import sys
import os
import pandas as pd

# Note: We should remove the quote escape character while setting the User level System Environment Variable
# ALL_CHARS = '0123456789 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~'
# ENCODED_CHARS can be get using ''.join(random.sample(ALL_CHARS, len(ALL_CHARS)))

ALL_CHARS = os.environ['ALL_CHARS']
ENCODED_CHARS = os.environ['ENCODED_CHARS']
ENCODING_MAP = dict(zip(ALL_CHARS, ENCODED_CHARS))
DECODING_MAP = dict(zip(ENCODED_CHARS, ALL_CHARS))

def encode(original_text=''):
    if (original_text):
        encoded_text = ''
        encoded_chars = [ENCODING_MAP.get(char) for char in original_text]
        encoded_text = ''.join(encoded_chars)
        return encoded_text
    else:
        return None


def decode(encoded_text=''):
    if (encoded_text):
        original_text = ''
        original_chars = [DECODING_MAP.get(char) for char in encoded_text]
        original_text = ''.join(original_chars)
        return original_text
    else:
        return None

def encode_csv(original_file_path):
    df = pd.read_csv(original_file_path, header=None)
    df = df.where(pd.notnull(df), None)
    df = df.applymap(encode)
    df.to_csv('encoded.csv', index=False, header=False)
    print('encoded.csv file generated successfully')

def decode_csv(encoded_file_path):
    df = pd.read_csv(encoded_file_path, header=None)
    df = df.where(pd.notnull(df), None)
    df = df.applymap(decode)
    df.to_csv('original.csv', index=False, header=False)
    print('original.csv file generated successfully')

if __name__ == '__main__':
    run_again = True
    if len(sys.argv) > 2:
        if sys.argv[1].strip().lower() == 'e':
            print(encode(sys.argv[2].strip()))
        elif sys.argv[1].strip().lower() == 'd':
            print(decode(sys.argv[2].strip()))
        elif sys.argv[1].strip().lower() == 'ef':
            encode_csv(sys.argv[2].strip())        
        elif sys.argv[1].strip().lower() == 'df':
            decode_csv(sys.argv[2].strip())                   
        else:
            print("Encode or decode option not passed correctly")
    
    elif len(sys.argv) > 1:
        print('Runtime arguments not passed correctly')

    else:

        while(run_again):
            encode_or_decode = input("Encode or Decode? Enter 'e' for encode or 'd' for decode or \n"
                                    "'ef' for enconde csv file or 'df' for decode csv file: ").strip()
            input_value = input( "Enter your text/file_name: ").strip()
            if encode_or_decode == 'e':
                print(encode(input_value))
            elif encode_or_decode == 'd':
                print(decode(input_value))
            elif encode_or_decode == 'ef':
                encode_csv(input_value)
            elif encode_or_decode == 'df':
                decode_csv(input_value)
            else:
                print("Encode or decode option not passed correctly")
            
            run_again_inp = input("Want to run again? Enter 'y' or 1 to continue or 'n' or 0 to exit: ").strip().lower()
            run_again = True if(run_again_inp in ["y", "1"]) else False