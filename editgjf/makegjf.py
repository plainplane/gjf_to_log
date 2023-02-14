import re

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


count_markers("cleaned_coordinates.txt")


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


import re


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
def makebatchgjf(coordinate_file, delimiter, output_path_name,multiplicity,nproc,):
    path = output_path_name
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


makebatchgjf("cleaned.txt", 'C:\Users\pete\OneDrive\Desktop\scripts\gjf')