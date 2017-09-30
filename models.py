import nltk


class Matchable():
    """
    Represent an object that can be matched to another one:
    * Allow mistakes
    * Match plural & singular thanks to stemming
    """
    def __init__(self, string):
        self.string = string
        self.normalized = self.normalize(string)

    def normalize(self, string):
        words = self.tokenize(string)
        return ' '.join([self.__stemmer__().stem(w) for w in words])

    @classmethod
    def tokenize(self, string):
        """Tokenization divide a string into smaller elements"""
        return nltk.tokenize.wordpunct_tokenize(string.lower().strip())

    def __stemmer__(self):
        """Stemming allow to match plural with singular"""
        return nltk.stem.PorterStemmer()

    def fuzzy_match(self, candidate, max_dist=1):
        return nltk.edit_distance(self.normalized,
                                  self.normalize(candidate)
                                  ) <= max_dist
