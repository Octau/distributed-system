import sys
n_huruf=0;
n_angka=0;
lines_number = 0
for line in sys.stdin:
    for chara in line:
        if(chara.isdigit()):
            n_angka+=1
        elif(chara.isalpha()):
            n_huruf+=1
    lines_number = lines_number + 1

sys.stdout.write('Jumlah huruf :'+str(n_huruf))
sys.stdout.write('\n')
sys.stdout.write('Jumlah angka :'+str(n_angka))
