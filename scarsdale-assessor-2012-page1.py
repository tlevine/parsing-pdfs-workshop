# Pretty way
import lxml.etree
svg = lxml.etree.parse('scarsdale-assessor-2012-page1.svg')
svg.xpath('//svg:g', namespaces = {'svg':'http://www.w3.org/2000/svg'})

# Ugly way
import lxml.html
svg = lxml.html.parse('scarsdale-assessor-2012-page1.svg')
svg.xpath('//g')

# Let's use the pretty way. It turns out that there are three nested groups,
# as we can see inside the Inkscape GUI.
svg = lxml.etree.parse('scarsdale-assessor-2012-page1.svg')
svg.xpath('//svg:g/svg:g/svg:g', namespaces = {'svg':'http://www.w3.org/2000/svg'})
svg.xpath('//svg:g/svg:g/svg:g/*', namespaces = {'svg':'http://www.w3.org/2000/svg'})
svg.xpath('//svg:g/svg:g/svg:g/svg:text/*', namespaces = {'svg':'http://www.w3.org/2000/svg'})
print(svg.xpath('count(//svg:g/svg:g/svg:g/svg:text/*)', namespaces = {'svg':'http://www.w3.org/2000/svg'}))

def rows(svg):
    texts = svg.xpath('//svg:g/svg:g/svg:g/svg:text/svg:tspan/text()', namespaces = {'svg':'http://www.w3.org/2000/svg'})
    thisrow = []
    for text in texts:
        thisrow.append(text)
        if '***' in text and thisrow != []:
            yield thisrow
            thisrow = []

import struct
def cleanrow(row):
    pass #01.01.3 OX 210 1 FAMILY RES COUNTY TAXABLE 20,200 

print(list(rows(svg)))
