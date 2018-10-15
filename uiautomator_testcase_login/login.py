# -*- coding:utf-8 -*-
import uiautomator2 as u2
from uiautomator2 import UiObject
import uiautomator2.ext.htmlreport as htmlreport
import time
d = u2.connect("172.16.56.174")
hrp = htmlreport.HTMLReport(d)
#d.app_stop("air.tv.douyu.android")
#d.app_clear("air.tv.douyu.android")

d.app_start("air.tv.douyu.android")

d(resourceId="air.tv.douyu.android:id/aql").click()
d.implicitly_wait(5)
#已登陆和未登陆两种情况
if d(text=u"登录 ").wait(10):
	print(0)
	d(text=u"登录 ").click()
	time.sleep(2)
	print(1)
	d(resourceId="air.tv.douyu.android:id/ph").click()
	d(description=u"微信",).click()
print(3)
d(text=u"icon_message",className="android.widget.Image").click()