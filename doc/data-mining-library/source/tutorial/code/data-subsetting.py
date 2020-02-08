import Arithmos

data = Arithmos.data.Table("iris.tab")
print("Dataset instances:", len(data))
subset = Arithmos.data.Table(data.domain, [d for d in data if d["petal length"] > 3.0])
print("Subset size:", len(subset))
