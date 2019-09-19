k = int(input())
if k < 10:
    k = "%04d" % k
elif k < 100 and k >= 10:
    k = "%04d" % k
elif k < 1000 and k >= 100:
    k = "%04d" % k
str = str(k)
rev =str[::-1]
if str == rev:
  print("Палиндром")
elif str != rev:
  print("Не палиндром")








