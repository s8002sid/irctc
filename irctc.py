#irctc javascript generator
import os;
#Input
dataFile="data.csv"
#Default validation data
#0-> name, 1-> age, 2-> sex, 3-> birthpref, 4-> idcardtype,
#5-> food, 6->idCardNumber, 7-> senior
nameLen=16
ageList=[13,110]
sexList=['M', 'F'];
birthPrefList=['UB', 'LB', 'MB', 'SU', 'SL'];
idCardTypeList=['DRIVING_LICENSE','PASSPORT,PANCARD','VOTER_ICARD','GOVT_ICARD',
                'STUDENT_ICARD','BANK_PASSBOOK','CREDIT_CARD','UNIQUE_ICARD'];
foorList=['V', 'N'];
seniorList=['TRUE', 'FALSE'];


mobileNumber="9582581552"
consAutoUpgrade="true"

mobileNumber=input('Mobile Number: ');

fob = open("data.csv");
data = fob.readlines();
fob.close();
splittedData=[e.split(",") for e in data]
for i in range(4,len(splittedData)):
    splittedData.remove(4);

for i in range(len(splittedData)):
    splittedData[i][0] = splittedData[i][0][:nameLen];
    splittedData[i][0]="%20".join(splittedData[i][0].split(" "));


basicIf="if(document.getElementById('%s')!=null){document.getElementById('%s').value='%s'}"
basicCheck="if(document.getElementById('%s')!=null){document.getElementById('%s').checked='%s'}"
ifCheck="if(document.getElementById('addPassengerForm:psdetail:%d:%s')!=null)\
{document.getElementById('addPassengerForm:psdetail:%d:%s').value='%s'}"
ifFocus="if(document.getElementById('%s')!=null){document.getElementById('%s').focus();document.getElementById('%s').select();}"

js=r"javascript:function%20E(){";

psgn = "document.getElementById('addPassengerForm:psdetail:tb').rows[%d].cells[1].children[0]"
psgnIf="if(" + psgn + "!=null){" + psgn + ".value='%s'}"
#    js+=ifCheck%(i, "psgnName", i, "psgnName", ld[0]);
for i in range(len(splittedData)):
    ld=splittedData[i];#localData
    js+=psgnIf%(i, i, ld[0]);
    js+=ifCheck%(i, "psgnAge", i, "psgnAge", ld[1]);
    js+=ifCheck%(i, "psgnGender", i, "psgnGender", ld[2]);
    js+=ifCheck%(i, "berthChoice", i, "berthChoice", ld[3]);
    js+=ifCheck%(i, "idCardType", i, "idCardType", ld[4]);
    js+=ifCheck%(i, "foodChoice", i, "foodChoice", ld[5]);
    js+=ifCheck%(i, "idCardNumber", i, "idCardNumber", ld[6]);
js+=basicIf%("addPassengerForm:mobileNo", "addPassengerForm:mobileNo", mobileNumber);
js+=basicCheck%("addPassengerForm:autoUpgrade", "addPassengerForm:autoUpgrade", consAutoUpgrade);
js+=ifFocus%("j_captcha", "j_captcha", "j_captcha")
js+="}E()"
print ( js );
html='<html>\n\t\
<Title>IRCTC Bookmark</Title>\
<body>\n\t\t\
<a href="' + js + '">IRCTC</a>\n\t\
<br/>Add this link to bookmark and click this bookmark on IRCTC form fill page to auto fill data\n\t\
<br/>' + "\n".join(data) +'\
</body>\n\
</html>'
fob=open("IRCTC.html","w");
fob.write(html);
fob.close();
os.system("start " + "IRCTC.html");

