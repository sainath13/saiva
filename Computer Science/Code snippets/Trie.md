It always is about breaking down into manageable chunks of logic.

```java
class TrieNode{
    private TrieNode[] links;
    private final int R = 26;
    private boolean isEnd;
    
    public TrieNode() {
        links = new TrieNode[R];
    }

    public boolean containsKey(char ch){
        return links[ch -'a'] != null;
    }

    public TrieNode get(char ch){
        return links[ch -'a'];
    }

	//put node at char, not the other way round
    public void put(char ch, TrieNode node) { 
        links[ch -'a'] = node;
    }

    public void setEnd() {
        isEnd = true;
    }

    public boolean isEnd() {
        return isEnd;
    }
}

class Trie {
    private TrieNode root;
    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode node = root;
        for(int i = 0; i < word.length(); i++) {
            char currChar = word.charAt(i);
            if(!node.containsKey(currChar)) {
                node.put(currChar, new TrieNode());
            }
            node = node.get(currChar);
        }
        node.setEnd();
    }
    
    public boolean search(String word) {
        TrieNode node = searchPrefix(word);
        return node != null && node.isEnd();
    }
    
    public boolean startsWith(String prefix) {
        TrieNode node = searchPrefix(prefix);
        return node != null;
    }

    private TrieNode searchPrefix(String word) {
        TrieNode node = root;
        for (int i = 0; i < word.length(); i++){
            char currChar = word.charAt(i);
            if(node.containsKey(currChar)) {
                node = node.get(currChar);
            }
            else{
                return null;
            }
        }
        return node;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
```


```java 
//Word Dictionary
class WordDictionary {
    
    TrieNode root;

    /** Initialize your data structure here. */
    public WordDictionary() {
        this.root = new TrieNode();
    }
    
    /** Adds a word into the data structure. */
    public void addWord(String word) {
        TrieNode node = root;
        for(char ch : word.toCharArray()){
            if (!node.containsKey(ch)){
                node.put(ch, new TrieNode());
            }
            node = node.get(ch);
        }
        node.isEnd = true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    public boolean search(String word) {
        return search(word, this.root, 0);
    }
    
    private boolean search(String word, TrieNode node, int index){
             
        if (index == word.length()) return node.isEnd;
        
        if(word.charAt(index) != '.'){
            return (node.get(word.charAt(index)) != null  && 
                   search(word, node.get(word.charAt(index)), index+1));
        }else{
            for(TrieNode n : node.links){
                if (n != null && search (word, n, index+1)) return true; 
            }
            return false;
        }
        
    }
}

class TrieNode{
    
    TrieNode[] links;
    boolean isEnd;
    
    TrieNode(){
        this.links = new TrieNode[26];
        this.isEnd = false;
    }

    public boolean containsKey(char ch){
        return links[ch - 'a'] != null;
    }
    
    public void put(char ch, TrieNode node) { //put node at char
        links[ch -'a'] = node;
    }

    public TrieNode get(char ch){
        return links[ch -'a'];
    }
}
/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 **/

```