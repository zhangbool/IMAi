
codes = ['600001','600002','600003','600004','600005','600006','600007','600008']

thread_len = int(len(codes)/4)

t1 = codes[0:thread_len]
t2 = codes[thread_len:thread_len*2]
t3 = codes[thread_len*2:thread_len*3]
t4 = codes[thread_len*3:]

print(t1)


