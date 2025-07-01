# COBOL-74 program from chapther 4 "Coding a Simple Program"
# from book "Computer Programming in COBOL"

### author of the book Melinda Fisher
### ISBN 0 340 20383 8
### printed 1982

author of Python code: Alexander Panov<br/>
email: a_panov@mail.ru<br/>
Tel(Bulgaria): +359 877 644011<br/>
Tel(Malta): +356 99912151<br/>
Tel(UK): +44 7741 397240<br/><br/>

Created 30 June - 1 Jily 2025.<br/><br/>

To  start Cobol program you need Linux. In terminal you can start it with:
```
./SALT
```
When you are in directory of the project. Also you can compile executable from Cobol source code file SALT.cbl with this command from console:
```
cobc -x SALT.cbl
```
Because its COBOL-74 you will need, like i've do the code indentation from the first position. The original reason was dealing with punch cards. Cobol kept the first 6 positions for a line sequence number. Column 7 was a continuation / comment / debug / form-feed. "Area A", or Columns 8-11, indicated certain special language artifacts like 01 levels, section or paragraph names, et al. "Area B", or Columns 12 - 72, was for open code. Columns 73 - 80 were for OS sequence numbers. Search in internet, read books, manuals, RFC or ask AI (hire you should know what to ask).<br/>
[https://public.support.unisys.com/aseries/docs/ClearPath-MCP-19.0/86000296-211.pdf](https://public.support.unisys.com/aseries/docs/ClearPath-MCP-19.0/86000296-211.pdf)<br/>
[https://public.support.unisys.com/aseries/docs/ClearPath-MCP-20.0/86000130-307.pdf](https://public.support.unisys.com/aseries/docs/ClearPath-MCP-20.0/86000130-307.pdf)<br/>
These two PDFs are COBOL ANSI-74 Programming Reference Manual Volume 1 and Volume 2<br/><br/>

I create record file using template SALARY-FILE file described in a book on a page 15 long before Chapter 4. I script in Python 3 a short program generate.py which generate file with 12 million records in it. Those records from SALARIES.DAT later are used in Cobol program SALT. To ganerate new SALARIES.DAT file from console you need to execute:
```
python3 generate.py
```

You are free to use this project under GPL3 license. License itself you can find on a link below:<br/>
[https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html)<br/>
I am not responsuble for anything with this code, use on your own risk.<br/><br/>

![Screenshot of a COBOL-74 and Python 3 programs](https://github.com/AlexanderPetrovPanov/COBOL-74_Chapter.4_ISBN0340203838/blob/main/Screenshot%20at%202025-07-01%2022-20-24.png)
