First ensure credentials.json file is present. 

Then daily workflow is to plug in calculator, mv *.8xl files to ./8xl_files

Then activate `color-conv`. Run retrieve_daily_csv.py, then upload daily.csv to google sheets

Then simply run process.py for profit.

Future versions might auto-tag dates to the output of retrieve_daily_csv.py, then append to dataframe, uploading it back to the final excel sheet, but it's too janky especially if I take a break in a day recording data. 