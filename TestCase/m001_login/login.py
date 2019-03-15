from library.core.TestCase import TestCase
from library.core.utils.applicationcache import current_mobile, current_driver, switch_to_mobile
from library.core.utils.testcasefilter import tags
from pages.Home import HomePage


REQUIRED_MOBILES = {
    'Android-移动': 'M960BDQN229CH',
    'IOS-移动': '',
    'Android-电信': 'single_telecom',
    'Android-联通': 'single_union',
    'Android-移动-联通': 'mobile_and_union',
    'Android-移动-电信': '',
    'Android-移动-移动': 'double_mobile',
    'Android-XX-XX': 'others_double',
}


class Preconditions(object):
    """
    分解前置条件
    """

    @staticmethod
    def select_single_cmcc_android_4g_client():
        """
        启动
        1、4G，安卓客户端
        2、移动卡
        :return:
        """
        client = switch_to_mobile(REQUIRED_MOBILES['测试机'])
        client.connect_mobile()

    @staticmethod
    def select_mobile(category):
        """选择手机手机"""
        client = switch_to_mobile(REQUIRED_MOBILES[category])
        client.connect_mobile()
        return client

    @staticmethod
    def app_start_for_the_first_time():
        """首次启动APP（使用重置APP代替）"""
        current_mobile().reset_app()

    @staticmethod
    def terminate_app():
        """
        强制关闭app,退出后台
        :return:
        """
        app_id = current_driver().desired_capability['appPackage']
        current_mobile().termiate_app(app_id)

    @staticmethod
    def background_app(seconds):
        """后台运行"""
        current_mobile().background_app(seconds)


class LoginTest(TestCase):
    """Login 模块"""

    @staticmethod
    def setUp_test_demo_0001():
        Preconditions.select_mobile('Android-移动')

    @tags('ALL', 'SMOKE', 'CMCC')
    def test_demo_0001(self):
        home = HomePage()
        home.wait_for_page_load()
        home.page_should_contain_text("软件")
        home.page_should_contain_text("榜单")
        home.click_element(home.locators['软件'])

    @staticmethod
    def setUp_test_demo_0002():
        Preconditions.select_mobile('Android-移动')

    @tags('ALL', 'SMOKE', 'CMCC')
    def test_demo_0002(self):
        home = HomePage()
        home.wait_for_page_load()
        home.page_should_contain_text("软件")
        home.page_should_contain_text("榜单")
        home.click_element(home.locators['榜单'])
