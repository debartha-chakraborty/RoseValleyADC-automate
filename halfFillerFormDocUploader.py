from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

#Verification URL
verificationURL = "https://www.rosevalleyadc.com/investors.aspx"


def readfile(filename):
    #read the data from the text file
    with open(filename, 'r') as file:
        data = file.read().split('\n')
    return data    

def botVerificationBypass(dig1, dig2):
    return dig1 + dig2

def specialDocUpload(entry):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get(verificationURL)
    
    
    #Certificate Number field txtCertificateNumber
    certificateNumber = driver.find_element(By.ID, 'txtCertificateNumber')
    certificateNumber.send_keys(entry['Investment certificate number'])
    
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
    
    #Redirect to the document upload page lnkUploadCertificate
    uploadButton = driver.find_element(By.ID, 'lnkUploadCertificate')
    uploadButton.click()
    sleep(4)
    
    #Document upload
    ActionChains(driver)\
        .move_to_element(driver.find_element(By.ID, "btnSaveInvestorTransfer"))\
        .perform()
        
    #Original certificate fupInvestorInvestmentCertificates 
    original_certificate = driver.find_element(By.ID, "fupInvestorInvestmentCertificates") #file upload
    original_certificate.send_keys(entry['Certificate_original'])
    sleep(5)
    upload_button = driver.find_element(By.ID, "updInvestorInvestmentCertificates") #button
    upload_button.click()
    
        
        
    #Matured certificate fupInvestorAcknowledgement
    matured_certificate = driver.find_element(By.ID, "fupInvestorAcknowledgement") #file upload
    matured_certificate.send_keys(entry['Certificate_matured_verified'])
    upload_button = driver.find_element(By.ID, "updInvestorAcknowledgement") #button
    upload_button.click()
    
    #ID proof fupInvestorIdentity
    id_proof = driver.find_element(By.ID, "fupInvestorIdentity") #file upload
    id_proof.send_keys(entry['ID_proof'])
    upload_button = driver.find_element(By.ID, "updInvestorIdentity") #button
    upload_button.click()
    
    #Address proof fupInvestorAddress
    address_proof = driver.find_element(By.ID, "fupInvestorAddress") #file upload
    address_proof.send_keys(entry['Address_proof'])
    upload_button = driver.find_element(By.ID, "updInvestorAddress") #button
    upload_button.click()
    
    #Bank first page fupInvestorBankPassbook
    bank_first_page = driver.find_element(By.ID, "fupInvestorBankPassbook") #file upload
    bank_first_page.send_keys(entry['Bank_first_page'])
    upload_button = driver.find_element(By.ID, "updInvestorBankPassbook") #button
    upload_button.click()
    
    #Bank cancelled cheque fupInvestorChequeFoil
    bank_cancelled_cheque = driver.find_element(By.ID, "fupInvestorChequeFoil") #file upload
    bank_cancelled_cheque.send_keys(entry['Bank_cancelled_cheque'])
    upload_button = driver.find_element(By.ID, "updInvestorChequeFoil") #button
    upload_button.click()
    sleep(2)
    
    #Submit btnSaveInvestorTransfer
    submit_button = driver.find_element(By.ID, "btnSaveInvestorTransfer")
    submit_button.click()
    
    sleep(2)
    
    #Close the browser
    driver.quit()

if __name__ == '__main__':
    formNumbers = readfile('alternate_data.txt')
    if formNumbers == ['']:
        print('No data found in the file')
    else:
        

        from dataViewer import readData, rowToDict
        file = 'forminfo.csv'
        data = readData(file)
        data = rowToDict(data)
        entry = data[1]
        specialDocUpload(entry)
        print('Uploaded the documents for certificate number:', entry)
    
