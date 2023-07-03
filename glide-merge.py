import os
all = os.listdir()
str1 = ''
for i in all:
    if i.endswith('.maegz'):
       str1 += i
       str1 += ' '
#e.g str1 = '01-SP_OUT_1_pv.maegz 02-SP_OUT_1_pv.maegz 03-SP_OUT_1_pv.maegz 04-SP_OUT_1_pv.maegz 05-SP_OUT_1_pv.maegz 06-SP_OUT_1_pv.maegz 07-SP_OUT_1_pv.maegz 08-SP_OUT_1_pv.maegz 09-SP_OUT_1_pv.maegz 10-SP_OUT_1_pv.maegz'

print(str1)
str3 = f' $SCHRODINGER/utilities/glide_merge -o out.maegz -r out.rept {str1} -c -6.5'
#print(str3)
os.system(str3)
