class A: #import function
    from mathy import doMath, circum, sqfoot
    doMath("1 + 2 + 3 * 4")
    circum(5)
    sqfoot(15,20)


class B: #import module as m
    import mathy as m
    m.doMath("1 / 2 * 3 * 4")
    m.cirum(5)
    m.sqfoot(15,20)


class C:  # import function as dm
    from mathy import doMath as dm
    from mathy import circum as c
    from mathy import sqfoot as sf
    dm("1 - 2 / 3 * 4")
    c(5)
    sf(15,20)
