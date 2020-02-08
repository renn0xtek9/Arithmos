import Arithmos
import numpy as np

data = Arithmos.data.Table("voting")
learner = Arithmos.classification.LogisticRegressionLearner()
classifier = learner(data)
x = np.sum(data.Y != classifier(data))
