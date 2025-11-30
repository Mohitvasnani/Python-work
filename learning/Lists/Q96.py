arr = [22,1,435,2,24433,523,2367,33,6,10]
total =0
count_ev = 0
count = 0
total_ev = 0
cnt2_5 =0
cnt3_4 =0
max = 0
for i in arr:
    if(i>max):
        max = i
print(f"the largets num is {max}")

for i in range(0,len(arr)):
    total = total +arr[i]
    if(arr[i]%2==0):
        count_ev = count_ev + 1
        total_ev = total_ev +arr[i]
    if(arr[i]%2==0 and arr[i]%5==0):
        cnt2_5 = cnt2_5+1
    if(arr[i]%3==0 and arr[i]%4==0):
        cnt3_4 = cnt3_4+1
print(total)
print(count)
print(count_ev)
print(total_ev)
print(cnt2_5)
print(cnt3_4)
