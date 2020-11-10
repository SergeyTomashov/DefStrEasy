import sys
# Подключение модуля sys для потокового ввода текста пользователем
from PyQt5.QtWidgets import QApplication, \
    QMainWindow, QAction, QMessageBox, \
    QTextEdit, QFileDialog, QInputDialog, \
    QFontDialog, QColorDialog
#Подключение модуля Qt
from PyQt5.QtCore import Qt
#Подключение модулей для отображения иконки приложения, курсора и цвета
from PyQt5.QtGui import QIcon, QTextCursor, QColor

#Создание класса для Текстового Редактора
class Notepad(QMainWindow):
    #Инициализация объекта класса
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        #Создание геометрического размера окна приложения
        self.setGeometry(100, 100, 700, 800)
        self.setWindowTitle('My Own Text Notepad 1 with GUI')
        #Создание объекта виджета
        self.createNotepadWidget()
        #Создание меню для текстового редактора
        self.notepadMenu()
        #Отображение текстового редактора
        self.show()

    def createNotepadWidget(self):
        #Создание виджета для текстового редактора
        self.text_field = QTextEdit()
        self.setCentralWidget(self.text_field)

    def notepadMenu(self):
        #Создание меню с графическим интерфейсом
        new_act = QAction(QIcon('images/new_file.png'), 'New', self)
        #Использование кратких команд для быстрых действий, как
        #Сохранить, копировать, вставить, выйти из приложения или выделить
        new_act.setShortcut('Ctrl+N')
        new_act.triggered.connect(self.clearText)
        open_act = QAction(QIcon('images/open_file.png'), 'Open', self)
        open_act.setShortcut('Ctrl+O')
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
        highlight_act = QAction(QIcon(
            'images/highlight.png'), 'Highlight', self)
        highlight_act.setShortcut('Ctrl+Shift+H')
        highlight_act.triggered.connect(self.chooseFontBackgroundColor)
        about_act = QAction('About', self)
        about_act.triggered.connect(self.aboutDialog)
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(new_act)
        file_menu.addSeparator()
        file_menu.addAction(open_act)
        file_menu.addAction(save_act)
        file_menu.addSeparator()
        file_menu.addAction(exit_act)
        #Создание вкладки меню 'Edit' для редактирования и всех функций
        edit_menu = menu_bar.addMenu('Edit')
        edit_menu.addAction(undo_act)
        edit_menu.addAction(redo_act)
        edit_menu.addSeparator()
        edit_menu.addAction(cut_act)
        edit_menu.addAction(copy_act)
        edit_menu.addAction(paste_act)
        edit_menu.addSeparator()
        edit_menu.addAction(find_act)
        #Создание вкладки меню 'Toolsж для выбора инструментов и функций
        tool_menu = menu_bar.addMenu('Tools')
        tool_menu.addAction(font_act)
        tool_menu.addAction(color_act)
        tool_menu.addAction(highlight_act)
        #Создание меню 'Help' с информацией о приложении
        help_menu = menu_bar.addMenu('Help')
        help_menu.addAction(about_act)

    def openFile(self):
        #Проверка открытия файла в HTML или txt формате
        file_name, _ = QFileDialog.getOpenFileName \
            (self, "Open File", "", "HTML Files (*.html);;Text Files (*.txt)")
        if file_name:
            with open(file_name, 'r') as f:
                notepad_text = f.read()
            self.text_field.setText(notepad_text)
        else:
            QMessageBox.information \
                (self, "Error", "Unable to open file", QMessageBox.Ok)

    def saveToFile(self):
        #Сохранение файла по желанию пользователя
        #в HTML или txt формате
        file_name, _ = QFileDialog.getSaveFileName \
            (self, 'Save File', "", "HTML Files (*.txt)")
        if file_name.endswith('.txt'):
            notepad_text = self.text_field.toPlainText()
            with open(file_name, 'w') as f:
                f.write(notepad_text)
        elif file_name.endswith('.html'):
            notepad_richtext = self.text_field.toHtml()
            with open(file_name, 'w') as f:
                f.write(notepad_richtext)
        else:
            #Если такого формата файла не существует, то
            #выводится ошибка
            QMessageBox.information(self,
                                    "Error", "Unable to save file",
                                    QMessageBox.Ok)

    def clearText(self):
        #Функция удаления текста в редакторе
        answer = QMessageBox.question(self,
                                      "Clear Text",
                                      "Do you want to clear the text?",
                                      QMessageBox.No | QMessageBox.Yes,
                                      QMessageBox.Yes)
        #Вопрос у пользователя, точно ли он хочет удаить текста
        if answer == QMessageBox.Yes:
            self.text_field.clear()
            #Если отве 'Yes', то текст удаляется
        else:
            #В другом случае текст остается в редакторе
            pass

    def findTextDialog(self):
        #Функция для поиска слова или фразы в текстовом редакторе
        find_text, ok = QInputDialog.getText(self,
                                             "Search Text", "Find:")
        extra_selections = []
        #Выделение текста желтым цветом, чтобы показать,
        #что слово найдено
        if ok and not self.text_field.isReadOnly():
            self.text_field.moveCursor(QTextCursor.Start)
            color = QColor(Qt.yellow)
            while (self.text_field.find(find_text)):
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(color)
                selection.cursor = self.text_field.textCursor()
            for i in extra_selections:
                self.text_field.setExtraSelections(extra_selections)

    def chooseFont(self):
        #Выбор шрифта для текста
        current = self.text_field.currentFont()
        font, ok = QFontDialog.getFont(current,
                                       self,
                                       options=QFontDialog.DontUseNativeDialog)
        #Если такой шрифт существует, то возможен его выбор
        if ok:
            self.text_field.setCurrentFont(font)

    def chooseFontColor(self):
        #Выбор цвета текста
        color = QColorDialog.getColor()
        #Проверка на наличие цвета
        if color.isValid():
            self.text_field.setTextColor(color)

    def chooseFontBackgroundColor(self):
        #Выбор цвета для выделения текста
        color = QColorDialog.getColor()
        #Проверка на наличие цвета
        if color.isValid():
            self.text_field.setTextBackgroundColor(color)

    def aboutDialog(self):
        #Создание и открытие окна с информацией о приложении
        QMessageBox.about(self,
                          "About Notepad",
                          "My Own PyQt5"
                          " Text Editor Developed"
                          " in PyCharm Professional")

#Запуск окна приложения с помощью модуля sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    #Отображение окна текстового редактора в графическом приложении
    window = Notepad()
    #Выход из приложения и завершение программы
    sys.exit(app.exec_())
