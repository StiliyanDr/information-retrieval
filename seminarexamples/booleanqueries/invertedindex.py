from collections import defaultdict


class InvertedIndex:
    """
    Represents an inverted index for a corpus of documents (files).
    """
    def __init__(self, corpus):
        """
        :param corpus: a PlaintextCorpusReader instance representing the
        corpus for which the index is built.
        """
        self.__occurrences = defaultdict(list)

        for index, file in enumerate(corpus.fileids()):
            for term in self.__class__.__terms_in(file, corpus):
                term_occurrences = self.__occurrences[term]

                if (not (term_occurrences and
                         term_occurrences[-1] == index)):
                    term_occurrences.append(index)

    @staticmethod
    def __terms_in(file, corpus):
        return (token.lower()
                for token in corpus.words(file)
                if (token.isalpha()))

    def occurrences_of(self, term, default=[]):
        """
        :param term: a str - the term whose occurrences to look up.
        :param default: the value to return if `term` is not one of the
        terms in the corpus. Defaults to an empty list.
        :returns: a list of ints - the term's corresponding posting
        list.
        """
        return self.__occurrences.get(term, default)

    def terms(self):
        """
        :returns: a generator of strs - the index's terms.
        """
        return iter(self.__occurrences.keys())
