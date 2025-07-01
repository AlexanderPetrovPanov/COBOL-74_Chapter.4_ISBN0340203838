########################################################################################
#                                                                                      #
# Pyhton program to support COBOL-74 program from chapther 4 "Coding a Simple Program" #
# from book "Computer Programming in COBOL"                                            #
# author of the book Melinda Fisher                                                    #
# ISBN 0 340 20383 8                                                                   # 
# printed 1982                                                                         #
#                                                                                      #
# author of this Python code: Alexander Panov                                          #  
# email: a_panov@mail.ru                                                               #
# Tel(Bulgaria): +359 877 644011                                                       #
# Tel(Malta): +356 99912151                                                            # 
# Tel(UK): +44 7741 397240                                                             #
#                                                                                      # 
# File created 1 Jily 2025.                                                            #
#                                                                                      # 
########################################################################################

import random
import gzip

# Configuration
TOTAL_ROWS = 12_000_000
# TOTAL_ROWS = 120 # Test code with less data to be genarated
SAMPLE_ROWS = 20
OUTPUT_FILE = "SALARIES.DAT"
GZIPPED_FILE = "SALARIES.DAT.gz"

# Character sets
DIGITS = "0123456789"
LETTERS = "ABCDF"  # Note: 'E' excluded as per specification
# Dam, fack! I am tired like a donkey, after submitting source code for QA in AI, pop up that I missed the 'E' from A to F sequence! 

with open(OUTPUT_FILE, "w") as f, gzip.open(GZIPPED_FILE, "wt") as gz:
    for i in range(TOTAL_ROWS):
        # Generate first column character
        col1 = random.choice(DIGITS + LETTERS)
        
        # Generate second column number (1-126) with zero padding
        num = random.randint(1, 126)
        col2 = f"{num:06d}"  # Format as 6-digit zero-padded string
        
        # Write row
        row = f"{col1} {col2}\n"
        f.write(row)
        gz.write(row)
        
        # Display first 20 rows
        if i < SAMPLE_ROWS:
            print(row.strip())
        if i == SAMPLE_ROWS + 1:
            print("Now wait all 12 millions rows to be genarated and written in files.")
            print("12 million rows might take a while and the file size will be about 12e6 * 8 bytes (each row: 1 char + 1 space + 6 digits + newline -> 9 characters) -> 108 MB.")
            print("File Sizes: Uncompressed: ~108 MB (12M rows × 9 bytes/row)")
            print("            Gzipped: ~54 MB (50% compression)")
print(f"\nFull file generated: {OUTPUT_FILE} ({TOTAL_ROWS} rows)")
print(f"Gzipped version available: {GZIPPED_FILE}")
