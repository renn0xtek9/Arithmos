import Arithmos
from collections import Counter

data = Arithmos.data.Table("lenses")
print(Counter(str(d.get_class()) for d in data))
