import os
import pandas as pd

filename = "/Users/evanbiederstedt/Marcin_bam10.gzip"  # 4.8 GB
hdf_fname = "result2.h5"   # define HDF5
hdf_key = "huge_df"   # define retrieval key
columns_list = ['QNAME', 'FLAG', 'RNAME', 'POS', 'MAPQ', 'CIGAR','RNEXT', 'PNEXT', 'TLEN',
                 'SEQ', 'QUAL', 'RX', 'QX', 'BC', 'QT', 'RG', 'XS', 'AS', 'XM', 'AM', 'XT', 'SA', 'BX']   # list all columns
columns_to_index = ["QNAME", "RNAME"]   # list columns to index now
chunksize = 10**6         # educated guess, fiddle with parameter                                             

store = pd.HDFStore(hdf_fname)

for chunk in pd.read_table(filename, compression='gzip', header=None, names=columns_list, chunksize=chunksize, error_bad_lines=False):
    # don't index data columns in each iteration - we'll do it later                                      
    store.append(hdf_key, chunk, data_columns=columns_to_index, index=False)   # not indexing now

# index data columns in HDFStore                                                                              
store.create_table_index(hdf_key, columns=columns_to_index, optlevel=9, kind='full')
store.close()


