import pandas as pd

# Read the original CSV file
data = pd.read_csv('/Users/luiza/Desktop/Source/combined_data.csv')

# Create a list to hold the sentences
sentences = []

# Loop through each row and add sentences to the list
for index, row in data.iterrows():
    sentences.append(row['Sentence1'])
    sentences.append(row['Sentence2'])

# Create a DataFrame with sentences
df_sentences = pd.DataFrame({
    'Sentence': sentences
})

# Print the first row of the DataFrame
print(df_sentences["Sentence"][0].split()[6])

# Save the DataFrame to a CSV file without headers or indices
df_sentences.to_csv('/Users/luiza/Desktop/Dataflow/data1.csv', index=False, header=False)

print("Sentences have been saved to /Users/luiza/Desktop/Dataflow/data1.csv")
