from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from dataViewer import readData, rowToDict

#Upload URL
uploadURL = "https://www.rosevalleyadc.com/upload_certificate.aspx"

#Data loading
file = 'forminfo.csv'
data = readData(file)
data = rowToDict(data)

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--window-size=1920,1080")

def autoFillForm(data):
    driver = webdriver.Chrome(options=options)
    driver.get(uploadURL)
    
    sleep(3)

    #Investor company
    company_selection = driver.find_element(By.ID, "ddlInvesterCompany")
    ActionChains(driver)\
        .move_to_element(company_selection)\
        .click(company_selection)\
        .send_keys(entry['Company'])\
        .click()\
        .perform()
    
    #1st investor details  
    #Name
    first_investor_name = driver.find_element(By.ID, "txtFirstInvestorName") #text box
    first_investor_name.send_keys(entry['1st Investor'])
    #age
    first_investor_age = driver.find_element(By.ID, "txtFirstInvestorAge") #text box
    first_investor_age.send_keys(entry['1st Age'])
    #gender
    first_investor_gender = driver.find_element(By.ID, "ddlFirstInvesterGender") #dropdown
    ActionChains(driver)\
        .move_to_element(first_investor_gender)\
        .click(first_investor_gender)\
        .send_keys(entry["1st Gender"])\
        .click()\
        .perform()
    #phone number
    first_investor_phone = driver.find_element(By.ID, "txtFirstInvestorPhoneNo") #text box
    first_investor_phone.send_keys(entry['1st Phone Number'])
    #email(optional)
    if entry['1st Email'] != 'None':
        first_investor_email = driver.find_element(By.ID, "txtFirstInvestorEmailId")
        first_investor_email.send_keys(entry['1st Email'])
    else:
        print("No email")        
    #verify 
    driver.execute_script("SendOTP();")
    
    sleep(3)
    
    #alert message comes up after clicking verify, press OK
    alert = driver.switch_to.alert
    alert.accept()  
    #Identity type
    first_investor_identity_type = driver.find_element(By.ID, "ddlFirstInvesterIdentity") #dropdown
    ActionChains(driver)\
        .move_to_element(first_investor_identity_type)\
        .click(first_investor_identity_type)\
        .send_keys(entry['1st Identity Type'])\
        .click()\
        .perform()
    #Identity number
    first_investor_identity_number = driver.find_element(By.ID, "txtFirstInvestorAddharNo") #text box
    first_investor_identity_number.send_keys(entry['1st Identity Number'])
    
    #2nd investor(optional)
    #Name
    if entry['2nd Investor'] == 'None':
        print("No 2nd investor")
    else:
        second_investor_name = driver.find_element(By.ID, "txtSecondInvestorName") #text box
        second_investor_name.send_keys(entry['2nd Investor'])
        #age
        second_investor_age = driver.find_element(By.ID, "txtSecondInvestorAge") #text box
        second_investor_age.send_keys(entry['2nd Age'])
        #gender
        second_investor_gender = driver.find_element(By.ID, "ddlSecondInvesterGender") #dropdown
        ActionChains(driver)\
            .move_to_element(second_investor_gender)\
            .click(second_investor_gender)\
            .send_keys(entry['2nd Gender'])\
            .click()\
            .perform()
        #phone number
        second_investor_phone = driver.find_element(By.ID, "txtSecondInvestorPhoneNo")
        second_investor_phone.send_keys(entry['2nd Phone Number'])
        #email(optional)
        if entry['2nd Email'] != 'None':
            second_investor_email = driver.find_element(By.ID, "txtSecondInvestorEmailId")
            second_investor_email.send_keys(entry['2nd Email'])
        #Identity type
        second_investor_identity_type = driver.find_element(By.ID, "ddlSecondInvesterIdentity")
        ActionChains(driver)\
            .move_to_element(second_investor_identity_type)\
            .click(second_investor_identity_type)\
            .send_keys(entry['2nd Identity Type'])\
            .click()\
            .perform()
        #Identity number
        second_investor_identity_number = driver.find_element(By.ID, "txtSecondInvestorAddharNo")
        second_investor_identity_number.send_keys(entry['2nd Identity Number'])  
        
    #Other details
    #Father/Husband name                                  
    father_name = driver.find_element(By.ID, "txtInvestorFatherName") #text box
    father_name.send_keys(entry['Name of Father/Husband'])
    #Address
    address = driver.find_element(By.ID, "txtInvestorAddress") #text box
    address.send_keys(entry['Address'])
    #Street
    street = driver.find_element(By.ID, "txtInvestorStreet") #text box
    street.send_keys(entry['Street'])
    #City
    city = driver.find_element(By.ID, "txtInvestorTown") #text box
    city.send_keys(entry['City'])
    #Post Office
    post_office = driver.find_element(By.ID, "txtInvestorPostOffice") #text box
    post_office.send_keys(entry['Post Office'])
    #Police Station
    police_station = driver.find_element(By.ID, "txtInvestorPoliceStation") #text box
    police_station.send_keys(entry['Police Station'])
    #State
    state = driver.find_element(By.ID, "ddlInvesterState") #dropdown
    ActionChains(driver)\
        .move_to_element(state)\
        .click(state)\
        .send_keys(entry['State'])\
        .click()\
        .perform()
    #District
    district = driver.find_element(By.ID, "ddlInvesterDistrict") #dropdown
    ActionChains(driver)\
        .move_to_element(district)\
        .click(district)\
        .send_keys(entry['District'])\
        .click()\
        .perform()
    #PIN Code
    pin = driver.find_element(By.ID, "txtInvestorPinCode") #text box
    pin.send_keys(entry['PIN Code'])
    
    sleep(1)
    
    
    #Bank details
    #Bank name
    bank_name = driver.find_element(By.ID, "ddlInvesterBank") #dropdown
    ActionChains(driver)\
        .move_to_element(bank_name)\
        .click(bank_name)\
        .send_keys(entry['Bank Name'])\
        .click()\
        .perform()
    #Branch name txtInvestorBankBranch
    branch_name = driver.find_element(By.ID, "txtInvestorBankBranch") #text box
    branch_name.send_keys(entry['Branch name'])
    #Branch code (Optional) txtInvestorBankBranchCode
    if entry['Branch Code'] == 'None':
        print("No branch code")
    else:
        branch_code = driver.find_element(By.ID, "txtInvestorBankBranchCode") #text box
        branch_code.send_keys(entry['Branch Code'])
    #Account number txtInvestorBankAccountNo
    account_number = driver.find_element(By.ID, "txtInvestorBankAccountNo") #text box
    account_number.send_keys(entry['Account Number'])
    #MICR(Optional) txtInvestorBankMICR
    if entry['MICR'] == 'None':
        print("No MICR")
    else:
        micr = driver.find_element(By.ID, "txtInvestorBankMICR") #text box
        micr.send_keys(entry['MICR'])
    #IFSC txtInvestorBankIFSC
    ifsc = driver.find_element(By.ID, "txtInvestorBankIFSC") #text box
    ifsc.send_keys(entry['IFSC'])
    
    sleep(1)
    
    #Investment details
    #Investment certificate number txtInvestmentCertificateNo
    certificate_number = driver.find_element(By.ID, "txtInvestmentCertificateNo") #text box
    certificate_number.send_keys(entry['Investment certificate number'])
    #Name of certificate holder txtInvestmentCertificateHolder
    certificate_holder = driver.find_element(By.ID, "txtInvestmentCertificateHoderName") #text box
    certificate_holder.send_keys(entry['Name of certificate holder'])
    
    #Date of Investment txtInvestmentDate
    investment_date = driver.find_element(By.ID, "txtInvestmentDate") #calendar
    #change read-only attribute to false
    driver.execute_script("document.getElementById('txtInvestmentDate').removeAttribute('readonly');")
    day, month, year = entry['Date of Investment'].split('/')
    investment_date.send_keys(f"{year}-{month}-{day}")
    
    #Amount of Investment txtInvestmentAmount
    investment_amount = driver.find_element(By.ID, "txtInvestmentAmount") #text box
    investment_amount.send_keys(entry['Amount of Investment'])
    
    #Date of Maturity txtInvestmentMaturityDate
    maturity_date = driver.find_element(By.ID, "txtMaturityDate") #calendar
    driver.execute_script("document.getElementById('txtMaturityDate').removeAttribute('readonly');")
    day, month, year = entry['Date of Maturity'].split('/')
    maturity_date.send_keys(f"{year}-{month}-{day}")
    #Amount Received at maturity txtInvestmentMaturityAmount
    maturity_amount = driver.find_element(By.ID, "txtAmountReceived") #text box
    maturity_amount.send_keys(entry['Amount Received at maturity'])
    #Principal not refunded txtInvestmentPrincipalNotRefunded
    principal_not_refunded = driver.find_element(By.ID, "txtAmountClaimed") #text box
    principal_not_refunded.send_keys(entry['Principal not refunded'])
    #Amount entitled to get txtInvestmentAmountEntitled
    amount_entitled = driver.find_element(By.ID, "txtAmountEntitled") #text box
    amount_entitled.send_keys(entry['Amount entitled to get'])
    
    #Move to Document upload
    driver.execute_script("SaveInvestor();")
    
    sleep(2)
    
    
    #Document upload
    
    #scroll to the bottom
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
    sleep(5)
    
    #Submit btnSaveInvestorTransfer
    submit_button = driver.find_element(By.ID, "btnSaveInvestorTransfer")
    submit_button.click()
    
    sleep(2)
    
    #close session
    driver.quit()


if __name__ == '__main__':
    for entry in data:
        autoFillForm(entry)
        print("All Form filled")
    





