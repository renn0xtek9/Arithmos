import Arithmos
import random

random.seed(42)
data = Arithmos.data.Table("housing")
test = Arithmos.data.Table(data.domain, random.sample(data, 5))
train = Arithmos.data.Table(data.domain, [d for d in data if d not in test])

lin = Arithmos.regression.linear.LinearRegressionLearner()
rf = Arithmos.regression.random_forest.RandomForestRegressionLearner()
rf.name = "rf"
ridge = Arithmos.regression.RidgeRegressionLearner()

learners = [lin, rf, ridge]
regressors = [learner(train) for learner in learners]

print("y   ", " ".join("%5s" % l.name for l in regressors))

for d in test:
    print(
        ("{:<5}" + " {:5.1f}" * len(regressors)).format(
            d.get_class(), *(r(d) for r in regressors)
        )
    )
