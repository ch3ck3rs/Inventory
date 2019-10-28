# Bug Log

### Current bug log

### Resolved bug log
* ~~.py is not importing all the values in the source .txt~~
    * ~~I think this is an encoding issues, as it is exported from SAP using the unconverted local file option.  
        I'm going to convert to an .xlsx output and see if that corrects the issue.
        see scratch_inventory.md for current progress~~
    * bug was due to encoding.  exported to .xlsx then had to copy past into new sheet.