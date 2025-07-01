       IDENTIFICATION DIVISION.
       PROGRAM-ID. SALT.
       AUTHOR. MELINDA FISHER, ISBN 0 340 20383 8.
       *> THIS PROGRAM ACCUMULATES SALARY DETAILS
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
            SOURCE-COMPUTER. ICL-2972.
            OBJECT-COMPUTER. ICL-2972.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
            SELECT SALARY-FILE ASSIGN TO "SALARIES.DAT". *> GnuCOBOL insist to change way in which open file from file system

       DATA DIVISION.
       FILE SECTION.
       FD SALARY-FILE.
       01 SALARY-RECORD.
            *>03 RECORD-TYPE PIC X. *> code present in a book but RECORD-TYPE is nowhere used in Division section. I found a lot mistakes in  book, till page 54 I fount 5 or more mistakes in a book. It's printed before personal computer era!
            05 SALARY PIC 9(6). *> Note: Non-standard level jump (03 to 05), reminder from QA of AI which I use. Or may be because I comment previous 03

       WORKING-STORAGE SECTION.
       01 SALARY-TOTAL PIC 9(8).

       PROCEDURE DIVISION.
       AA-START.
           OPEN INPUT SALARY-FILE.
           MOVE ZEROS TO SALARY-TOTAL.
       BB-READ.
           READ SALARY-FILE
                AT END GO TO CC-END.
           ADD SALARY TO SALARY-TOTAL.
           GO TO BB-READ.
       CC-END.
           DISPLAY "TOTAL SALARY: " SALARY-TOTAL. *> Added descriptive text
           CLOSE SALARY-FILE.
           STOP RUN.
