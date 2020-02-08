import Arithmos

data = Arithmos.data.Table("titanic")
tree = Arithmos.classification.tree.TreeLearner(max_depth=3)
knn = Arithmos.classification.knn.KNNLearner(n_neighbors=3)
lr = Arithmos.classification.LogisticRegressionLearner(C=0.1)
learners = [tree, knn, lr]

print(" " * 9 + " ".join("%-4s" % learner.name for learner in learners))
res = Arithmos.evaluation.CrossValidation(data, learners, k=5)
print("Accuracy %s" % " ".join("%.2f" % s for s in Arithmos.evaluation.CA(res)))
print("AUC      %s" % " ".join("%.2f" % s for s in Arithmos.evaluation.AUC(res)))
