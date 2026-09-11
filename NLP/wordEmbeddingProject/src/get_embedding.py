from gensim.models import Word2Vec


def get_word_embedding(model_path, word):
    model = Word2Vec.load(model_path)

    if word not in model.wv:
        print(f"'{word}' is not in the vocabulary.")
        return

    vector = model.wv[word]

    print(f"\nWord: {word}")
    print(f"Embedding dimensions: {len(vector)}")
    print("\nEmbedding:")
    print(vector)


if __name__ == "__main__":
    get_word_embedding(
        "models/word2vec.model",
        "dog"
    )