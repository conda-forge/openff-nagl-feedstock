from openff.nagl import GNNModel
from openff.nagl_models import list_available_nagl_models

from openff.toolkit import Molecule

assert len(list_available_nagl_models()) > 0

[GNNModel.load(model) for model in list_available_nagl_models()]

molecule = Molecule.from_smiles("CC(=O)OC1=CC=CC=C1C(=O)O")

molecule.assign_partial_charges(
    partial_charge_method=list_available_nagl_models()[-1],
)
