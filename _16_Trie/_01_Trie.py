"""Here I will create the Trie
Trie -> used to to smooth string operation
     -> also used in search operation
"""

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfString = False
    
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word : str):
        current = self.root  # get the TrieNode class
        for i in word:
            character = i   # getting each character from the word
            node = current.children.get(character)  # if not exits character we get None else the next TrieNode
            if node == None:    # character don't exits since it equal to None
                node = TrieNode()   # create an new Trie node to the next next character of character
                current.children.update({character : node}) # node adding {"d" : new TrieNode pointer}
            
            # If we found the word then it means current is now set to next new Trie pointer of the word
            current = node  # now current goes to newly create TrieNode
            
        # after adding the word we set the end of string for that current (TrieNode)
        current.endOfString = True
        print("Word added successfully")        
        
    def search(self, word : str):
        current_node = self.root
        for character in word:
            node = current_node.children.get(character)
            if node == None:    # means word don't exits
                return False
            
            current_node = node  # here node is next Trie node value of found character as {ch : new TrieNode}
        
        # If ends of string for current node is not True means search word is just prefix not exits independently
        if current_node.endOfString is False:
            return False
        else:   # means word is present also exits as independently not as prefix of another word
            return True
  
def delete(root_node: TrieNode, word: str, index = 0):
    ch = word[index]  # Get the current character in the word.
    current_node: TrieNode = root_node.children.get(ch)  # Get the node for this character.

    # If the current node does not exist, the word is not in the Trie.
    if current_node is None:
        return False

    # Check if this is the last character of the word.
    if index == len(word) - 1:
        # If this node has children, it's a prefix of another word.
        if len(current_node.children) >= 1:
            current_node.endOfString = False  # Un mark end of string but don't delete the node.
            return False
        else:
            # No children means this is the end of the word to be deleted.
            # Remove this node from the parent's children.
            root_node.children.pop(ch)  # Correct: remove 'd' from 'r'
            return True

    # If the node marks the end of another word.
    if current_node.endOfString:
        delete(current_node, word, index + 1)
        return False  # Cannot delete since it's an end of another word.

    # Recursively delete the next character.
    can_this_node_be_deleted = delete(current_node, word, index + 1)
    
    # If the next character can be deleted, remove it from the current node's children.
    if can_this_node_be_deleted:
        # Only remove the node if it's no longer the end of a word and has no children.
        if not current_node.endOfString and len(current_node.children) == 0:
            root_node.children.pop(ch)
            return True
        else:
            return False

    # If the next character cannot be deleted, keep this node intact.
    return False


    
newTrie = Trie()
newTrie.insert("Word")
newTrie.insert("God")

delete(newTrie.root, "Word")
# print(newTrie.search("Word"))