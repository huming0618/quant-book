import itertools

def test_permutations(items):
    for item in itertools.permutations(items):
        print(item)

def test_combinations(items, qty):
    for item in itertools.combinations(items, qty):
        print(item)

def test_combinations_replace(items, qty):
    for item in itertools.combinations_with_replacement(items, qty):
        print(item)

def test_product(item1, item2):
    for item in itertools.product(item1, item2):
        print(item)

if __name__ == "__main__":
    print('# Permuations - [6,9,7]')
    test_permutations([6,9,7])
    
    print('# Combinations - [a,b,c,d]')
    test_combinations(['a','b','c','d'], 2)
    
    print('# Combinations with replacement - [a,b,c,d]')
    test_combinations_replace(['a','b','c','d'], 2)

    print('# Product [dog,duck] [blue, gray]')
    test_product(['dog','duck'],['blue','gray'])

    
