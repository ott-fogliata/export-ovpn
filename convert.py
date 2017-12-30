import os
import re
import sys


def get_contents(tagname, filecontents):
    output = re.compile('<' + tagname + '>\n(.*?)</' + tagname + '>', re.DOTALL | re.IGNORECASE).findall(filecontents)
    if output:
        print(output[0])
        return output[0]
    else:
        return ''


def create_file(filename, strdata):
    # --------------------------------
    # create_file(strNamaFile, strdata)
    # create a text file
    #
    try:

        f = open(filename, "w")
        f.writelines(str(strdata))
        f.close()

    except IOError:

        filename = filename.split(os.sep)[-1]
        f = open(filename, "w")
        f.writelines(str(strdata))
        f.close()

    print "file created: " + filename + "\n"


def read_file(filename):
    f = open(filename, "r")

    print "file being read: " + filename + "\n"

    return f.read()


def convert(filename):
    filecontents = read_file(filename)

    strdata = ""

    tagFile = {'ca': 'ca.crt', 'cert': 'client.crt', 'key': 'client.key', 'tls-auth': 'tls-auth.key'}

    for tag, file in tagFile.iteritems():
        strdata = strdata + get_contents(tag, filecontents)

        filename = filename.replace(".ovpn", "")

        print tag, filename + "-" + file

        create_file(filename + "-" + file, strdata)
        strdata = ''  # < force empty


def main(filename):

    convert(filename)

main(sys.argv[1])
