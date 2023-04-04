for i in range(123456789, 987654321):
    if i % 10 == 0:
        j = int(i/10)
        if j % 9 == 0:
            k = int(j/10)
            if k % 8 == 0:
                l = int(k/10)
                if l % 7 == 0:
                    m = int(l/10)
                    if m % 6 == 0:
                        n = int(m/10)
                        if n % 5 == 0:
                            o = int(n/10)
                            if o % 4 == 0:
                                p = int(o/10)
                                if p % 3 == 0:
                                    q = int(p/10)
                                    if q % 2 == 0:
                                        r = int(q/10)
                                        print(i)