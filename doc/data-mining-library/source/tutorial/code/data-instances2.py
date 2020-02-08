import Arithmos

average = lambda x: sum(x) / len(x)

data = Arithmos.data.Table("iris")
print("%-15s %s" % ("Feature", "Mean"))
for x in data.domain.attributes:
    print("%-15s %.2f" % (x.name, average([d[x] for d in data])))
