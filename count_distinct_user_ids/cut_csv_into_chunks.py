import pandas as pd

input_file = "export_segment_DDF11-D1BF9_1695033687.csv"

num_rows = sum(1 for row in open(input_file)) - 1
chunk_size = num_rows // 4

# Read and write each chunk to a separate CSV
for i, chunk in enumerate(pd.read_csv(input_file, chunksize=chunk_size, dtype={24: 'str'})):
    chunk.to_csv(f"chunk_{i+1}.csv", index=False)

    if i == 3:
        break
