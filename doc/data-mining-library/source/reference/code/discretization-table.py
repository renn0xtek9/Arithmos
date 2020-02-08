import Arithmos

iris = Arithmos.data.Table("iris.tab")
disc = Arithmos.preprocess.Discretize()
disc.method = Arithmos.preprocess.discretize.EqualFreq(n=3)
d_iris = disc(iris)

print("Original dataset:")
for e in iris[:3]:
    print(e)

print("Discretized dataset:")
for e in d_iris[:3]:
    print(e)
