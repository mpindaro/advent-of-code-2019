start=245182
end=790572

flag=True;
flag2=True;
counter=0;
ns=[0]*10

for number in range(start, end):

    dig = list(int(d) for d in str(number))
    prev=dig[0]

    for i in range(0, len(dig)):

        current=dig[i]
        if(current<prev):
            flag=False
            break;
        prev=current

    for m in range(0, len(dig)):
        ns[dig[m]]=ns[dig[m]]+1

    if flag:

        for i in range(0, len(ns)):
            if ns[i]==2:
                flag2=True
                break


        if flag2:
            counter=counter+1

    ns=[0]*10
    flag=True
    flag2=False



print(counter)
