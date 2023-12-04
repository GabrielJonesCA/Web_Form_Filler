import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import numpy as np



def my_function():

        global driver
        driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
        driver.get('https://advertising.amazon.com/en-us/sign-in?countrycode=uk');
        time.sleep(3) # Let the user actually see something!

        act=ActionChains(driver)

        clk_adcon =  driver.find_element_by_xpath ("//*[@id='pre-select-by-countrycode']/div/div/div/div[2]/div/a")
        clk_adcon.click()
        time.sleep(2)


        ###SIGN IN
        user_name =  driver.find_element_by_name ("email")
        user_name.send_keys('winslowjones900@gmail.com')
        time.sleep(1)


        user_pass =  driver.find_element_by_name ("password")
        user_pass.send_keys('jolietT11!')
        time.sleep(1)

        clk_si =  driver.find_element_by_xpath ("//*[@id='signInSubmit']")
        clk_si.click()
        time.sleep(2)


        ###NAV TO FORM

        clk_sj =  driver.find_element_by_xpath ("//*[@id='left_nav_portfolio_list']/li[5]/span/span")
        clk_sj.click()
        time.sleep(2)

        clk_cc =  driver.find_element_by_xpath ("//*[@id='SINGLE_PORTFOLIO']/div[2]/div/div[1]/div/div/div/button[1]")
        clk_cc.click()
        time.sleep(3)

        clk_contin =  driver.find_element_by_xpath ("//*[@id='sspa_cb_ingress_button_continue_sp']")
        clk_contin.click()
        time.sleep(6)



        #FORM INFO

        prod =  driver.find_element_by_xpath ("//*[@id='ucb:sp:ucb-sp-ups:ups-asin-search-input']")
        prod.send_keys('B00D8KZH0M')
        time.sleep(3)

        prod_src =  driver.find_element_by_xpath ("//*[@id='asins-field-wrapper-id']/fieldset/div/span[2]/div/div[1]/div/div[1]/form/button")
        prod_src.click()
        time.sleep(4)

        prod_add =  driver.find_element_by_xpath ("//*[@id='asins-field-wrapper-id']/fieldset/div/span[2]/div/div[1]/div/div[3]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/button")
        prod_add.click()
        time.sleep(3)

        mt =  driver.find_element_by_xpath ("//*[@id='isExpress-false']")
        mt.click()
        time.sleep(2)
        
        phr =  driver.find_element_by_xpath ("//*[@id='keywords-field-wrapper-id']/fieldset/div/span[2]/div/div/div[1]/div[3]/div/div[2]/div[2]/label")
        phr.click()
        time.sleep(2)

        exa =  driver.find_element_by_xpath ("//*[@id='keywords-field-wrapper-id']/fieldset/div/span[2]/div/div/div[1]/div[3]/div/div[3]/div[2]/label")
        exa.click()
        time.sleep(2)
        

        ent_li =  driver.find_element_by_xpath ("//*[@id='keywords-field-wrapper-id']/fieldset/div/span[2]/div/div/div[1]/div[1]/div/nav/ul/li[2]/button")
        ent_li.click()
        time.sleep(2)

        ### COSTS

        sb =  driver.find_element_by_xpath ("//*[@id='keywords-field-wrapper-id']/fieldset/div/span[2]/div/div/div[1]/div[2]/div/div/div/div/button/div")
        sb.click()
        time.sleep(2)


        db =  driver.find_element_by_xpath ("//*[@id='portal']/div/div/button[3]/div/div[1]")
        db.click()
        time.sleep(2)

        cos1 =  driver.find_element_by_xpath ("//*[@id='ucb:sp:kwp:kwp-bid-selector-input-field']")
        act.double_click(cos1).perform()
        cos1.send_keys('.25')
        time.sleep(3)
        

        
        db2 =  driver.find_element_by_xpath ("//*[@id='keywords-field-wrapper-id']/fieldset/div/span[2]/div/div/div[1]/div[2]/div/div/div[1]/div/button/div")
        db2.click()
        time.sleep(3)

        cusb =  driver.find_element_by_xpath ("//*[@id='portal']/div/div/button[2]")
        cusb.click()
        time.sleep(3)

        cos2 =  driver.find_element_by_xpath ("//*[@id='ucb:sp:kwp:kwp-bid-selector-input-field']")
        act.double_click(cos2).perform()
        cos2.send_keys('.25')
        time.sleep(3)


        lis =  driver.find_element_by_xpath ("//*[@id='ucb:sp:kwp:kwp-enter-list-text-input-area']")
        lis.click()
        lis.send_keys('test')
        time.sleep(4)
    
        adkey =  driver.find_element_by_xpath ("//*[@id='keywords-field-wrapper-id']/fieldset/div/span[2]/div/div/div[1]/div[6]/div[2]/div/button")
        adkey.click()
        time.sleep(3)
        


        campn =  driver.find_element_by_xpath ("//*[@id='campaignName-field-wrapper-id']/fieldset/div/span[2]/div/div[1]/div/div/input")
        campn.clear()
        campn.click()
        campn.send_keys('test title')
        time.sleep(3)
        

        dayb =  driver.find_element_by_xpath ("//*[@id='dailyBudget-field-wrapper-id']/fieldset/div/span[2]/div/div/span/div/div/input")
        dayb.click()
        dayb.send_keys('5')
        time.sleep(2)


        time.sleep(30)
        driver.quit()

my_function()


