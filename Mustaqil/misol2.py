def find_top_seller(products: dict, sales: dict) -> str:
        products_sum = []
        for item in products:
                total_sales = products[item] * sales.get(item, 0)
                products_sum.append((item, total_sales))
    
        return max(products_sum, key=lambda x: x[1])[0]

print(find_top_seller(
        {"Olma": 5000, "Banan": 8000, "Uzum": 7000}, 
        {"Olma": 10, "Banan": 5, "Uzum": 8}
                )
      )