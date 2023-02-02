import subprocess
import re
# call bash; variable=bash string output of queue


def queuedata():
    str1 = subprocess.run(["qs"])
    return str1


#
def findopennode_queuedata():
    #regex fgor any number but 32?
    #make counter to count node # when checking
    for i in range(1-14):
        open_state_pattern = re.compile('all.q@n1\wBIP\w32^*/32')
    match_data = open_state_pattern.start(queuedata())
    ##catch no match here and return to another function
    ##queue : line under all.q@n# when job running, then dashes and so on
    #states 1 at end of job line, au at end of nodeline, ID at start, # of nodes used 0/32 r?, load_avg 0.00
    #find q@n# ---> 0/32 -> save node num --> return tup node # and TRUE/FALSE
    return match_data
##one function to find open computer n# one function to find node #/32?

def determine node number():
    list of possible pos indexed in order of node number
    if matchdata == list:
        node#=indexofTRUE
        functiontoinputgjf(node#)
    return node#

def functiontoinputgjf():
    #rung16 file_name node_num
    subprocess.run(["rung16",gjf_name,node_num])


