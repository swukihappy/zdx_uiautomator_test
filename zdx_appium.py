# -*- coding:utf-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import mysql
from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "8.1.0"
caps["deviceName"] = "PACM00"
caps["automationName"] = "UiAutomator2"
caps["appPackage"] = "air.tv.douyu.android"
caps["appActivity"] = "/tv.douyu.view.activity.launcher.DYLauncherActivity"
caps["autoLaunch"] = False

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

driver.back()
TouchAction(driver).press(x=543, y=2003).move_to(x=543, y=1298).release().perform()
    
TouchAction(driver).press(x=534, y=1959)   .move_to(x=551, y=1171)   .release()   .perform()
    
el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.view.ViewGroup[6]/android.view.ViewGroup/android.widget.ImageView[1]")
el1.click()
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView[1]")
el2.click()
driver.back()

driver.quit()