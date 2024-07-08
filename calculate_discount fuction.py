def calculate_discount(price,discount_percent):
    if discount_percent>=20:
        discount_percent=price*
    (discount_percent/100)
    final_price=price-discount_amount
    return final_price
else:
return price

#prompting user for input
original_price=float(input(enter the original price of the item:"))
                           
discount_percentage =float(input(enter the discount percentage:"))
                                                            
 #calculate the final price using calculate_discount function
 final_price=calculate_discount(original_price,discount_percent)

 #output the result
 if final_price==original_price:
 print(f"No discount applied.Final price:$
       {final_price:.2f}"}
       else:
       print(f"discount applied.final price after
            {discount_percent}%discount:${final_price:.2f}"}

