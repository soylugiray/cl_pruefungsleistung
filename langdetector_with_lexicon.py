"""
NAME: Asim Soylu
MATRIKELNUMMER: 108019256229
"""

"""WAS TUT DAS PROGRAMM?
Das Programm liest und tokenisiert den Lexikons und den vom Benutzer eingegebenen Text (Input-Text).
Dann vergleicht es die Token des Benutzers mit den Token des Lexikons,
und bestimmt die Punktzahl für jedes Lexikon der Sprachen.
Schließlich ordnet es die Sprachen und gibt die Sprache mit der höchsten Punktzahl
als die wahrscheinliche Sprache des vom Benutzer eingegebenen Textes aus. 
"""

################################
# Funktionen
################################

################################
# Input aus dem Lexicon nehmen
################################

def read_text(filename):
    """Funktion, die einen Dateinamen als Input nimmt
    und den Inhalt dieser Datei in ein geeignetes Format einliest:

    Input:  filename (str):    Dateinamen
    Output: lexicon_tokens (list):     Liste von Tokens"""

#öffnet, liest und schließt die Datei
    with open (filename, 'r', encoding="utf-8") as f:
        source_text = f.read()
#ruft die Funktion "wordpunct_tokenize" aus der Bibliothek "nltk" auf
    from nltk import wordpunct_tokenize
#Tokenisierung
    tokens = wordpunct_tokenize(source_text)
#macht die Lexicon-Tokens kleiner
    lexicon_tokens = [words.lower() for words in tokens]

    return lexicon_tokens

################################
# Input vom Benutzer nehmen
################################

def take_input_tokenize():
    """Funktion, die den Benutzer nach einem Input-Text fragt,
    diesen tokenisiert und verkleinert:

     Input: -----
     Return: user_ngrams (list):     Liste der Benutzer-Ngramme in Kleinbuchstaben"""

#fragt den Benutzer nach einem Eingabe-Text
    input_text = input("Bitte geben Sie einen Text:")
#ruft die Funktion "wordpunct_tokenize" aus der Bibliothek "nltk" auf
    from nltk import wordpunct_tokenize
#tokenisierung
    input_tokens = wordpunct_tokenize(input_text)
#macht die eingegebenen Wörter kleiner
    user_tokens = [words.lower() for words in input_tokens]

    return user_tokens

def compare_user_with_lexicon(user_tokens, lexicon_tokens):
    """Function that compares input tokens with the resource tokens
    from 1000 most common words with the help of two for-loop:

     Input:
     1. user_tokens (list): Liste der Benutzer-Tokens
     2. lexicon_tokens (list): Liste der Lexicon-Tokens
     Output:
     1. scores (list): Die Anzahl der übereinstimmenden Tokens """

#die Variable "scores" auf "0" setzen
    scores = 0
#sucht das Element der user_tokens
    for user_words in user_tokens:
#mit den Elementen der lexicon_tokens
        for lexicon_words in lexicon_tokens:
#wenn es Übereinstimmungen zwischen zwei Daten gibt
            if user_words == lexicon_words:
#erhöht die Punktzahl um +1
                scores +=1

    return scores

def rank(langscore):
    """Function that asks from user for an input-text
     tokenizes and makes them lowered:

     Input: langscore (dict): Dictionary der Sprachen und ihrer unsortierten Punktezahl
     Output: lang_sorted (dict): Dictionary der Sprachen und ihrer sortierten Punktezahl"""

#definiert ein Dictionary namens "lang_sorted"
    lang_sorted = {}
#definiert die Variable "listSorted" und sortiert das Dictionary langscore nach ihren "values" und kehrt sie um
    listSorted = sorted(langscore, key=langscore.get, reverse=True)
#für jedes Element der Liste listSorted
    for elt_sorted in listSorted:
#weist die sortierten Elemente der Liste "listSorted" dem Dictionary "lang_sorted" als Keys zu
#und die sortierten "values" des Dictionarys "langscore" in das Dictionary "lang_sorted" als "values"
        lang_sorted[elt_sorted] = langscore[elt_sorted]

    return lang_sorted

def run_script(filename):
    """Funktion, die alle weiteren Funktionen aufruft
    Input:
    1. filename (str): Dateinamen der einzulesenden Textdateien
    Return: --
    kein Rueckgabewert, aber Ausgabe der Ergebnisse auf der Konsole (mit prints)"""

#macht die User-Input zu Tokens
    user_tokens = take_input_tokenize()
#definiert ein Dictionary namens "langscore" für jede Sprache und ihre Punktzahl
    langscores = {}

#liest jeden Lexicontext jeder Sprache ein, macht sie zu Tokens
    for lang in filename.keys():
        lexicon_tokens = read_text(filename[lang])
#vergleicht Tokens vom User und Tokens aus den Lexicontexten und weist jeder einzelnen Sprache eine Punktzahl im Dictionary "langscores" zu
        langscores[lang] = compare_user_with_lexicon(user_tokens, lexicon_tokens)

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

#definiert das Dictionary "filename", das aus den Dateipfaden besteht
    filename = {
    "Deutsch": "resources\de\lexicon-de.txt",
    "Englisch": "resources\en\lexicon-en.txt",
    "Spanisch": "resources\es\lexicon-es.txt",
    "Niederländisch": "resources\\nl\lexicon-nl.txt",
    "Polnisch": "resources\pl\lexicon-pl.txt"
    }

#diese Funktion ruft alle weiteren Funktionen auf
    run_script(filename)
