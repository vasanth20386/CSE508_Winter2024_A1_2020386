import os
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download the necessary NLTK datasets
nltk.download('punkt')
nltk.download('stopwords')

# Set the path to your dataset directory
dataset_directory = 'text_files'

# Function to preprocess a single file
def preprocess_file(file_path):
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Lowercase the text
    text = text.lower()
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove punctuation from tokens
    table = str.maketrans('', '', string.punctuation)
    stripped_tokens = [w.translate(table) for w in tokens]
    
    # Remove non-alphabetic tokens and stopwords
    stopped_tokens = [word for word in stripped_tokens if word.isalpha()]
    stopwords_set = set(stopwords.words('english'))
    words = [w for w in stopped_tokens if not w in stopwords_set]
    
    # Remove blank space tokens, if any remain
    words = [word for word in words if word.strip() != '']
    
    return words

# Process all files in the dataset
for filename in os.listdir(dataset_directory):
    file_path = os.path.join(dataset_directory, filename)
    if os.path.isfile(file_path):
        processed_words = preprocess_file(file_path)
        # Here you could write the processed_words back to a file or continue processing
        print(f'Processed {filename}: {processed_words}')

# Make sure to replace 'path/to/your/dataset' with the actual path to your dataset directory.
