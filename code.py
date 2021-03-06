# -*- coding: utf8 -*-
import math

# --------------------- EDIT THIS PART

#define columns
c = 4

# you can define to alphabetical list here
# i used to numbers, because range func. very effective for testing
list = range(1, 26, 1)

# ---------------------- END OF EDIT

# firstly sort
list = sorted(list)

# calculate total row
r = int(math.ceil(len(list) / c)) + (1 if len(list) % c is not 0 else 0)

index = 0
table1 = []
for x in range(c):
    table1.append([])
    for y in range(r):
        if len(list) > index:
            table1[x].extend([list[index]])
            index += 1


res = ''
for i in range(r):
    for x in table1:
        try:
            #print x[i]
            res += "%s\t|\t" % x[i]
        except IndexError:
            res += "%s\t|\t" % "_"
            pass
    res += "\n"

#print table1
print res



# --- Functional if you need START

def sort_by_column(list=[], column=3):
        import math
        c = column
        list = sorted(list)
        r = int(math.ceil(len(list) / c)) + (1 if len(list) % c is not 0 else 0)

        index = 0
        table = []
        for x in range(c):
            table.append([])
            for y in range(r):
                if len(list) > index:
                    table[x].extend([list[index]])
                    index += 1

        items = []
        for i in range(r):
            for x in table:
                try:
                    items.append(x[i])
                except IndexError:
                    items.append("")
                    pass

        return items
        
# --- Functional if you need END
