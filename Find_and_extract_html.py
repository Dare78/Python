import os
import re
# using os walk check all dir and files and find file ends with .html
for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.html'):
            # after find the html file join to get the complete path of the html file
            thefile = os.path.join(dirname,filename)
#            print(thefile)
            #  open each html file and read each line
            fout = open(thefile, 'r')
            # since it returns a list join to form a string to pass to regex
            str = " ".join(fout.readlines())
            #build the pattern to match the phone number
            pat = r'\d\.-\d\.-\d'
            #use findall regex to find the all matching email id from the string
            matched = re.findall(pat,str)

            print(matched)
#           match the email ids and replace with your pattern. 
            pat_email = r'([\w\.-]+)@([\w\.-]+)'
            print re.sub(pat_email, r'\1@yo-yo-pur.com', str)
            fout.close()
