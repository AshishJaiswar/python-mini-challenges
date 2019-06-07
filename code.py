# --------------
#Code starts here
def palindrome(num):
    num+=1
    num_arr = list((int(x) for x in str(num)))
    if num_arr==num_arr[::-1]:
        return int(''.join(str(x) for x in num_arr))
    arr_len = len(num_arr)
    if arr_len%2==0:
        mid = arr_len//2-1
    else:
        mid = arr_len//2
    temp=0
    for i in range(mid,-1,-1):
        if num_arr[i]!=num_arr[arr_len-i-1]:
            temp = i
            break
    if int(''.join(str(x) for x in num_arr[:temp+1][::-1])) > int(''.join(str(x) for x in num_arr[arr_len-temp-1:])):
        for i in range(mid+1):
            num_arr[arr_len-i-1] = num_arr[i]
    else:
        num_arr[mid]+=1
        for i in range(mid,-1,-1):
            if num_arr[i]==10:
                num_arr[i]=0
                num_arr[i-1]+=1
        for i in range(mid+1):
            num_arr[arr_len-i-1] = num_arr[i]
    return int(''.join(str(x) for x in num_arr))


palindrome(123)



# --------------
#Code starts here
def a_scramble(str_1, str_2):
    list_str1=list(str_1.lower().replace(" ",""))
    list_str2=list(str_2.lower().replace(" ",""))
    list_str1=sorted(list_str1)
    list_str2=sorted(list_str2)
    for letter in list_str1:
        if letter in list_str2:
            list_str2.remove(letter)
    if len(list_str2)==0:
        return True
    else:
        return False
print(a_scramble("ticket","chat"))


# --------------
#Code starts here
import math
def check_fib(num):
    phi = 0.5 + 0.5 * math.sqrt(5.0)
    a = phi * num
    return num == 0 or abs(round(a) - a) < 1.0 / num

print(check_fib(377))


# --------------
#Code starts here
def compress(word):

    if len(word) == 0:
        return None
    word=word.lower()
    final_arr = []
    index = 0
    letter = word[0]
    
    for el in word:
        if el == letter and ord(el) == ord(letter):
            index += 1
        else: 
            final_arr.append(letter + repr(index))
            letter = el
            index = 1
            
    final_arr.append(letter + repr(index))       
    return "".join(final_arr)
print(compress('xxcccdex'))


# --------------
#Code starts here
def k_distinct(string,k):
    string=string.lower()
    unique=[]
    for i in range(len(string)):
        if string[i] not in unique:
            unique.append(string[i])
    return len(unique)==k

print(k_distinct('Messoptamia',8))


