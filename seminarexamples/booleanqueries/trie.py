
class Trie:
    def __init__(self, words=None):
        self.__transitions = [{}]
        self.__final_states = set([0])

        if (words is not None):
            for w in words:
                self.__add_word(w)

    def __add_word(self, w):
        state, i = self.__traverse(w)

        while (i < len(w)):
            new_state = len(self.__transitions)
            self.__transitions.append({})
            transitions = self.__transitions[state]
            transitions[w[i]] = new_state
            state = new_state
            i += 1

        self.__final_states.add(state)

    def __traverse(self, word):
        state = 0
        i = 0

        while (i < len(word) and
               word[i] in self.__transitions[state]):
            state = self.__transitions[state][word[i]]
            i += 1

        return (state, i)

    def __contains__(self, word):
        state, i = self.__traverse(word)

        return (i == len(word) and
                state in self.__final_states)

    def words_with_prefix(self, p):
        state, i = self.__traverse(p)

        return ([f"{p}{w}"
                 for w in self.__words_from_state(state)]
                if (i == len(p))
                else [])

    def __words_from_state(self, s):
        assert s < len(self.__transitions)

        answer = []

        if (s in self.__final_states):
            answer.append("")

        transitions = self.__transitions[s]

        for c, next_state in transitions.items():
            answer.extend(
                f"{c}{w}"
                for w in self.__words_from_state(next_state)
            )

        return answer
