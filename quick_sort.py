def q_sort(a=[45,36,15,92,35,71]):
    print 'unsorted', a
    pivot	=	a[0]
    for q in a:
        i = 0
        for x in (a[1:]):
            if x > pivot:
                break
            i += 1
        i += 1 	    #index of x
        k = -1
        while -(k)<len(a):
            y = a[k]
            if y < pivot:
                break
            k -= 1
        j = len(a) + k	#index of y
        
        if i < j:
            a[i], a[j] = a[j], a[i] #Swaping
        else:
            a[j], pivot = pivot, a[j]
    if a[len(a)-1] < a[len(a)-2]:
        a[len(a)-2], a[len(a)-1] = a[len(a)-1], a[len(a)-2] 
    print 'sorted', a
q_sort(a=[45,36,15,92,35,71])
