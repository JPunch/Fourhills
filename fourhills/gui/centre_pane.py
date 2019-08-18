"""
Definition for centre pane, which shows various kinds of information such as scene information,
battle information, and will be updated to contain other kinds.
"""


from PySide2 import QtWidgets


class CentrePane(QtWidgets.QWidget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = QtWidgets.QVBoxLayout()

        # Centre pane is really just a large, non-editable text box
        self.layout.addWidget(QtWidgets.QLabel("Information:"))
        self.centre_text = QtWidgets.QTextEdit()
        self.centre_text.setReadOnly(True)
        self.layout.addWidget(self.centre_text)

        self.setLayout(self.layout)

    def set_content(self, content_source):
        """Set the contents text based on the content_source"""
        with open(content_source) as f:
            self.centre_text.setText(f.read())
