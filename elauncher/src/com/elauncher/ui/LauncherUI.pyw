
from PyQt4 import QtGui


class LauncherDialog(QtGui.QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(LauncherDialog, self).__init__()

#         self.createMenu()
        self.createFormGroupBox()

        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QtGui.QVBoxLayout()
#         mainLayout.setMenuBar(self.menuBar)
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Launch Eclipse Based Application")
        
    '''
    #TODO will consider on configuration with menu&dialog
   
    def createMenu(self):
        self.menuBar = QtGui.QMenuBar()

        self.fileMenu = QtGui.QMenu("&File", self)
        self.exitAction = self.fileMenu.addAction("E&xit")
        self.menuBar.addMenu(self.fileMenu)

        self.exitAction.triggered.connect(self.accept)

    '''
    def createFormGroupBox(self):
        self.formGroupBox = QtGui.QGroupBox("Launch Options")
        
        self.eclipseAppCmb = QtGui.QComboBox()
        self.version = QtGui.QComboBox()
        self.workitemNumber = QtGui.QLineEdit()
        
        self.eclipseAppCmb.addItem("Eclipse 3.7") 
        self.eclipseAppCmb.addItem("Eclipse 3.8")        
        self.eclipseAppCmb.addItem("Eclipse 4.2.2")
        self.eclipseAppCmb.addItem("Eclipse 4.3")
        self.eclipseAppCmb.addItem("RBD 8014")
        self.eclipseAppCmb.addItem("RBD 8015")
        self.eclipseAppCmb.addItem("RBD 8016")
        self.eclipseAppCmb.addItem("RBD 851")
        self.eclipseAppCmb.addItem("RBD 90")
    
        self.version.addItem("90")
        self.version.addItem("850")
        self.version.addItem("8511")
        
        
        layout = QtGui.QFormLayout()
        layout.addRow(QtGui.QLabel("Eclipse Based Product:"), self.eclipseAppCmb)
        layout.addRow(QtGui.QLabel("Version Number:"), self.version)
        layout.addRow(QtGui.QLabel("WorkItem Number:"), self.workitemNumber)
        self.formGroupBox.setLayout(layout)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    dialog = LauncherDialog()
    sys.exit(dialog.exec_())
