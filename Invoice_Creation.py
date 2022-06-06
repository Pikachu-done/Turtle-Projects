product1_name , product1_price = "Monitor" , 20000
product2_name , product2_price = "Books" , 560
product3_name , product3_price = "Calculator" , 200

Company_Name = "The Clever Programmer"
Company_Address = "144 , Kaji - 1"
Company_City = "Delhi"

print("*"*50)
print("\t\t{}".format(Company_Name))
print("\t\t{}".format(Company_Address))
print("\t\t{}".format(Company_City))
print("="*50)
print("\tProduct Name  \tProduct Price")
print("\t{}\t\t{}".format(product1_name , product1_price))
print("\t{}\t\t{}".format(product2_name , product2_price))
print("\t{}\t{}".format(product3_name , product3_price))
print("="*50)
print("\t\t\tTotal")
total = product1_price + product2_price + product3_price
print("\t\t\t{}".format(total))
print("*"*50)
