from lxml import etree
import sys

f = open('C:\\xml\\output.xml', 'a', encoding="utf-8")
results = []

# 1~50000
tree = etree.parse("C:\\xml\\857973_50000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)

# 50001~100000
tree = etree.parse("C:\\xml\\857973_100000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)

# 100001~150000
tree = etree.parse("C:\\xml\\857973_150000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)

# 150001~200000
tree = etree.parse("C:\\xml\\857973_200000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)
		
# 200001~250000
tree = etree.parse("C:\\xml\\857973_250000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)
		
# 250001~300000
tree = etree.parse("C:\\xml\\857973_300000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)
		
# 300001~350000
tree = etree.parse("C:\\xml\\857973_350000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)
		
# 350001~400000
tree = etree.parse("C:\\xml\\857973_400000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)
		
# 400001~450000
tree = etree.parse("C:\\xml\\857973_450000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)
		
# 450001~500000
tree = etree.parse("C:\\xml\\857973_500000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)
		
# 500001~550000
tree = etree.parse("C:\\xml\\857973_550000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)
		
# 550001~600000
tree = etree.parse("C:\\xml\\857973_600000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)
		
# 600001~650000
tree = etree.parse("C:\\xml\\857973_650000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)
		
# 650001~700000
tree = etree.parse("C:\\xml\\857973_700000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)
		
# 700001~750000
tree = etree.parse("C:\\xml\\857973_750000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)
		
# 750001~800000
tree = etree.parse("C:\\xml\\857973_800000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)
		
# 800001~850000
tree = etree.parse("C:\\xml\\857973_850000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)
		
# 850001~900000
tree = etree.parse("C:\\xml\\857973_900000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)
		
# 900001~950000
tree = etree.parse("C:\\xml\\857973_950000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)
		
# 950001~1000000
tree = etree.parse("C:\\xml\\857973_1000000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)
		
# 1000001~1050000
tree = etree.parse("C:\\xml\\857973_1050000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)
		
# 1050001~1100000
tree = etree.parse("C:\\xml\\857973_1100000.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)
		
# 1100001~1145050
tree = etree.parse("C:\\xml\\857973_1145050.xml")
root = tree.getroot()

for region_info in root.findall("item/senseInfo/region_info"):
	if(region_info.findtext("region") == "경남" or region_info.findtext("region") == "경북" or region_info.findtext("region") == "경상"):
		item = region_info.getparent().getparent()
		results.append(item)

# save XML
for result in results:
	f.write(etree.tostring(result, encoding="unicode"))

f.close()
