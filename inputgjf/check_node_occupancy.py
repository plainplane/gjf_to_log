import subprocess
import re
import time

# call bash; variable=bash string output of queue
with open("queue.txt", "r") as q:
    queue = q.read()
    queue = queue + '\n---------------'


def qdata():
    with open("queue.txt", "r") as q:
        queue = q.read()
        queue = queue + '\n---------------'
    return queue
    str1 = subprocess.run(["qs"])
    str1 += '\n------'
    return str1


def parsed_qdata(begin_node_range, end_node_range):
    node_num = begin_node_range - 1
    individual_node_data = []
    for i in range(begin_node_range, end_node_range + 1):
        node_num += 1
        time.sleep(.1)
        job_num_match_list = []
        node_datum_pattern = re.compile(r'all\.q@n' + str(i) + ' *BIP *[0-9]*[0-9]/32.*?---', flags=re.DOTALL)
        node_datum_search = node_datum_pattern.search(qdata())
        node_datum_string = node_datum_search.group()

        node_occupancy_pattern = re.compile(r'([0-9]|[12][0-9]|[3][12])/32')
        node_occupancy_match = node_occupancy_pattern.search(node_datum_string)
        node_occupancy_string = node_occupancy_match.group()
        n_o_int_pattern = re.compile(r'[0-9]{1,2}')
        n_o_int_match = n_o_int_pattern.match(node_occupancy_string)
        node_occupancy_int_string = n_o_int_match.group()

        if node_occupancy_string[0] == '0':
            individual_node_data += [[node_num, 0, None, None]]
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

        individual_node_data += [[node_num, node_occupancy_int_string, job_num_match_list, job_tags_string]]
        #print('node [' + str(node_num) + '] data: ' + '\n[ ' + node_datum_string + ' ]\n')

    return individual_node_data


def parsed_qdatum(node):
    node_datum_pattern = re.compile(r'all\.q@n' + str(node) + ' *BIP *[0-9]*[0-9]/32.*?---', flags=re.DOTALL)
    node_datum_search = node_datum_pattern.search(qdata())
    node_datum_string = node_datum_search.group()

    node_occupancy_pattern = re.compile(r'([0-9]|[12][0-9]|[3][12])/32')
    node_occupancy_match = node_occupancy_pattern.search(node_datum_string)
    node_occupancy_string = node_occupancy_match.group()
    n_o_int_pattern = re.compile(r'[0-9]{1,2}')
    n_o_int_match = n_o_int_pattern.match(node_occupancy_string)
    node_occupancy_int_string = n_o_int_match.group()

    if node_occupancy_string[0] == '0':
        return [node, 0, None, None]

    newline_to_job_num_pattern = re.compile(r'(\n +[0-9]{5})')
    newline_to_job_num_match_list = newline_to_job_num_pattern.findall(node_datum_string)
    job_num_match_list = []
    for i in newline_to_job_num_match_list:
        job_num_match_list += [i[3:8]]

    job_tags_to_date_pattern = re.compile(r'[a-z]+ +[0-9]{1,2}/[0-9]{1,2}/')
    job_tags_to_date_match = job_tags_to_date_pattern.search(node_datum_string)
    job_tags_to_date_string = job_tags_to_date_match.group()
    job_tags_pattern = re.compile(r'[a-z]')
    job_tags_match = job_tags_pattern.search(job_tags_to_date_string)
    job_tags_string = job_tags_match.group()

    individual_node_data = [node, node_occupancy_int_string, job_num_match_list, job_tags_string]
    #print('node [' + str(node_num) + '] data: ' + '\n[ ' + node_datum_string + ' ]\n')

    return individual_node_data

print(parsed_qdatum(5))
print(parsed_qdata(5,5))
def node_occupancy(nodenum):
    node_data = parsed_qdata(1, 14)
    node_occupancy = int(node_data[nodenum-1][1])
    return node_occupancy
#print(node_occupancy(14))




# ?? other limitations: nproc, set num per node, (read nproc of gjf and determine max?)

# enter job

#def enter_job(job_filename_list):
    # get filename from list
    #g16_output = subprocess.run(["g16"+filename+nodenum])
    #return g16_output
