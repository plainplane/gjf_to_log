import subprocess
import re
# call bash; variable=bash string output of queue


def queuedata():
    str1 = subprocess.run(["qs"])
    return str1


def findopenstate_queuedata():
    open_state_pattern = re.compile('somepattern')
    match_data = open_state_pattern.start(queuedata())
    ##catch no match here and return to another function
    return match_data


def elif_queuedata():
    list of possible pos indexed in order of node number
    search_queuedata()


