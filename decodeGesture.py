#!/usr/bin/python

__author__ = 'iNV4d3R S4M'

##  Description
#       This script is very useful to brute force android's pattern lock.
#       Android's pattern lock contains a SHA1 hash of the pattern in a
#       gesture.key file in /data/system folder in the internal memory
#       of the android.
#
#       The SHA1 of the android uses some kind of a salt, and the dictionary
#       that is compatible with Android's pattern lock hash can be found at
#       http://www.android-forensics.com/tools/AndroidGestureSHA1.rar which
#       is around 25 MB.
#
#       Author: iNV4d3R S4M
#       Repo:   @c0d3r4ck
##

from optparse import OptionParser


def read_gesture(gesture_file_loc=""):
    #Reading gesture.key file and converting bytes to string
    try:
        gesture_file = open(gesture_file_loc, "rb")
        sha1bytes = []
        for i in range(0, 20):
            sha1hash = gesture_file.read(1)
            sha1bytes.append(sha1hash.encode('hex'))
            i += 1
        sha1hash = ""
        for i in range(0, 20):
            sha1hash += sha1bytes[i]
        return sha1hash
    except IOError:
        print "[-] Gesture file cannot be opened. File not present or you don't have permission to access the file."
        exit(1)


def match_pattern(dictionary="", sha1hash=""):
    #matching the pattern with the dictionary
    sha1hash = str.upper(sha1hash)
    dictionary_file = open(dictionary, "r")
    lines = dictionary_file.readlines()
    for line in lines:
        if line.__contains__(sha1hash):
            index = line.index(";", 0, 10)
            pattern = line[0:index]
            print ""
            print pattern.center(80)


def parse_opt():
    #Create a option parser
    parser = OptionParser("%prog [options].\n\rThis program is used to bruteforce android's pattern passowrd.\n\rCreated By\n\r"
                        "     =====       //||        //||  //||\n\r"
                        "    //          // ||       // || // ||\n\r"
                        "   //          //  ||      //  ||//  ||\n\r"
                        "   =====      //===||     //         ||\n\r"
                        "       //    //    ||    //          ||\n\r"
                        "      //    //     ||   //           ||\n\r"
                        " =====     //      ||  //            ||")
    #Add options
    parser.add_option("-g", "--gesture", type="string", dest="gesture_file", help="Path to your gesture.key file in your local system")
    parser.add_option("-d", "--dictionary", type="string", dest="dictionary_file", help="Path to your dictionary file in your local system")
    #Parse options
    options, arguments = parser.parse_args()
    #Verify all options are used
    if options.gesture_file and options.dictionary_file:
        #Brute force the hash
        sha1hash = read_gesture(options.gesture_file)
        match_pattern(options.dictionary_file, sha1hash)
    else:
        #If all options are not used then show the help on the screen.
        print "Please see usage for proper options. You have not entered proper arguments."
        parser.print_help()
        exit(1)



def main():
    parse_opt()

if __name__ == "__main__":
    main()