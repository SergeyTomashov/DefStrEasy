import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, QTextEdit, QFileDialog, QInputDialog, QFontDialog, QColorDialog
from PyQt5.QtGui import QIcon, QTextCursor, QColor
from PyQt5.QtCore import Qt

class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    def initializeUI(self):
        self.setGeometry(100, 100, 400, 500)
        self.setWindowTitle('My Own Text Notepad 1 with GUI')
        self.createNotepadWidget()
        self.notepadMenu()
        self.show()
    def createNotepadWidget(self):
        self.text_field = QTextEdit()
        self.setCentralWidget(self.text_field)
    def notepadMenu(self):
        new_act = QAction(QIcon('images/new_file.png'), 'New', self)
        new_act.setShortcut('Ctrl+N')
        new_act.triggered.connect(self.clearText)
        open_act = QAction(QIcon('images/open_file.png'), 'Open', self)
        open_act.setShortcut('Ctrl+0')
        open_act.triggered.connect(self.openFile)
        save_act = QAction(QIcon('images/save_file.png'), 'Save', self)
        save_act.setShortcut('Ctrl+S')
        save_act.triggered.connect(self.saveToFile)
        exit_act = QAction(QIcon('images/exit.png'), 'Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(self.close)
        undo_act = QAction(QIcon('images/undo.png'), 'Undo', self)
        undo_act.setShortcut('Ctrl+Z')
        undo_act.triggered.connect(self.text_field.undo)
        redo_act = QAction(QIcon('images/redo.png'), 'Redo', self)
        redo_act.setShortcut('Ctrl+Shift+Z')
        redo_act.triggered.connect(self.text_field.redo)
        cut_act = QAction(QIcon('images/cut.png'), 'Cut', self)
        cut_act.setShortcut('Ctrl+X')
        cut_act.triggered.connect(self.text_field.cut)
        copy_act = QAction(QIcon('images/copy.png'), 'Copy', self)
        copy_act.setShortcut('Ctrl+C')
        copy_act.triggered.connect(self.text_field.copy)
        paste_act = QAction(QIcon('images/paste.png'), 'Paste', self)
        paste_act.setShortcut('Ctrl+V')
        paste_act.triggered.connect(self.text_field.paste)
        find_act = QAction(QIcon('images/find.png'), 'Find', self)
        find_act.setShortcut('Ctrl+F')
        find_act.triggered.connect(self.findTextDialog)
        font_act = QAction(QIcon('images/font.png'), 'Font', self)
        font_act.setShortcut('Ctrl+T')
        font_act.triggered.connect(self.chooseFont)
        color_act = QAction(QIcon('images/color.png'), 'Color', self)
        color_act.setShortcut('Ctrl+Shift+C')
        color_act.triggered.connect(self.chooseFontColor)
        highlight_act = QAction(QIcon('images/highlight.png'), 'Highlight', self)
        highlight_act.setShortcut('Ctrl+Shift+H')
        highlight_act.triggered.connect(self.chooseFontBackgroundColor)
        about_act = QAction('About', self)
        about_act.triggered.connect(self.aboutDialog)
        #Creating the menu bar for the app
        menu_bar = self.menu_bar()
        menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(new_act)
        file_menu.addSeparator()
        file_menu.addAction(open_act)
        file_menu.addAction(save_act)
        file_menu.addSeparator()
        file_menu.addAction(exit_act)
        #Creating the editing menu and adding all the additions
        edit_menu = menu_bar.addMenu('Edit')
        edit_menu.addAction(undo_act)
        edit_menu.addAction(redo_act)
        edit_menu.addSeparator()
        edit_menu.addAction(cut_act)
        edit_menu.addAction(copy_act)
        edit_menu.addAction(paste_act)
        edit_menu.addSeparator()
        edit_menu.addAction(find_act)
        # Creating the tools menu and adding all the actions
        tool_menu = menu_bar.addMenu('Tools')
        tool_menu.addAction(font_act)
        tool_menu.addAction(color_act)
        tool_menu.addAction(highlight_act)
        # Creating the help menu and adding actions
        help_menu = menu_bar.addMenu('Help')
        help_menu.addAction(about_act)
    def openFile(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "HTML Files (*.html);;Text Files (*.txt)")
        if file_name:
            with open(file_name, 'r') as f:
                notepad_text = f.read()
            self.text_field.setText(notepad_text)
        else:
            QMessageBox.information(self, "Error", "Unable to open file", QMessageBox.Ok)
    def saveToFile(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', "", "HTML Files (*.txt)")
        if file_name.endswith('.txt'):
            notepad_text = self.text_field.toPlainText()
            with open(file_name, 'w') as f:
                f.write(notepad_text)
        elif file_name.endswith('.html'):
            notepad_richtext = self.text_field.toHtml()
            with open(file_name, 'w') as f:
                f.write(notepad_richtext)
        else:
            QMessageBox.information(self, "Error", "Unable to save file", QMessageBox.Ok)
    def clearText(self):
        answer = QMessageBox.question()
