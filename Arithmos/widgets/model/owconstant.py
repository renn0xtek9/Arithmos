from Arithmos.data import Table
from Arithmos.modelling.constant import ConstantLearner
from Arithmos.widgets.utils.owlearnerwidget import OWBaseLearner
from Arithmos.widgets.utils.widgetpreview import WidgetPreview


class OWConstant(OWBaseLearner):
    name = "Constant"
    description = "Predict the most frequent class or mean value " \
                  "from the training set."
    icon = "icons/Constant.svg"
    replaces = [
        "Arithmos.widgets.classify.owmajority.OWMajority",
        "Arithmos.widgets.regression.owmean.OWMean",
    ]
    priority = 10
    keywords = ["majority", "mean"]

    LEARNER = ConstantLearner


if __name__ == "__main__":  # pragma: no cover
    WidgetPreview(OWConstant).run(Table("iris"))
