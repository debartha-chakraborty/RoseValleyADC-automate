from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

#Verification URL
verificationURL = "https://www.rosevalleyadc.com/investors.aspx"


def readfile(filename):
    from dataViewer import readData, rowToDict
    data = readData(filename)
    data = rowToDict(data)
    
    formNumbers = [entry['Investment certificate number'] for entry in data]
    return formNumbers

def botVerificationBypass(dig1, dig2):
    return dig1 + dig2


if __name__ == '__main__':
    formNumbers = readfile('alternate_data.txt')
    if formNumbers == ['']:
        print('No data found in the file')
    else:
        #Open the browser
        #headless mode
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument("--window-size=1920,1080")

        for entry in formNumbers[5:]:
            driver = webdriver.Chrome(options=options)
            driver.get(verificationURL)
            
            #Certificate Number field txtCertificateNumber
            certificateNumber = driver.find_element(By.ID, 'txtCertificateNumber')
            certificateNumber.send_keys(entry)
            
            #Solve the captcha
            captcha = driver.find_element(By.ID, 'lblCaptcha')
            captcha = captcha.find_element(By.CLASS_NAME, 'submit__generated')
            digits = captcha.find_elements(By.TAG_NAME, 'span')
            sleep(1)
            result = botVerificationBypass(int(digits[0].text), int(digits[1].text))
            sleep(2)
            
            #Enter the result in the captcha field class submit__input
            captchaField = driver.find_element(By.CLASS_NAME, 'submit__input')
            captchaField.send_keys(result)
            
            #search for the certificate number 
            searchButton = driver.find_element(By.ID, 'btnSearch')
            searchButton.click()
            
            sleep(2)
            
            #open download modal span id divInvestorAcknowledgementNo
            downloadButton = driver.find_element(By.ID, 'divInvestorAcknowledgementNo')
            downloadButton.click()
            
            sleep(2)
            #print 
            printButton = driver.find_element(By.ID, 'btnPrint')
            printButton.click()
            
            #Allow user to download the file
            sleep(10)
            
            #Close the browser
            driver.quit()
