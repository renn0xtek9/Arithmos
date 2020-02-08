import Arithmos

data = Arithmos.data.Table("iris.tab")
new_domain = Arithmos.data.Domain(
    list(data.domain.attributes[:2]),
    data.domain.class_var
)
new_data = Arithmos.data.Table(new_domain, data)

print(data[0])
print(new_data[0])
