# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SigCaceres
                                 A QGIS plugin
 SIG Cáceres
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-06-04
        copyright            : (C) 2021 by cotesa
        email                : sistemascotesa@grupotecopy.es
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SigCaceres class from file SigCaceres.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .sig_caceres import SigCaceres
    return SigCaceres(iface)
