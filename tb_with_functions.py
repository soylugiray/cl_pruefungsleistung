"""
NAME: Asim Soylu
MATRIKELNUMMER: 108019256229
"""

"""WAS TUT DAS PROGRAMM?
The program reads and tokenizes the text given text, creates ngrams from tokens, counts them, and sorts them.
Ultimately, orders the ngrams with the highest frequencies to the lowest, to determine which letter combinations are used
the most in the language in question.
"""

################################
# Funktionen
################################

def read_text(filename):
    """Funktion, die einen Dateinamen als Input nimmt
    und den Inhalt dieser Datei in ein geeignetes Format einliest:
    Input:  filename (str):    Dateiname
    Output: tokens (list):     Liste von Tokens"""
    
    with open (filename, 'r', encoding="utf-8") as f:
        source_text = f.read()

    from nltk import wordpunct_tokenize

    tokens = wordpunct_tokenize(source_text)
    tokens_lowered = [word.lower() for words in tokens]


def create_ngrams(tokens_lowered, n):
    """Funktion, die aus einem gegebenen Text saemtliche Ngramme der
    Laenge n extrahiert und in einer Liste speichert.
    Input:
    1. tokens_lowered (list): Text als Liste von Tokens
    2. n (int):       Laenge der Ngramme
    Return:
    1. ngrams(list):  Liste von Ngrammen"""

    ngrams = []
    for words in tokens_lowered:
        for elt_words in range(len(words) - n + 1):
            ngrams.append(words[elt_words:elt_words + n])


def count_ngrams(ngrams):
    """Funktion, die eine Liste von Ngrams einliest und deren Frequenzen
    bestimmt. Die Ngramms und deren Frequenzen werden in
    einem Dictionary abgespeichert.

    Input:
    1. ngrams (list): Liste von Ngramm-Tokens
    Return:
    1. freq (dict): Dict von Ngrammen und Frequenzen
    """

    freq = {}
    for elt_ngrams in ngrams:
        if elt_ngrams in freq:
            freq[elt_ngrams] += 1
        else:
            freq[elt_ngrams] = 1


def sort_ngrams(freq):
    """Funktion, die aus dem Dictionary von Ngramms und deren
    Frequenzen reverse sortiert.

    Input:
    1. freq (dict): Dict von Ngrammen und Frequenzen
    Return:
    1. freq_srtd (dict): Dict von sortierten Ngrammen und Frequenzen

    """

    freq_srtd = {}
    sorted = sorted(freq, key=freq.get, reverse=True)
    for elt_srtd in sorted:  # burada sort olan değerleri atadık
        freq_srtd[elt_srtd] = freq[elt_srtd]


def run_script(filename, n):
    """Funktion, die alle weiteren Funktionen aufruft
    Input:
    1. text: Dateiname der einzulesenden Textdatei (str)
    2. lexicon: Dateiname des Tagger-Lexikons
    Return: --

    kein Rueckgabewert, aber Ausgabe der Ergebnisse auf der Konsole (mit print)
    """

    print(freq_srtd)


################################
# Hauptprogramm
################################

if __name__ == "__main__":
    infile = "C:\\Users\PC\Desktop\#W21-22\CL PL\sample texts\de\#mergedde.txt"
    n = 4

    # diese Funktion ruft alle weiteren Funktionen auf
    run_script(infile, n)
