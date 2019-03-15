from appium.webdriver.common.mobileby import MobileBy

from library.core.BasePage import BasePage
from library.core.TestLogger import TestLogger


class HomePage(BasePage):
    """首页页"""

    ACTIVITY = '.home.HomeTabActivity'

    locators = {

        '软件许可及服务协议': (MobileBy.ID, 'com.chinasofti.rcs:id/title'),
        '和飞信软件许可及服务协议': (MobileBy.ID, ''),
        '协议内容': (MobileBy.ID, 'com.chinasofti.rcs:id/tv_content2'),
        '不同意': (MobileBy.ID, 'com.chinasofti.rcs:id/btn_cancel'),
        '同意': (MobileBy.ID, 'com.chinasofti.rcs:id/btn_agree'),
        '软件': (MobileBy.XPATH, "//*[contains(@text, '软件')]"),
        '榜单': (MobileBy.XPATH, "//*[contains(@text, '榜单')]"),
        # 'android:id/statusBarBackground': (MobileBy.ID, 'android:id/statusBarBackground')
    }

    @TestLogger.log()
    def click_agree_button(self):
        """点击同意"""
        self.click_element(self.locators['同意'])

    @TestLogger.log()
    def click_not_agree_button(self):
        """点击不同意"""
        self.click_element(self.locators['不同意'])
