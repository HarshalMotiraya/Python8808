from gensim.models import Word2Vec


MODEL_PATH = "models/word2vec.model"


def show_embedding(model, word):
    if word not in model.wv:
        print(f"\n'{word}' not found.")
        return

    vector = model.wv[word]

    print("\n" + "=" * 50)
    print(f"WORD: {word}")
    print("=" * 50)

    print(f"Embedding size: {len(vector)}")

    print("\nFirst 10 values:")
    print(vector[:10])


def show_similar_words(model, word):
    if word not in model.wv:
        print(f"\n'{word}' not found.")
        return

    print("\n" + "=" * 50)
    print(f"WORDS SIMILAR TO: {word}")
    print("=" * 50)

    results = model.wv.most_similar(word, topn=5)

    for similar_word, score in results:
        print(f"{similar_word:12} {score:.4f}")


def main():

    model = Word2Vec.load(MODEL_PATH)

    print("\nWORD EMBEDDING DEMO")

    word = input("\nEnter a word: ").lower().strip()

    show_embedding(model, word)

    show_similar_words(model, word)


if __name__ == "__main__":
    main()