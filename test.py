import pandas as pd
import ezodf

def read_ods(filename, sheet_no=0, header=0):
    tab = ezodf.opendoc(filename=filename).sheets[sheet_no]
    return pd.DataFrame({col[header].value:[x.value for x in col[header+1:]] for col in tab.columns()})

df = read_ods("schedule.ods")
print(df)
# for determining what cells are merged, investigate content.xml within .ods file
# use lxml for this
# http://lxml.de/tutorial.html#parsing-from-strings-and-files
