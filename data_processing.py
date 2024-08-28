import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os


# nltk.download('stopwords')
# nltk.download('wordnet')

output_directory = os.getcwd()

def clean_csv(input_file, output_file):
    try:
       
        df = pd.read_csv(input_file, sep=';', on_bad_lines='skip', encoding='latin1')

        num_rows_before = df.shape[0]
        print(f"File: {input_file}")
        print("Numarul de randuri inainte de curatarea setului de date: ", num_rows_before)

       
        df = df.drop_duplicates()
        df = df.dropna()

        
        def clean_text(text):
            
            text = text.lower()
           
            text = re.sub(r'[^a-z\s]', '', text)
            # Remove stopwords
            stop_words = set(stopwords.words('english'))
            text = ' '.join([word for word in text.split() if word not in stop_words])
            
            lemmatizer = WordNetLemmatizer()
            text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])
            return text

        df['comment'] = df['comment'].apply(clean_text)

        # Salvare fisier dupa normalizarea textului
        df.to_csv(output_file, sep=';', index=False)

        # Afisare randuri before/after normalizarea textului
        num_rows_after = df.shape[0]
        print("Numarul de randuri dupa curatarea setului de date: ", num_rows_after)
        print("Data cleaning completed. Noul set de date este:", output_file)
        print()

    except pd.errors.ParserError as e:
        print("ParserError:", e)

# fisierlee csv pe care le-am procesat 
file_paths = ['Data/new_data_sets/GooglePixelComments_2020_V2.csv','Data/new_data_sets/GooglePixelComments_2021_V2.csv', 'Data/new_data_sets/GooglePixelComments_2022_V2.csv', 'Data/new_data_sets/GooglePixelComments_2023_V2.csv']

# aplicarea functiilor de mai sus pt fiecare fisier
for file_path in file_paths:
    output_file = os.path.join(output_directory, 'cleaned' + os.path.basename(file_path))  # Output file path
    clean_csv(file_path, output_file)