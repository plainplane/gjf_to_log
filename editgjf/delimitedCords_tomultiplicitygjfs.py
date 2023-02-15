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


def multi_header_edit(blankheader, namechk, multiplicity, nproc):
    # not calling the header blank function and instead saving the variable
    # before a loop allows for the file to only be opened and read once
    headerdata = blankheader
    headerdata = headerdata.replace('chk=EDIT', 'chk=' + str(namechk))
    headerdata = headerdata.replace('0 1EDIT', multiplicity)
    headerdata = headerdata.replace('nprocshared=EDIT', 'nprocshared=' + str(nproc))
    return headerdata


def multi_header_blank():
    cwd = os.getcwd()
    path = cwd + '/multi_templates/' + 'multi_header.txt'
    with open(path, 'r') as headerfile:
        headerdata = headerfile.read()
    return headerdata


def multi_basis():
    cwd = os.getcwd()
    path = cwd + '/multi_templates/' + 'multi_basisset.txt'
    with open(path, 'r') as f:
        basis = f.read()
    return basis

def makebatch_multiplicitygjf():
    # parameters
    rawfile_nowstring_patterns = ['Ir ','C ','H ','N ','O ']
    name_rawfile = 'delimited_by_newline.txt'
    stringto_listdelimiter = 'Ir '
    nproc = str(1)
    multiplicity_list = ['0 1', '0 2', '0 3', '1 1', '1 2', '1 3']
    path = os.getcwd()

    # get header, body, and basis out of file and into variables
    # should this be a seperate function? probably: files_to_variables()
    blank_header = multi_header_blank()
    rawfile_nowstring = rawcoord_tostring(rawfile_nowstring_patterns, name_rawfile)
    print(rawfile_nowstring)
    string_nowlist_coordinates = cord_stringto_list(stringto_listdelimiter,rawfile_nowstring)
    print(string_nowlist_coordinates)
    basis = multi_basis()

    #
    for i in range(0, (len(string_nowlist_coordinates)-14)):
        time.sleep(1)
        multi_count = 0
        for j in multiplicity_list:
            multi_count += 1
            name = 'z1_index' + str(i+1) + '_multiplicity' + str(multi_count) + '_1.gjf'
            checkpoint = 'z1_index' + str(i+1) + '_multiplicity' + str(multi_count) + '_1.chk'
            data = multi_header_edit(blank_header, checkpoint,j,nproc)
            data += string_nowlist_coordinates[i]
            data += basis
            print("coordinate " + str(i + 1) + " multi" + str(multi_count) + '\n' + data)
            completename = path + '/multi_gjfs/' + name
            with open(completename, 'w') as f:
                f.write(data)
                print(completename+" wrote.")

makebatch_multiplicitygjf()
