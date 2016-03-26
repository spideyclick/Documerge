### CONFIGURATION ###

markerStart='<!-- marker start-->'
markerEnd='<!-- marker end-->'

### END CONFIGURATION ###

import os, sys

if os.name == 'posix':
    osSlash='/'
else:
    osSlash='\\'
errorLog=''

#print(os.listdir(os.path.dirname(os.path.realpath(sys.argv[0])))) # print contents of the folder in which the script resides
#print(os.path.basename(sys.argv[0])) # Just current running file's name
#print(sys.argv[0]) #Current path from CWD + filename
#print(os.listdir(os.getcwd())) # Contents of folder you were in when calling the script
currentDir = os.path.dirname(os.path.realpath(sys.argv[0])) # The path up to the folder of the currently running script
oldFiles = os.listdir(currentDir + osSlash + 'old')
newFiles = os.listdir(currentDir + osSlash + 'new')

for file in oldFiles:
    if os.path.isfile(currentDir + osSlash + 'old' + osSlash + file) and file != os.path.basename(sys.argv[0]):
        print('')
        mergedData={}
        if file not in newFiles:
            errorLog+=('\nreplacement file not found for ' + file)
        else:
            print('Merging text in ' + file)
            currentNewFile=open(str(currentDir + osSlash + 'new' + osSlash + file), 'r')
            currentOldFile=open(str(currentDir + osSlash + 'old' + osSlash + file), 'r')
            replacelines=True
            segmentNumber=0 # Evens
            for line in currentNewFile:
                if markerStart in line:
                    try:
                        mergedData[segmentNumber] += (markerStart + '\n')
                    except KeyError:
                        mergedData[segmentNumber] = ''
                        mergedData[segmentNumber] += (markerStart + '\n')
                    replacelines=False
                    segmentNumber+=2
                elif markerEnd in line:
                    replacelines=True
                else:
                    if replacelines == True:
                        try:
                            mergedData[segmentNumber] += (line)
                        except KeyError:
                            mergedData[segmentNumber] = ''
                            mergedData[segmentNumber] += (line)
            segmentNumber=1 # Odds
            for line in currentOldFile:
                if markerStart in line:
                    replacelines=False
                elif markerEnd in line:
                    try:
                        mergedData[segmentNumber] += (markerEnd + '\n')
                    except KeyError:
                        mergedData[segmentNumber] = ''
                        mergedData[segmentNumber] += (markerEnd + '\n')
                    segmentNumber+=2
                    replacelines=True
                else:
                    if replacelines == False:
                        try:
                            mergedData[segmentNumber] += (line)
                        except KeyError:
                            mergedData[segmentNumber] = ''
                            mergedData[segmentNumber] += (line)
            currentNewFile.close()
            currentOldFile.close()
            currentMergedFile=open(currentDir + osSlash + 'merged' + osSlash + file, 'w')
            for line in mergedData:
                currentMergedFile.write(mergedData[line])
            currentMergedFile.close()
print(errorLog)
