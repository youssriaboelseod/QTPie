#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Control Widget part of the UI for QTPie.
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5

#First Party Imports
from QTPie.UI.widget import QTPieWidget


class QTPieControlWidget(QTPieWidget):
    """
    A super function extending the QTPieWidget class from QTPie. Specialized for media control attributes.

    Args:\n
        QTPieWidget (UI.widget.QTPieWidget): Inherits from QTPieWidget.
    """

    def __init__(self, parent=None, doesSignal=False):
        """
        Initializes the super class.

        Args:\n
            parent (PyQt5.QtWidgets.*): The object to put the widget on. Defaults to None.
            doesSignal (bool, optional): Whether or not signals for leaving and entering are emitted. Defaults to False.
        """

        super().__init__(parent, doesSignal)

        #Grid varibles for the widget
        self.grid = None
        self.gridCount = 0

        #Control variables for the widget
        self.playPause = None
        self.volumeWidget = None
        self.openFile = None
        self.videoProgress = None

        self.controls = [self.playPause,
                         self.volumeWidget,
                         self.openFile,
                         self.videoProgress]
    
    def updateControls(self):
        """
        Updates the items in the controls list.s
        """

        self.controls = [self.playPause,
                         self.volumeWidget,
                         self.openFile,
                         self.videoProgress]
