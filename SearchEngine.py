from TrieFunc import Trie
import pickle

# print(Trie().search("of"))
print('==============================================================')
print('================ THIS IS A SIMPLE SEARCH ENGINE ==============')
print('===created by Hangyu Wang')
print('===you can try the following words:')
print('===\'algorithm\', \'sort\', \'complexity\', \'merge\', etc.')
print('==============================================================')
print('\n')

def SearchEngine():
    search = Trie().search
    while True:
        in_data = input('========== Please input the word you want to search(Q to quit): =========\n')
        if in_data == "Q":
            break
        print('================ The searching result is below: ==============')
        with open('Trie_model/trie_test.pkl','rb') as f:
            Stored_trie = pickle.load(f)
        result = Stored_trie.search(in_data)
        if not result is None:
            # print(result)
            sortedR = sorted(result, key = result.get, reverse=True)
            for re in sortedR:
                print(re)
        else:
            print('no match result')
# print(sortedR)
SearchEngine()