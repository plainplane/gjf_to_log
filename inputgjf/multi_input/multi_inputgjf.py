import os
import subprocess
import re
import time
print('hi')
cwd = os.cwd()
cwd

print('hi')
#def back_to_dir():



#def in_to_dir():



def multi_inputgjf():
    cwd = os.cwd()
    cwd_to_multigjfs = cwd + '/'
    os.listdir()
    list_gjf_names = []
    nodes_range = (3,5)
    nodenum_list = []
        for i in range(nodes_range[0],nodes_range[1]):
            nodenum_list += i
    if check_to_input(nodenum) is True:
        input_gjf(filename,nodenum)
    for i in nodes_range:
        loop


# call bash; variable=bash string output of queue
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
        # print('node [' + str(node_num) + '] data: ' + '\n[ ' + node_datum_string + ' ]\n')

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
    # print('node [' + str(node_num) + '] data: ' + '\n[ ' + node_datum_string + ' ]\n')

    return individual_node_data


def jobs_on_node_int(nodenum):
    node_data = parsed_qdatum(nodenum)
    node_occupancy_value = int(node_data[1])
    return node_occupancy_value


def check_to_input(nodenum):
    safe_to_input = False
    if jobs_on_node_int(nodenum) < 3:
        safe_to_input = True
    return safe_to_input


def input_gjf(filename, nodenum):
    return_data = subprocess.run(["rung16", filename, nodenum], capture_output=True)
    return return_data


def files_and_parameters(txtfile_of_gjfnames, node_range_min, node_range_max):
    with open(txtfile_of_gjfnames, "r") as f:
        filename_string = f.read()
        filename_list = filename_string.split("\n")

    nodes_list = []
    for i in range(node_range_min, node_range_max):
        nodes_list += i

    return_data = ''
    for i in range(0, len(filename_list)):
        return_data += loop_nodes_till_entry(nodes_list, filename_list[i]) + '\n'
    with open("123_abc_scratchy.txt", 'w') as w:
        return_data += w.write(return_data)
    return return_data

def loop_nodes_till_entry(nodes_list, filename):
    job_entered = False
    while not job_entered:
        for i in nodes_list:
            time.sleep(3)
            if check_to_input(i):
                return_data = input_gjf(filename, int(i))
                return return_data






# ?? other limitations: nproc, set num per node, (read nproc of gjf and determine max?)

# enter job

# def enter_job(job_filename_list):
# get filename from list
# g16_output = subprocess.run(["g16"+filename+nodenum])
# return g16_output
