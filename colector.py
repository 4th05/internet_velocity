from splinter import Browser
import datetime as dt
import time
import pandas as pd
# import os

#===========================================
#Functions to interact with browser elements
#===========================================
# def screenshot(browser):
#     browser.driver.save_screenshot('screenshot.png')
#     from PIL import Image
#     return Image.open('screenshot.png')

def button_click(browser, text_):
    try:
        buttons = browser.find_by_css('button')
        for button in buttons:
            if button.text == text_:
                button.click()
                break
    except:
        pass
#===========================================
#Functions to get internet download speed
#from different sites
#===========================================
def velocidadeideal(browser):
    browser.visit('https://www.velocidadeideal.com.br/')
    button_click(browser, 'INICIAR\nTESTE')
    time.sleep(40)
    down_speed = browser.find_by_css('div[class="title-result downloadTitle"]')
    
#     browser.driver.save_screenshot('{}.png'.format(time_now))
#     os.rename("{}.png".format(time_now), "screenshot/velocidadeideal/{}.png".format(time_now))
    return float(down_speed.text.split('\n')[1])

def fast(browser):
    browser.visit('https://fast.com/pt/')
    time.sleep(40)
    down_speed = browser.find_by_css('div[class="bordered-speed-container"]')
    
#     browser.driver.save_screenshot('{}.png'.format(time_now))
#     os.rename("{}.png".format(time_now), "screenshot/fast/{}.png".format(time_now))
    return float(down_speed.text)

def brasilBandaLarga(browser):
    browser.visit('https://www.brasilbandalarga.com.br/bbl')
    down_speed = browser.find_by_id('btnIniciar')
    down_speed.click()
    time.sleep(40)
    speed = browser.find_by_css('div[class="textao"]')
    
#     browser.driver.save_screenshot('{}.png'.format(time_now))
#     os.rename("{}.png".format(time_now), "screenshot/brasilbandalarga/{}.png".format(time_now))
    return float(speed.text)

#===========================================
#Main function
#===========================================
def job(filename):
    browser = Browser('firefox', headless = True)
    
    speed_list = []
    time_now = dt.datetime.now()

    v1 = velocidadeideal(browser)
    v2 = fast(browser)
    v3 = brasilBandaLarga(browser)

    speed_list.append((v1,v2,v3, time_now))

    df = pd.DataFrame(speed_list, columns=['velocidadeideal','fast','brasilBandaLarga','time'])
    df.time = pd.to_datetime(df.time)
    df.to_csv('{}.csv'.format(filename), mode='a', header=False)
    
    browser.quit()
    