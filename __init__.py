# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CRSTools
                                 A QGIS plugin
 Check, define and convert CRS
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-05-25
        copyright            : (C) 2018 by Hieu Van
        email                : hieuvan@disroot.org
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
    """Load CRSTools class from file CRSTools.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .crs_tools import CRSTools
    return CRSTools(iface)
