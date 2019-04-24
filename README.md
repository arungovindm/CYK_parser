# PCFG-trainer-CYK-parser
Implementation of CYK parser for constituency parsing using probabilistic context free grammar using a small subset of parse trees from the Penn Treebank, and a CYK parser that uses that PCFG.

## To run parser from terminal
```
sh script.sh
```


## To learn grammar and parse
First preprocess the tree bank to replace single occurence terminals with "\<unk\>"
```
python create_test.py
cat train.trees | python replace_onecounts.py > train.trees_unk 2> train.dict
cat train.trees_unk | python binarize.py > train.trees.bin
```

Learning the grammar
```
python learn_pcfg.py train.trees.bin grammar.pcfg.bin
```

Run the CYK parser
```
cat testing.txt | python cky.py grammar.pcfg.bin train.dict > test.parsed
```

Evaluate the results
```
python evalb.py truth.txt test.parsed
```

### Note:
grammar file can be found here
```
./data/grammar.pcfg.bin
```
