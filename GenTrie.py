from HTMLParser import HTML_parser
from TrieFunc import Trie
import pickle

def TRIE_gen(file_dir):
    allcontent = HTML_parser(file_dir)
    keys = allcontent.keys()
    trie = Trie()
    for key in keys:
        for word in allcontent[key]:
            trie.insert(word, key)

    with open('Trie_model/trie_test.pkl','wb') as f:
        pickle.dump(trie, f)

TRIE_gen('./HtmlSource')
print('The trie is created and relating occurencelists are built.')