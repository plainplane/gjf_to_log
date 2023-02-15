import re
import os
import time

# first get a text file w coordinates ordered by newline
# make a list of matches (matches at start of line/string)
# input the regex to split the coordinates apart (this assumes somethign like Ir is at the start of each coordinate group)
# a list of coordinates is returned, a file is written with all the coordinates.
def rawcoord_tostring(REGEX_listpatterns_toParse_raw, rawfilein):
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


def multi_header_edit(namechk, multiplicity, nproc):
    headerdata = multi_header_blank()
    headerdata = headerdata.replace('chk=EDIT', 'chk=' + str(namechk))
    headerdata = headerdata.replace('0 1EDIT', multiplicity)
    headerdata = headerdata.replace('nprocshared=EDIT', 'nprocshared=' + str(nproc))
    return headerdata


def multi_header_blank():
    with open('multi_header.txt', 'r') as headerfile:
        headerdata = headerfile.read()
    return headerdata


def multi_basis():
    with open('multi_basisset.txt', 'r') as f:
        basis = f.read()
    return basis

def makebatch_multiplicitygjf():
    rawfile_nowstring_patterns = ['Ir ','C ','H ','N ','O ']
    name_rawfile = 'delimited_by_newline.txt'
    stringto_listdelimiter = 'Ir '
    nproc = str(1)
    multiplicity_list = ['0 1', '0 2','0 3']

    path = os.getcwd()
    gjf_count = 0
    rawfile_nowstring = rawcoord_tostring(rawfile_nowstring_patterns, name_rawfile)

    string_nowlist_coordinates = cord_stringto_list(stringto_listdelimiter,rawfile_nowstring)
    basis = multi_basis()

    for i in range(1, len(string_nowlist_coordinates)):
        gjf_count += 1
        multi_count = 0
        for j in multiplicity_list:
            multi_count += 1
            name = 'z1_index' + str(gjf_count) + '_multiplicity' + str(multi_count) + '_1.gjf'
            checkpoint = 'z1_index' + str(gjf_count) + '_multiplicity' + str(multi_count) + '_1.chk'
            data = multi_header_edit(checkpoint,j,nproc)
            data += string_nowlist_coordinates[i][0]
            print("coordinate "+str(i)+" multi"+str(multi_count))
            data += basis
            completename = path + '/multi_gjfs/' + name
            with open(completename, 'w') as f:
                f.write(data)
                print(completename+" wrote.")

makebatch_multiplicitygjf()