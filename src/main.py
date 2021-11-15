from .hangmanClass import HangMan
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMenuBar,
    QMenu,
    QAction, 
    QDesktopWidget
)
import sys
from typing import Tuple
from darkdetect import isDark
from qt_material import apply_stylesheet

#
# @breif gives screen size has (width, height)
# @return Tuple of width, height
# 
def getScreenSize(app) -> Tuple[int]:
    sizeObject = app.primaryScreen().size()
    return sizeObject.width(), sizeObject.height()

def cleanALayout(layout) -> None:
    for i in reversed(range(layout.count())): 
            layout.itemAt(i).widget().setParent(None)


darkTheme, lightTheme = 'dark_blue.xml', 'light_blue.xml'

class HangManGUI(QApplication):
    def __init__(self) -> None:
        self.gameObject = HangMan()

        super().__init__(["HangMan"])
        self.mainWindow = QMainWindow()
        self.mainWid = QWidget()
        
        ss = getScreenSize(self)
        size = [
            ss[0] if ss[0] <= 540 else ss[0] // 2,
            ss[1] if ss[1] <= 960 else ss[1] // 2
        ]

        self.mainWindow.resize(*size) # You can also use setGeometry() method but I prefer this one.
        # I do not care where Window is coming.

        self.initUI()
        self.initMenu()
        self.initQSS()

        self.mainWindow.setCentralWidget(self.mainWid)
        self.mainWindow.show()
        sys.exit(self.exec_())

    def initUI(self):
        self.mainWidLayout = QVBoxLayout()

        self.winLabel = QLabel('')
        self.mainWidLayout.addWidget(self.winLabel)

        self.livesLabel = QLabel("Lives left: " + str(self.gameObject.lives))   
        self.mainWidLayout.addWidget(self.livesLabel)

        self.displayWidget = QWidget()
        self.displayLayout = QHBoxLayout()
        self.displayWidget.setLayout(self.displayLayout)

        self.charLabels = []

        for i in range(len(self.gameObject.display)):
            self.charLabels.append(QLabel('_'))
            self.displayLayout.addWidget(self.charLabels[i])

        self.mainWidLayout.addWidget(self.displayWidget)
        self.mainWid.setLayout(self.mainWidLayout)

        self.inputWid = QWidget()
        inputLayout = QHBoxLayout()
        self.inputWid.setLayout(inputLayout)

        self.inputLabel = QLabel('Guess: ')
        inputLayout.addWidget(self.inputLabel)

        self.inputLineEdit = QLineEdit()
        inputLayout.addWidget(self.inputLineEdit)

        self.mainWidLayout.addWidget(self.inputWid)

        self.guessButton = QPushButton('Guess')
        self.guessButton.clicked.connect(self.guess)
        self.mainWidLayout.addWidget(self.guessButton)

    def guess(self):
        txt = self.inputLineEdit.text()
        if len(txt) == 1:
            self.gameObject.guess_letter(txt)
        else:
            self.gameObject.guess_word(txt)
        if self.gameObject.win:
            self.winLabel.setText('You win!')
        if self.gameObject.lose:
            self.winLabel.setText('You lose!')
        self.livesLabel.setText('Lives left: ' + str(self.gameObject.lives))
    
        for i in range(len(self.gameObject.display)):
            self.charLabels[i].setText(self.gameObject.display[i])

    def initMenu(self):
        self.mainMenuBar = QMenuBar()

        self.menu = QMenu('Game Menu')
        self.menu.addAction('New Game', self.startNewGame)
        
        self.mainMenuBar.addMenu(self.menu)

        self.themeMenu = QMenu('Theme Menu')

        self.setOSTheme = QAction('Set OS Theme')
        self.setOSTheme.triggered.connect(lambda : self.setTheme(0))

        self.setDarkTheme = QAction('Set Dark Theme')
        self.setDarkTheme.triggered.connect(lambda : self.setTheme(1))

        self.setLightTheme = QAction('Set Light Theme')
        self.setLightTheme.triggered.connect(lambda : self.setTheme(2))

        self.themeMenu.addAction(self.setOSTheme)
        self.themeMenu.addAction(self.setDarkTheme)
        self.themeMenu.addAction(self.setLightTheme)

        self.mainMenuBar.addMenu(self.themeMenu)

        self.mainWindow.setMenuBar(self.mainMenuBar)

    def initQSS(self):
        self.setTheme(0)

    def startNewGame(self):
        self.gameObject = HangMan()
        self.winLabel.setText('')
        self.livesLabel.setText('Lives left: ' + str(self.gameObject.lives))
        
        cleanALayout(self.displayLayout)
        
        self.charLabels = []

        for i in range(len(self.gameObject.display)):
            self.charLabels.append(QLabel('_'))
            self.displayLayout.addWidget(self.charLabels[i])

    def setTheme(self, theme: int):
        if theme == 0:
            if isDark():
                apply_stylesheet(self, darkTheme)
            else:
                apply_stylesheet(self, lightTheme)
        elif theme == 1:
            apply_stylesheet(self, darkTheme)
        elif theme == 2:
            apply_stylesheet(self, lightTheme)        

if __name__ == "__main__":
    gui = HangManGUI()
