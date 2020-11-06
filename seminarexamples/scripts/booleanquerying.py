import os
import sys

from seminarexamples.booleanqueries.searcher import Searcher


def make_queries_for(corpus):
    searcher = Searcher(corpus)
    query = read_query()

    while (query is not None):
        print_results(list(searcher(query)))
        query = read_query()


def read_query():
    terms = input("Please enter a list of terms "
                  "delimiterd by comma (or exit):")

    return ((t.strip()
             for t in terms.split(","))
            if (terms != "exit")
            else None)


def print_results(document_names):
    if (document_names):
        print("All terms were found in the following documents:",
              *document_names,
              sep="\n")
    else:
        print("No documents contain all the terms.")


if (__name__ == "__main__"):
    if (len(sys.argv) == 2 and os.path.isdir(sys.argv[1])):
        corpus = sys.argv[1]
        make_queries_for(corpus)
    else:
        print(sys.argv[0], "expects a corpus root!")
