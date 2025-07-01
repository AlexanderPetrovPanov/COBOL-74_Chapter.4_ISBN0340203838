#COBOL-74 program from chapther 4 "Coding a Simple Program"
#from book "Computer Programming in COBOL"

###author of the book Melinda Fisher
###ISBN 0 340 20383 8
###printed 1982

author of Python code: Alexander Panov
email: a_panov@mail.ru
Tel(Bulgaria): +359 877 644011
Tel(Malta): +356 99912151
Tel(UK): +44 7741 397240

Created 30 June - 1 Jily 2025. 

To  start Cobol program you need Linux. In terminal you can start it with:
```
./SALT
```
when you are in directory of the project. Also you can compile executable from Cobol source code file SALT.cbl with this command from console:
```
cobc -x SALT.cbl
```
Because its COBOL-74 you will need, like i've do the code indentation from the first position. The original reason was dealing with punch cards. Cobol kept the first 6 positions for a line sequence number. Column 7 was a continuation / comment / debug / form-feed. "Area A", or Columns 8-11, indicated certain special language artifacts like 01 levels, section or paragraph names, et al. "Area B", or Columns 12 - 72, was for open code. Columns 73 - 80 were for OS sequence numbers. Search in internet, read books, manualr, RFC or ask AI (hire you should know what to ask).
[https://public.support.unisys.com/aseries/docs/ClearPath-MCP-19.0/86000296-211.pdf](https://public.support.unisys.com/aseries/docs/ClearPath-MCP-19.0/86000296-211.pdf)
[https://public.support.unisys.com/aseries/docs/ClearPath-MCP-20.0/86000130-307.pdf](https://public.support.unisys.com/aseries/docs/ClearPath-MCP-20.0/86000130-307.pdf)
These two PDFs are COBOL ANSI-74 Programming Reference Manual Volume 1 and Volume 2

I create record file using template SALARY-FILE file described in a book on a page 15 long before Chapter 4. I script in Python 3 a short program generate.py whish generate file with 12 milion records in it. Those records from SALARIES.DAT later are used in Cobol program SALT. To ganerate new SALARIES.DAT file from console you need to execute:
```
python3 generate.py
```

You are free to use this project under GPL3 license. License itself you can find on a link below:
[https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html)
I am not responsuble for anything with this code, use on your own risk.

![Screenshot of a COBOL-74 and Python 3 programs](https://myoctocat.com/assets/images/base-octocat.svg)
