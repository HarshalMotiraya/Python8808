from gensim.models import Word2Vec

def load_sentences(file_path):
    sentences = []

    with open(file_path , "r",encoding = "utf-8") as file :
        for line in file:
            words = line.strip().lower().split()

            if words:
                sentences.append(words)

    return sentences


def train_word2vec(sentences):
    model = Word2Vec(
        sentences = sentences,
        vector_size = 100,
        window = 5,
        min_count = 1,
        workers = 1,
        sg = 1,
        epochs = 100
    )
    return model


def main():
    data_path = "data/cleaned_data.txt"
    model_path = "models/word2vec_model"

    sentences = load_sentences(data_path)

    print("traing sentence")
    print(len(sentences))

    model = train_word2vec(sentences)

    model.save(model_path)

    print(f"Model saved to {model_path} ")

if __name__ == "__main__":
    main()

