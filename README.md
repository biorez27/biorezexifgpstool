# Biorez Exif GPS Tool
Python script for changing location metadata from images using exiftool.

## Requirements
Linux OS with python3 and exiftool installed.

## Usage

```bash
cd /path/to/folder/containing/(subfolders/with/)images
python3 GPS.py
```
The script will ask for the following input:
  - fast or slow mode (explaination in script)
  - (a part of the) image file name(s)
  - confirmation
  - new coordinates | format like this: 47.61539141008304, -58.640506595653015 | copy from google maps works
  - rerun or quit

You can also erase GPS metadata by entering 0, 0 coordinates.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
