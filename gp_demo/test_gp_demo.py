from gp_demo.demo import calculateFitness

# from gp-demo.gp_demo import calculate_fitness

def test_mutation_demo():
    assert 2 == 2

def test_crossover_demo():
    assert 2 == 1

def test_simple_calculate_fitness():
    assert calculateFitness("a","a") == 1
# command to run tests
# nosetest [filename]