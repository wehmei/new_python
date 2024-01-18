#Number of column
no_of_column=int(input('enter the number of the table column\n-'))
# input integer for ur mean for the mean

fx_list = []
freq_list = []

for i in range(no_of_column):
    #input class mark
    mark = int(input('class mark\n-'))
    #input frequency
    freq = int(input('frequency\n-'))
    freq_list.append(freq)
    # multiplying the frequency and class mark
    fx = mark * freq
    fx_list.append(fx)

#executing mean formulae
summation_fx = sum(fx_list)
summation_freq = sum(freq_list)

mean = summation_fx/summation_freq

print(fx_list)
print(f'the mean is {mean}')