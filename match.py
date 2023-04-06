def match(x1, x2):
    x1 = x1.lower()
    x2 = x2.lower()
    # if one of the xs is only one word...
    if ' ' not in x1 and ' ' not in x2:
        # if x1 and x2 are BOTH only one word...
        if ' ' not in x1 and ' ' not in x2:
            # if they are 3 or more characters
            # different, it's not a good match.
            # else, anything above 80% is good
            difference = abs(len(x1)-len(x2))
            if difference > 3:
                return False
            return SequenceMatcher(a=x1, b=x2).ratio() > .8
        else:
            # if one x is one word but the other
            # is not, it can't be a good match.
            return False
    else:
        # if both are multiple words, we need to split them.
        x1_words, x2_words = x1.split(' '), x2.split(' ')
        # not a good match if there are too many words in one.
        if len(x1_words) != len(x2_words):
            return False
        # match each word
        matches = []
        for a, b in zip(x1_words, x2_words):
            matches.append(SequenceMatcher(a=a, b=b).ratio())
        # we have a good match if the average ratio is better than 80%
        return sum(matches)/len(matches) > .8
