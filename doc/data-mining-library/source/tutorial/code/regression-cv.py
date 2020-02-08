import Arithmos

data = Arithmos.data.Table("housing.tab")

lin = Arithmos.regression.linear.LinearRegressionLearner()
rf = Arithmos.regression.random_forest.RandomForestRegressionLearner()
rf.name = "rf"
ridge = Arithmos.regression.RidgeRegressionLearner()
mean = Arithmos.regression.MeanLearner()

learners = [lin, rf, ridge, mean]

res = Arithmos.evaluation.CrossValidation(data, learners, k=5)
rmse = Arithmos.evaluation.RMSE(res)
r2 = Arithmos.evaluation.R2(res)

print("Learner  RMSE  R2")
for i in range(len(learners)):
    print("{:8s} {:.2f} {:5.2f}".format(learners[i].name, rmse[i], r2[i]))
