import random,uuid,string

# rand_str = lambda n: ''.join([random.choice(string.lowercase) for i in range(n)])
# s = rand_str(10);
# print(s);

# def randomWord(len):
#     methlinks = ''.join(random.choice(string) for i in range(len))

#     print(methlinks.lower)

# randomWord(9);

def randomWord(length):
   rand = ''.join(random.choice(string) for i in range(length))
   return rand.lower()

randomWord(10);  

print(uuid.uuid4())
