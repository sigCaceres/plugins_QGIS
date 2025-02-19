# -*- coding: utf-8 -*-
"""
Modulo de ppal dialogo

"""
__author__ = "Eduardo Risco"
__copyright__ = "Copyright 2021, SIG Caceres"
__credits__ = ["Eduardo Risco","Sandra Pérez"]

__version__ = "1.1.0"
__maintainer__ = "Eduardo Risco"
__email__ = "eduardorisco@grupotecopy.es"
__status__ = "Production"

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'sig_caceres_dialog_base.ui'))


class SigCaceresDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SigCaceresDialog, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.handleHide)

    def handleHide(self):
        """Hide handle"""
        self.hide()