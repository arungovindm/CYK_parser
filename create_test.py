import nltk
#nltk.download('treebank')
from nltk.corpus import treebank
from nltk.grammar import CFG, Nonterminal
import random
import itertools

def get_distribution(tb, file_ids):
  freqs = nltk.probability.FreqDist()
  for document in file_ids:
    doc = tb.parsed_sents(document)
    for tree in doc:  
      tree.chomsky_normal_form()
      l= tree.subtrees()
      l_ = list(itertools.chain(*l))
      k=[]
      for line in l_:
        if (type(line))==str:
          continue
        k.append(line.productions())
      for i in range(len(k)):
        freqs.update(k[i])
        
  scale = 1/sum(freqs.values())
  for gramm , count in freqs.items():
    freqs[gramm]=scale*freqs[gramm]
  return freqs

def test_train_split(tb,test_ratio):
  test=[]
  train=[]
  size = len(tb.fileids())
  test_id = random.sample(range(size), int(test_ratio*size))
  for i in range(size):
    if i in test_id:
      test.append(tb.fileids()[i])
    else:
      train.append(tb.fileids()[i])
  return (test,train)


(test, train) = test_train_split(treebank,0.2)
test_tree = nltk.corpus.reader.bracket_parse.BracketParseCorpusReader(treebank.root,test)
train_tree = nltk.corpus.reader.bracket_parse.BracketParseCorpusReader(treebank.root,train)

test_set = open('/home/arun/Courses/sem2/NLU/assignments/assignment_3/PCFG-trainer-CYK-parser-master/testing.txt','w')
truth = open('/home/arun/Courses/sem2/NLU/assignments/assignment_3/PCFG-trainer-CYK-parser-master/truth.txt','w')
train_ = open('/home/arun/Courses/sem2/NLU/assignments/assignment_3/PCFG-trainer-CYK-parser-master/train.trees','w')
for doc in train_tree.fileids():
  sents = train_tree.sents(doc)
  parsed_sents = train_tree.parsed_sents(doc)
  for line_ in parsed_sents:
    temp = str(line_).replace('\n','')
    temp = ' '.join(temp.split())
    temp = '(TOP ' + temp + ')'
    train_.write(temp)
    train_.write('\n')


for doc in test_tree.fileids():
  sents = test_tree.sents(doc)
  parsed_sents = test_tree.parsed_sents(doc)
  for line in sents:
  	test_set.write(' '.join(line)[:-1])
  	test_set.write('\n')
  for line_ in parsed_sents:
    temp = str(line_).replace('\n','')
    temp = ' '.join(temp.split())
    temp = '(TOP ' + temp + ')'
    truth.write(temp)
    truth.write('\n')
