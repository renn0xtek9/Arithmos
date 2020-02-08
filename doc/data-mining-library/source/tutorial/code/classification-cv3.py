import Arithmos

data = Arithmos.data.Table("voting")
lr = Arithmos.classification.LogisticRegressionLearner()
rf = Arithmos.classification.RandomForestLearner(n_estimators=100)
res = Arithmos.evaluation.CrossValidation(data, [lr, rf], k=5)

print("Accuracy:", Arithmos.evaluation.scoring.CA(res))
print("AUC:", Arithmos.evaluation.scoring.AUC(res))