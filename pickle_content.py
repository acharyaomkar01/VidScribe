import pprint, pickle

pkl_file = open('/home/cuda/Group46/work/abc.pkl', 'rb')
data = pickle.load(pkl_file)
pprint.pprint(data)
