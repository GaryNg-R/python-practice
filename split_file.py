import io
import os 

def split(input_filename):
    with open(input_filename+'.txt','r') as f:
        txtfile = f.readlines()

    lines_per_file = 5000 
    count = 1 
    folder_name = 1
    os.mkdir(f'./{folder_name}')

    for i in range (0, len(txtfile), lines_per_file):
        if(i != 0 and i % 250000 == 0):
            folder_name += 1
            os.mkdir(f'./{folder_name}')
        with open(f'{folder_name}/{input_filename}_part{str(count)}.txt', 'w+') as f:
            #  with open(str(folder_name)+'/'+str(input_filename)+'_part'+str(count)+'.txt', 'w+') as f:
            if count > 1: # this is the second or later file, we need to write the 
                f.write(txtfile[0])
            f.writelines(txtfile[i:i+lines_per_file]) 
        count +=1 

split('bot')

