"""
NAME: Asim Soylu
MATRIKELNUMMER: 108019256229
"""

"""WAS TUT DAS PROGRAMM?
Das Programm liest, tokenisiert und erstellt Ngramme aus dem vom Benutzer eingegebenen Text (Input-Text).
Zusätzlich zu diesen Prozessen zählt und sortiert es die ersten 1000 höchsten Ngramme der Korpustexte.
Dann vergleicht es die Ngramme des Benutzers mit den sortierten Ngrammen aus dem Korpus und bestimmt die Punktzahl
für jede Sprache. Schließlich werden die Sprachen in eine Rangfolge gebracht,
und die Sprache mit der höchsten Punktzahl wird
als wahrscheinliche Sprache des vom Benutzer angegebenen Textes ausgegeben.
"""

################################
# Funktionen
################################

################################
# Input aus dem Korpus nehmen
################################

def read_text(filename):
    """Funktion, die einen Dateinamen als Input nimmt
    und den Inhalt dieser Datei in ein geeignetes Format einliest:

    Input:  filename (str):    Dateinamen
    Return: corpus_tokens (list):     Liste von Tokens"""

#öffnet, liest und schließt die Datei
    with open (filename, 'r', encoding="utf-8") as f:
        source_text = f.read()
#ruft die Funktion "wordpunct_tokenize" aus der Bibliothek "nltk" auf
    from nltk import wordpunct_tokenize
#Tokenisierung
    tokens = wordpunct_tokenize(source_text)
#macht die Korpus-Tokens kleiner
    corpus_tokens = [words.lower() for words in tokens]

    return corpus_tokens

def create_ngrams(corpus_tokens, n):
    """Funktion, die aus den gegebenen Token saemtliche Ngramme der
    Laenge n extrahiert und in einer Liste speichert.

    Input:
    1. corpus_tokens (list): Text als Liste von Tokens
    2. n (int):       Laenge der Ngramme
    Return:
    1. ngrams(list):  Liste von Ngrammen"""

#definiert eine leere Liste namens ngrams
    ngrams = []
#für jedes Element in der Liste "corpus_tokens"
    for tokens in corpus_tokens:
#iteriert über die Charaktere im "corpus_tokens", um Ngramme zu erzeugen
#z.B.: "deutschland" 0-8(11 - 4 +1) = 8 = ['deut', 'euts', 'utsc', 'tsch', 'schl', 'chla', 'hlan', 'land']
        for elt_tokens in range(len(tokens) - n + 1):
#fügt alle Ngramme zur Liste "ngrams" hinzu
            ngrams.append(tokens[elt_tokens:elt_tokens + n])

    return ngrams

def count_ngrams(ngrams):
    """Funktion, die die Liste ngrams nimmt,
    zählt und die Frequenz der einzelnen Ngrammen findet.

    Input:
    1. ngrams (list): Liste von Ngramm
    Return:
    1. freq (dict): Dict von Ngrammen und Frequenzen"""

#definiert ein Dictionary namens "freq"
    freq = {}
#für jedes Element in der Liste ngrams
    for elt_ngrams in ngrams:
#wenn die Elemente der Keys des freq-Dictionary mehr als einmal vorkommen
        if elt_ngrams in freq:
#erhöht die Punktzahl von "elt_ngrams" += 1
            freq[elt_ngrams] += 1
#wenn nicht, setzt den Wert auf 1
        else:
            freq[elt_ngrams] = 1

    return freq

def sort_ngrams(freq,count):
    """Funktion, die das Dictionary Freq nimmt und die Ngramm-Frequenzen reverse sortiert,
    bis der row-Wert größer ist als der count-Wert, der 1000 beträgt.

    Input:
    1. freq (dict): Dict von Ngrammen und Frequenzen
    2. count (int): Der Count-Wert
    Return:
    1. freq_sorted (dict): Dict von sortierten Ngrammen und Frequenzen"""

#definiert ein Dictionary namens "freq_sorted"
    freq_sorted = {}
#die Variable "row" auf 0 setzen
    row = 0
#definiert die Variable "listSorted" und sortiert das Dictionary freq nach ihren "values" und kehrt sie um
    listSorted = sorted(freq, key=freq.get, reverse=True)
#für jedes Element der Liste listSorted
    for freq_key in listSorted:
#erhöht "row " +=1
        row += 1
#weist die sortierten Elemente der Liste "listSorted" dem Dictionary "freq_sorted" als Keys zu
#und die sortierten "values" des Dictionarys "freq" in das Dictionary "freq_sorted" als "values"
        freq_sorted[freq_key] = freq[freq_key]
#wenn "row " größer als "count" ist
        if row > count:
#bricht die Funktion
            break

    return freq_sorted

################################
# Input vom Benutzer nehmen
################################

def take_input_tokenize(n):
    """Funktion, die den Benutzer nach einem Input-Text fragt,
    diesen tokenisiert und verkleinert:

     Input: n (int): Laenge der Ngramme
     Return: user_ngrams (list):     Liste der Benutzer-Ngramme in Kleinbuchstaben"""

