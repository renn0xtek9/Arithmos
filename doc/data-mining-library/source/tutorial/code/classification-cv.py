import Arithmos

data = Arithmos.data.Table("titanic")
lr = Arithmos.classification.LogisticRegressionLearner()
res = Arithmos.evaluation.CrossValidation(data, [lr], k=5)
print("Accuracy: %.3f" % Arithmos.evaluation.scoring.CA(res)[0])
print("AUC:      %.3f" % Arithmos.evaluation.scoring.AUC(res)[0])
