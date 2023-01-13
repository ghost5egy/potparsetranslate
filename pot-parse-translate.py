import time, sys
from googletrans import Translator

def translate(t):
	if t == "":
		return ""
	trans = Translator()
	time.sleep(10)
	tt = trans.translate(t, dest='ar', src='en')
	return tt.text

f = open(sys.argv[1], 'r')
o = open(sys.argv[2], 'a')
msgidflag = False
texttotranslate = ""
texttranslated = ""

for line in f.readlines():
	if msgidflag == True:
	    if line.find('msgstr') != -1 :
		    msgidflag = False
		    texttranslated = line.replace('""', '"' + translate(texttotranslate) + '"')
		    print(texttranslated)
		    o.write('msgstr "' + texttranslated + '"\n')
		    continue
	    else:
		    texttotranslate = texttotranslate + line.split('"')[1]
		    print('"' + texttotranslate + '"')
		    o.write('"' + texttotranslate + '"\n')
		    continue

	if line.find('msgid') > -1 :
		msgidflag = True
		texttotranslate = line.split('"')[1]
		print(line)
		o.write(line + '\n')
