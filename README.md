# Rose Vally ADC automation

####  Before running any files make sure you have all dependencies.
Install _Python 3.8+_
Open the terminal and run 
`pip install -r requirements.txt`

### Data should be CSV file with all the columns in the file.
Default CSV name *forminfo.csv*
## Input Data Format
#### Columns
- Company
- 1st Investor
- 1st Age
- 1st Gender
- 1st Phone Number
- 1st Email (Optional)
- 1st Identity Type
- 1st Identity Number
- 2nd Investor (Optional)
- 2nd Age (Optional)
- 2nd Gender (Optional)
- 2nd Phone Number (Optional)
- 2nd Email (Optional)
- 2nd Identity Type (Optional)
- 2nd Identity Number (Optional)
- Name of Father/Husband,Address
- Street
- City
- Post Office
- Police Station
- State
- District
- PIN Code
- Bank Name
- Branch name
- Branch Code (Optional)
- Account Number
- MICR (Optional)
- IFSC
- Investment certificate number
- Name of certificate holder
- Date of Investment
- Amount of Investment
- Date of Maturity
- Amount Received at maturity
- Principal not refunded
- Amount entitled to get
- Certificate_original (path to the pdf document)
- Certificate_matured_verified (path to the pdf document)
- ID_proof (path to the pdf document)
- Address_proof (path to the pdf document)
- Bank_first_page (path to the pdf document)
- Bank_cancelled_cheque (path to the pdf document)


## Execution instructions
To fill fresh forms, run the `autoFormFiller.py` file
To fill forms which are filled upto basic information, run `halfFilledFormDocUploader.py` file
To Download Acknowledgement forms, run `semiAutoAcknowledgementDownloader.py` file

