m_array(array):

     '''Return sum of all items in array'''
    n = array
    l = array[1:]
    if len(n)>0:
        return  array[0] + sum_array(l)
    else :
        return 0

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
     if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def reverse(word):

    n = word
    l= word[:-1]
    if len(n)>0:
        return  n[-1] + str(reverse(l))
    else :

        return ''
