from ConfigParser import SafeConfigParser
import datetime

def getGlobal(vari):
    parser = SafeConfigParser()
    parser.read('config.ini')
    variable = parser.get('SETTINGS', vari)
    return variable


#remember when you set variable, if you put string, use ' instead of ". 
# using qutation means you want to put qutation into the string literally.
def setGlobal(variableName, newValue):
    parser = SafeConfigParser()
    parser.read('config.ini')
    parser.set('SETTINGS', variableName, newValue)
    with open('config.ini', 'wb') as configfile: 
        parser.write(configfile)
    variable = parser.get('SETTINGS', variableName)
    return variable

def setTime():
    parser = SafeConfigParser()
    parser.read('config.ini')
    now = datetime.datetime.now()
    parser.set('SETTINGS', 'year', str(now.year))
    with open('config.ini', 'wb') as configfile: 
        parser.write(configfile)
    parser.set('SETTINGS', 'month', str(now.month))
    with open('config.ini', 'wb') as configfile: 
        parser.write(configfile)
    parser.set('SETTINGS', 'day', str(now.day))
    with open('config.ini', 'wb') as configfile: 
        parser.write(configfile)
    parser.set('SETTINGS', 'hour', str(now.hour))
    with open('config.ini', 'wb') as configfile: 
        parser.write(configfile)
    parser.set('SETTINGS', 'minute', str(now.minute))
    with open('config.ini', 'wb') as configfile: 
        parser.write(configfile)
    parser.set('SETTINGS', 'second', str(now.second))
    with open('config.ini', 'wb') as configfile: 
        parser.write(configfile)
    date = '{0}-{1}-{2}'.format(str(now.year), str(now.month), str(now.day))
    parser.set('SETTINGS', 'date', date)
    with open('config.ini', 'wb') as configfile: 
        parser.write(configfile)



    
if __name__=='__main__':
    # variable = getGlobal(parser, 'useremail')
    setTime()

