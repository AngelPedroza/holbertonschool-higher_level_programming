#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """replace al the text with the new lines"""

    with open(filename, mode="r+", encoding="utf-8") as fd:
        line = fd.readlines()
        my_list = []
        for i in range(len(line)):
            my_list.append(line[i])
            if search_string in line[i]:
                my_list.append(new_string)

        fd.seek(0)
        fd.write("".join(my_list))
