class Network:

    def __init__(self, biases, weights):
        self.biases = biases
        self.weights = weights

    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a) + b)
        return a