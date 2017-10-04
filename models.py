import nltk
from isodate import parse_duration, parse_date


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


class Recipe():
    def __init__(self, attrs):
        self.ingredients = Matchable.tokenize(attrs["ingredients"])
        self.description = attrs["description"]

        self.name = attrs.get("name", None)
        self.url = attrs.get("url", None)
        self.image = attrs.get("image", None)
        self.recipe_yield = attrs.get("recipeYield", None)

        if attrs.get("datePublished", None):
            self.date_published = parse_date(attrs["datePublished"])

        if attrs.get("prepTime", None):
            self.preparation_duration = \
              parse_duration(attrs["prepTime"]).seconds
        else:
            self.preparation_duration = None

        if attrs.get("cookTime", None):
            self.cooking_duration = parse_duration(attrs["cookTime"]).seconds
        else:
            self.cooking_duration = None

    def difficulty(self):
        if not self.preparation_duration or not self.cooking_duration:
            return "Unkown"

        total_duration = self.preparation_duration + self.cooking_duration
        if total_duration > 60 * 60:
            return "Hard"
        elif total_duration > 30 * 60:
            return "Medium"
        elif total_duration > 0:
            return "Easy"
        else:
            return "Unkown"

    def has_chili(self):
        def has_chili_for(ingredient):
            return Matchable(ingredient).fuzzy_match("chili")

        has_chili = filter(has_chili_for, self.ingredients)
        return len(has_chili) >= 1
