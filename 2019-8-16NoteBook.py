import VisualPage
import wx
import os
import codecs

class page (VisualPage.MyFrame1):      ##VisualPage.MyFrame1 的意義是繼承VisualPage.MyFrame1的程式碼
	def CreateNew( self, event ):
		self.m_richText1.Clear()
		self.SetTitle(wx.EmptyString)

	def OpenFile( self, event ):
		FileName = wx.FileSelector(
			"測試",
			wildcard = "txt文字(*.txt)|*.txt",
			flags = wx.FD_OPEN
		)
		x = os.path.basename(FileName)
		self.SetTitle(x)

		y = codecs.open( FileName ,"r","utf-8")
		self.m_richText1.SetValue(y.read())
		y.close()

	def SaveFile( self, event ):
		z = self.GetTitle()
		# print(z)
		# path = os.getcwd()
		# print(path)
		# x = os.path.basename(path)
		# print(x)
		print(bool(z != str("")))

		if z != str(""):
			y = codecs.open( z , "w", "utf-8")
			y.write(self.m_richText1.GetValue())
			y.close()
		else:

			FileName = wx.FileSelector(
				"測試",
				wildcard = "txt文字(*.txt)|*.txt",
				flags = wx.FD_SAVE
				)
		
			y = codecs.open( FileName , "w", "utf-8")
			y.write(self.m_richText1.GetValue())
			y.close()
			

	def Exit( self, event ):
		self.Close()


app = wx.App() #建立應用程式
win = page(None) #把視窗class存成變數   ##page的意義是開啟現在這邊的程式碼
win.Show()     #顯示視窗
app.MainLoop() #持續開著,否則頁面跑完就消失