from gensim.models import Word2Vec


def find_similar_words(model_path, word, number=5):
    model = Word2Vec.load(model_path)

    if word not in model.wv:
        print(f"'{word}' is not in the vocabulary.")
        return

    results = model.wv.most_similar(
        word,
        topn=number
    )

    print(f"\nWords similar to '{word}':\n")

    for similar_word, score in results:
        print(f"{similar_word:10} {score:.4f}")


if __name__ == "__main__":
    find_similar_words(
        "models/word2vec.model",
        "dog"
    )