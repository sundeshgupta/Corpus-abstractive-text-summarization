#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
import re
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

# Finding Extractive Fragment

def extractive_fragment(article, summary):
    F = []
    i = 0
    j = 0
    p = len(article)
    q = len(summary)
    while i < q:
        f = []
        while j < p:
            if summary[i] == article[j]:
                tmp_i = i
                tmp_j = j
                while tmp_i < q and tmp_j < p and summary[tmp_i] == article[tmp_j]:
                    tmp_i += 1
                    tmp_j += 1
                if len(f) < (tmp_i - i):
                    f = summary[i:tmp_i]
                j = tmp_j
            else:
                j += 1
        i = i + max(len(f), 1)
        j = 0
        F.append(f)
    return F

# Plotting Graph

def plot(data, title, name):
    x = []
    y = []
    cur = 0
    for key in sorted(data):
        x.append(key)
        cur += data[key]
        y.append(cur)
        
    plt.plot(x, y)
    plt.title(title)
    plt.savefig(name, dpi=300, bbox_inches='tight')
    plt.show()

# CNN Dataset

cnn = tfds.load('cnn_dailymail')

cnn = cnn['train']

vocab_article = set()
vocab_summary = set()

cnt = 0
sentence = 0
word_article = 0
word_highlight = 0
comp_ratio = 0
ext_coverage = 0
ext_density = 0

mean_word_article = {}
mean_word_highlight = {}
mean_cmp_ratio = {}
mean_ext_coverage = {}
mean_ext_density = {}
  
for i in cnn:
    
    cnt += 1
        
    highlight = i['highlights']
    article = i['article']
    
    highlight = np.array(highlight).tolist().decode("utf-8")
    article = np.array(article).tolist().decode("utf-8")
    
#     print(highlight, article)
    
    highlight = highlight.split('\n')
    
    r = len(highlight)
    sentence += r
    
    article = article.split(' ')
    for i in range(r):
        highlight[i] = highlight[i].split(' ')
    
    article = [re.sub('[^a-zA-Z0-9]',' ',char.lower()).replace(' ', '') for char in article]
    article = [char for char in article if char != '']
    
    for i in range(r):
        highlight[i] = [re.sub('[^a-zA-Z]',' ',char.lower()).replace(' ', '') for char in highlight[i]]
        highlight[i] = [char for char in highlight[i] if char != '']
    
    for j in article:
        vocab_article.add(j)
    
    p = len(article)
    
    word_article += p
    
    summary = []
    
    for i in range(r):
        q = len(highlight[i])
        for word in highlight[i]:
            summary.append(word)
        word_highlight += q
        
    m = len(summary)
    
    comp_ratio += (p/m)
    for j in summary:
        vocab_summary.add(j)
    F = extractive_fragment(article, summary)
    cov = 0
    den = 0
    for f in F:
        cov += len(f)
        den += len(f) * len(f)
    cov = cov / m
    den = den / m
    ext_coverage += cov
    ext_density += den
    
    if round(p/m, 2) in mean_cmp_ratio:
        mean_cmp_ratio[round(p/m, 2)] += 1
    else:
        mean_cmp_ratio[round(p/m, 2)] = 1
    
    if p in mean_word_article:
        mean_word_article[p] += 1
    else:
        mean_word_article[p] = 1
    
    if m in mean_word_highlight:
        mean_word_highlight[m] += 1
    else:
        mean_word_highlight[m] = 1
    
    if round(cov, 2) in mean_ext_coverage:
        mean_ext_coverage[round(cov, 2)] += 1
    else:
        mean_ext_coverage[round(cov, 2)] = 1
        
    if round(den, 2) in mean_ext_density:
        mean_ext_density[round(den, 2)] += 1
    else:
        mean_ext_density[round(den, 2)] = 1

    if cnt % 10000 == 0:
        print(cnt)
    
# print(len(vocab_article), len(vocab_summary))
    
comp_ratio = comp_ratio / cnt
word_highlight = word_highlight / cnt
ext_coverage = ext_coverage / cnt
ext_density = ext_density / cnt
word_article = word_article / cnt
sentence = sentence / cnt

common = 0
for word in vocab_summary:
    if word in vocab_article:
        common += 1
    
# print(common)
# print(sentence, word_article, word_highlight, comp_ratio, ext_coverage, ext_density)

