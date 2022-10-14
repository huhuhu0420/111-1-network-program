import xml.etree.ElementTree as et
tree = et.parse('data1.xml') #解析xml檔，回傳ElementTree物件
root = tree.getroot() #獲得根節點
row = et.SubElement(root, 'row')
sno = et.SubElement(row, 'sno')
sno.text = '1033'
sna = et.SubElement(row, 'sna')
sna.text = '家樂福新店店'
tot = et.SubElement(row, 'tot')
tot.text = '30'
sbi = et.SubElement(row, 'sbi')
sbi.text = '29'
sarea = et.SubElement(row, 'sarea')
sarea.text = '新店區'
for data in root:
    if (data.find('sno').text == '1018'):
        data.find('sbi').text = '0'
tree.write("data2.xml",encoding= "utf-8")

tree = et.parse('data2.xml')
root = tree.getroot()
for data in root:
    if (data.find('sarea').text == '新店區'):
        print(data.find('sno').text, data.find('sna').text, data.find('tot').text, data.find('sbi').text)