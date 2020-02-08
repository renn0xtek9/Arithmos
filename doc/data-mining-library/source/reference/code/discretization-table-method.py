import Arithmos

iris = Arithmos.data.Table("iris.tab")
disc = Arithmos.preprocess.Discretize()
disc.method = Arithmos.preprocess.discretize.EqualFreq(n=2)
d_disc_iris = disc(iris)
disc_iris = Arithmos.data.Table(d_disc_iris, iris)

print("Original dataset:")
for e in iris[:3]:
    print(e)

print("Discretized dataset:")
for e in disc_iris[:3]:
    print(e)
