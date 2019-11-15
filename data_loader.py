def load_file(filepath):
    file_data = []
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            line = line.replace('\n', '')
            line = line.split(',')
            processed_line = list(map(lambda x: float(x), line[:-1]))
            processed_line.append(line[-1])
            file_data.append(processed_line)
            line = fp.readline()
    
    return file_data