from panflute import *
import sys

heads = []


def boldToBold(file, _):
    file.replace_keyword("BOLD", Strong(Str("BOLD")))


def sameHeader(elem):
    if isinstance(elem, Header):
        if stringify(elem) in heads:
            sys.stderr.write("Same header!" + stringify(elem))
        else:
            heads.append(stringify(elem))


def makeHeadHigher(elem, _):
    if isinstance(elem, Header) and elem.level >= 3:
        return Header(Str(stringify(elem).upper()), level=elem.level)


if __name__ == "__main__":
    run_filters([sameHeader, makeHeadHigher], prepare=boldToBold)
