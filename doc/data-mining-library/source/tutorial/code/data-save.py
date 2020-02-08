import Arithmos

data = Arithmos.data.Table("lenses")
myope_subset = [d for d in data if d["prescription"] == "myope"]
new_data = Arithmos.data.Table(data.domain, myope_subset)
new_data.save("lenses-subset.tab")
