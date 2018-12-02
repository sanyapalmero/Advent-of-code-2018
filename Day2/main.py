def find_checksum(list_id):  #solution of part 1
    temp = []
    res1 = 0
    res2 = 0
    for line in list_id:
        two_count = 0
        three_count = 0

        for letter in line:
            temp.append(letter)

        for letter in temp:
            if temp.count(letter) == 2:
                two_count = 1
            if temp.count(letter) == 3:
                three_count = 1

        res1 += two_count
        res2 += three_count
        temp.clear()

    return res1 * res2


def find_common_letters(list_id): #solution of part 2
    for line1 in list_id:
        for line2 in list_id:
            diff_letter_count = 0
            for i in range(len(line1)):
                if line1[i] != line2[i]:
                    diff_letter_count += 1
            if diff_letter_count == 1:
                return line1, line2 #find 2 lines that differ by 1 letter



def main():
    list_id = []
    file = open("list.txt")

    for line in file:
        list_id.append(str(line))

    print(find_checksum(list_id))

    line1, line2 = find_common_letters(list_id)

    res = "res: "
    for letter1, letter2 in zip(line1, line2):
        if letter1 == letter2:
            res += letter1 #remove extra letter

    print(res)


if __name__ == '__main__':
    main()
