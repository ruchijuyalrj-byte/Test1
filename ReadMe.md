Hello world, Ruchi was here!
python

pandas

series.loc[ind] Returns specific rows
series.iloc[ind]

Reading data from csv
pd.read_csv(file path)


pd.read_exceel(file path, sheet_name = "file1")

Titanic data code:
import pandas as pd
from sklearn.datasets import fetch_openml

titanic = fetch_openml(name="titanic", version=1, as_frame=True)
data = pd.DataFrame(titanic.data)
data.head()


How to save the file:
git add FILENAME
git commit -m "MESSAGE HERE"
git push


What worked~~

cd "C:\Users\Admin\Desktop\Test1\Day 3"
git add day3.ipynb
git commit -m "Add day3 notebook"
git push origin main


How:
in Git bash
cd "Day 3"

and then the above ones


#JSON file
{
    "books": [
        {"title": "Dracula", "availability": "available"},
        {"title": "Nationalism", "availability": "not available"},
        {"title": "The Last Girl", "availability": "available"},
        {"title": "Educated", "availability": "not available"}
    ]
}
