import subprocess
import re
import time
# call bash; variable=bash string output of queue


def qdata():
    str1 = subprocess.run(["qs"])
    return str1


#
def nodeslist_qdata(begin_node_range,end_node_range):
    # sequence of regex to parse out useful stuff.
    # start with whole node n1--> \n--- parse out from front to back using desiredpattern$
    node_num = 0
    individual_node_data = []
    for i in range(begin_node_range,end_node_range+1):
        node_num += 1
        open_node_pattern = re.compile(r'all.q@n'+str(i)+' *BIP *[0-9]|[12][0-9]|[3][01]|/32')
        closed_node_pattern = re.compile(r'all.q@n'+str(i)+' *BIP *32/32')

        if re.match(open_node_pattern, queuedata()):
            is_open = True
        if re.match(closed_node_pattern, queuedata()):
            is_open = False

        node_to_endofnodesdata_pattern = re.compile(r'all.q@n[0-9]*[0-9] *BIP *[1-9]*[1-9]/32(.*)---')
        node_datum_match = node_to_endofnodesdata_pattern.match(queuedata())
        node_datum_string = node_datum_match.group()


        node_occupancy_pattern = re.compile(r'[0-9]|[12][0-9]|3[12]/32')
        node_occupancy_match = node_occupancy_pattern.match(node_datum_string)
        node_occupancy_string = node_occupancy_match.group()

        newline_to_job_num_pattern = re.compile(r'[0-9]{5}')
        newline_to_job_num_match = newline_to_job_num_pattern.match(node_datum_string)
        newline_to_job_num_string = newline_to_job_num_match.group()
        job_num_pattern = re.compile(r'[0-9]{5}')
        job_num_match = job_num_pattern.match(newline_to_job_num_string)
        job_num_string = job_num_match.group()

        job_tags_to_date_pattern = re.compile(r'[a-z]+ +[0-9]{1,2}/[0-9]{1,2}/')
        job_tags_to_date_match = job_tags_to_date_pattern.match(node_datum_string)
        job_tags_to_date_string = job_tags_to_date_match.group()
        job_tags_pattern = re.compile(r'[a-z]')
        job_tags_match = job_tags_pattern.match(job_tags_to_date_string)
        job_tags_string = job_tags_match.group()

        individual_node_data += [[node_num,is_open,node_datum]]
    time.sleep(3)
    print('node'+node_num+': '+'\n'+node_datum+'\n\n')
    return individual_node_data

def nodejobs_qdata(begin_node_range,end_node_range):
    jobs_on_node = []
    node_data = nodeslist_qdata(begin_node_range,end_node_range)
    for i in range(begin_node_range,end_node_range + 1):
        node_datum = node_data[i][3]
        node_datum_lines = node_datum.split("\n")
        #node_datum_lines_jobs= node_datum_lines.remove(node_datum_lines[0])
        node_datum_lines_jobs = node_datum_lines[0:(len(node_datum_lines) + 1)]

        jobs_num_id_pattern = re.compile('([0-9]{6}) [0-9]/.')
        job_letter_id_pattern = re.compile(' ([a-z]) ')

        jobs_on_node += [[count,job_num]]

    return jobs_on_node


def determine node number():
    list of possible pos indexed in order of node number
    if matchdata == list:
        node#=indexofTRUE
        functiontoinputgjf(node#)
    return node#

def functiontoinputgjf():
    #rung16 file_name node_num
    subprocess.run(["rung16",gjf_name,node_num])


