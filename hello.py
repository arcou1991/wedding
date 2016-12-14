# coding:utf-8

# Created by KaiCao 2016.11.29

from flask import Flask
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask import render_template as template


app = Flask(__name__)


class CTestData(object):
	"""测试数据"""
	def __init__(self, sName):
		super(CTestData, self).__init__()
		self._initData(sName)

	def _initData(self, sName):
		self.m_sName = sName

		self.m_lList = []

		import random
		for i in range(10):
			self.m_lList.append(random.randint(1, 100))

	def GetName(self):
		return self.m_sName

	def GetListNum(self):
		return self.m_lList


@app.route("/")
def user():
	# return "<h1>Hello %s!</h1>" % name, 400
	# from flask import redirect
	# return redirect("index.html")
	name = "caokai"
	return template("index.html", oTestData=CTestData(name))

manager = Manager(app)
bootstrap = Bootstrap(app)

if __name__ == "__main__":
	manager.run()
