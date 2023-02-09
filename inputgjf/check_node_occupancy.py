import subprocess
import re
import time

# call bash; variable=bash string output of queue
with open("queue.txt", "r") as q:
    queue = q.read()
    queue = queue + '\n---------------'


def qdata():
    str1 = subprocess.run(["qs"])
    str1 += '\n------'
    return str1


def parsed_qdata(begin_node_range, end_node_range):
    node_num = begin_node_range - 1
    individual_node_data = []
    for i in range(begin_node_range, end_node_range + 1):
        node_num += 1
        job_num_match_list = []
        node_datum_pattern = re.compile(r'all\.q@n' + str(i) + ' *BIP *[0-9]*[0-9]/32.*?---', flags=re.DOTALL)
        node_datum_search = node_datum_pattern.search(qdata())
        node_datum_string = node_datum_search.group()
        node_occupancy_pattern = re.compile(r'([0-9]|[12][0-9]|[3][12])/32')
        node_occupancy_match = node_occupancy_pattern.search(node_datum_string)
        node_occupancy_string = node_occupancy_match.group()

        if node_occupancy_string[0] == '0':
            individual_node_data += [[node_num, node_occupancy_string, None, None]]
            continue

        newline_to_job_num_pattern = re.compile(r'\n +[0-9]{5}')
        newline_to_job_num_match = newline_to_job_num_pattern.findall(node_datum_string)
        job_num_pattern = re.compile(r'[0-9]{5}')
        for i in newline_to_job_num_match:
            job_num_match = job_num_pattern.findall(i)
            job_num_match_list += job_num_match

        job_tags_to_date_pattern = re.compile(r'[a-z]+ +[0-9]{1,2}/[0-9]{1,2}/')
        job_tags_to_date_match = job_tags_to_date_pattern.search(node_datum_string)
        job_tags_to_date_string = job_tags_to_date_match.group()
        job_tags_pattern = re.compile(r'[a-z]')
        job_tags_match = job_tags_pattern.search(job_tags_to_date_string)
        job_tags_string = job_tags_match.group()

        individual_node_data += [[node_num, node_occupancy_string, job_num_match_list, job_tags_string]]
        print('node [' + str(node_num) + '] data: ' + '\n[ ' + node_datum_string + ' ]\n')
        time.sleep(1)

    return individual_node_data

