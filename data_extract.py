import os
from tqdm import tqdm #Decorator for loop to show progress
import lzma
# Get all files directory
def xz_ext(dir):
    file = []
    for filename in os.listdir(dir):
        if os.path.isfile(os.path.join(dir,filename)) and filename.endswith('.xz'):
            file.append(filename)
    return file

# Initialize location
loc = """D:\dev\LLM Tutorial\openwebtext"""

# Create train test file
output_file = ['output_train.txt','output_val.txt']
# Create vocab file
vocab_text = 'vocab.txt'

# Get list of files directory
files = xz_ext(loc)
# Get length of files directory
total_files = len(files)

# Train Test Split
split_data = int(total_files*0.9)

# Get Unique character
vocab = set()

# Write file
for i in output_file:    
    # Get train if i is train, else test
    file_type = files[:split_data] if 'train' in i else files[split_data:]
    file_length =  len(file_type)
    
    with open(i,'w',encoding='utf-8') as outfile:
        
        # Loop Through file and show the progress
        for count, filename in enumerate(tqdm(file_type, total=file_length)):            
            # Get filename path
            filepath = os.path.join(loc,filename)
            
            # Read xz file in text format
            with lzma.open(filepath,'rt',encoding='utf-8') as infile:
                text = infile.read()
                outfile.write(text)
                character = set(text)
                vocab.update(character)

with open(vocab_text,'w',encoding='utf-8') as vcab:
    
    for char in vocab:
        vcab.write(char +'\n')