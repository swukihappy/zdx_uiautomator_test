# -*- coding:utf-8 -*-
import config
import uiautomator2 as u2
from uiautomator2 import UiObject
import uiautomator2.ext.htmlreport as htmlreport
import time
d = u2.connect("172.16.56.174")
#hrp = htmlreport.HTMLReport(d)
#d.app_stop("air.tv.douyu.android")
#d.app_clear("air.tv.douyu.android")

d.app_start("air.tv.douyu.android")


d.implicitly_wait(5)
#已登陆和未登陆两种情况
if config.LOGIN==True:
	d(resourceId="air.tv.douyu.android:id/aql").click()
	if not d(text=u"sign").wait(10):
		print(0)
		d(text=u"登录 ").click()
		time.sleep(2)
		print(1)
		d(resourceId="air.tv.douyu.android:id/ph").click()
		d(description=u"微信",).click()
	print(3)
	d(text=u"icon_message",className="android.widget.Image").click()
	d(resourceId="air.tv.douyu.android:id/aa")[0].click()
	i=0
	while i<10:
		d(resourceId="air.tv.douyu.android:id/c8h").set_text("TEST123")
		d(resourceId="air.tv.douyu.android:id/c8j").click()
		i+=1
	d.press("back")
	d.press("back")
	d(resourceId="air.tv.douyu.android:id/bx6").click()
	d(text=u"arrow back ").click()
#发消息
if config.MESSAGE==True:
	d(resourceId="air.tv.douyu.android:id/art").click()
	if not d(resourceId="air.tv.douyu.android:id/d_2").wait(10):
		d(resourceId="air.tv.douyu.android:id/d4s").click()
	d(resourceId="air.tv.douyu.android:id/d_2").click()
	d(resourceId="air.tv.douyu.android:id/kj", text=u"好友/群").click()
	d(resourceId="air.tv.douyu.android:id/vr").click()
	d(resourceId="air.tv.douyu.android:id/brg").click()
	d.press("back")
#滑动屏幕
if config.SWIPE==True:
	for i in range(3):
		d.swipe(0.472,0.832,0.496,0.278,0.1)