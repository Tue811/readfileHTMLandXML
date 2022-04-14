import xml.etree.ElementTee as ET

data = ET.Element('chess')

element1 = ET.SubElenment(data, 'Opening')

s_elem1 = ET.SubElenment(element1, 'E4')
s_elem2 = ET.SubElenment(element2, 'D4')

s_elem1.set('type','Accepted')
s_elem2.set('type', 'Declined')

s_elem1.text= "King's Gambit Accepted"
s_elem2.text = "Queen's Gambit Delined"

b_xml = ET.tostring(data)

with open("GFG.xml","wb") as f:
    f.write(b_xml)