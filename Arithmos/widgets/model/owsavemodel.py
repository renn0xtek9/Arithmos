import pickle

from Arithmos.widgets.widget import Input
from Arithmos.base import Model
from Arithmos.widgets.utils.save.owsavebase import OWSaveBase
from Arithmos.widgets.utils.widgetpreview import WidgetPreview


class OWSaveModel(OWSaveBase):
    name = "Save Model"
    description = "Save a trained model to an output file."
    icon = "icons/SaveModel.svg"
    replaces = ["Arithmos.widgets.classify.owsaveclassifier.OWSaveClassifier"]
    priority = 3000
    keywords = []

    class Inputs:
        model = Input("Model", Model)

    filters = ["Pickled model (*.pkcls)"]

    @Inputs.model
    def set_model(self, model):
        self.data = model
        self.on_new_input()

    def do_save(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.data, f)


if __name__ == "__main__":  # pragma: no cover
    WidgetPreview(OWSaveModel).run()
