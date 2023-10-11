from openff.nagl import GNNModel
from openff.nagl_models import list_available_nagl_models

assert len(list_available_nagl_models()) > 0

[GNNModel.load(model) for model in list_available_nagl_models()]
