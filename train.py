"""
Train our Tokenizers on some data, just to see them in action.
The whole thing runs in ~25 seconds on my laptop.
"""

import os
import time
from minbpe import RegexTokenizer

# open some text and train a vocab of 512 tokens
text = open("tests/taylorswift.txt", "r", encoding="utf-8").read()
text = "".join([text for _ in range(1)])
# create a directory for models, so we don't pollute the current directory
os.makedirs("models", exist_ok=True)

t0 = time.time()
for TokenizerClass, name in zip([RegexTokenizer], ["regex"]):
    # construct the Tokenizer object and kick off verbose training
    tokenizer = TokenizerClass()
    merges1, vocab1 = tokenizer.trainFaster(text, 512, verbose=True)
    merges2, vocab2 = tokenizer.train(text, 512, verbose=True)
    print(merges1)
    print("")
    print(merges2)
    print(merges1 == merges2)
    print(len(merges1))
    print(len(merges2))
    # writes two files in the models directory: name.model, and name.vocab
    prefix = os.path.join("models", name)
    tokenizer.save(prefix)

t1 = time.time()

print(f"Training took {t1 - t0:.2f} seconds")