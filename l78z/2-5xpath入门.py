from lxml import etree


xml="""
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <author>
        <nick>周大强</nick>
        <nick>周芷若</nick>
    </author>
</book>
"""
tree=etree.XML(xml)
result1=tree.xpath("/book/name/text()")
print(type(result1))
result2=tree.xpath("/book/author/nick/text()")
print(result1)
print(result2)