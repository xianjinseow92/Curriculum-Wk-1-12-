# Sample Lesson Plan
**WordEmbeddings.ppt** (60-80 minutes): Counts, TF-IDF, word2vec, GloVe, how embeddings are evaluated, and a brief nod to contextualized word embeddings.

**Word Embeddings.ipynb** (20-30 mins): Code examples of count vectorizatin and tf-idf with sklearn and Gensim, creating and loading word2vec models with Gensim, and loading GloVe vectors into Gensim.  Student exercises include exploration of the word vector space and it's structure.

**Transfer_Learning.pptx** (30 mins): Overview on transfer learning and how it's typically applied to NLP with pre-trained word embeddings. 

**NeuralNet_Features_TransferLearning.ipynb** (30 mins): This notebook contains a lot of extra content building conceptual intuition for neural networks as feature learners as well as giving keras examples, but for this lecture the focus can be on the sections toward the end -- an applied example of transfer learning with RNNs for a text classification task.


# Learning Objectives

Students can

* Explain vector representations of words describe how vector representations can be used to store meaning.

* Summarize how vector representations of words can be created using Language Models/Semi-Supervised learning.

* Summarize the gist of modern approaches for building word vectors.
* Outline common uses of word vectors and apply them in code:
  * Compute simple count/tf-idf vectors with sklearn and Gensim  
  * Use Gensim to train a custom word2vec model from a corpus of text.
  * Load pre-trained embeddings for both word2vec and GloVe
  * Explore relationships between words in a corpus.

* Understand the transfer learning framework and how it can concretely be applied to machine learning problems in NLP.


# Additional Resources
* Great Blog Post on Word2Vec Intuition: http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/

* GloVe Paper: https://nlp.stanford.edu/pubs/glove.pdf

* Word2Vec Paper: https://arxiv.org/abs/1310.4546

* Stanford Lecture notes on word vectors: http://web.stanford.edu/class/cs224n/lectures/lecture2.pdf

* TensorFlow tutorial on word vectors: https://www.tensorflow.org/tutorials/representation/word2vec