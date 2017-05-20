from gensim.models.keyedvectors import KeyedVectors

model = KeyedVectors.load_word2vec_format('../data/text8-vector.bin', binary=True)
model.save_word2vec_format('../data/text8-vector.txt', binary=False)
