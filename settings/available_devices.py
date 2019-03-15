# 可用手机以及启动配置
from library.core.common.simcardtype import CardType
from library.core.common.supportedmodel import SupportedModel

# 测试APP信息
TARGET_APP = dict(
    # DOWNLOAD_URL="https://www.pgyer.com/apiv2/app/install?_api_key=298b363e3288c07f2683b96ca9bc5ab6&appKey=andfetiondev&buildPassword=qwer!234",
    DOWNLOAD_URL="http://dlrcs.fetion-portal.com/mobile/RCS_V6.2.8.0129_20190130.apk",
    APP_PACKAGE="com.chinasofti.rcs",
    APP_ACTIVITY="com.cmcc.cmrcs.android.ui.activities.WelcomeActivity",
    INSTALL_BEFORE_RUN=False
)

# ======================= 移动CI环境手机配置 =======================
AVAILABLE_DEVICES = {
    'M960BDQN229CH--': {
        "MODEL": SupportedModel.HUAWEI_P20,
        "SERVER_URL": 'http://221.176.34.113:5000/wd/hub',
        "DEFAULT_CAPABILITY": {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "8DF6R17526001515",
            "udid": "8DF6R17526001515",
            "automationName": "UiAutomator2",
            "newCommandTimeout": 600,
            "appPackage": "com.chinasofti.rcs",
            "appActivity": "com.cmcc.cmrcs.android.ui.activities.WelcomeActivity",
        },
        'CARDS': [
            {
                'TYPE': CardType.CHINA_MOBILE,
                'CARD_NUMBER': '14775970982'
            },
        ]
    },
    'M960BDQN229CH': {
        "MODEL": SupportedModel.RED_MI_NOTE_4X,
        "SERVER_URL": 'http://127.0.0.1:4724/wd/hub',
        "DEFAULT_CAPABILITY": {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "VCO7IFTKKZZ5FI9T",
            "udid": "VCO7IFTKKZZ5FI9T",
            "automationName": "UiAutomator2",
            "newCommandTimeout": 600,
            "appPackage": "com.market2345",
            "appActivity": ".home.HomeTabActivity",
        },
        'CARDS': [
            {
                'TYPE': CardType.CHINA_MOBILE,
                'CARD_NUMBER': '14775290489'
            },
        ]
    },
}

# ======================= 本地CI环境手机配置 =======================
AVAILABLE_DEVICES_DEV = {
    'M960BDQN229CH': {
        "MODEL": SupportedModel.MEIZU_PRO_6_PLUS,
        "SERVER_URL": 'http://192.168.200.130:4723/wd/hub',
        "DEFAULT_CAPABILITY": {
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "deviceName": "M960BDQN229DK",
            "udid": "M960BDQN229DK",
            "automationName": "UiAutomator2",
            "newCommandTimeout": 600,
            "appPackage": "com.chinasofti.rcs",
            "appActivity": "com.cmcc.cmrcs.android.ui.activities.WelcomeActivity",
        },
        'CARDS': [
            {
                'TYPE': CardType.CHINA_MOBILE,
                'CARD_NUMBER': '13480860547'
            },
        ]
    },
    'M960BDQN229CH-BACK': {
        "MODEL": SupportedModel.MEIZU_PRO_6_PLUS,
        "SERVER_URL": 'http://127.0.0.1:5000/wd/hub',
        "DEFAULT_CAPABILITY": {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "95AQACPMGJP5L",
            "automationName": "UiAutomator2",
            "newCommandTimeout": 600,
            "appPackage": "com.chinasofti.rcs",
            "appActivity": "com.cmcc.cmrcs.android.ui.activities.WelcomeActivity",
        },
        'CARDS': [
            {
                'TYPE': CardType.CHINA_MOBILE,
                'CARD_NUMBER': '14775970982'
            },
            None
        ]
    },
}