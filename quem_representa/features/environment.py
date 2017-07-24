from appium import webdriver

#device description

desired_caps = {}
desired_caps['platformName'] = 'Android' #sistema operacional do target (ex: IOS, Windows Mobile)
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'br.com.eleicoes'
desired_caps['appActivity'] = ''

def before_feature(context, feature):
    context.driver = webdriver.Remote(context.config.userdata['appiumServerUrl'], desired_caps)

#behave -DappiumServerUrl=http://localhost:4723/wd/hub
