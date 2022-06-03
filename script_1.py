def detect_problems(filename):
    '''
    A function which detects problems in files
    :param filename: A file
    :return: None
    '''
    data = numpy.loadtxt(fname=filename, delimiter=',')
    if numpy.max(data, axis=0)[0] == 0 and numpy.max(data, axis=0)[20] == 20:
        print('Suspicious looking maxima!')
    elif numpy.sum(numpy.min(data, axis=0)) == 0:
        print('Minima add up to zero!')
    else:
        print('Seems OK!')