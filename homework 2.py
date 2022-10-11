months = {"January": "1", "February": "2", "March": "3", "April": "4", "May": "5", "June": "6", "July": "7",
          "August": "8", "September": "9", "October": "10", "November": "11", "December": "12"}

input_file = open("C:\\Users\\awusmani\\Desktop\\inputDates.txt", 'r')
output_file = open("C:\\Users\\awusmani\\Desktop\\parsedDates.txt", 'w')

for each in input_file:
    if each != "-1":
        arr = each.split()
        if len(arr) >= 3:
            months = arr[0]
            days = arr[1]
            years = arr[2]

            if months.lower() in months:
                comma = days[-1]
                if comma == ',':
                    days = days[:len(day) - 1]
                    month_num = months[months.lower()]
                    solution = month_num + "/" + days + "/" + years

                    output_file.write(solution)
                    output_file.write("\n")
print(output_file)
output_file.close()
input_file.close()
