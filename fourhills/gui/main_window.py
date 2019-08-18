"""Main window for Fourhills GUI"""

from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget

from fourhills.gui.content_pane import ContentPane
from fourhills.gui.notes_pane import NotesPane


class TestWidget(QWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.test_lbl = QtWidgets.QLabel("Hello from TestWidget!", parent=self)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Basic window construction
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Root layout creation
        self.root_layout_widget = QtWidgets.QWidget(self.centralwidget)
        self.root_layout_widget.setObjectName("root_layout_widget")
        self.root_layout = QtWidgets.QVBoxLayout(self.root_layout_widget)
        self.root_layout.setObjectName("root_layout")

        # Content pane with stretch 2, so it is 2x height of notes pane
        self.content_pane = ContentPane()
        self.root_layout.addWidget(self.content_pane, 2)

        # Notes pane
        self.notes_pane = NotesPane(parent=self)
        self.root_layout.addWidget(self.notes_pane, 1)

        # Final window setup
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setLayout(self.root_layout)

        # Set up keyboard shortcuts
        self.open_shortcut = QtWidgets.QShortcut("Ctrl+O", self.centralwidget, self.handle_open)
        self.save_shortcut = QtWidgets.QShortcut("Ctrl+S", self.centralwidget, self.handle_save)
        self.monster_shortcut = QtWidgets.QShortcut(
            "m",
            self.centralwidget,
            self.handle_monster_open
        )
        self.npc_shortcut = QtWidgets.QShortcut(
            "n",
            self.centralwidget,
            self.handle_npc_open
        )
        self.clear_shortcut = QtWidgets.QShortcut(
            "c",
            self.centralwidget,
            self.handle_clear_panes
        )

    def handle_open(self,):
        self.notes_pane.load_notes()

    def handle_save(self):
        self.notes_pane.save_notes()

    def handle_monster_open(self):
        self.content_pane.show_monster_pane()

    def handle_npc_open(self):
        self.content_pane.show_npc_pane()

    def handle_clear_panes(self):
        self.content_pane.clear_additional_panes()


def main():
    import sys
    app = QApplication([])
    app.setApplicationName("FourHills GUI")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
