from requests import delete


def chop(list):
    del list[0]
    del list[-1]
    