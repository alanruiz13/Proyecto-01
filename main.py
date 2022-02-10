import operator 

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches 

userAccess= False 
trys = 0
#Welcome 
welcome = "Welcome to the sistem\nPlease enter user and password: "
print(welcome)

#attemps that you try
while not userAccess :
  user= input("User: ")
  password=input("Password: ")
  trys +=1
  #<Check that par coincides 
  if user == "admin" and password == "admin" :
   userAccess = True 
   print ("Hello, welcome back! :)")
  else :
    print ("Error, you have " , 3 - trys, "trys left")
    if user == "admin":
     print ("Wrong password")
    else : 
     print(f"The user : '{user}' is not register")
  if trys == 3:
    print ("Please contact us for further assitance :() \n Tel : (123) 456 7890  or by e-mail : contact@help.com")
    exit()

#print ("Si se pudo")

#############  PART 1 

sales = [[producto [0], producto[1]] for producto in lifestore_sales ]

best_sale = {}
for par in sales:
  ticket = par[0]
  num_part = par[1]
  if num_part not in best_sale.keys():
    best_sale[num_part] = []
  best_sale[num_part].append(ticket)
##print(type(best_sale))

times_sold = {} #We create this dictionary so we can know how many times a piece item was sold
for k,v in best_sale.items():
    times_sold[k] = (len(v))
#print(times_sold) #THIS PRINT IS USED TO SEE THE LIST THER ORDER IT 
"""
#THIS WAS PRINTED TO SEE THE WHOLE LIST 
for key in times_sold.keys():
  print(f"The piece number: {key}")
  print(f"was sold {times_sold[key]} times ")
"""

top_sale = input("Plase tell me, how long would you like the Top to be? ") #This input is addded so we can know how long the list is going to be, we can ask for the top 3 or top 5 most or less sold

top_sale = int(top_sale)
sort_times_sold = sorted(times_sold.items(), key=operator.itemgetter(1), reverse = True)[:top_sale]
print("The highest sales per item is listed as follow:")

for sale in enumerate(sort_times_sold):
  print(f"The item number: {sale[1][0]} ")
  print(f"Has been sold {times_sold[sale[1][0]]} times ")
  #print(sale[1][0], 'category has', cat_sum[sale[1][0]], 'average sales')

min_top_sale = sorted(times_sold.items(), key=operator.itemgetter(1))[:top_sale]
print("The lowest sale per item are listed as follow:")
for sale in enumerate(min_top_sale):
  print(f"The item number: {sale[1][0]} ")
  print(f"Has been sold {times_sold[sale[1][0]]} times")
  #print(sale[1][0], 'category has', cat_sum[sale[1][0]], 'average sales')
 
#####################################################

#top search

search = [[producto [0], producto[1] ] for producto in lifestore_searches]
best_search = {}
for par in search:
  id_search = par[0]
  id_product = par[1]
  if id_product not in best_search.keys():
    best_search[id_product] = []
  best_search[id_product].append(id_search)
#print(best_search)

times_search = [] #new list to get new values 
for key, value in best_search.items(): 
    #print value
    times_search.append([key, len([item for item in value if item])]) #piece and time sold are added 
#print(times_search) #suggested print to confirm 
times_search.sort(key=lambda x: x[1])#sort from min to max  
print(f"The lowest searches where (piece number, amount): {times_search[0:5]} ") 

times_search.sort(key=lambda x: x[1],reverse=True) #invertimos el orden y ahora sera de mayor a menor
print(f"The highest searches where (piece number, amount): {times_search[0:5]} ")

################################

#The top of sales by category dictionary it's created

category = [[producto[0], producto[3]] for producto in lifestore_products]
categorized_product = {}
for par in category:
  id = par[0]
  cat = par[1]
  if cat not in categorized_product.keys():
    categorized_product[cat] = []
  categorized_product[cat].append(id)
#print(categorized_product) #suggested print to check 
'''
sold_mod = {}
for key, value in categorized_product.items():
	temp = []	
	for i in value:
		temp.append([i, times_sold[int(i)]])
	sold_mod.update({ key: temp})
'''

