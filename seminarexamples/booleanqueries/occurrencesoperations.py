
def intersection_of(lhs, rhs):
    """
    Intersects two posting lists.
    """
    i = 0
    j = 0
    intersection = []

    while (i < len(lhs) and j < len(rhs)):
        if (lhs[i] == rhs[j]):
            intersection.append(lhs[i])
            i += 1
            j += 1
        elif (lhs[i] < rhs[j]):
            i += 1
        else:
            j += 1

    return intersection


def intersection_of_all(posting_lists):
    """
    Intersects multiple posting lists. 
    """
    posting_lists = _to_list(posting_lists)

    if (posting_lists):
        posting_lists.sort(key=len)
        answer = posting_lists[0]

        for list in posting_lists[1:]:
            answer = intersection_of(answer, list)

        return answer
    else:
        return []


def _to_list(iterable):
    return (list(iterable)
            if (not isinstance(iterable, list))
            else iterable)


def union_of(lhs, rhs):
    """
    Computes the union of two posting lists.
    """
    i = 0
    j = 0
    answer = []

    while (i < len(lhs) or j < len(rhs)):
        if (j == len(rhs) or
            (i < len(lhs) and lhs[i] < rhs[j])):
            answer.append(lhs[i])
            i += 1
        elif (i == len(lhs) or rhs[j] < lhs[i]):
            answer.append(rhs[j])
            j += 1
        else:
            answer.append(lhs[i])
            i += 1
            j += 1

    return answer


def union_of_all(posting_lists):
    """
    Computes the union of multiple posting lists. 
    """
    answer = []

    for p in posting_lists:
        answer = union_of(answer, p)

    return answer


def difference_of(lhs, rhs):
    """
    Computes the difference of two posting lists, that is, the elements
    in the first list which are not elements in the second list.
    """
    i = 0
    j = 0
    answer = []

    while (i < len(lhs)):
        if (j == len(rhs) or lhs[i] < rhs[j]):
            answer.append(lhs[i])
            i += 1
        elif (rhs[j] < lhs[i]):
            j += 1
        else:
            i += 1

    return answer
