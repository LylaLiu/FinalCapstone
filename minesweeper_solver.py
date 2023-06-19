def mines_weeper(input_list):
    #creat an output list
    output_list = [[None] * len(input_list[0]) for _ in range(len(input_list))]
    
    #for every row in the inputlist
    for row in range(len(input_list)):
        # for every col in the row
        for col in range(len(input_list[0])):
            # if the col is  "-"
            if input_list[row][col] == "-":
                count = 0
                # check the surrounding
                for r_offset in range(-1, 2):
                    for c_offset in range(-1, 2):
                        a_row = row + r_offset
                        a_col = col + c_offset
                        #check if it is on the eadge
                        if 0 <= a_row < len(input_list) and 0 <= a_col < len(input_list[0]) and (r_offset, c_offset) != (0,0):
                            #check if there is "#"
                            if input_list[a_row][a_col] =="#":
                                count += 1
                #store the value of count
                output_list[row][col] = str(count)
            # if the col is "#"
            else:
                output_list[row][col] = input_list[row][col]
# return the result
    return output_list


input_list = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

#call the fuction
output_list = mines_weeper(input_list)

# print the list
for row in output_list:
    print(row)