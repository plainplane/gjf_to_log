import subprocess
import re
# call bash; variable=bash string output of queue


def queuedata():
    str1 = subprocess.run(["qs"])
    return str1


#
def findopennode_queuedata(node_range_min,node_range_max):
    #regex fgor any number but 32?
    count = 0
    open_nodes= []
    for i in range(1,14):
        count += 1
        open_state_pattern = re.compile(r'all.q@n'+str(i)+'\wBIP\w[0-9]/32')
        if re.match(open_state_pattern,queuedata()):
            open_nodes += count
        if re.match()


    ##catch no match here and return to another function

    #find q@n# ---> 0/32 -> save node num --> return tup node # and TRUE/FALSE
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


