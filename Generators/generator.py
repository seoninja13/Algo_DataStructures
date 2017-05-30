capitals={"France":"Paris", "Netherlands":"Amsterdam","Germany":"Berlin"}
# for country in capitals:
#     print("The capital cty of " + country + " is " + capitals[country])

# Generator is a function that returns a generator object  
# Local variable still exist, they are saved between calls 
# eevryrthin that can be done with generator, can be implemented with a class based iterator.But the crucial advantage of generators consists in automatically creating the methods __iter__() and next() 

#Fn=Fn-1 +Fn-2; F0=0;F1=1
# def fibo(n):
#     a,b,counter=0,1,0
#     while True:
#         if(counter>n):
#             return
#         yield a
#         a,b=b,a+b
#         counter +=1
# f=fibo(5)
# for x in f:
#     print(x," ", end="")
# print()

def city_generator():
    yield("London")
    yield("Sofia")
    yield("Hamburg")
    yield("Berlin")

city = city_generator()
print(next(city))
print(next(city))
print(next(city))
city2=city_generator()
print(next(city2))
# print(next(city))