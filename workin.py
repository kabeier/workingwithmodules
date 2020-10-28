class A: #import function
    from mathy import doMath
    print(doMath("1 + 2 + 3 * 4"))

class B: #import module as m
    import mathy as m
    print(m.doMath("1 / 2 * 3 * 4"))

class C:  # import function as dm
    from mathy import doMath as dm
    print(dm("1 - 2 / 3 * 4"))
