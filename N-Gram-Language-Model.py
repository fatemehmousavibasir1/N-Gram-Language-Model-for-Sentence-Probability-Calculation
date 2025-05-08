from nltk import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter
import re
import hazm



with open('hamshahri.txt', 'r', encoding='utf-8') as file:
     data = file.read()
data= re.sub(r'\\u200c', ' ', data)
data= re.sub(r'\u200c', ' ', data)


normalizer = hazm.Normalizer()
data=normalizer.normalize(data)

lemmatizer=hazm.Lemmatizer()
data=lemmatizer.lemmatize(data)

stemmer=hazm.Stemmer()
deta=stemmer.stem(data)

data=word_tokenize(data)



def calculate_probability(sentence, Count_N_gram, total):
    words = word_tokenize(sentence)
    sentence_probs = 1
    for i in range(len(words) - n + 1):
        n_gram_tuple = tuple(words[i:i+n])
        n_gram_count = Count_N_gram.get(n_gram_tuple, 0)
        sentence_probs *= (n_gram_count + 1) / (total + len(Count_N_gram))  

    return sentence_probs
  

n = 5
n_grams = ngrams(data, n)
Count_N_gram = Counter(n_grams)
total = sum(Count_N_gram.values())

sentence = "پیش بینی کلمه بعدی کاری است که می تواند توسط یک مدل زبان انجام شود. "
sentence_prob = calculate_probability(sentence, Count_N_gram, total)
print(f"probability: {sentence_prob}")



n = 5  
n_grams = ngrams(data, n)
Count_N_gram = Counter(n_grams)
total = sum(Count_N_gram.values())


sentence = "تازه ترین اخبار ورزشی را در صفحه ورزش خبرگزاری بخوانید."
sentence_prob = calculate_probability(sentence, Count_N_gram, total)
print(f"probability {sentence_prob}")



