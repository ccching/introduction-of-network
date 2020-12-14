citys =input("請輸入5個城市,並用,做區隔")
city=citys.title().split(",")
print(city)
city.append("Londen")
print(city)
city.insert(3,"Xian")

print(city)
name=input("請輸入欲刪除的城市名稱：").title()
if name in city:
    city.remove(name)
    print(city)
else:
    print("{},不在串列裡".format(name))
