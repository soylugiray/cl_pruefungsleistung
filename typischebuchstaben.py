with open ("C:\\Users\PC\Desktop\#W21-22\CL PL\sample texts\de\#mergedde.txt", 'r', encoding="utf-8") as f:
    words = f.read()

from nltk import wordpunct_tokenize

tokens = wordpunct_tokenize(words)
tokens = [word.lower() for word in tokens]

n = 4
n_tokens = []
for words in tokens:
    for elt_words in range(len(words) - n + 1):
        n_tokens.append(words[elt_words:elt_words + n])

freq = {}
freq_srtd = {}
for elt_n_tokens in n_tokens:
    if elt_n_tokens in freq:
        freq[elt_n_tokens] += 1
    else:
        freq[elt_n_tokens] = 1

sorted = sorted(freq,key=freq.get,reverse=True)
for elt_srtd in sorted: # burada sort olan değerleri atadık
    freq_srtd[elt_srtd]=freq[elt_srtd]

print(freq_srtd)