# Importing pandas
import pandas as pd

# Data in dictionary format
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Zainab", "Usman", "Ayesha", "Bilal", "Hira", "Imran", "Nida",
             "Kashif", "Maha", "Tariq", "Fatima", "Danish", "Sana", "Junaid", "Mehwish", "Rizwan", "Laiba"],
    "Age": [25, 28, 32, 23, 29, 27, 35, 26, 30, 24,
            31, 22, 36, 27, 33, 25, 29, 26, 34, 23],
    "Salary": [45000, 55000, 60000, 40000, 48000, 52000, 70000, 46000, 50000, 42000,
               61000, 39000, 75000, 53000, 67000, 47000, 59000, 49000, 72000, 41000],
    "City": ["Karachi", "Lahore", "Islamabad", "Quetta", "Peshawar", "Multan", "Faisalabad", "Hyderabad",
             "Sialkot", "Sukkur", "Rawalpindi", "Gujranwala", "Bahawalpur", "Sahiwal", "Okara", "Abbottabad",
             "Mirpur", "Gilgit", "Skardu", "Muzaffarabad"]
}

# Create DataFrame
df = pd.DataFrame(data)
df.loc[2, 'Salary']=40000
print(df)