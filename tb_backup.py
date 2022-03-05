with open ("C:\\Users\PC\Desktop\#W21-22\CL PL\sample texts\de\#mergedde.txt", 'r', encoding="utf-8") as f:
    words = f.read()

from nltk import wordpunct_tokenize

tokens = wordpunct_tokenize(words)
tokens = [word.lower() for word in tokens]

n = 4
lists = []
for words in tokens:
    for i in range(len(words) - n + 1):
        lists.append(words[i:i + n])

d = {}
s = {}
for l in lists:
    if l in d:
        d[l] += 1
    else:
        d[l] = 1

sorted = sorted(d,key=d.get,reverse=True)
for x in sorted: # burada sort olan değerleri atadık
    s[x]=d[x]

print(s)

