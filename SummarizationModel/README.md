This repository contains code for Abstractive and Extractive Summarization Models.

Abstractive Model code is from *[@becxer's](https://github.com/becxer/pointer-generator/)* repository, which is *[@abisee's](https://github.com/abisee/pointer-generator/)* code but updated for Python 3.

Extractive Model uses Python's summa package

Data preprocessing Code: *[@abisee](https://github.com/abisee/cnn-dailymail)*

# Abstractive Model

## Original Paper
ACL 2017 paper *[Get To The Point: Summarization with Pointer-Generator Networks](https://arxiv.org/abs/1704.04368)*

## Pretrained model
A pretrained model is available here:
* [Version for Tensorflow 1.2.1](https://drive.google.com/file/d/0B7pQmm-OfDv7ZUhHZm9ZWEZidDg/view?usp=sharing)

## About the code
This code is based on the [TextSum code](https://github.com/tensorflow/models/tree/master/textsum) from Google Brain.

This code was developed for Tensorflow 0.12, but has been updated to run with Tensorflow 1.0.
In particular, the code in attention_decoder.py is based on [tf.contrib.legacy_seq2seq_attention_decoder](https://www.tensorflow.org/api_docs/python/tf/contrib/legacy_seq2seq/attention_decoder), which is now outdated.
Tensorflow 1.0's [new seq2seq library](https://www.tensorflow.org/api_guides/python/contrib.seq2seq#Attention) probably provides a way to do this (as well as beam search) more elegantly and efficiently in the future.

## How to run

### For Abstractive model

1. Download the pretrained zip file

2. After extracting the zip file, there will be folder with the same name as the zip file. Rename it to '0pretrained_model', and place it in the SummarizeModel directory

3. We will need Stanford CoreNLP to tokenize the data. Download it *[here](https://stanfordnlp.github.io/CoreNLP/)*, unzip it, and place the folder 'stanford-corenlp-4.0.0' in SummarizeModel directory.

4. `decode.py` uses the Python package pyrouge to run ROUGE evaluation. pyrouge provides an easier-to-use interface for the official Perl ROUGE package, which you must install for pyrouge to work.

5. Install pyrouge by running `cd pyrouge && python setup.py install`

6. Download a directory called ROUGE-1.5.5 from *[here](https://github.com/andersjo/pyrouge)*

7. Tell pyrouge the ROUGE path with this command: `pyrouge_set_rouge_path /absolute/path/to/ROUGE-1.5.5/directory`

8. To test if pyrouge is configured correctly, run: `python -m pyrouge.test`

10. Place the text to summarize in /IO/in.txt

11. Run `get_summ_abs.sh` for Summarization, output will be placed in IO/out.txt

### For Extractive model

1. Install summa package for extractive summarization by running `pip install summa`

2. Place the text to summarize in /IO/in.txt

3. Run `get_summ_ext.sh` for Summarization, output will be placed in IO/out.txt

**More Information about running the abstractive model for custom input can be found here** *[How to use the pretrain model?](https://github.com/abisee/pointer-generator/issues/77#issuecomment-367723906)*
