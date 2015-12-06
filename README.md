# factor_rotation
This Python package the gradient projection rotation algorithms (GPA)
developed by Bernaards, C.A. and Jennrich, R.I.
The code is based on code developed Bernaards, C.A. and Jennrich, R.I.
and is ported and made available with permission of the authors.
The package uses numpy.

Basic example:

    import factor_rotation as fr
    A = np.random.randn(8,2)
    L, T = rotate_factors(A,'varimax')
    print(L)
    print(A.dot(T))

