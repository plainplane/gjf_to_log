import subprocess
import re
import time
# call bash; variable=bash string output of queue


def qdata():
    str1 = subprocess.run(["qs"])
    return str1


#
def nodeslist_qdata():
    # node_to_jobnum_pattern= re.compile(r'all.q@n'+str(i)+' *BIP *[1-9]*[1-9]/32(.*)\n\s*[0-9]{5}')
    # node_to_jobnum_string = node_to_jobnum_pattern.group()
    # node_to_jobnum_substrings_bywhitespace = node_to_jobnum_string.split()
    # job_num = int(node_to_jobnum_substrings_bywhitespace[[len(node_to_jobnum_substrings_bywhitespace)]])
    node_num = 0
    individual_node_data = []
    for i in range(1,14):
        time.sleep(30)
        node_num += 1
        open_node_pattern = re.compile(r'all.q@n'+str(i)+' *BIP *[0-9]|[12][0-9]|[3][01]|/32')
        closed_node_pattern = re.compile(r'all.q@n'+str(i)+' *BIP *32/32')

        if re.match(open_node_pattern, queuedata()):
            is_open = True
        if re.match(closed_node_pattern, queuedata()):
            is_open = False

        node_to_endofnodesdata_pattern = re.compile(r'all.q@n' + str(i) + ' *BIP *[1-9]*[1-9]/32(.*)---')
        node_datum = node_to_endofnodesdata_pattern.group(queuedata())


        individual_node_data += [(node_num,is_open,node_datum)]
    return individual_node_data

def nodejobs_qdata(nodeslist_queuedata(),):


def determine node number():
    list of possible pos indexed in order of node number
    if matchdata == list:
        node#=indexofTRUE
        functiontoinputgjf(node#)
    return node#

def functiontoinputgjf():
    #rung16 file_name node_num
    subprocess.run(["rung16",gjf_name,node_num])


