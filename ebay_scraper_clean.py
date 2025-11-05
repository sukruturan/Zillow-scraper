# Clean ebay scrapper version placeholderimport pandas as pd
import pandas as pd
# READ EXEL DATA
try:
        df = pd.read_excel("ebay.xlsx")
except:
        print("ERROR: THERE IS NO EXCEL FILE")
        quit()
df = df.iloc[:, 1:6]
df.columns = ["Title", "Price", "Shipping Price", "Delivery Start", "Delivery End"]
# CHANGE COLUMNS
df["Price"] = df["Price"].str.replace(r"[^\d.]", "", regex=True).astype(float)
df["Shipping Price"] = df["Shipping Price"].str.replace(r"[^\d.]", "", regex=True).astype(float)

df["Delivery Start"] = pd.to_datetime(df["Delivery Start"] + " 2025", format="%a, %b %d %Y", errors="coerce")
df["Delivery End"]   = pd.to_datetime(df["Delivery End"]   + " 2025", format="%a, %b %d %Y", errors="coerce")
df["Delivery Start"] = df["Delivery Start"].dt.date
df["Delivery End"]   = df["Delivery End"].dt.date
df.index = range(1, len(df)+1)
df.index.name = "INDEX"

print(df.to_string())
print(df.dtypes)
df.to_excel("ebay_clean.xlsx",index=False)




