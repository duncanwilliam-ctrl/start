'''
open file to read
read records
if record contains identifier to fix,
then find "-" and correct with nothing
write record to new file
'''


with open("lifelabs.ics", mode="r") as infile:
    for record in infile:
        if "DTSTART" in record:
            record = record.replace("-", "")
            record = record.replace(":", "")
            print(record.strip())  # strip() removes the newline character (\n)
        elif "DTEND" in record:
            print(record.strip())
        else:
            output = record.strip()
            print(output)

with open("lifelabsfixed.ics", mode="a") as outfile:
    outfile.write(record + "\n")

#    with open("lifelabsfixed.txt", mode="a") as outfile:


# read(infile)
# if infile(1) == "DTSTART:" or "DTEND:":
  #   data = (infile.read(1))
    # find and replace "-"

# write the fixed file
# appointment.write(infile)
