'''def nodejobs_qdata(1,15):
    jobs_on_node = []
    node_data = nodeslist_qdata(begin_node_range,end_node_range)
    for i in range(begin_node_range,end_node_range + 1):
        node_data[3]
        jobs_on_node += job_num+count

    return jobs_on_node
'''
import os
print('hi')
x = os.getcwd()
w = os.path.abspath(x)
v = os.path.split(w)

print(v)
print()

def back(num_of_dir_back):
    x = os.getcwd()
    w = os.path.abspath(x)
    for i in range(0,num_of_dir_back):
        w = os.path.split(w)
        w = w[0]
    return w

print(back(2))
