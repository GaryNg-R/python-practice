class MyClass:
  sum = 0
  size = 0
  arraylist = {}
  
  def add_number(self, n):
    self.sum += n
    self.size += 1
    if n in self.arraylist:
        self.arraylist[n] = self.arraylist[n] + 1
    else :
        self.arraylist[n] = 1

  def median(self):
    return self.sum/self.size





p1 = MyClass()

p1.add_number(1)
p1.add_number(1)

p1.add_number(4)


# print(p1.sum)
# print(p1.size)
print(p1.arraylist)
print(p1.median())


for i in p1.arraylist:
  print("key = ",i ,  " value = ", p1.arraylist[i])




##sort by key
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
for key in sorted(incomes):
   print(key, '->', incomes[key])

#Sorted by Values

incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
def by_value(item):
     return item[1]

for k, v in sorted(incomes.items(), key=by_value):
    print(k, '->', v)
