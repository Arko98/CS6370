import nltk
nltk.download('punkt')
nltk.download('wordnet')

Paragraph = "The president of India, officially the President of the Republic of India is the ceremonial head of state of India"

Tokenized = nltk.word_tokenize(Paragraph)
ps =  nltk.stem.PorterStemmer()
w_lemmatizer = nltk.stem.WordNetLemmatizer()

print('Tokenized: {}'.format(Tokenized))
print('\nStemmed: \n\n')
for w in Tokenized: 
    print(w, " : ", ps.stem(w))
print('\nLemmatized: \n\n') 

for w in Tokenized:
  print(w, " : ", w_lemmatizer.lemmatize(w)) 
