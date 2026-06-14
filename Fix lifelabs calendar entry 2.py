'''
open file to Read
read records
if record contains identifier to fix,
then find "-" and correct with nothing 
write record to new file
'''


def fix(record):
    if "DTSTART" in record or "DTEND" in record:
        record = record.replace(
            "-", "").replace(":", "").replace("DTSTART", "DTSTART:").replace("DTEND", "DTEND:")

    fixed = record
    return fixed


fixed = ""
with open("download (3).ics", mode="r") as infile, open("lifelabsfixed3.ics", mode="w") as outfile:
    for record in infile:
        fixed = fix(record)

        outfile.write(fixed)
