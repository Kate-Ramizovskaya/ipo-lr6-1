spis=['клубника', 'малина', 'голубика', 'ежевика', 'смородина', 'арбуз']
i=0
kolv=0
for str1 in spis:
    str1=spis[i]
    l=0
    for str2 in str1:
        if len(str1)>l:
            if str1[l]=='б':
                kolv+=1
                l+=1
            else: l+=1
    i+=1
print(kolv, ' строки')