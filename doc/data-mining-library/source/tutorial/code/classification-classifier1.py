import Arithmos

data = Arithmos.data.Table("voting")
learner = Arithmos.classification.LogisticRegressionLearner()
classifier = learner(data)
c_values = data.domain.class_var.values
for d in data[5:8]:
    c = classifier(d)
    print("{}, originally {}".format(c_values[int(classifier(d))], d.get_class()))