print("Number of articles-summary pairs: " + str(cnt))
print("Number of distinct words in article: " + str(len(vocab_article)))
print("Number of distinct words in summary: " + str(len(vocab_summary)))
print("Number of distinct words common in article and summary: " + str(common))
print("Mean number of word in summary: " + str(word_highlight))
print("Mean number of word in article: " + str(word_article))
print("Mean number of sentences per article: " + str(sentence))
print("Mean compression ratio: " + str(comp_ratio))
print("Mean extractive fragment coverage: " + str(ext_coverage))
print("Mean extractive fragment density: " + str(ext_density))
    
plot(mean_ext_coverage, 'Extractive fragment coverage', 'cnn_mean_ext_coverage.png')
plot(mean_ext_density, 'Extractive fragment density', 'cnn_mean_ext_density.png')
plot(mean_word_highlight, 'Number of word in summary', 'cnn_mean_word_highlight.png')
plot(mean_word_article, 'Number of word in article', 'cnn_mean_word_article.png')
plot(mean_cmp_ratio, 'Compression Ratio', 'cnn_mean_cmp_ratio.png')

# Gigaword Dataset

gigaword = tfds.load('gigaword')

gigaword = gigaword['train']

vocab_article = set()
vocab_summary = set()

cnt = 0
sentence = 0
word_article = 0
word_highlight = 0
comp_ratio = 0
ext_coverage = 0
ext_density = 0

mean_word_article = {}
mean_word_highlight = {}
mean_cmp_ratio = {}
mean_ext_coverage = {}
mean_ext_density = {}

for i in gigaword:
    
    cnt += 1
        
    highlight = i['summary']
    article = i['document']
    
    highlight = np.array(highlight).tolist().decode("utf-8")
    article = np.array(article).tolist().decode("utf-8")
    
#     print(highlight, article)
    
    highlight = highlight.split('\n')
    
    r = len(highlight)
    sentence += r
    
    article = article.split(' ')
    for i in range(r):
        highlight[i] = highlight[i].split(' ')
    
    article = [re.sub('[^a-zA-Z0-9]',' ',char.lower()).replace(' ', '') for char in article]
    article = [char for char in article if char != '']
    
    for i in range(r):
        highlight[i] = [re.sub('[^a-zA-Z]',' ',char.lower()).replace(' ', '') for char in highlight[i]]
        highlight[i] = [char for char in highlight[i] if char != '']
    
    for j in article:
        vocab_article.add(j)
    
    p = len(article)
    
    word_article += p
    
    summary = []
    
    for i in range(r):
        q = len(highlight[i])
        for word in highlight[i]:
            summary.append(word)
        word_highlight += q
        
    m = len(summary)
    
    comp_ratio += (p/m)
    for j in summary:
        vocab_summary.add(j)
    F = extractive_fragment(article, summary)
    cov = 0
    den = 0
    for f in F:
        cov += len(f)
        den += len(f) * len(f)
    cov = cov / m
    den = den / m
    ext_coverage += cov
    ext_density += den
    
    if round(p/m, 2) in mean_cmp_ratio:
        mean_cmp_ratio[round(p/m, 2)] += 1
    else:
        mean_cmp_ratio[round(p/m, 2)] = 1
    
    if p in mean_word_article:
        mean_word_article[p] += 1
    else:
        mean_word_article[p] = 1
    
    if m in mean_word_highlight:
        mean_word_highlight[m] += 1
    else:
        mean_word_highlight[m] = 1
    
    if round(cov, 2) in mean_ext_coverage:
        mean_ext_coverage[round(cov, 2)] += 1
    else:
        mean_ext_coverage[round(cov, 2)] = 1
        
    if round(den, 2) in mean_ext_density:
        mean_ext_density[round(den, 2)] += 1
    else:
        mean_ext_density[round(den, 2)] = 1

    if cnt % 10000 == 0:
        print(cnt)
    
# print(len(vocab_article), len(vocab_summary))
    
comp_ratio = comp_ratio / cnt
word_highlight = word_highlight / cnt
ext_coverage = ext_coverage / cnt
ext_density = ext_density / cnt
word_article = word_article / cnt
sentence = sentence / cnt

common = 0
for word in vocab_summary:
    if word in vocab_article:
        common += 1
    
# print(common)
# print(sentence, word_article, word_highlight, comp_ratio, ext_coverage, ext_density)

print("Number of articles-summary pairs: " + str(cnt))
print("Number of distinct words in article: " + str(len(vocab_article)))
print("Number of distinct words in summary: " + str(len(vocab_summary)))
print("Number of distinct words common in article and summary: " + str(common))
print("Mean number of word in summary: " + str(word_highlight))
print("Mean number of word in article: " + str(word_article))
print("Mean number of sentences per article: " + str(sentence))
print("Mean compression ratio: " + str(comp_ratio))
print("Mean extractive fragment coverage: " + str(ext_coverage))
print("Mean extractive fragment density: " + str(ext_density))

