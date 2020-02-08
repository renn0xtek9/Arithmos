import Arithmos

data = Arithmos.data.Table("titanic")
lr = Arithmos.classification.LogisticRegressionLearner(data)

tree = Arithmos.classification.tree.TreeLearner(data)
