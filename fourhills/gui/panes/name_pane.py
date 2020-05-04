from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import yaml
from fourhills.gui.utils.namegen import generate_name
import sys

class GenerateNamePane(QWidget):
    def __init__(self):
        super().__init__()
        self.name_dict = None
        with open("fourhills/gui/resources/names.yaml", "r") as fh:
            self.name_dict = yaml.safe_load(fh)
        self.createWindow(250, 200)

    def createWindow(self, width, height):
        parent=None
        super(GenerateNamePane, self).__init__(parent)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.resize(width, height)
        self.box = self.namedrop()
        self.setWindowTitle("Generate a name I dare you")

        genbtn = QPushButton("Generate Name", self)
        genbtn.sizeHint()
        genbtn.move(100, 80)
        genbtn.clicked.connect(self.getrandomname)

    def namedrop(self):
        box = QComboBox(self)
        box.addItems(list(self.name_dict.keys()))
        box.move(100, 40)
        return box

    def getrandomname(self):
        try:
            self.name.clear()
        except:
            None

        print("A", self.box.currentText(), "You could call them:")
        print(generate_name(self.name_dict[self.box.currentText()]))
        self.name = QLabel(f"{generate_name(self.name_dict[self.box.currentText()])}", self)
        self.name.move(100, 120)
        self.name.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = GenerateNamePane()
    win.show()
    sys.exit(app.exec_())