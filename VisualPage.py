# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext
import os

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_richText1 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer1.Add( self.m_richText1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar2 = wx.MenuBar( 0 )
		self.檔案 = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.檔案, wx.ID_ANY, u"建立檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.檔案.Append( self.m_menuItem3 )

		self.m_menuItem4 = wx.MenuItem( self.檔案, wx.ID_ANY, u"開啟檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.檔案.Append( self.m_menuItem4 )

		self.m_menuItem5 = wx.MenuItem( self.檔案, wx.ID_ANY, u"儲存檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.檔案.Append( self.m_menuItem5 )

		self.m_menuItem6 = wx.MenuItem( self.檔案, wx.ID_ANY, u"關閉程式", wx.EmptyString, wx.ITEM_NORMAL )
		self.檔案.Append( self.m_menuItem6 )

		self.m_menubar2.Append( self.檔案, u"檔案" )

		self.SetMenuBar( self.m_menubar2 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.CreateNew, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.OpenFile, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.SaveFile, id = self.m_menuItem5.GetId() )
		self.Bind( wx.EVT_MENU, self.Exit, id = self.m_menuItem6.GetId() )

	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def CreateNew( self, event ):
		event.Skip()    #觸發點擊效果

	def OpenFile( self, event ):
		event.Skip()    #觸發點擊效果

	def SaveFile( self, event ):
		event.Skip()    #觸發點擊效果

	def Exit( self, event ):
		event.Skip()    #觸發點擊效果


