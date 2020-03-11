# Animorphs Authorship Authenticity Analysis
by Ethan Henley

This project was completed as a part of General Assembly's Data Science Intensive.

---

### Project Notebooks
- [01 Data Collection, Cleaning, and EDA](./code/01_collection_cleaning_eda.ipynb)
- [02 Word2Vec Vectorization](./code/02_w2v.ipynb)
- [03 Support Vector Machine on Word2Vec](./code/03_svm_on_w2v.ipynb)
- [04 Naive Bayes and SVM on Wordcounts](./code/04_classifiers_on_words.ipynb)

### Contents
- [Problem Statement](#Problem-Statement)
- [Executive Summary](#Executive-Summary)
    - [Collection & EDA](#Collection-&-EDA)
    - [Unsupervised Modeling](#Unsupervised-Modeling)
    - [Transfer Learning Supervised Modeling](#Transfer-Learning-Supervised-Modeling)
    - [Alternate Supervised Modeling](#Alternate-Supervised-Modeling)
- [Conclusion](#Conclusion)
- [Sources](#Sources)

---

## Problem Statement

When authorship is uncertain, specific word choices and text patterns can be used to determine whether or not a text was written by a certain author. We want to develop a model for reading in two large corpuses, one authentically written by an author and one ghostwritten, and predicting which corpus a text belongs to. 

One recent [paper](https://arxiv.org/abs/1911.05652) by Petr Plecháč analyzed the authorship of specific subsections of the play Henry VIII to determine where either of the authors suspected of involvement contributed. Its methodology is not directly applicable to non-poetic texts, as it greatly involves cadence and meter in its modeling process. We will perform similar analysis on another, non-metered corpus to generalize author authenticity analysis.

For this analysis, we will use the Animorphs series, 54 children's science-fiction/fantasy books of which about half were ghostwritten, as our corpus. The model will be specific to this collection of books, but the strategies implemented should be relevant for other authorship analyses. 

We will vectorize words in individual chapters of Animorphs books using Word2Vec against the corpus as a whole, and then take each chapter's average vector and use a Support Vector Machine classifier to delineate author authenticity. The classifier will be scored on accuracy, as the two types of misattribution are similarly undesirable, but we will pay special attention to books in the series we expect to be most 'challenging'—the few authentic books in the latter half of the series and the single ghostwritten book in the first half. Conceptually, our model or process will be able to take in a hypothetical new or heretofore-lost Animorphs book and determine whether or not it was truly written by K. A. Applegate, whose name appears on the cover of each book in the series.

As another component to our essential problem, we are curious about the efficacy of Word2Vec for stylometric analysis. We believe the Animorphs series to be an especially challenging stylometric problem for authorship analysis, as content shifts over time within author categories and may confound signs of author style, and would like to find if Word2Vec is effective in authenticity analysis. To do this, we will treat our W2V results as a baseline and compare against a similar process on simple CountVectorized data. 

---

## Executive Summary

Our process was broken up into 4 major steps: the collection and analysis of the Animorphs corpus, W2V unsupervised modeling, transfer learning off of the W2V results, and separate supervised modeling to compare against the tranfer learning model.

### Collection & EDA

The corpus was gathered from [Richard's Animorphs Forum](https://animorphsforum.com/ebooks/), where the Animorphs series of books is hosted for free access with the blessing of the creator. We use the main series only. Authenicity was taken from [this Wikipedia section](https://en.wikipedia.org/wiki/Animorphs#Ghostwriters). Books were read chapter by chapter using `ebooklib` and `BeautifulSoup`. Chapters were processed, proper nouns and stopwords were removed, and then words were tokenized to develop a corpus. A first look showed what words were most common across the corpus.

### Unsupervised Modeling

Books and chapters were vectorized based on [Milokov et al's Word2Vec algorithm](https://arxiv.org/abs/1301.3781) with the specific vector model generated off of the corpus as a whole. This use of the whole corpus might cause concerns for a model that required an ordinary train/test split, but as should be apparent in the notebooks that follow, we used a leave-one-out supervised modeling strategy for which it is appropriate to generate a vector model off of the entire corpus.

### Transfer Learning Supervised Modeling

Our problem was structured in a way such that we could not do an ordinary train/test split; ideally, our model makes a prediction on a single Animorphs book of unknown authorship, trained on all the other books in the series. In order to simulate this for validation, we adapted the strategy of leave-one-out cross validation, which generates seperate models each trained on all but one data point and then assesses the scores for each individual result to help determine the worthwhileness of a model. This is typically very expensive, but made sense for our dataset of only 54 book-level datapoints. We extrapolated this to leave-one-book-out cross validation for modeling based on chapter, as a model that requires other chapters from the same book to have known authorship to predict authorship of a single chapter would not fit our intended use case.

Ultimately, we determined that the results of the Word2Vec-based transfer learning process were likely not useful for stylometry or authorship analysis—they were more likely swayed by variation in content than in style across the texts, as visible in linearly sequential shifting predicted authenticity probabilities across the first 24 all-authentic books.

### Alternate Supervised Modeling

Because W2V-SVM transfer learning proved insufficient, we ran Naive Bayes and Support Vector Machine classifiers on CountVectorized Animorphs books instead, and found that the wordcount-based SVM was the most accurate predictor on both the corpus as a whole and on individual books. We used the same strategy of leave-one-out validation as before. 

We concluded that, though the Word2Vec-based transfer learning models were not useful for this type of authorship analysis, the count-based SVM was a sufficiently accurate model for authorship analysis.

---

## Conclusion

It is somewhat disappointing that our Word2Vec-based model was outperformed by a simpler count-based model, but not every tool fits every task, and this is evidence that might help resolve disputes over its relevance to stylometry at large. 

That established, our count-based model was effective and accurate, and were a 55th canonical Animorphs book released today in the style of the 54 that preceded and with its authenticity unknown, we believe that the model would be well-suited to assess its authorship.

The Animorphs corpus may be an especially challenging problem for stylometry and authorship detection—it is a series of books with related but progressing content with authorship split mostly sequentially which was edited for consistency by the listed author even when she did not write a book. That an authorship detection model such as this can be established with high accuracy is a testament to the power of natural language processing, even without the involvement of neural networks. 

Many experiments in stylometry use standard, historic corpuses such as 'great' novels, the Federalist Papers, or the works of Shakespeare, but these corpuses are not representative of the diversity of English writing. We recommend that less formal writing—internet posts, film and television scripts, and yes, even children's and middle-grade book series—also be used as standards against which to assess stylometric techniques, and hope that this project shows that sylometry on informal writing can offer unique insights.

---

## Sources
- The Animorphs Book Series by Applegate et al
- [Richard's Animorphs Forum](https://animorphsforum.com/ebooks/)
- [Animorphs on Wikipedia](https://en.wikipedia.org/wiki/Animorphs)
- [EbookLib](https://pypi.org/project/EbookLib/)
- [Relative contributions of Shakespeare and Fletcher in Henry VIII](https://arxiv.org/abs/1911.05652) by Plecháč
- [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781) by Mikolov et al
- [Benchmarking Authorship Attribution Techniques](https://scholarworks.iupui.edu/handle/1805/15938) by Gungor
- [Improving Distributional Similarity with Lessons Learned from Word Embeddings](https://www.aclweb.org/anthology/Q15-1016/) by Levy et al
