import pandas as pd

df = pd.DataFrame({
    'name': ['Anita', 'Bhavesh', 'Chetan', 'Deepa', 'Esha'],
    'maths': [88, 76, 90, 69, 84],
    'sci':   [92, 85, 78, 74, 88],
    'eng':   [81, 79, 85, 77, 80]
})

# Calculate total, percentage, grade, result
df['total'] = df[['maths', 'sci', 'eng']].sum(axis=1)
df['percentage'] = df['total'] / 3
df['grade'] = df['percentage'].apply(lambda x: 'A' if x >= 75 else 'B')
df['result'] = df['percentage'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')

# Print DataFrame
print("Student Data:")
print(df)

# Export to CSV
df.to_excel('new_students.xlsx')

# Export to XML
df.to_csv('new_students.csv')

# Reading back for verification (optional)
df_csv = pd.read_excel('new_students.xlsx')
df_xml = pd.read_csv('new_students.csv')

print("\nCSV Read Output:")
print(df_csv)

print("\nXML Read Output:")
print(df_xml)
