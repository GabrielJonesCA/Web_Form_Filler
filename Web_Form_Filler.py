import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import numpy as np



def my_function():

        global driver
        driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
        driver.get('https://gov.texas.gov/apps/contact/opinion.aspx');
        time.sleep(1.5) # Let the user actually see something!


        # PREFIX DROP DOWN
        pre_dropdwn = driver.find_element_by_name("ctl00$ContentPlaceHolder1$DropDownList1")
        pdd = Select(pre_dropdwn)
        pdd.select_by_index(8) #8 is 'none'
        time.sleep(1.5)

        # FIRST NAME BOX 
        arrayf = ['Liam', 'Noah', 'Mateo', 'Elijah', 'Sebastian', 'Olivia', 'Emma', 'Camila', 'Isabella', 'Mia']
        x = np.random.choice(arrayf, size=1)
        search_box_first = driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtFirst")
        search_box_first.send_keys(x)
        time.sleep(1.5)

        # LAST NAME BOX 
        arrayl = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia']
        y = np.random.choice(arrayl, size=1)
        search_box_last = driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtLast")
        search_box_last.send_keys(y)
        time.sleep(1.5)

        # ADDRESS Click 
        clk_ad =  driver.find_element_by_name("ctl00$ContentPlaceHolder1$RadioButtonList1")
        clk_ad.click()
        time.sleep(1.5)

        # ADDRESS BOX 
        arrayst = ['Second st', 'First st', 'Pecan st', 'Third st', 'Cedar st', 'Fourth st', 'Main st' , 'Fifth']
        x1 = np.random.choice(arrayst, size=1)
        arraynum = ['101', '262', '193', '405', '35', '782', '924' , '530']
        x2 = np.random.choice(arraynum, size=1)
        search_box_add = driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtAddress")
        search_box_add.send_keys(x2)
        search_box_add.send_keys(" ")
        search_box_add.send_keys(x1)
        time.sleep(1.5)

        # CITY BOX 
        arrayc = ['Houston', 'San Antonio', 'Dallas', 'Austin', 'Fort Worth', 'El Paso', 'Arlington' , 'Corpus Christi']
        y1 = np.random.choice(arrayc, size=1)
        search_box_cty = driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtCity")
        search_box_cty.send_keys(y1)
        time.sleep(1.5)


        # ZIP CODE BOX
        z = '77001' 
        if y1 == 'Houston':
            z = '77001' 
        elif y1 == 'San Antonio':
            z = '78015'
        elif y1 == 'Dallas':
            z = '75001'
        elif y1 == 'Austin':
            z = '73301'
        elif y1 == 'Fort Worth':
            z = '76006' 
        elif y1 == 'El Paso':
            z = '79835'
        elif y1 == 'Arlington':
            z = '76001'
        elif y1 == 'Corpus Christi':
            z = '78336'


        search_box_zp = driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtZip")
        search_box_zp.send_keys(z)
        time.sleep(1.5)


        # EMAIL BOX
        search_box_e = driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtEmail")
        search_box_e.send_keys(x , y ,'@Gmail.com')
        time.sleep(1.5)

        # CONFIRM EMAIL BOX
        search_box_e2 = driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtEmail2")
        search_box_e2.send_keys(x , y ,'@Gmail.com')
        time.sleep(1.5)

        # ISSUE DROP DOWN
        iss_dropdwn = driver.find_element_by_name("ctl00$ContentPlaceHolder1$DropDownList2")
        pdd = Select(iss_dropdwn)
        pdd.select_by_index(11)
        time.sleep(1.5)


        #MESSAGE BOX
        search_box_e = driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtMessage")


        ##########################################################
        ########## HERE IS WHERE YOU ENTER YOUR MESSAGE ##########
        ##########################################################

        search_box_e.send_keys('Go fuck yourself Governor Abbott')
        time.sleep(1.5)


        ##########################################################

        # ADDRESS Click 
        clk_send =  driver.find_element_by_name("ctl00$ContentPlaceHolder1$Button1")
        clk_send.click()
        time.sleep(1.5)

        driver.quit()


# running function how ever many times you want
count = 0

while count < 3:
        my_function()
        count = count + 1






