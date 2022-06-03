def calculate_critical_value(size : int, alpha : float) -> float:

    '''
    A function that calculates the critical value

    :param size: integer
    :param alpha: float
    :return: critical_value: float
    '''

    t_dist = stats.t.ppf(1 - alpha / (2 * size), size - 2)
    numerator = (size - 1) * np.sqrt(np.square(t_dist))
    denominator = np.sqrt(size) * np.sqrt(size - 2 + np.square(t_dist))
    critical_value = numerator / denominator
    print("Grubbs Critical Value: {}".format(critical_value))
    return critical_value