import exifread
import pprint
import time
import sys
# Asking for directory of photo
print("___  ___     _        _____                                ")
print("|  \/  |    | |      /  ___|                               ")
print("| .  . | ___| |_ __ _\ `--.  ___ _ __ __ _ _ __   ___ _ __ ")
print("| |\/| |/ _ \ __/ _` |`--. \/ __| '__/ _` | '_ \ / _ \ '__|")
print("| |  | |  __/ || (_| /\__/ / (__| | | (_| | |_) |  __/ |   ")
print("\_|  |_/\___|\__\__,_\____/ \___|_|  \__,_| .__/ \___|_|   ")
print("                                          | |              ")
print("                                          |_|              ")

print("Created By Tw0Reas0ns")

dir = input("Enter the full directory of your photo >")


print("Scraping metadata")
print(" ")
for i in range(50):
    sys.stdout.write("/--/")
    sys.stdout.flush()
    time.sleep(.1)
print(" ")
print("Metadata found!!!")



f = open(dir, 'rb')

# Return Exif tags
tags = exifread.process_file(f)
print(tags.keys())
pprint.pprint(tags)
f.close()
