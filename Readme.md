### Environment Info:

Language: Python 3.7.3;
Dependencies: pickle, BeautifulSoup, regexp_tokenize(in nltk), os. Make sure relating dependencies are propertly installed before running my codes.

### boundary conditions:

1, The htmls are parsered with Regular Expression. Thus, I only parser out the a-zA-Z with length not less than two. Other typy of words and numbers are not contained in my compressed trie. Once you try such words, the reuslt will print 'no match result'.

### Data structure:

1, Exactly use the data structure mention in Section 23.5.4, Compressed trie.

### Algorithm Implementation(step by step):
Ranking Rule: easily use the occurrence in the html to rank.

1, Get 10 htmls from Wikipedia, which I stored in the file, HtmlSource;

2, Parser the content from htmls by using BeatifulSoup (function in the HTMLParser.py).

3, Store the words in each html into the compressed trie. In the trie, each external node of the trie relating to its occurence list. In the list, appearence times in the relating htmls are recorded. (functions are in the TrieFunc.py and GenTrie.py; the trie based on the exsiting htmls are stored in the Trie_model file)

4, Of course, occurrence list will be stored outside in pickle format(a useful format usually be used in python). The folder to store them are 'occurencelists'.

5, Everytime we start a search, we will search the compressed trie. According to the trie, we can decide whether this word exists. If this word exists, then the occurencelist will be read. Then the htmls will be sorted based on the occurence times of this word in each htmls. And the rank of the htmls will be shown. If a html does not have this word, then this html will not be listed. More details to mention, the search is not case sensitive. For example, 'algorithm' and 'Algorithm' is same for the search engine I design. And the 'Q' is set as a command to stop the search engine(only capital Q).


### Result Samples:
The htmls I found comes from Wikipedia with the topic 'algorithm'.

Thus, you can try the following inputs to the the ranking: algorithm, sort, complexity etc. 

These are from the actual result:

========== Please input the word you want to search: =========
algorithm
================ The searching result is below: ==============
Algorithm.html
TimeComplexity.html
SortingAlgorithm.html
Quicksort.html
MergeSort.html
Heapsort.html
AverageCaseComplexity.html
BubbleSort.html
BucketSort.html
SelectionSort.html
========== Please input the word you want to search: =========
sorted
================ The searching result is below: ==============
SortingAlgorithm.html
MergeSort.html
Quicksort.html
Heapsort.html
BubbleSort.html
BucketSort.html
SelectionSort.html
TimeComplexity.html
Algorithm.html
AverageCaseComplexity.html
========== Please input the word you want to search: =========
sort
================ The searching result is below: ==============
SortingAlgorithm.html
MergeSort.html
BucketSort.html
BubbleSort.html
Quicksort.html
SelectionSort.html
Heapsort.html
TimeComplexity.html
Algorithm.html
========== Please input the word you want to search: =========
merge
================ The searching result is below: ==============
MergeSort.html
SortingAlgorithm.html
Heapsort.html
Quicksort.html
BucketSort.html
BubbleSort.html
SelectionSort.html
Algorithm.html
TimeComplexity.html
========== Please input the word you want to search: =========
complexity
================ The searching result is below: ==============
TimeComplexity.html
AverageCaseComplexity.html
SortingAlgorithm.html
Algorithm.html
Heapsort.html
BubbleSort.html
Quicksort.html
MergeSort.html
BucketSort.html
SelectionSort.html
========== Please input the word you want to search: =========

================ The searching result is below: ==============
no match result
========== Please input the word you want to search: =========
asdf
================ The searching result is below: ==============
no match result
========== Please input the word you want to search: =========
Q

To get more infomation about the test and the result, please go to the 'Output' folder.
