# File: xml_format.py
# Description: Examples on how to process xml files in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Examples on how to process xml files in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/XML_files_in_Python (date of access: XX.XX.XXXX)




# Working with files in xml format

from xml.etree import ElementTree

# Building a tree from the xml file
tree = ElementTree.parse('example.xml')

# Extracting the root from the tree
root = tree.getroot()
# To get root from string we can use:
# root = ElementTree.fromstring(string_xml_data)

# Showing the root, tags and attributes
print(root)
print(root.tag, root.attrib)

# Going through all children from the tree
for child in root:
    print(child.tag, child.attrib)

# Showing the information from first child about its first child
print(root[0][0].text)

# Using iter showing the scores
for element in root.iter('scores'):
    score_sum = 0
    for child in element:
        score_sum += float(child.text)
    print(score_sum)

# Changing some information
greg = root[0]
module1 = next(greg.iter('module1'))
print(module1, module1.text)
module1.text = str(float(module1.text) + 30)

# Adding the attribute to the certificate with method 'set'
certificate = greg[2]
certificate.set('type', 'with distinction')

# Adding new tag with 'Element'
description = ElementTree.Element('description')
description.text = 'Showed excellent skills during the course'
greg.append(description)

# Removing tag with method 'find' - it'll find only the first found tag
description = greg.find('description')
greg.remove(description)

# Writing data in the xml file
tree.write('example_copy.xml')


# Creating xml file from the very beginning
# Creating tag 'student'
root = ElementTree.Element('student')

# Creating a children of elements by 'SubElement' and writing the text inside them
first_name = ElementTree.SubElement(root, 'firstName')
first_name.text = 'Greg'

second_name = ElementTree.SubElement(root, 'secondName')
second_name.text = 'Dean'

scores = ElementTree.SubElement(root, 'scores')

module1 = ElementTree.SubElement(scores, 'module1')
module1.text = '100'

module2 = ElementTree.SubElement(scores, 'module2')
module2.text = '100'

module3 = ElementTree.SubElement(scores, 'module3')
module3.text = '100'

# Collecting all tags into the tree
tree = ElementTree.ElementTree(root)

# Writing tree in the xml file
tree.write('example_new.xml')

