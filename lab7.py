#Yamel Hernandez
#80590552
#CS 2302
#Diego Aguirre
#Anindita Nath
#Lab 7 ver A
#Purpose of this lab was to understand how to 
# implement edit distance

########################################################

#edit distance
def editDistance(s1, s2):
    string1 = len(s1)+1
    string2 = len(s2)+1
    array = {} #making the array a set for 2d purpose
    for i in range(string1):
        array[i,0] = i #filling in for first string
    for j in range(string2):
        array[0,j] = j #filling in for 2nd string
    for i in range(1, string1): 
        for j in range(1, string2):
            if s1[i-1] == s2[j-1]: #checking characters
                add = 0 #setting value to add if same
            else:
                add = 1 #otherwise setting it to add 1
            array[i,j] = min(array[i, j-1] + 1, array[i-1, j] + 1, array[i-1, j-1] + add)

    return array[i,j]

##########################################################3

def main():
    string1 = input("Enter string 1: ")
    string2 = input("Enter string 2: ")    
    print("Edit distance: ")
    print(editDistance(string1, string2))  
    
main()
