import sys, os, zipfile, shutil, subprocess
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
from PyQt5.uic import loadUi
from pathlib import Path



downloads_path = str(Path.home() / "Downloads")

class MainWindow(QDialog):
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    # 변수
    forgeVer = 'none'
    sixForgePath = resource_path('forge/forge-1.16.5-36.1.0-installer.jar')
    twoForgePath = resource_path('forge/forge-1.12.2-14.23.5.2855-installer.jar')
    remods12Path = resource_path('remods12.zip')
    remods16Path = resource_path('remods16.zip')
    mineRoot = os.getenv('APPDATA')+"\\.minecraft"

    gui = resource_path('gui.ui')
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi(self.gui,self)
        self.twelvetwo.toggled.connect(self.twelvetwoClicked)
        self.sixfive.toggled.connect(self.sixfiveClicked)
        self.browse.clicked.connect(self.brosefiles)
        self.install.clicked.connect(self.installClicked)

    def twelvetwoClicked(self):
        self.check.setDisabled(False)
        self.filename.setDisabled(False)
        self.browse.setDisabled(False)
        self.forgeVer = '1.12.2'

    def sixfiveClicked(self):
        self.check.setDisabled(False)
        self.filename.setDisabled(False)
        self.browse.setDisabled(False)
        self.forgeVer = '1.16.5'

    def brosefiles(self):
        self.fname=QFileDialog.getOpenFileName(self, '모드 파일 찾기',downloads_path, '*.zip')
        self.filename.setText(self.fname[0])
        self.install.setDisabled(False)\
    
    def installClicked(self):
        # btn = self.sender()
        self.twelvetwo.setDisabled(True)
        self.check.setDisabled(True)
        self.filename.setDisabled(True)
        self.browse.setDisabled(True)
        if(self.forgeVer=='1.12.2'):
            self.installForge(self.twoForgePath)
        elif(self.forgeVer=='1.16.5'):
            self.installForge(self.sixForgePath)
        else:
            print('Error')
        self.installMod()

    
    def installForge(self, forge_path):
        subprocess.call(['java', '-jar', forge_path])

    def installMod(self):
        
        # 기존의 mods 폴더 삭제
        if os.path.isdir(self.mineRoot+"\\mods"):
            shutil.rmtree(self.mineRoot+"/mods", ignore_errors=True)
        
        # mods폴더 없을 시 생성
        if not os.path.exists(self.mineRoot+"\\mods"):
            os.makedirs(self.mineRoot+"\\mods")
        
        # 포지 버전 확인 + 필수 모드 설치
        if self.check.isChecked():
            if self.forgeVer=='1.12.2':
                zipfile.ZipFile(self.remods12Path).extractall(self.mineRoot+"/mods")
            elif self.forgeVer=='1.16.5':
                zipfile.ZipFile(self.remods16Path).extractall(self.mineRoot+"/mods")
            else:
                pass
        else:
            pass

        zipfile.ZipFile(self.fname[0]).extractall(self.mineRoot+"/mods")
        QMessageBox.Question(self, '설치 완료', '설치가 완료되었습니다.',
                                    QMessageBox.Ok)




    



app = QApplication(sys.argv)
mainwindow = MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(440)
widget.setFixedHeight(150)
widget.setWindowTitle("모드 설치기")
widget.show()
sys.exit(app.exec_())