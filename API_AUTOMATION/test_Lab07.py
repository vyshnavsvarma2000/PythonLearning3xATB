import csv
import pandas as pd
class Test_CRUD(object):
    def test_update1(self):
        #Read the file
        with open("API_AUTOMATION/user_data.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row[0], row[1])

    def test_update2(self):
        # Read the file using pandas
        df = pd.read_csv("API_AUTOMATION/user_data.csv")
        print(df)