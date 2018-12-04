import re


def day3(coordinates):
    #---part1---#
    parsed_list = []

    for coordinate in coordinates:
        parsed = list(re.split(r'[#@,:x]', coordinate.replace(" ", "")[1:-1]))
        parsed = list(map(int, parsed))  #convert to int
        parsed_list.append(parsed)  #add to main list

    dict_coordinates = {}
    for n, x, y, w, h in parsed_list:
        temp_x = x
        for i in range(w):
            temp_x += 1  #because iteration by width
            temp_y = y
            for j in range(h):
                temp_y += 1  #because iteration by height
                temp_coordinates = (temp_x, temp_y)
                if temp_coordinates in dict_coordinates.keys():
                    count = dict_coordinates[temp_coordinates]
                    dict_coordinates[temp_coordinates] = count + 1
                else:
                    dict_coordinates[temp_coordinates] = 1

    common_squares = 0
    for count in dict_coordinates.values():
        if count > 1:
            common_squares += 1

    #---part2---#
    for n, x, y, w, h in parsed_list:
        temp_x = x
        count = 0
        for i in range(w):
            temp_x += 1
            temp_y = y
            for j in range(h):
                temp_y += 1
                temp_coordinates = (temp_x, temp_y)
                coordinate_count = dict_coordinates[temp_coordinates]
                if coordinate_count == 1:
                    count += 1
                if count == w * h:
                    req_id = n

    return common_squares, req_id


def main():
    file = open("coordinates.txt")

    coordinates = []
    for line in file:
        coordinates.append(str(line))

    print(day3(coordinates))


if __name__ == '__main__':
    main()
