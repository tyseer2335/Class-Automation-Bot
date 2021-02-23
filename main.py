# All necessary imports for our script to work  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options 
import time  
import pyautogui as pg 
import passwords as pas

# Disables all extensions and auto allows acess to mic, camera, location and notifications
opt=Options() 
opt.add_argument("--start-maximized")
opt.add_argument("--disable-extensions")
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1,
"profile.default_content_setting_values.notifications": 1
})  
 
# Connects to our Chrome driver to exicute our script in the Chrome browser 
driver = webdriver.Chrome(chrome_options=opt, executable_path="chromedriver.exe")  
    
# Delay function waits 3 seconds and makes sure page is loaded
def Delay (): 
    time.sleep(5)
    driver.implicitly_wait(20)

def LogInMaster (): 
    # Redirects to Gmail login page 
    driver.get("https://accounts.google.com/")  

    # Logs into Gmail Page and clicks button to next page
    path = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
    search = driver.find_element_by_xpath(path)
    search.send_keys(pas.email)  
    Delay()
    search.send_keys(Keys.RETURN)  
  
    # Logs into school Email page and clicks button to next page
    path_2 = "/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]"
    driver.implicitly_wait(20)
    search_2 = driver.find_element_by_xpath(path_2) 
    search_2.send_keys(pas.email)   
    Delay()
    search_2.send_keys(Keys.RETURN)  

    # Inputs password and clicks button to next page
    path_3 = "/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input"
    search_3 = driver.find_element_by_xpath(path_3 ) 
    search_3.send_keys(pas.password)   
    Delay() 
    button_3 ="/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input"
    driver.find_element_by_xpath(button_3).click()
    
    # Clicks on verification button 
    Delay() 
    button_4 ="/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]"
    driver.find_element_by_xpath(button_4).click()  
    Delay()

    # Redirects to Meet link  
    driver.get(pas.meetLink) 
    Delay() 
    pg.hotkey('ctrl','d')  
    Delay() 
    pg.hotkey('ctrl','e')
    
    # Joins Meet
    Delay()  
    button_5 = "/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span"
    driver.find_element_by_xpath(button_5).click()   

    # Clicks on message icon   
    Delay()   
    pg.click(1607,136)      

    # Types "Here" in chat 
    Delay()
    pg.typewrite("Here\n", 0.3)
    
    # Terminates program after a certain time
    time.sleep(pas.duration)  
    
    # Leaves Meet  
    Delay() 
    leave = pg.locateCenterOnScreen("Leave.png")  
    pg.click(leave)
    Delay() 
    driver.quit()
    

LogInMaster()


 

  