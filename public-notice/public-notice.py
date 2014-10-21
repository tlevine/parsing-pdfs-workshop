#!/usr/bin/env python
import lxml.etree

xml = lxml.etree.parse('public_notice.xml')

# Select the header
print(xml.xpath('//text[b[contains(text(),"PUBLIC NOTICE")]]'))

# Select the from address
print(xml.xpath('//page[@number="1"]/text[@top < 300 and @left < 400]/text()'))