plot(mean_ext_coverage, 'Extractive fragment coverage', 'giga_mean_ext_coverage.png')
plot(mean_ext_density, 'Extractive fragment density', 'giga_mean_ext_density.png')
plot(mean_word_highlight, 'Number of word in summary', 'giga_mean_word_highlight.png')
plot(mean_word_article, 'Number of word in article', 'giga_mean_word_article.png')
plot(mean_cmp_ratio, 'Compression Ratio', 'giga_mean_cmp_ratio.png')

# Free Press Journal Dataset 

tree = ET.parse('freepressjournal.xml')
root = tree.getroot()

vocab_article = set()
vocab_summary = set()

cnt = 0
sentence = 0
word_article = 0
word_highlight = 0
comp_ratio = 0
ext_coverage = 0
ext_density = 0

mean_word_article = {}
mean_word_highlight = {}
mean_cmp_ratio = {}
mean_ext_coverage = {}
mean_ext_density = {}
    
for i in range(0, len(root), 4):
    
    highlight = root[i+1].text
    article = root[i+2].text
#     print(highlight, article)
    
    highlight = highlight.split('\n')
    
    r = len(highlight)
    
    article = article.split(' ')
    for i in range(r):
        highlight[i] = highlight[i].split(' ')
    
    article = [re.sub('[^a-zA-Z0-9]',' ',char.lower()).replace(' ', '') for char in article]
    article = [char for char in article if char != '']
    
    for i in range(r):
        highlight[i] = [re.sub('[^a-zA-Z]',' ',char.lower()).replace(' ', '') for char in highlight[i]]
        highlight[i] = [char for char in highlight[i] if char != '']
    
    p = len(article)
        
    summary = []
    
    for i in range(r):
        q = len(highlight[i])
        for word in highlight[i]:
            summary.append(word)
        
    m = len(summary)
    
    F = extractive_fragment(article, summary)
    cov = 0
    den = 0
    for f in F:
        cov += len(f)
        den += len(f) * len(f)
    cov = cov / m
    den = den / m
        
    sentence += r
    word_highlight += m
    word_article += p
    
    for j in article:
        vocab_article.add(j)
    
    for j in summary:
        vocab_summary.add(j)
    
    cnt += 1
    
    comp_ratio += (p/m)
    
    
    ext_coverage += cov
    ext_density += den
    
    if round(p/m, 2) in mean_cmp_ratio:
        mean_cmp_ratio[round(p/m, 2)] += 1
    else:
        mean_cmp_ratio[round(p/m, 2)] = 1
    
    if p in mean_word_article:
        mean_word_article[p] += 1
    else:
        mean_word_article[p] = 1
    
    if m in mean_word_highlight:
        mean_word_highlight[m] += 1
    else:
        mean_word_highlight[m] = 1
    
    if round(cov, 2) in mean_ext_coverage:
        mean_ext_coverage[round(cov, 2)] += 1
    else:
        mean_ext_coverage[round(cov, 2)] = 1
        
    if round(den, 2) in mean_ext_density:
        mean_ext_density[round(den, 2)] += 1
    else:
        mean_ext_density[round(den, 2)] = 1
    
comp_ratio = comp_ratio / cnt
word_highlight = word_highlight / cnt
ext_coverage = ext_coverage / cnt
ext_density = ext_density / cnt
word_article = word_article / cnt
sentence = sentence / cnt

common = 0
for word in vocab_summary:
    if word in vocab_article:
        common += 1
    
print("Number of articles-summary pairs: " + str(cnt))
print("Number of distinct words in article: " + str(len(vocab_article)))
print("Number of distinct words in summary: " + str(len(vocab_summary)))
print("Number of distinct words common in article and summary: " + str(common))
print("Mean number of word in summary: " + str(word_highlight))
print("Mean number of word in article: " + str(word_article))
print("Mean number of sentences per article: " + str(sentence))
print("Mean compression ratio: " + str(comp_ratio))
print("Mean extractive fragment coverage: " + str(ext_coverage))
print("Mean extractive fragment density: " + str(ext_density))
    
