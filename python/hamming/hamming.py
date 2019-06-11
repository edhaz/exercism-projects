def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands not equal in length")
    return len([i for i in zip(strand_a, strand_b) if i[0] != i[1]])
