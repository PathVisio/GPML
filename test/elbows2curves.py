import glob
import xml.etree.ElementTree as ET

NS = {'gpml': "http://pathvisio.org/GPML/2013a"}

ET.register_namespace('', NS['gpml'])

inputs = set(glob.glob('./2013a/edge-elbow-*.gpml'))
for source_path in inputs:
    output_path = source_path.replace('elbow', 'curved')

    tree = ET.parse(source_path)

    pathway = tree.getroot()

    graphics_els = pathway.findall(
        ".//*[@ConnectorType='Elbow']",
        NS)

    for graphics_el in graphics_els:
        graphics_el.set("ConnectorType", 'Curved')

    tree.write(output_path,
               xml_declaration=True,
               encoding='utf-8',
               method='xml')
