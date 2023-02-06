import subprocess
import re
import time
# call bash; variable=bash string output of queue


def qdata():
    str1 = subprocess.run(["qs"])
    return str1


#
def nodeslist_qdata(begin_node_range,end_node_range):
    node_num = 0
    individual_node_data = []
    for i in range(begin_node_range,end_node_range+1):
        node_num += 1
        node_datum_pattern = re.compile(r'all.q@n'+str(i)+'[0-9]*[0-9]'' *BIP *[1-9]*[1-9]/32(.*)---')
        node_datum_match = node_datum_pattern.match(qdata())
        node_datum_string = node_datum_match.group()


        node_occupancy_pattern = re.compile(r'[0-9]|[12][0-9]|3[12]/32')
        node_occupancy_match = node_occupancy_pattern.match(node_datum_string)
        node_occupancy_string = node_occupancy_match.group()

        newline_to_job_num_pattern = re.compile(r'\n +[0-9]{5}')
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

        individual_node_data += [[node_num,node_occupancy_string,job_num_string,job_tags_string]]
    time.sleep(3)
    print('node'+str(node_num)+': '+'\n'+node_datum_string+'\n\n')
    return individual_node_data



