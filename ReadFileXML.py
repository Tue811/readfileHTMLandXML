from bs4 import BeautifulSoup

with open('FileXML.xml', 'r') as f:
    data = f.read()
wf = open('KetQua.txt', 'w')

bs_data = BeautifulSoup(data, 'xml')

wf.write("ID       Name             Age  Room\n")
id = 0
for employee in bs_data.findAll('employee'):
    id+=1
    wf.write("{}  {}     {}  {}\n".format(id, employee.fullname.get_text(), employee.age.get_text(), employee.room.get_text()))

f.close()
wf.close()