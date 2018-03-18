from ConfigParser import SafeConfigParser

def getGlobal(vari):
    parser = SafeConfigParser()
    parser.read('config.ini')
    variable = parser.get('SETTINGS', vari)
    return variable

def setGlobal(variableName, newValue):
    parser = SafeConfigParser()
    parser.read('config.ini')
    parser.set('SETTINGS', variableName, newValue)
    with open('config.ini', 'wb') as configfile: 
        parser.write(configfile)
    variable = parser.get('SETTINGS', variableName)
    return variable

    
if __name__=='__main__':
    # variable = getGlobal(parser, 'useremail')
    variable2 = setGlobal('useremail', 'change222d@gmail.com')
    print variable2
    




