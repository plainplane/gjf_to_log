import re
import os
import time

# first get a text file w coordinates ordered by newline
# make a list of matches (matches at start of line/string)
# input the regex to split the coordinates apart (this assumes somethign like Ir is at the start of each coordinate group)
# a list of coordinates is returned, a file is written with all the coordinates.
def coordrawfile_tostring(REGEX_listpatterns_toParse_raw, rawfilein):
    cwd = os.getcwd()
    path = cwd + '/' + 'parse_byelements.txt'
    lines_string = ''
    with open(rawfilein, 'r') as file_input:
        REGEX_list = REGEX_listpatterns_toParse_raw
        for line in file_input:
            for i in REGEX_list:
                pattern = re.compile(i, re.IGNORECASE)
                if pattern.match(line):
                    lines_string += line
                    break
        coordinate_string = lines_string
        return coordinate_string




def cord_stringto_list(regex_pattern_toParse_intocorlist,coordinate_string):
    coordinate_list = []
    coordinate_list_pattern = re.compile(regex_pattern_toParse_intocorlist, re.IGNORECASE)
    variable_with_1coord = ""
    newline_to_newline = coordinate_string.split('\n')
    for i in newline_to_newline:
        if coordinate_list_pattern.match(i):
            coordinate_list += [variable_with_1coord]
            variable_with_1coord = ''
        variable_with_1coord += i
    return coordinate_list

def gjf_header(headerfile, namechk, multiplicity, nproc):
    with open(headerfile, 'r') as headerfile:
        headerdata = headerfile.read()
    headerdata = headerdata.replace('chk=EDIT', 'chk=' + str(namechk))
    headerdata = headerdata.replace('0 1EDIT', multiplicity)
    headerdata = headerdata.replace('nprocshared=EDIT', 'nprocshared=' + str(nproc))
    return headerdata


def gjf_basis(file_with_basis):
    with open(file_with_basis, 'r') as f:
        basis = f.read()
    return basis

def makebatch_multiplicitygjf(coordinate_list, delimiter, multiplicity_list,nproc):
    path = os.getcwd()
    gjf_count = 0
    coordinate_list = output_match_startof_lines_ignorecase(list_of_regex_elements,raw_file)
    return_data = []

    for i in range(1, len(cor_list)):
        gjf_count += 1
        multi_count = 0
        for j in multiplicity_list:
            multi_count += 1
            name = 'z1_' + str(gjf_count) + '_' + str(multi_count) + '_a.gjf'
            checkpoint = 'z1_' + str(gjf_count) + '_' + str(multi_count) +'a.chk'
            data = gjf_header('multiheader.txt', checkpoint, j, nproc)
            data += cor_list[i][0]
            print("coordinate "+str(i)+" multi"+str(multi_count))
            data += gjf_basis('multi_basis_sets.txt')
            completename = path + '/multi_gjfs/' + name
            with open(completename, 'w') as f:
                return_data += str(f.write(data)) + '\n'
                print(completename+" wrote.")
    return return_data

