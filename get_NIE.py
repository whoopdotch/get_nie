#####################
# EDIT THESE LINES: #
#####################

passport = ""
first_name = ""
family_name = ""
complete = False
tel_number = "" 
email = ""

#######################
# START OF THE SCRIPT #
#######################

# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import FirefoxOptions

import time

opts = FirefoxOptions()
#opts.add_argument("--headless")

import winsound
duration = 1000  # milliseconds
freq = 440  # Hz

#driver = webdriver.Firefox(options=opts)
driver = webdriver.Firefox()
#driver = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')

complete = False
while complete == False:
    
    time.sleep(5) 

    driver.get("https://sede.administracionespublicas.gob.es/icpplus/index")
    
    driver.find_element_by_xpath("//select[contains(@id, 'form')]/option[text()='Barcelona']").click()
    #driver.find_element_by_xpath("//select[contains(@id, 'form')]/option[text()='Burgos']").click()
    driver.find_element_by_xpath("//input[contains(@id, 'btnAceptar')]").click()
    
    #driver.find_element_by_xpath("//select[contains(@id, 'sede')]/option[text()='CNP COMISARIA BADALONA, AVDA. DELS VENTS, 9']").click()
 
    driver.find_element_by_xpath("//select[contains(@id, 'tramiteGrupo[0]')]/option[text()='POLICIA-CERTIFICADO DE REGISTRO DE CIUDADANO DE LA U.E.']").click()
    
    driver.find_element_by_xpath("//input[contains(@id, 'btnAceptar')]").click()
    driver.find_element_by_xpath("//input[contains(@id, 'btnEntrar')]").click()

    driver.find_element_by_xpath("//input[contains(@id, 'rdbTipoDocPas')]").click()

    time.sleep(3)

    driver.find_element_by_xpath("//input[contains(@id, 'txtIdCitado')]").send_keys(passport)
    driver.find_element_by_xpath("//input[contains(@id, 'txtDesCitado')]").send_keys(first_name + " " + family_name)

    driver.find_element_by_xpath("//input[contains(@id, 'btnEnviar')]").click()

    driver.find_element_by_xpath("//input[contains(@id, 'btnEnviar')]").click()
    
    
    if "En este momento no hay citas disponibles." in driver.page_source:
        print("not found")
        continue
    else: 
        winsound.Beep(freq, duration)
        page_source = driver.page_source
        
        #driver.find_element_by_xpath("//select[contains(@id, 'idSede')]").click()
        driver.find_element_by_xpath("//input[contains(@id, 'btnSiguiente')]").click()

        driver.find_element_by_xpath("//input[contains(@id, 'txtTelefonoCitado')]").send_keys(tel_number)

        driver.find_element_by_xpath("//input[contains(@id, 'emailUNO')]").send_keys(email)
                       
        driver.find_element_by_xpath("//input[contains(@id, 'emailDOS')]").send_keys(email)
                       
        driver.find_element_by_xpath("//input[contains(@id, 'btnSiguiente')]").click()

        driver.find_elements_by_xpath("//input[contains(@name, 'rdbCita')]")[0].click()
    
        driver.find_element_by_xpath("//input[contains(@id, 'btnSiguiente')]").click()

        driver.switch_to.alert.accept() 
        
        # add SMS

        driver.find_element_by_xpath("//input[contains(@id, 'chkTotal')]").click()
        driver.find_element_by_xpath("//input[contains(@id, 'enviarCorreo')]").click()

        driver.find_element_by_xpath("//input[contains(@id, 'btnConfirmar')]").click()
        complete = True
        

driver.quit() 
