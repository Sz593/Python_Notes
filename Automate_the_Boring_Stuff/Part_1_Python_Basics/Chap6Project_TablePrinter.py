#! python3

def printTable(tbl):
    numOfCols = len(tbl[0])
    colLength = []
    for i in range(len(tbl)):
        colLength.append(len(max(tbl[i],key=len)))
    maxColLength = max(colLength)
    for j in range(len(tbl[0])):
        for k in range(len(tbl)):
            print(tbl[k][j].rjust(maxColLength), end='')
        print()
            

tableData = [['apples','oranges','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]

##tableData2 = [['my','milkshake','brings','all','the','boys'],
##              ['and','they\'r','like','it\'s','better','than'],
##              ['yours','damn','right','it\'s','better','than'],
##              ['yours','I','could','teach','you','but'],
##              ['I\'d','have','to','charge','your','ass']]

printTable(tableData2)

