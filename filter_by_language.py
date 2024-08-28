import pandas as pd
from langdetect import detect, LangDetectException

# variabile pt input si output files
inputFile = 'combined_top_comments.csv'
outputFile = 'combined_top_comments.csv'

# verificare daca textul este in engleza
def language_check(text):
    try:
        # Check if text is a string
        if isinstance(text, str):
            return detect(text)
        else:
            return None  
    except LangDetectException:
        return None

# citire fisier csv cu separator ; si ecnocind in latin1
df = pd.read_csv(inputFile, sep=';', on_bad_lines='skip', encoding='latin1')

# creare coloana pt limba
df['language'] = df['comment'].apply(language_check)

# filtrare dupa limba, in cazul nostru engleza
df_english = df[df['language'] == 'en']

# stergere coloana creata
df_english = df_english.drop(columns=['language'])

# Salvare fisier
df_english.to_csv(outputFile, index=False, sep=';')