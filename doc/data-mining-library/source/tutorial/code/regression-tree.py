import Arithmos

data = Arithmos.data.Table("housing")
tree_learner = Arithmos.regression.SimpleTreeLearner(max_depth=2)
tree = tree_learner(data)
print(tree.to_string())
