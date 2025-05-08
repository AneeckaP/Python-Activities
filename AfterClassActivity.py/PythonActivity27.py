def palindrome(tuplex):
    start_index=0
    end_index=len(tuplex)-1
    while start_index < end_index:
        if tuplex[start_index]!= tuplex[end_index]:
            return False
        start_index+=1
        end_index-=1
    return True
tuplex=(1,2,3,5,2,1)
if palindrome(tuplex):
    print("The given numbers form a palindrome")
else:
    print("The given numbers do not form a palindrome")