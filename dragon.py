c = 'a'
i = 0
a = ' '
s = 10#probeli
r = 10 #probeli-zerkalno


count = 0
#отрисовываю рога
while(s > 0 or i < 20):
    s -=1
    i +=1
    count +=1
    print((a*s)+(c*i)+(a*(r*2))+(c*i))
    if count > 9:
        r -= 1

#а теперь морда
x = 20 # morda kolvo symbols polovina
l = 'g'
dl = 20
count = 0
zerk = dl
morda = 0
while morda < 3:
    morda +=1
    print(l*(dl+dl))
print((l*40)+l)
morda = 0
prob = 15
t = 6
t_inv = 0
while morda < 3:
    morda +=1
    prob -= 1
    t -= 1
    t_inv += 2
    print((l*(morda*2))+(a*prob)+(l*t)+(l*t)+(a*(prob-1))+(l*(t_inv-1))+l*2)

morda = 0
while morda < 3:
    morda +=1
    print(l*(dl+dl)+l*2)
sh = 0
print((l*40)+l)
while dl > 0:
    count += 2
    dl -=2
    x -= 2
    print((a*count)+(l*x)+(l*(dl+2)))
    if sh == 4:
        print((a*9)+(l*3)+(a*3)+(l*11)+(a*3)+(l*4))
    if sh == 4:
        print((a*11)+(l*3)+(a*3)+(l*7)+(a*3)+(l*4))
    sh += 1
    
    