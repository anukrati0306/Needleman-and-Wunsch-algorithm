import numpy as np 

#user input for sequences 
seq_1 = input("enter the sequence 1 :")
seq_2 = input("enter the sequence 2 :") 

#for conveniance lets take 
 
#seq_1 = "ATCGT"
#seq_2 = "ATGT"

#zero matrices using numpy

main_matrix = np.zeros((len(seq_1)+1,len(seq_2)+1)) # +1 because we have to make an empty column acc. to Needleman and wunch 

match_check_matrix = np.zeros((len(seq_1),len(seq_2))) #matrices of M and N size

#providing penalty values for match mismatch and gap

match_reward = 1
mismatch_penalty = -1 
gap_penalty = -2

#now first fill the match check matrices with reward and penalty 

for i in range(len(seq_1)):
    for j in range(len(seq_2)):
        if seq_1[i]== seq_2[j]:
            match_check_matrix[i][j]= match_reward
        else:
            match_check_matrix[i][j]=mismatch_penalty
 #print to check
#print(match_check_matrix)

#now fill the main matrices using the also rules. 
#STEP 1 - initialization adding progresive gap penalty to the first row and column.

for i in range(len(seq_1)+1):
    main_matrix[i][0] = i*gap_penalty
for j in range(len(seq_2)+1):
    main_matrix[0][j] = j*gap_penalty

# STEP 2 - fill the matrix match mismatch penalty digonally and gap penalty to vertical and horizontal movement. the block will get the higher value. 
# we have to add the match check matrix value diagonally and gap penalty hori and vertically. 

for i in range(1,len(seq_1)+1):
    for j in range(1,len(seq_2)+1):
        main_matrix[i][j] = max(main_matrix[i-1][j-1]+match_check_matrix[i-1][j-1],
                            main_matrix[i-1][j]+gap_penalty, main_matrix[i]   [j-1]+gap_penalty)

print(main_matrix)

#traceback 

align1 = ""
align2 = ""

ti = len(seq_1)
tj = len(seq_2)

while(ti >0 and tj >0) :
     
     if (ti>0 and tj>0 and main_matrix[ti][tj] == main_matrix[ti-1][tj-1] + match_check_matrix[ti-1][tj-1]):
         align1 = seq_1[ti-1] + align1
         align2 = seq_2[tj-1] + align2
         
         ti = ti - 1
         tj = tj - 1
         
     elif(ti>0 and main_matrix[ti][tj] == main_matrix[ti-1][tj] + gap_penalty):
         align1 = seq_1[ti-1] + align1
         align2 = "-" + align2
         
         ti = ti -1 
     else :
          align1 = "-" + align1
          align2 = seq_2[tj-1] + align2 
          
          tj = tj-1
 
#testing
print(align1)
print(align2)
     
          
     
     








