# factor_rotation
This Python package contains several factor rotation algorithms. It contains three families of rotation methods: oblimin (for orthogonal and oblique rotation), orthomax (for orthogonal rotation) and the Crawford-Ferguson family (for orthogonal and oblique rotation). As special cases of these families the following rotation methods are supported: quartimin, biquartimin, quartimax, biquartimax, varimax, equamax, parsimax, parsimony. Additionally the following methods are supported: target rotation, partial target rotation, promax and Procrustes.

Basic example:

    import factor_rotation as fr
    A = np.random.randn(8,2)
    L, T = rotate_factors(A,'varimax')
    print(L)
    print(A.dot(T))

For more details see the example file in the package and the documentation.
