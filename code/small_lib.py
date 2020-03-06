"""
A small module of functions applied across multiple notebooks in this
authorship authenticity project.
by Ethan Henley
"""

import re
from nltk.corpus import stopwords

replace_punc_dict = {
    '<':' ANGLEPUNC ',
    '>':' ANGLEPUNC ',
    ':':' COLONPUNC ',
    '!':' EXCLMPUNC ',
#     ',':' COMMAPUNC ',
#     '.':' PRIODPUNC ',
    ';':' SEMICPUNC ',
    '?':' QSTINPUNC ',
    '(':' PARENPUNC ',
    ')':' PARENPUNC ',
    '[':' SQBKTPUNC ',
    ']':' SQBKTPUNC ',
    '{':' CURLYPUNC ',
    '}':' CURLYPUNC ',
    '-':' ODASHPUNC ',
    '–':' NDASHPUNC ',
    '—':' MDASHPUNC '
}

def sumtwo(a,b):
    return a+b

def get_rpd():
    """
    A simple function to return the punctuation replacement dictionary.
    """
    return replace_punc_dict

def replace_punc(char):
    """
    A function to replace meaningful punctuation with 'words.'
    """
    
    return (char if char not in replace_punc_dict.keys() 
            else replace_punc_dict[char])
            
def get_stops_A(s=1,n=1,p=1,o=1):
    """
    A function that returns a list of stopwords specific to the Animorphs series.
    """
    # frequent character names and other proper nouns
    # manually collected from the text and animorphs.fandom.com
    names = ['jake','rachel','marco','james','craig','erica','tobias',
             'cassie','aximili','esgarrouth','isthill', 'ax',
             'aximiliesgarrouthisthill','david','melissa','chapman',
             'collette','kelly','timmy','julio','liam','tricia','jessie',
             'judy','ray', 'gafinilan','estrif','valad','gafinilanestrifvalad',
             'erek','king','tom','taylor','karen','arbat','elivat','estoni',
             'arbatelivatestoni','aldrea','iskillion','falan',
             'aldreaiskillionfalan','william','tennant','mertil','iscar',
             'elmand','mertiliscarelmand']
    pnouns = ['taxon','helmacron','helmacrons','leera']

    # some other stopwords to include
    other_stops = ['said', 'like','one','']

    # all extra stopwords
    extra_stops = names + pnouns + other_stops
    
    # set up stopwords
    stops = stopwords.words('english') + extra_stops

    # clean stops to same format as other text
    stops = re.sub(r'[^a-zA-Z ]','',' '.join(stops)).lower().split()
    
    return stops
    
def clean_chapter(chapter, stops=get_stops_A()):
    """
    A function to clean and tokenize a chapter of text.
    """
    # regex non-letters, lowercase, tokenize
    chapter = chapter.replace('\n',' ')
    new_chap = ''
    for i in range(len(chapter)):
        new_chap += replace_punc(chapter[i]) # rewrite punctuation as words
    chapter = new_chap
    chapter = re.sub(r'[^a-zA-Z ]','',chapter).lower().split()
    chapter = [w for w in chapter if w not in stops]
    return chapter
    
if __name__ == '__main__':
    print('No need to run this—it\'s just a resource for the notebooks!')
    t2c = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way - in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only. Some punctuation: -–—([{<>}])# iamnotpunctuation Jake said'
    print(clean_chapter(t2c))