plot(mean_ext_coverage, 'Extractive fragment coverage', 'free_mean_ext_coverage.png')
plot(mean_ext_density, 'Extractive fragment density', 'free_mean_ext_density.png')
plot(mean_word_highlight, 'Number of word in summary', 'free_mean_word_highlight.png')
plot(mean_word_article, 'Number of word in article', 'free_mean_word_article.png')
plot(mean_cmp_ratio, 'Compression Ratio', 'free_mean_cmp_ratio.png')

# Hindustan Times Dataset

tree = ET.parse('HindustanTimes.xml')
root = tree.getroot()

vocab_article = set()
vocab_summary = set()

cnt = 0
sentence = 0
word_article = 0
word_highlight = 0
comp_ratio = 0
ext_coverage = 0
ext_density = 0

mean_word_article = {}
mean_word_highlight = {}
mean_cmp_ratio = {}
mean_ext_coverage = {}
mean_ext_density = {}

for i in range(0, len(root), 4):
    
    highlight = root[i+1].text
    article = root[i+2].text
    
#     print(highlight, article)
    
    highlight = highlight.split('\n')
    
    r = len(highlight)
    
    article = article.split(' ')
    for i in range(r):
        highlight[i] = highlight[i].split(' ')
    
    article = [re.sub('[^a-zA-Z0-9]',' ',char.lower()).replace(' ', '') for char in article]
    article = [char for char in article if char != '']
    
    for i in range(r):
        highlight[i] = [re.sub('[^a-zA-Z]',' ',char.lower()).replace(' ', '') for char in highlight[i]]
        highlight[i] = [char for char in highlight[i] if char != '']
    
    p = len(article)
        
    summary = []
    
    for i in range(r):
        q = len(highlight[i])
        for word in highlight[i]:
            summary.append(word)
        
    m = len(summary)
    
    F = extractive_fragment(article, summary)
    cov = 0
    den = 0
    for f in F:
        cov += len(f)
        den += len(f) * len(f)
    cov = cov / m
    den = den / m
    
    sentence += r
    word_highlight += m
    word_article += p
    
    for j in article:
        vocab_article.add(j)
    
    for j in summary:
        vocab_summary.add(j)
    
    cnt += 1
    
    comp_ratio += (p/m)
    
    
    ext_coverage += cov
    ext_density += den
    
    if round(p/m, 2) in mean_cmp_ratio:
        mean_cmp_ratio[round(p/m, 2)] += 1
    else:
        mean_cmp_ratio[round(p/m, 2)] = 1
    
    if p in mean_word_article:
        mean_word_article[p] += 1
    else:
        mean_word_article[p] = 1
    
    if m in mean_word_highlight:
        mean_word_highlight[m] += 1
    else:
        mean_word_highlight[m] = 1
    
    if round(cov, 2) in mean_ext_coverage:
        mean_ext_coverage[round(cov, 2)] += 1
    else:
        mean_ext_coverage[round(cov, 2)] = 1
        
    if round(den, 2) in mean_ext_density:
        mean_ext_density[round(den, 2)] += 1
    else:
        mean_ext_density[round(den, 2)] = 1
    

# print(len(vocab_article), len(vocab_summary))
    
comp_ratio = comp_ratio / cnt
word_highlight = word_highlight / cnt
ext_coverage = ext_coverage / cnt
ext_density = ext_density / cnt
word_article = word_article / cnt
sentence = sentence / cnt

common = 0
for word in vocab_summary:
    if word in vocab_article:
        common += 1
    
# print(common)
# print(sentence, word_article, word_highlight, comp_ratio, ext_coverage, ext_density)

print("Number of articles-summary pairs: " + str(cnt))
print("Number of distinct words in article: " + str(len(vocab_article)))
print("Number of distinct words in summary: " + str(len(vocab_summary)))
print("Number of distinct words common in article and summary: " + str(common))
print("Mean number of word in summary: " + str(word_highlight))
print("Mean number of word in article: " + str(word_article))
print("Mean number of sentences per article: " + str(sentence))
print("Mean compression ratio: " + str(comp_ratio))
print("Mean extractive fragment coverage: " + str(ext_coverage))
print("Mean extractive fragment density: " + str(ext_density))

plot(mean_ext_coverage, 'Extractive fragment coverage', 'hindustan_mean_ext_coverage.png')
plot(mean_ext_density, 'Extractive fragment density', 'hindustan_mean_ext_density.png')
plot(mean_word_highlight, 'Number of word in summary', 'hindustan_mean_word_highlight.png')
plot(mean_word_article, 'Number of word in article', 'hindustan_mean_word_article.png')
plot(mean_cmp_ratio, 'Compression Ratio', 'hindustan_mean_cmp_ratio.png')
