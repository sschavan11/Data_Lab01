with open(r"C:\Northeastern Univesity\Academic\MLOps\Labs\Lab01-Data\Data\reddit_text.txt", "r", encoding="utf-8", errors="ignore") as infile, \
     open(r"C:\Northeastern Univesity\Academic\MLOps\Labs\Lab01-Data\Data\reddit_text_sample.txt", "w", encoding="utf-8") as outfile:
    
    for i, line in enumerate(infile):
        if i >= 10000:
            break
        outfile.write(line)

print("Sample file created successfully")