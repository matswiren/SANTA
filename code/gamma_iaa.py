def unit_equality(u, v):
    return True if u == v else False

def dissim_pos(u, v, empty_delta):
    deno = (u.start - v.start) + (u.end - v.end)
    nume = pow((u.end - u.start) + (v.end - v.start), 2) * empty_delta
    return deno/nume

def dissim_cat(u, v, empty_delta):
    pass

def dissim_combi(u, v, alpha, beta):
    pass

def disorder_unit_mapping(u, v):
    pass

def disorder_mapping(u, v):
    pass

def expected_disorder(mapping_a, mapping_b):
    pass