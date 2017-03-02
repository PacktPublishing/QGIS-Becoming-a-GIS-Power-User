# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MyFirstPlugin
                                 A QGIS plugin
 This is my first plugin
                             -------------------
        begin                : 2016-01-23
        copyright            : (C) 2016 by Anita
        email                : foo@bar.com
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
    """Load MyFirstPlugin class from file MyFirstPlugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .my_first_plugin import MyFirstPlugin
    return MyFirstPlugin(iface)
