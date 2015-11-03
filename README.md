irctc - irctc site auto form filler

#USE

To use this script install python 2.7.x 
generate the data.csv file
data.csv is a comma separated file which contains following information in one line for each passenger:

- NAME: Name of the person
- AGE: Age of the person
- GENDER: [M/F] One of this value in gender
- BIRTH PREF: [LB/MB/UB/SL/SU] Provide of the these values for birth preference
- ID CARD TYPE: [DRIVING_LICENSE/PASSPORT,PANCARD/VOTER_ICARD/GOVT_ICARD/STUDENT_ICARD/BANK_PASSBOOK/CREDIT_CARD/UNIQUE_ICARD] Provide one of these values
- FOOD PREF: [V/N] V for Veg and N for Non-Veg
- ID CARD NUMBER: Provide valid ID Card Number
- SENIOR CITIZEN: [TRUE/FLASE] provide one of these value.

#HOW TO RUN
1. Prepare the data.csv in above format.
2. Run the irctc.py file
3. Enter mobile number
4. A HTML page will get generated and will get opened in the default browser.
5. There will be a link named IRCTC, bookmark this link
6. login to IRCTC site, select the train, once redirected to passenger detail page click on this newly added bookmark.
7. All details including mobile number, auto-upgradation will be done and page will be focussed on captcha box.
8. Enter the captcha and make payment.

Thats all.
