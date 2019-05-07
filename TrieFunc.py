import pickle

class Node:
    def __init__(self):
        self.value = ""
        self.children = {}    # children is of type {char, Node}   
        self.end = False                                                                                              

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, in_key, index):      # key is of type string
        key = in_key.lower()                                                                                            
        node = self.root
        # print(node.value)
        for char in key:
            if char not in node.children:
                child = Node()
                child.value = char
                node.children[char] = child
                node = child
            else:
                node = node.children[char]
        # print(node.end)
        if node.end is False:
            node.end = True
            filename = './occurrencelists/occurlist_{}.pickle'.format(key)
            html_dic = {index: 1}
            # print(filename)
            f=open(filename,'wb')
            pickle.dump(html_dic, f)
            # print(html_dic)
            f.close()
        else:
            filename = './occurrencelists/occurlist_{}.pickle'.format(key)
            f=open(filename,'rb')
            Dic = pickle.load(f)
            f.close()
            if (index in Dic.keys()) is True:
                Dic[index] = Dic[index] + 1
                # print(Dic)
            else:
                Dic[index] = 1
            f=open(filename,'wb')
            pickle.dump(Dic, f)
            f.close()


    def search_truncated(self, in_key):
        key = in_key.lower()
        node = self.root
        for char in key:
            if char not in node.children:
                return None
            else:
                node = node.children[char]
        if node.end is False:
            return None
        else: 
            filename = './occurrencelists/occurlist_{}.pickle'.format(key)
            f=open(filename,'rb')
            Dic = pickle.load(f)
            f.close()
        return Dic
    
    def search(self, in_key):
        key = in_key.lower()
        node = self.root
        '''
        if node.value == key:
            filename = './occurrencelists/occurlist_{}.pickle'.format(key)
            f=open(filename,'rb')
            Dic = pickle.load(f)
            f.close()
            return Dic
        '''
        key_i = 0
        length = len(key)
        while key_i<length:
            char = key[key_i]
            if char not in node.children:
                return None
            else:
                node = node.children[char]
                chars = node.value
                if not key.startswith(chars, key_i):
                    return None
                key_i += len(chars)
        if key_i==length and node.end:
            # return True
            filename = './occurrencelists/occurlist_{}.pickle'.format(key)
            # print(node.end)
            f=open(filename,'rb')
            Dic = pickle.load(f)
            f.close()
            return Dic
        else:
            return None

    def compress(self):
        self._compress(self.root)

    def _compress(self, root):
        if root is {}:
            return
        while len(root.children.keys())==1 and not root.end and root!=self.root:
            child = list(root.children.values())[0]
            root.value += child.value
            root.children = child.children
            root.end = child.end
        
        for child in root.children.values():
            self._compress(child)

        """
        Child_node = node.children

        Grand_node = Child_node[list(Child_node.keys())[0]].children

        if Grand_node is None: 
            return

        if Child_node.end is False and len(Grand_node) is 1:
            New_node = Node()

        else:
            return compress(Child_node)
        """