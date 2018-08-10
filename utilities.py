class clXML():
    def __init__(self):
        '''
            input: [folder, filename, path, width, heigth, name, xmin, xmax, ymin, ymax]
        '''

        self.folder     = ''
        self.filename   = ''
        self.path       = ''
        self.width      = ''
        self.heigth     = ''
        self.boxes      = []

def xml_to_xy(file):
    lines = [line.rstrip('\n') for line in open(file)]

    xml_data = clXML()

    xml_data.folder   = lines[1].replace('<folder>'  , '').replace('</folder>'  , '').replace(' ', '').replace('\t', '').lstrip(' ').lstrip('\t')
    xml_data.filename = lines[2].replace('<filename>', '').replace('</filename>', '').replace(' ', '').replace('\t', '').lstrip(' ').lstrip('\t')
    xml_data.path     = lines[3].replace('<path>'    , '').replace('</path>'    , '').replace(' ', '').replace('\t', '').lstrip(' ').lstrip('\t')
    xml_data.width    = lines[8].replace('<width>'    , '').replace('</width>'    , '').replace(' ', '').replace('\t', '').lstrip(' ').lstrip('\t')
    xml_data.height   = lines[9].replace('<height>'    , '').replace('</height>'    , '').replace(' ', '').replace('\t', '').lstrip(' ').lstrip('\t')

    NON_OBJECT_LINE_COUNT = 15
    OBJECT_LINE_COUNT     = 12

    boxes_count = int((len(lines) - NON_OBJECT_LINE_COUNT)/OBJECT_LINE_COUNT)

    xml_data.boxes = []

    for box in range(boxes_count):

        name = lines[NON_OBJECT_LINE_COUNT - 2 + box * OBJECT_LINE_COUNT + 1].replace('<name>'  , '').replace('</name>'  , '').replace(' ', '').replace('\t', '').lstrip(' ').lstrip('\t')

        xmin = lines[NON_OBJECT_LINE_COUNT - 2 + box * OBJECT_LINE_COUNT + 6].replace('<xmin>'  , '').replace('</xmin>'  , '').replace(' ', '').replace('\t', '').lstrip(' ').lstrip('\t')
        xmax = lines[NON_OBJECT_LINE_COUNT - 2 + box * OBJECT_LINE_COUNT + 7].replace('<xmax>'  , '').replace('</xmax>'  , '').replace(' ', '').replace('\t', '').lstrip(' ').lstrip('\t')
        ymin = lines[NON_OBJECT_LINE_COUNT - 2 + box * OBJECT_LINE_COUNT + 8].replace('<ymin>'  , '').replace('</ymin>'  , '').replace(' ', '').replace('\t', '').lstrip(' ').lstrip('\t')
        ymax = lines[NON_OBJECT_LINE_COUNT - 2 + box * OBJECT_LINE_COUNT + 9].replace('<ymax>'  , '').replace('</ymax>'  , '').replace(' ', '').replace('\t', '').lstrip(' ').lstrip('\t')

        xml_data.boxes.append({'name' : name, 'xmin' : xmin, 'xmax' : xmax, 'ymin' : ymin, 'ymax' : ymax })

    return xml_data

def xy_to_xml(path, xml_data):
    xml = open(path + xml_data.filename[:-4] + '.xml', "w")

    xml.write(
                '<annotation>\n'                                        +
                '    <folder>'   + xml_data.folder   + '</folder>\n'    +
                '    <filename>' + xml_data.filename + '</filename>\n'  +
                '    <path>'     + xml_data.path     + '</path>\n'      +
                '    <source>\n'                                        +
                '        <database>Unknown</database>\n'                +
                '    </source>\n'                                       +
                '    <size>\n'                                          +
                '        <width>'  + xml_data.width  + '</width>\n'     +
                '        <height>' + xml_data.height + '</height>\n'    +
                '        <depth>3</depth>\n'                            +
                '    </size>\n'                                         +
                '    <segmented>0</segmented>\n'
             )
    for box in xml_data.boxes:
        xml.write(
                '    <object>\n'                                        +
                '        <name>' + box['name'] + '</name>\n'            +
                '        <pose>Unspecified</pose>\n'                    +
                '        <truncated>1</truncated>\n'                    +
                '        <difficult>0</difficult>\n'                    +
                '        <bndbox>\n'                                    +
                '            <xmin>' + box['xmin'] + '</xmin>\n'        +
                '            <ymin>' + box['ymin'] + '</ymin>\n'        +
                '            <xmax>' + box['xmax'] + '</xmax>\n'        +
                '            <ymax>' + box['ymax'] + '</ymax>\n'        +
                '        </bndbox>\n'                                   +
                '    </object>\n'
                 )
    xml.write(
                '</annotation>\n'
             )
    xml.close()
