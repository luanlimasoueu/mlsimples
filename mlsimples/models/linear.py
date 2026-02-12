class RegressaoLinearSimples:
    def __init__(self):
        self.beta_0 = None
        self.beta_1 = None

    def fit(self, X, Y):
        n = len(X)
        media_x = sum(X) / n
        media_y = sum(Y) / n

        numerador = 0
        denominador = 0

        for i in range(n):
            numerador += (X[i] - media_x) * (Y[i] - media_y)
            denominador += (X[i] - media_x) ** 2

        self.beta_1 = numerador / denominador
        self.beta_0 = media_y - self.beta_1 * media_x

    def predict(self, X):
        return [self.beta_0 + self.beta_1 * x for x in X]
