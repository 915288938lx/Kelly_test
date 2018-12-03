import numpy as np
def get_randint():
    np.random.seed(9)

    for i in range(40):
        randint = np.random.randint(1,100)
        yield randint


randint_ = get_randint()
a = np.array([x for x in randint_]).reshape(8,5)
print(a)
print(a[0])
print(a[:,0:2])
print('\n')
print('\n')
print(a.min(axis = 0))
print('\n')

print(a.min(axis = 1))
print('\n')

