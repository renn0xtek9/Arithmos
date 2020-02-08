"""Naive Bayes Learner
"""

from Arithmos.data import Table
from Arithmos.classification.naive_bayes import NaiveBayesLearner
from Arithmos.widgets.utils.owlearnerwidget import OWBaseLearner
from Arithmos.widgets.utils.widgetpreview import WidgetPreview


class OWNaiveBayes(OWBaseLearner):
    name = "Naive Bayes"
    description = "A fast and simple probabilistic classifier based on " \
                  "Bayes' theorem with the assumption of feature independence."
    icon = "icons/NaiveBayes.svg"
    replaces = [
        "Arithmos.widgets.classify.ownaivebayes.OWNaiveBayes",
    ]
    priority = 70
    keywords = []

    LEARNER = NaiveBayesLearner


if __name__ == "__main__":  # pragma: no cover
    WidgetPreview(OWNaiveBayes).run(Table("iris"))
