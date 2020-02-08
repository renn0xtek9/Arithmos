import Arithmos
import random

random.seed(42)
data = Arithmos.data.Table("voting")
test = Arithmos.data.Table(data.domain, random.sample(data, 5))
train = Arithmos.data.Table(data.domain, [d for d in data if d not in test])

tree = Arithmos.classification.tree.TreeLearner(max_depth=3)
knn = Arithmos.classification.knn.KNNLearner(n_neighbors=3)
lr = Arithmos.classification.LogisticRegressionLearner(C=0.1)

learners = [tree, knn, lr]
classifiers = [learner(train) for learner in learners]

target = 0
print("Probabilities for %s:" % data.domain.class_var.values[target])
print("original class ", " ".join("%-5s" % l.name for l in classifiers))

c_values = data.domain.class_var.values
for d in test:
    print(
        ("{:<15}" + " {:.3f}" * len(classifiers)).format(
            c_values[int(d.get_class())], *(c(d, 1)[target] for c in classifiers)
        )
    )
