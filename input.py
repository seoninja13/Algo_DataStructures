# wordlist = ['cat','dog','rabbit']
# letterlist = [ ]
# for aword in wordlist:
#     for aletter in aword:
#         if aletter in letterlist:
#             continue
#         else:    
#             letterlist.append(aletter)
        
# print(letterlist);

# sqlist=[];
# for x in range(1,11):
#     sqlist.append(x*x);

#print(sqlist);    

#  -- 1 -- using list comprehension
#sqlist=[x*x for x in range(1,11)];
#sqlist=[x*x for x in range(1,11)if x%2 !=0]; """Only odd numbers"""
#print(sqlist);

# remove duplicates with list comprehension
# wordlist = ['cat','dog','rabbit']
# letterlist=[aletter in aword for aword in wordlist if aletter in letterlist]

# letterlist = [ ]
# for aword in wordlist:
#     for aletter in aword:
#         if aletter in letterlist:
#             continue
#         else:    
#             letterlist.append(aletter)
        
#print(letterlist);
#print("".join(['tiger','cat','rabbit']))
#print([ch for ch in "".join(['cat','dog','bigcat'])])

#print([word[i] for word in ['cat','dog','bigcat']])
print([word[i] for word in ['cat','dog','bigcat'] for i in range(len(word))])
print("--------------------")
print(set([word[i] for word in ['cat','dog','bigcat'] for i in range(len(word))]))
# convert the "set" to "list"
print(list(set([word[i] for word in ['cat','dog','bigcat'] for i in range(len(word))])))

