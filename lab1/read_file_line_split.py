def file_line_split(line):
    if line.find(' ') != -1:
        line = line.split(' ')
    else:
        if len(line) != 0:
            line = [line]

    res = []
    for j in range(len(line)):
        if line[j].endswith('\n'):
            if len(line[j]) != 1:
                res.append(line[j][0:-1])
        elif len(line[j]) != 0:
            res.append(line[j])

    return res
