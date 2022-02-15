import io

stopwords_file = 'vietnamese-stopwords.txt'


def remove_stopwords(tokens):
    stopwords = set(line.strip() for line in open(stopwords_file))
    result = [token for token in tokens if token not in stopwords]
    return result
