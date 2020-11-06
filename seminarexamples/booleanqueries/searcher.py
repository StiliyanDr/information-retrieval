from nltk.corpus import PlaintextCorpusReader
import nltk

from seminarexamples.booleanqueries import occurrencesoperations as ops
from seminarexamples.booleanqueries.invertedindex import InvertedIndex
from seminarexamples.booleanqueries.trie import Trie


class Searcher:
    """
    An object that is able to do AND searches of multiple terms which
    optionally have a trailing *.
    """
    __DOCUMENT_PATTERN = ".*[.]txt"

    def __init__(self, corpus_root, pattern=None):
        """
        :param corpus_root: a str - the path of the root of the corpus
        with documents to search.
        :param pattern: a str - a regular expression selecting the
        documents within the corpus which to include. Defaults to
        DOCUMENT_PATTERN.
        """
        if (pattern is None):
            pattern = self.__class__.__DOCUMENT_PATTERN

        corpus = PlaintextCorpusReader(
            corpus_root,
            fileids=pattern
        )
        self.__file_names = corpus.fileids()
        self.__index = InvertedIndex(corpus)
        self.__trie = Trie(self.__index.terms())

    def __call__(self, terms):
        """
        Finds the documents which contain each of the terms.

        :param terms: an iterable of strs - the terms for which to
        perform an AND search. They are assumed to either contain no
        * or end with a single one.
        :returns: an iterable of strs - the names of the documents
        found.
        """
        indices = ops.intersection_of_all(
            self.__posting_lists_of_expanded(terms)
        )

        return (self.__file_names[i]
                for i in indices)

    def __posting_lists_of_expanded(self, terms):
        for term in terms:
            if (not term.endswith("*")):
                yield self.__index.occurrences_of(term)
            else:
                lists = (self.__index.occurrences_of(t)
                         for t in self.__expand(term))
                yield ops.union_of_all(lists)

    def __expand(self, term):
        return self.__trie.words_with_prefix(
            term.rstrip("*")
        )
