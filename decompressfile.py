import gzip
import pickle 
with gzip.open('your_large_file.pkl.gz', 'rb') as f:
    data = pickle.load(f)
