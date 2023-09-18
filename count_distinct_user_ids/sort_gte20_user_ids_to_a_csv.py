import pandas as pd

chunk_files = ["chunk_1.csv", "chunk_2.csv", "chunk_3.csv", "chunk_4.csv"]

all_counts = pd.Series(dtype=int)

for chunk_file in chunk_files:
    # Load the data from the file
    df = pd.read_csv(chunk_file, usecols=["User ID"])
    # Count the occurrences of each User ID in this chunk
    user_counts = df["User ID"].value_counts()
    all_counts = all_counts.add(user_counts, fill_value=0)

# Filter those User IDs that appear more than 20 times
filtered_ids = all_counts[all_counts > 20].index

# Save User IDs to a file
pd.DataFrame(filtered_ids, columns=["User ID"]).to_csv("filtered_user_ids.csv", index=False)
