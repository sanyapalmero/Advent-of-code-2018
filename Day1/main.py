def get_final_frequency(frequency_list):  #part 1
    final_frequency = 0
    for frequency in frequency_list:
        final_frequency += frequency
    return final_frequency


def get_first_double_freq_slow(frequency_list):  #my first decision of part 2, and it works very slow
    double_frequency = 0
    double_frequency_list = []
    is_founded = False
    count = 0
    while not is_founded:
        for frequency in frequency_list:
            double_frequency += frequency
            double_frequency_list.append(double_frequency)
            if double_frequency_list.count(double_frequency) == 2:
                res = double_frequency
                is_founded = True
                break
        else:
            count += 1
            print(count)  #last value: 143
    return res


def get_first_double_freq_fast(frequency_list):  #my second decision of part 2, it works very fast :)
    double_frequency = 0
    double_frequency_list = set()
    is_founded = False
    while not is_founded:
        for frequency in frequency_list:
            double_frequency += frequency
            if double_frequency in double_frequency_list:
                res = double_frequency
                is_founded = True
                break
            else:
                double_frequency_list.add(double_frequency)
    return res


def main():
    frequency_list = []
    file = open("frequency_list.txt")  #977 elements

    for frequency in file:
        frequency_list.append(int(frequency))

    print(get_final_frequency(frequency_list))

    print(get_first_double_freq_fast(frequency_list))


if __name__ == '__main__':
    main()
