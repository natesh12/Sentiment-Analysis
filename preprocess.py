import re
import nltk
nltk.download('stopwords') #stop Words in English
nltk.download('wordnet') #Vocabulary for Lemmatization
nltk.download('punkt') #Tokenizer Rules
nltk.download('punkt_tab')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))
lemmatizer=WordNetLemmatizer()

def preprocess(text):
  text = text.lower()
#Remove punctuations,numbers
  text = re.sub(r"[^a-z\s]","",text)
#Tokenize the review: convert sentence into words
  tokens = word_tokenize(text)
#Remove stop words
  
  tokens= [token for token in tokens if token not in stop_words]

#Lemmatization
  
  tokens = [lemmatizer.lemmatize(token) for token in tokens]

#Join tokens back to string
  return" ".join(tokens)

if __name__=="__main__":
 print(__name__)
 print(preprocess("The product was really good!!!"))