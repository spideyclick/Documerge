# Documerge
A Python 3 script for merging text, HTML and many other kinds of documents.

## Configuration and use
python3 Documerge.py

This script currently requires you to put old files in the old folder, and new files (of the same name) in the new folder. Merged files will of course appear in the merged folder.

Use the first couple lines in the file to configure the delimiters for the beginning and end of fields. These are currently set to "<!-- marker start-->" and "<!-- marker end-->" because I intend to use this program for changing the template of an entire website without modifying the content. These markers are HTML comments, so they shouldn't mess with the actual body of the page--but you can change them to whatever you want.

Theoretically, you should be able to toggle between as many markers as your machine can handle. Make sure your document names are exactly the same (or else it will just tell you at the end of the merge which documents had no match).

Have fun with the script, let me know if it saved you some time, and of course let me know if you have any suggestions! Thanks!
