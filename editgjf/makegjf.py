import re
import os

## PARSE out lines that match at beginning of string to an output file
# make a list of regex patterns
pattern_list = ['Ir ', 'O ', 'N ', 'C ', 'H ']

def output_match_startof_lines_ignorecase(REGEX_listofpatterns, filein, fileout):
    path = 'C:/Users/pete/Jupyter/gaussianscripts/test_gjfmaker/' + fileout
    lines_variable = ''
    with open(filein, 'r') as file_input, open(path, 'w') as file_output:
        REGEX_list = REGEX_listofpatterns
        for line in file_input:
            for i in REGEX_list:
                pattern = re.compile(i, re.IGNORECASE)
                if pattern.match(line):
                    lines_variable += line
                    break
        file_output.write(lines_variable)


# output_match_startof_lines_ignorecase(pattern_list,"madlib.txt","cleaned_coordinates.txt")
# count number of (#)
def count_markers(filein):
    count = 0
    pattern = re.compile("Ir ", re.IGNORECASE)
    with open(filein, 'r') as file_input:
        for line in file_input:
            if pattern.match(line):
                count += 1
    return count


# Create a variable to pass around until it is ready to be written to the disk.
# pull header data -> edit header data
# unfinished ???
def gjf_header(headerfile, namechk, multiplicity, nproc):
    with open(headerfile, 'r') as headerfile:
        headerdata = headerfile.read()
    headerdata = headerdata.replace('chk=EDIT', 'chk=' + str(namechk))
    headerdata = headerdata.replace('0 1EDIT', multiplicity)
    headerdata = headerdata.replace('nprocshared=EDIT', 'nprocshared=' + str(nproc))
    return headerdata


# create list of (coordinates,orderinlist)
def gjf_cor_list(coordinate_file, regex):
    mark = re.compile(regex, re.IGNORECASE)
    count = -1
    cor_list = []
    variable = ''
    with open(coordinate_file, 'r') as f:
        for line in f:
            if mark.match(line):
                count += 1
                tup = (variable, count)
                cor_list += [tup]
                variable = ''
            variable += line
    return cor_list


### append basis from input template file to specific output file

def gjf_basis(file_with_basis):
    with open(file_with_basis, 'r') as f:
        basis = f.read()
    return basis


##making gjfs
def makebatchgjf(coordinate_file, delimiter,multiplicity,nproc,):
    path = os.getcwd()
    path += '/lowest_energy_multiplicity/'
    count = 0
    cor_list = gjf_cor_list(coordinate_file, delimiter)

    for i in range(1, len(cor_list)):
        count += 1
        checkpoint = 'z' + str(count) + '_a.chk'
        name = 'z' + str(count) + '_a.gjf'
        data = gjf_header('baseheader.txt', checkpoint, multiplicity, nproc)
        data += cor_list[i][0]
        print("coordinate "+i+"")
        data += gjf_basis('basefooter.txt')
        completename = path + name
        with open(completename, 'w') as f:
            f.write(data)



def makebatch_multiplicitygjf(coordinate_file, delimiter, multiplicity_list,nproc):
    path = os.getcwd()
    gjf_count = 0
    cor_list = gjf_cor_list(coordinate_file, delimiter)
    return_data = []

    for i in range(1, len(cor_list)):
        gjf_count += 1
        multi_count = 0
        for j in multiplicity_list:
            multi_count += 1
            name = 'z1_' + str(gjf_count) + '_' + str(multi_count) + '_a.gjf'
            checkpoint = 'z1_' + str(gjf_count) + '_' + str(multi_count) +'a.chk'
            data = gjf_header('header.txt', checkpoint, j, nproc)
            data += cor_list[i][0]
            print("coordinate "+str(i)+" multi"+str(multi_count))
            data += gjf_basis('basis_sets.txt')
            completename = path + '/multi_gjfs/' + name
            with open(completename, 'w') as f:
                return_data += str(f.write(data)) + '\n'
                print(completename+" wrote.")
    return return_data


multiplicity_list = ['0 1', '0 2','0 3']

print(makebatch_multiplicitygjf('coordinates_test.txt', 'Ir',multiplicity_list,'1'))
#input and save in groups 1 -> i

def makebatchgjf_from_lowest_e_multi(multiplicity_log_files,nproc):
    path = os.getcwd()
    path += '/lowest_energy_multiplicity/'
    count = 0
    cor_list = gjf_cor_list(coordinate_file, delimiter)

    for i in range(1, len(cor_list)):
        count += 1
        checkpoint = 'z' + str(count) + '_a.chk'
        name = 'z' + str(count) + '_a.gjf'
        data = gjf_header('baseheader.txt', checkpoint, multiplicity, nproc)
        data += cor_list[i][0]
        print("coordinate "+i+"")
        data += gjf_basis('basefooter.txt')
        completename = path + name
        with open(completename, 'w') as f:
            f.write(data)
