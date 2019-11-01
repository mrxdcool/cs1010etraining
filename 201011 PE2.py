
def hamming_distances(dna_str_list):
    lst = dna_str_list
    dist_list = []
    if len(dna_str_list) == 1:
        return dist_list
    while len(lst) >1 :
        if len(lst[0]) != len(lst[1]):
            return 'Strings are of unequal length.'
        else: 
            counter = 0
            for i in range(len(lst[0])):
                if lst[0][i] != lst[1][i]:
                    counter+= 1
                else:
                    continue
        lst = [lst[0]] + lst[2:]
        dist_list.append(counter)
    return  dist_list + hamming_distances(dna_str_list[1:])

print(hamming_distances(['ATTCC', 'CCATT']))                                    #[5]
print(hamming_distances(['AATCCCGT', 'TCCAACGT', 'CGTAATCC']))                  #[5, 7, 6]
print(hamming_distances(['CCATTGCC', 'ATGCCGCC', 'ATTGCCCC', 'TTACCCGT']))      #[5, 6, 7, 3, 5, 5]
print(hamming_distances(['ATTCCGT', 'ACCTGA']))                                 #Strings are of unequal length


def check_rotations(dna_str_list):
    lst = (dna_str_list)
    results = [0 for i in range(len(lst))]


    if len(lst) == 1:
        return results        #terminating condition
    for i in range(1,len(lst)): #check each element
        if len(lst[0]) != len(lst[i]):
            return 'Strings are of unequal length.'
            
        for j in range(len(lst[0])): #
            lst[0] = lst[0][1:] + lst[0][0]
            if lst[0] == lst[i]:
                results[0] =1
                results[i] =1
               
                    
        
    return results

check_rotations(['ATTCC', 'CCATT'])
            

