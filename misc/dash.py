s='__.____________.__.__________.___________._____________.__._____________.__._____________.___________.__.__.______._______________.______________.___________._______________._____________.._______________._______________.___________.________________._______________._______________._____________.__.___________._____________.__._______._____________._______________.___________.________________._______________.__.______._._____________.__.___________.__.___________.________________.______._________.__._______.__._______._____________.._______________.__________._____________._________.______._______.______._______________.___________.________________.__.__________.___________.________________.______.____________._____________._____________.______._________.______._______.___________.________________.__.______._______________.___________.__._______.___________.________________._____________.__.__._______.__.__.___________.________________._____________._________.______._______.___________.__._____________._____________._______________.____._____________._____________.___________._____________._______________.__._____________._________.__._______.______._______________._______________.____________'

test1= []
count = 0

for i in s:
    if i == '_':
        count += 1
    else:
        test1.append(chr(count+64))
        count = 0
print(test1)
