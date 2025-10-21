# 3rd
def selectionSort(nlist):
    for fillSlot in range(len(nlist)-1,0,-1):
        maxpos=0
        for location in range(1, fillSlot+1):
            if nlist[location]>nlist[maxpos]:
                maxpos=location
        temp= nlist[fillSlot]
        nlist[fillSlot]=nlist[maxpos]
        nlist[maxpos]=temp

nlist=[14,46,43,27,57,41,45,21,70]
selectionSort(nlist)
print(nlist)