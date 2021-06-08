import numpy as np
import matplotlib
import csv
import pandas as pd
import time  

def replaceIngredient(recipe , ingred):
    newrecipe = recipe.copy()
    p = len(recipe)
    pair = np.zeros(p)
    
    r = recipe[ingred]
    ingredctg = dfct(r)

    if ingredctg == 'Bakery/Dessert/Snack':
        tfile = foodlist_bakery
    elif ingredctg == 'Beverage': 
        tfile = foodlist_beverage 
    elif ingredctg == 'BeverageAlcoholic':
        tfile = foodlist_Alcoholic
    elif ingredctg == 'Cereal/Crop/Bean':
        tfile = foodlist_Cereal
    elif ingredctg == 'Dairy':
        tfile = foodlist_dairy
    elif ingredctg == 'Dish/EndProduct':
        tfile = foodlist_dish
    elif ingredctg == 'EssentialOil/Fat':
        tfile = foodlist_oil
    elif ingredctg == 'ETC':
        tfile = foodlist_etc
    elif ingredctg == 'Flower':
        tfile = foodlist_flower
    elif ingredctg == 'Fruit':
        tfile = foodlist_fruit
    elif ingredctg == 'Fungus':
        tfile = foodlist_fungus
    elif ingredctg == 'Meat/AnimalProduct':
        tfile = foodlist_meat
    elif ingredctg == 'Nut/Seed':
        tfile = foodlist_nut
    elif ingredctg == 'Plant/Vegetable':
        tfile = foodlist_plant
    elif ingredctg == 'Sauce/Powder/Dressing':
        tfile = foodlist_sauce
    elif ingredctg == 'Seafood':
        tfile = foodlist_seafood
    elif ingredctg == 'Spice':
        tfile = foodlist_spice
    elif ingredctg == 'None':
        tfile = "None"

    if tfile == "None" :
        candindex = (recipe[ingred], '', '', '', '')

    else :
        rpairscore = np.zeros(len(tfile))
        for i in range(len(tfile)):
            for j in range(len(recipe)):
                if(tfile[i] != recipe[ingred]):
                    pair[j] = checkpairing(recipe[j], tfile[i])
                elif(tfile[i] == recipe[ingred]):
                    pair[j] = -1
            rpairscore[i] = pair.sum() / p

        rsortpscore = rpairscore.argsort()
        sortpscore = np.flip(rsortpscore)

        a = sortpscore[0]
        b = sortpscore[1]
        c = sortpscore[2]
        d = sortpscore[3]
        e = sortpscore[4]

        candindex = (tfile[a], tfile[b], tfile[c], tfile[d], tfile[e])
    
    return candindex

def shifting(recipe, ing, ring):
    recipe[ing] = ring
    return recipe

def checkpairing(ingred1, ingred2):
    
    pair = (ingred1, ingred2)
    
    try:
        found = rpairlist.index(pair)
        pairing = pairscore[found][2]
        return pairing
    except ValueError:
        return 0

def printrecipe(recipe):
    print('\n')
    for i in range(len(recipe)):
        print(recipe[i])

def dfct(r):
    try:
        found = rfoodlist.index(r)
        ingredctg = foodlist[found][1]
        return ingredctg
    except ValueError:
        return 'None'
        
start = time.time()
foodlist = list() 
pairscore = list()
# test_recipe = list()
candiindex = list()
lenlist = len(foodlist)
foodlist_Alcoholic = list()
foodlist_bakery = list()
foodlist_beverage = list()
foodlist_Cereal = list()
foodlist_dairy = list()
foodlist_dish = list()
foodlist_etc = list()
foodlist_flower = list()
foodlist_fruit = list()
foodlist_fungus = list()
foodlist_meat = list()
foodlist_nut = list()
foodlist_oil = list()
foodlist_plant = list()
foodlist_sauce = list()
foodlist_seafood = list()
foodlist_spice = list()
tfile = list()

a = open('food_list_kkr.csv', 'r')
ar = csv.reader(a)
b = open('pairing_scores.csv', 'r')
br = csv.reader(b)
# c = open('test_recipe.csv', 'r')
# cr = csv.reader(c)
d = open('food_list_Alcoholic.csv', 'r')
dr = csv.reader(d)
e = open('food_list_bakery.csv', 'r')
er = csv.reader(e)
f = open('food_list_beverage.csv', 'r')
fr = csv.reader(f)
g = open('food_list_Cereal.csv', 'r')
gr = csv.reader(g)
h = open('food_list_dairy.csv', 'r')
hr = csv.reader(h)
i = open('food_list_dish.csv', 'r')
ir = csv.reader(i)
j = open('food_list_etc.csv', 'r')
jr = csv.reader(j)
k = open('food_list_flower.csv', 'r')
kr = csv.reader(k)
l = open('food_list_fruit.csv', 'r')
lr = csv.reader(l)
m = open('food_list_fungus.csv', 'r')
mr = csv.reader(m)
n = open('food_list_meat.csv', 'r')
nr = csv.reader(n)
o = open('food_list_nut.csv', 'r')
oor = csv.reader(o)
p = open('food_list_oil.csv', 'r')
pr = csv.reader(p)
q = open('food_list_plant.csv', 'r')
qr = csv.reader(q)
r = open('food_list_sauce.csv', 'r')
rr = csv.reader(r)
s = open('food_list_seafood.csv', 'r')
sr = csv.reader(s)
t = open('food_list_spice.csv', 'r')
tr = csv.reader(t)

for row in ar:
    foodlist.append((row[0], row[1]))
    
for row in br:
    pairscore.append((row[0], row[1], row[2]))
    
#for row in cr:
#   test_recipe.append(row[0])
                       
for row in dr:
    foodlist_Alcoholic.append(row[0])
    
for row in er:
    foodlist_bakery.append(row[0])
    
for row in fr:
    foodlist_beverage.append(row[0])

for row in gr:
    foodlist_Cereal.append(row[0])
    
for row in hr:
    foodlist_dairy.append(row[0])
    
for row in ir:
    foodlist_dish.append(row[0])
    
for row in jr:
    foodlist_etc.append(row[0])
    
for row in kr:
    foodlist_flower.append(row[0])
    
for row in lr:
    foodlist_fruit.append(row[0])
    
for row in mr:
    foodlist_fungus.append(row[0])
    
for row in nr:
    foodlist_meat.append(row[0])
    
for row in oor:
    foodlist_nut.append(row[0])
    
for row in pr:
    foodlist_oil.append(row[0])
    
for row in qr:
    foodlist_plant.append(row[0])
    
for row in rr:
    foodlist_sauce.append(row[0])
    
for row in sr:
    foodlist_seafood.append(row[0])
    
for row in tr:
    foodlist_spice.append(row[0])

#여기까지 데이터들 리스트로 만들어줌

findc = pd.DataFrame(pairscore)
findc.drop(2, axis=1, inplace = True)
rpairlist0 = findc[0].to_list()
rpairlist1 = findc[1].to_list()
rpairlist = list(zip(rpairlist0, rpairlist1))

findct = pd.DataFrame(foodlist)
rfoodlist = findct[0].to_list()

# print(test_recipe)

# candiindex = replaceIngredient(test_recipe, 2)

# replaceIngredient는 대체 재료 상위 5개 출력
# 대체하는 함수는 shifting, 대체하는부분은 맨 아래에 있음

#(레시피, 기존 재료의 인덱스, 바꿀 재료의 인덱스(아까 출력된 후보중에))
# newrecipe = shifting(test_recipe, 2, candiindex[0])
# print(newrecipe)