#fragt den Benutzer nach einem Eingabe-Text (input-text)
    user_text = input("Bitte geben Sie einen Text:")
#ruft die Funktion "wordpunct_tokenize" aus der Bibliothek "nltk" auf
    from nltk import wordpunct_tokenize
#Tokenisierung
    user_tokens = wordpunct_tokenize(user_text)
#macht die Tokens kleiner
    user_tokens_lowered = [words.lower() for words in user_tokens]
#wandelt die User-Tokens entsprechend dem Wert von "n" in Ngramme um
    user_ngrams = create_ngrams(user_tokens_lowered, n)

    return user_ngrams

def compare_user_with_corpus(user_ngrams, corpus_ngrams):
    """Funktion, die die Ngramme des Benutzers mit den Ngrammen des Korpus vergleicht
    und bei Übereinstimmung zwischen diesen beiden Ressourcen jedes Mal
    den Wert der Punktzahl +=1 der betreffenden Sprache erhöht.

    Input:
    1. user_ngrams (list): Liste der Benutzer-Ngramme
    2. corpus_ngrams (dict): Dict von sortierten Korpus_Ngramme und Frequenzen
    Return:
    1. score (int): Die Anzahl der übereinstimmenden Ngramme """

#setzt die Variable "score" auf 0
    score = 0
#vergleicht für jedes Element der Liste "user_ngrams"
    for elt_user in user_ngrams:
#mit jedem Element der Liste "corpus_ngrams"
        for elt_corpus in corpus_ngrams.keys():
#wenn es eine Übereinstimmung zwischen zwei Ressourcen gibt
            if elt_user == elt_corpus:
#erhöht die Punktzahl +=1
                score +=1

    return score

def rank(langscore):
    """Funktion, die die Sprachen und ihre Punktzahlen
    im Dictionary "langscore" sortiert.

    Input: langscore (dict): Dict von Sprachen und ihre Punktzahlen
    Return: lang_sorted (dict): Dict von sortierten Sprachen und ihre Punktzahlen """

#definiert ein Dictionary namens "lang_sorted"
    lang_sorted = {}
#definiert die Variable "listSorted" entsprechend den Werten von "langscore" und kehrt diese um
    listSorted = sorted(langscore, key=langscore.get, reverse=True)
#für jedes Element in der Liste "listSorted"
    for sorted_key in listSorted:
#weist die sortierten Elemente (sorted_key) der Liste "listSorted" dem Dictionary "lang_sorted" als Keys zu
#und die sortierten Werte des Dictionarys "langscore" in das Dictionary "lang_sorted" als Values
        lang_sorted[sorted_key] = langscore[sorted_key]

    return lang_sorted


def run_script(filename, n):
    """Funktion, die alle weiteren Funktionen aufruft

    Input:
    1. filename (str): Dateinamen der einzulesenden Textdateien
    2. n (int): Laenge der Ngramme
    Return: --
    kein Rueckgabewert, aber Ausgabe der Ergebnisse auf der Konsole (mit prints)"""

#macht die User-Tokens zu Ngrammen
    user_ngrams = take_input_tokenize(n)
#definiert ein Dictionary namens "langscore" für jede Sprache und ihre Punktzahl
    langscores = {}

#liest jeden Korpustext jeder Sprache ein, macht sie zu Tokens, Ngrammen
    for lang in filename.keys():
        corpus_tokens = read_text(filename[lang])
        ngrams = create_ngrams(corpus_tokens, n)
#zählt die Ngramme im Korpus und ermittelt ihre Frequenzen, sortiert die ersten 1000 höchsten Ngramme
        freq = count_ngrams(ngrams)
        corpus_ngrams = sort_ngrams(freq, 1000)
#vergleicht Ngramme vom User und Ngramme aus den Korpustexten und weist jeder einzelnen Sprache eine Punktzahl im Dictionary "langscores" zu
        langscores[lang] = compare_user_with_corpus(user_ngrams, corpus_ngrams)

#ordnet die Punktzahlen der Sprachen ein
    ranked_langscores = rank(langscores)

#prints die Sprachen und ihre Punktzahlen
    print(ranked_langscores)
#gibt das erste Element des Dictionarys "ranked_langscores" aus
    print("Nach den Ergebnissen ist die wahrscheinliche Sprache: "+ list(ranked_langscores.keys())[0])


    return

################################
# Hauptprogramm
################################

if __name__ == "__main__":

#definiert den Wert der Variable "n", die die Länge der Ngramme bestimmt
    n = 4

#definiert das Dictionary "filename", das aus den Dateipfaden besteht
    filename = {
    "Deutsch": "resources\de\corpus-de.txt",
    "Englisch": "resources\en\corpus-en.txt",
    "Spanisch": "resources\es\corpus-es.txt",
    "Niederländisch": "resources\\nl\corpus-nl.txt",
    "Polnisch": "resources\pl\corpus-pl.txt"
    }

#diese Funktion ruft alle weiteren Funktionen auf
    run_script(filename, n)