###### CATEGORY DATA
from lifestore_file import lifestore_products, lifestore_sales

# Id review dictionary
prods_reviews = {}
for sale in lifestore_sales:
    prod_id = sale[1]
    review = sale[2]
    if prod_id not in prods_reviews.keys():
        prods_reviews[prod_id] = []
    prods_reviews[prod_id].append(review)

# id per cat product
cat_prods = {}
for prod in lifestore_products:
    prod_id = prod[0]
    cat = prod[3]
    if cat not in cat_prods.keys():
        cat_prods[cat] = []
    cat_prods[cat].append(prod_id)

# cateory sales 
cat_ventas = {}
for cat in cat_prods.keys():
    # products per category list 
    prods_list = cat_prods[cat]
    reviews_cat = []
    ganancias = 0
    ventas = 0

    # for every prodcut in the catehory
    for prod_id in prods_list:
        # acces reviews, times sold 
        if prod_id not in prods_reviews.keys():
            continue
        reviews = prods_reviews[prod_id]
        precio = lifestore_products[prod_id-1][2]
        total_sales = len(reviews)
        ganancias += precio * total_sales
        ventas += total_sales
        reviews_cat += reviews

    #  review average per cat
    rev_prom_cat = sum(reviews_cat) / len(reviews_cat)
    # Guardo todo en mi diccionario
    cat_ventas[cat] = {
        'average review': rev_prom_cat,
        'total profit ': ganancias,
        'total sales ': ventas
    }

f'string'

for key in cat_ventas.keys():
    print(f"The category: {key} ")
    for llave, valor in cat_ventas[key].items():
        print(f'\t {llave}: {valor}')

#Part 2, Best reviews and worts reviews
review= [[sale[1], sale[2]]for sale in lifestore_sales if sale [4]==0]

best_review = {}
for par in review:
  id_item=par[1]
  id_star=par[0]
  if id_star not in best_review.keys():
    best_review[id_star]=[]
  best_review[id_star].append(id_item)
#Here we calculate the average calification or star of every item 
avg_star = {}
for k,v in best_review.items():
    avg_star[k] = sum(v)/ float(len(v))
#print(avg_star)
'''
for key in avg_star.keys():
  print(f"The Article: {key}")
  print(f"Has {avg_star[key]} average stars/review")
'''

top_stars = input ("How long would you like the top to be?: ")
print("The highest star per item is listed as follow:")

top_stars = int(top_stars)
sort_avg_star = sorted(avg_star.items(), key=operator.itemgetter(1), reverse = True)[:top_stars]
for star in enumerate(sort_avg_star):
  print(f"The item number: {star[1][0]} ")
  print(f"Has been review with {avg_star[star[1][0]]} stars ")

top_stars = int(top_stars)
sort_avg_star_min = sorted(avg_star.items(), key=operator.itemgetter(1))[:top_stars]
for star in enumerate(sort_avg_star_min):
  print(f"The item number: {star[1][0]} ")
  print(f"Has been review with {avg_star[star[1][0]]} stars ")


###########################
#Part 3, listed of how much income per month was 

id_date = [[sale[0], sale[3]]for sale in lifestore_sales if sale [4]==0]
#to categorize we use a dicctionary 
cat_months = {}
for par in id_date:
  id = par[0]
  _, months, _ = par[1].split('/')
  if months not in cat_months.keys():
    cat_months[months] = []
  cat_months[months].append(id)

"""  
for key in cat_months.keys():
  print(key)
  print(cat_months[key])
"""

for key in cat_months.keys():
  months_list = cat_months[key]
  months_sum = 0
  for id_sales in months_list:
    index = id_sales - 1
    info_sale = lifestore_sales[index]
    id_product = info_sale[1]
    price = lifestore_products[id_product-1][2]
    months_sum += price
    
  print(f'In the month {key},the total income was {months_sum}, Total Sales in this month: {len(months_list)}')
