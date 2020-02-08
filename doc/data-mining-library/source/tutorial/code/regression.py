import Arithmos

data = Arithmos.data.Table("housing")
learner = Arithmos.regression.LinearRegressionLearner()
model = learner(data)

print("predicted, observed:")
for d in data[:3]:
    print("%.1f, %.1f" % (model(d), d.get_class()))
