import json

with open("text_7.txt", "r", encoding="utf-8") as my_file:
    total_revenue = 0
    total_costs = 0
    results = {}
    count = 0
    for line in my_file:
        print(f"Компания: {line.split()[0]} {line.split()[1]} Выручка: {line.split()[2]} Затраты: {line.split()[3]}")
        profit = int(line.split()[2]) - int(line.split()[3])
        if profit > 0:
            total_revenue += int(line.split()[2])
            total_costs += int(line.split()[3])
            count += 1
        line_dict = {line.split()[0]: profit}
        results.update(line_dict)
    average_profit = (total_revenue - total_costs) / count
    full_results = [results, {"average_profit": average_profit}]
    print(full_results)
    with open("text77.json", "w", encoding="utf-8") as new_file:
        json.dump(full_results, new_file, ensure_ascii=False, indent=4)
