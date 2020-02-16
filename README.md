# SheetsPy01
## Installation:
```
pip install SheetsPy01
#Or
git clone https://github.com/GrandMoff100/SheetsPy01/
```

## Usage:
```
import SheetsPy01 as sheets

sheet = sheets.Spreadsheet(<int:length>,<int:width>)

sheet.change_cell(<int:x>,<int:y>,<new_content>)

sheet.get_cell(<int:x>,<int:y>)
#Returns:
('X<int:x>','Y<int:y>',<content>)

sheet.pretty_format(formating=<int>) # Number of spaces to format sheet with.
sheet.pretty_print()

sheet.output
# A list of all lines of the spreadsheet.
# You can use this however you like.
```

## Changelog:
1.0.0 - Initial Upload
1.0.1 - Distribution changes
1.0.2 - First stable release.
1.0.3 - Added various outputs processes besides just printing.
