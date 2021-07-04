from gui import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
import sys

from PIL import Image
import time
import os
import shutil

class MyWin(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ui.checkBox_CharString.clicked.connect(self.onStrCB)
		self.ui.checkBox_UnicodeChar.clicked.connect(self.onUnicodeCB)
		self.ui.toolButton_Build.clicked.connect(lambda: self.runExtraction(self.fonts, self.uniChar_From, self.uniChar_To, self.charDelay))
		self.ui.toolButton_AddFont.clicked.connect(self.onAddFont)
		self.ui.toolButton_Remove.clicked.connect(lambda: self.onRemove(self.fonts, self.fontsCB))
		self.ui.toolButton_ChangeSampsDir.clicked.connect(self.onChangeSampsDir)
		self.ui.toolButton_OpenInFolder.clicked.connect(self.onOpenInFolder)
		self.ui.toolButton_DeleteSamps.clicked.connect(self.onDeleteSamps)

		self.ui.progressBar.hide()

		self.uniChar_From = self.ui.spinBox_UniStart.value()
		self.uniChar_To = self.ui.spinBox_UniEnd.value()
		self.charDelay = self.ui.doubleSpinBox_Delay.value()

		self.charString = "".join([chr(i) for i in range(self.uniChar_From,self.uniChar_To)])
		self.fonts = []
		self.fontsCB = []
		self.stopFlag = True
		pcName = os.environ['COMPUTERNAME']
		try:
			self.samplesDir = "C:\\Users\\{}\\AppData\\Local\\OCR Generator".format(pcName)
			if not os.path.exists(self.samplesDir):
				os.mkdir(self.samplesDir)
		except:
			self.samplesDir = "C:\\Users\\{}\\AppData\\Local\\OCR Generator".format(pcName[:-3])
			if not os.path.exists(self.samplesDir):
				os.mkdir(self.samplesDir)
		self.defaultSampDir = str(self.samplesDir)
		self.ui.lineEdit_SampsDir.setText(self.samplesDir)

		self.ui.splitter.setSizes([150,300,162])
		
	def onDeleteSamps(self):
		for root, dirs, files in os.walk(self.samplesDir):
			for f in files:
				os.unlink(os.path.join(root, f))
			for d in dirs:
				shutil.rmtree(os.path.join(root, d))

	def onOpenInFolder(self):
		os.startfile(self.samplesDir)

	def onChangeSampsDir(self):
		self.samplesDir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
		if not self.samplesDir:
			self.samplesDir = str(self.defaultSampDir)
		self.ui.lineEdit_SampsDir.setText(self.samplesDir)

	def onRemove(self, fonts, fontsCB):
		temp1 = []
		temp2 = []
		for i, cb in enumerate(fontsCB):
			if not cb.isChecked():
				temp1.append(cb)
				temp2.append(fonts[i])
		self.fonts = temp2
		self.fontsCB = temp1
		self.updateScrollArea(self.fonts, self.fontsCB, self.ui.verticalLayout_6)

	def clearLayout(self, layout):
		'''
		:As the name suggests, it cleans widgets from layout.
		:As long as the layout has items, ie it is not 0, the first (0) item 
			is taken.
		:If the item is a widget, then that widget is deleted.
		'''
		while layout.count():
			child = layout.takeAt(0)
			if child.widget():
				child.widget().deleteLater()

	def updateScrollArea(self, fonts, fontsCB, layout):
		self.clearLayout(layout)

		for i, font in enumerate(fontsCB):
			fontsCB[i] = QCheckBox(fonts[i])
			layout.addWidget(fontsCB[i])
		verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
		layout.addItem(verticalSpacer)

		self.ui.label_FontCount.setText(str(len(fonts)))

	def onAddFont(self):
		font = self.ui.fontComboBox.currentText()
		self.fonts.append(font)
		self.fonts = list(set(self.fonts))
		self.fontsCB = list(self.fonts)

		self.updateScrollArea(self.fonts, self.fontsCB, self.ui.verticalLayout_6)

	def onStrCB(self):
		self.ui.checkBox_CharString.setChecked(True) #Selektuje ga
		self.ui.checkBox_CharString.setEnabled(False) #Iskljucuje ga
		self.ui.lineEdit_CharString.setEnabled(True) #Ukljuci ga

		self.ui.checkBox_UnicodeChar.setChecked(False)
		self.ui.checkBox_UnicodeChar.setEnabled(True)
		self.ui.label_UnicodeChar.setEnabled(True)
		
	def onUnicodeCB(self):
		QApplication.processEvents()
		self.ui.checkBox_CharString.setChecked(False)
		self.ui.checkBox_CharString.setEnabled(True)
		self.ui.lineEdit_CharString.setEnabled(False)

		self.ui.checkBox_UnicodeChar.setChecked(True)
		self.ui.checkBox_UnicodeChar.setEnabled(False)
		self.ui.label_UnicodeChar.setEnabled(False)

	def runExtraction(self, fontList, fromUniNo, toUniNo, delay):
		self.ui.progressBar.show()
		if self.stopFlag:
			self.stopFlag = False
			self.ui.toolButton_Build.setIcon(QIcon(":/img/Icons/stop-svgrepo-com.svg"))
		else:
			self.stopFlag = True
			self.ui.toolButton_Build.setIcon(QIcon(":/img/Icons/transfer-svgrepo-com.svg"))
		fromUniNo = self.ui.spinBox_UniStart.value()
		toUniNo = self.ui.spinBox_UniEnd.value()
		delay = self.ui.doubleSpinBox_Delay.value()

		if self.ui.checkBox_CharString.isChecked():
			self.charString = self.ui.lineEdit_CharString.text()
			try:
				step = 100/(len(fontList)*(len(self.charString)))
			except:
				pass
		if self.ui.checkBox_UnicodeChar.isChecked():
			QApplication.processEvents()
			self.charString = "".join([chr(i) for i in range(fromUniNo,toUniNo)])
			try:
				step = 100/(len(fontList)*(toUniNo-fromUniNo))
			except:
				pass

		count = 0
		successfulCount = 0
		failedCount = 0
		breakFlag = False
		#qwertzuiopšđasdfghjklčćžyxcvbnmQWERTZUIOPŠĐASDFGHJKLČĆŽYXCVBNM
		for i, font in enumerate(fontList):
			self.ui.label_Font.setText(font)
			self.ui.label_Phase.setText("Extraction")
			for char in list(set(list(self.charString))):
				if not self.stopFlag:
					count+=step
					self.ui.progressBar.setStyleSheet("QProgressBar{text-align: center;height:10px;border-style:solid;border-width:1px;border-color: rgba(0, 0, 0, 30%)}QProgressBar::chunk {background-color: rgba(0, 202, 0, 50%);}")
					self.ui.progressBar.setValue(count)
					try:
						QApplication.processEvents()
						self.ui.label_Character.setFont(QFont(font))
						self.ui.label_Character.setText(char) #Š
						self.ui.label_Character.setStyleSheet("min-width:16px;max-width:16px;min-height:16px;max-height:16px;background-color: rgb(255, 255, 255);")
						p = self.ui.label_Character.grab()
						p.save("{}/{}-{}.jpg".format(self.samplesDir,char, i))
						image = Image.open("{}/{}-{}.jpg".format(self.samplesDir,char, i))
						image.convert("L").save("{}/{}-{}.jpg".format(self.samplesDir,char, i))
						self.ui.label_Character.setStyleSheet("min-width:80px;max-width:80px;min-height:80px;max-height:80px;background-color: rgb(255, 255, 255);")
						time.sleep(delay)
						self.ui.label_Character.setPixmap(QPixmap("{}/{}-{}.jpg".format(self.samplesDir,char, i)))
						successfulCount+=1
						self.ui.label_Successful.setText(str(successfulCount))
					except:
						failedCount+=1
						self.ui.label_Failed.setText(str(failedCount))
						pass

				else:
					self.ui.toolButton_Build.setIcon(QIcon(":/img/Icons/transfer-svgrepo-com.svg"))
					self.ui.progressBar.setValue(100)
					self.ui.progressBar.setStyleSheet("QProgressBar{text-align: center;height:10px;border-style:solid;border-width:1px;border-color: rgba(0, 0, 0, 30%)}QProgressBar::chunk {background-color: rgba(230, 0, 0, 70%);}")
					self.stopFlag = True
					breakFlag = True
					break
			if not breakFlag:
				self.ui.progressBar.setValue(100)
		self.ui.toolButton_Build.setIcon(QIcon(":/img/Icons/transfer-svgrepo-com.svg"))
		self.stopFlag = True

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	myapp = MyWin()
	myapp.show()
	sys.exit(app.exec_())