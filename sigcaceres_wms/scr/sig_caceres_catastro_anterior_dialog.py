# -*- coding: utf-8 -*-
"""
modulo que carga los catastros de años anteriores

"""

__author__ = "Eduardo Risco"
__copyright__ = "Copyright 2021, SIG Caceres"
__credits__ = ["Eduardo Risco", "Sandra Pérez"]

__version__ = "1.1.0"
__maintainer__ = "Eduardo Risco"
__email__ = "eduardorisco@grupotecopy.es"
__status__ = "Production"

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.PyQt.QtCore import *

# Initialize Qt resources from file resources.py

from qgis.core import *  # No borrar
from ..rutas_capas.rutas_capas import *

from qgis.utils import iface
from ..sig_caceres import *
from .funciones_util import *

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'sig_caceres_catastro_anterior_base.ui'))


class SigCaceresCatastroAnterior(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SigCaceresCatastroAnterior, self).__init__(parent)
        self.setupUi(self)

        rellena_combobox(dict_capas=catastro_anteriores, combobox=self.comboBox_capas)
        self.boton_carga.clicked.connect(lambda: cargar_capa_combobox(combobox=self.comboBox_capas,
                                                                      dict_capas=catastro_anteriores))
