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
        return lines_variable


def gjf_header(headerfile, namechk, multiplicity, nproc):
    with open(headerfile, 'r') as headerfile:
        headerdata = headerfile.read()
    headerdata = headerdata.replace('chk=EDIT', 'chk=' + str(namechk))
    headerdata = headerdata.replace('0 1EDIT', multiplicity)
    headerdata = headerdata.replace('nprocshared=EDIT', 'nprocshared=' + str(nproc))
    return headerdata

def gjf_cor_list(coordinate_file, regex_to_match):
    mark = re.compile(regex_to_match, re.IGNORECASE)
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


def gjf_basis(file_with_basis):
    with open(file_with_basis, 'r') as f:
        basis = f.read()
    return basis


##making gjfs
path = 'C:/Users/pete/Jupyter/gaussianscripts/test_gjfmaker/GJFS/'
count = 0
cor_list = gjf_cor_list('cleaned_coordinates.txt', 'Ir')

for i in range(1, len(cor_list)):
    count += 1
    checkpoint = 'aaa_' + str(count) + '.chk'
    data = gjf_header('baseheader.txt', checkpoint, '0 1', '1')
    data += cor_list[i][0]
    data += gjf_basis('basefooter.txt')
    name = 'aaa_' + str(count) + '.gjf'
    completename = os.path.join(path, name)
    with open(completename, 'w') as f:
        f.write(data)

        REGEX_listofpatterns, filein, fileout(coordinate
        file)
        headerfile, namechk, multiplicity, nproc, coordinate_file
        regex_to_match(delimiter for coordinatevariable), file_with_basis)
def filenamemaker(filenamein):
    could use coordinates
    return filenameout
