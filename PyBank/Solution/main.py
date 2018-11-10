import os
import csv

csvpath = os.path.join('..', 'Data', 'budget_data.csv')

rows = []
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(csvreader):
        if i==0:
            header = row
        else:
            rows.append(row)

    count = 0
    total_revenue = 0
    prev_revenue = 0
    revenue_change = 0
    total_change = 0
    avg_change = 0
    ppnl =0

    greatest_increase = ["", 0]
    greatest_decrease = ["", 9999999999999999999999]

    for i in range(len(rows)):
        pnl = int(rows[i][1])
        #Count Months
        count += 1
        print(count)
        #Find total revenue
        total_revenue = total_revenue + pnl
        #Find average change
        if i > 0:
            ppnl = int(rows[i-1][1])
            revenue_change = (pnl - ppnl)

            total_change = total_change + revenue_change

            if (revenue_change > greatest_increase[1]):
                greatest_increase[1] = revenue_change
                greatest_increase [0] = rows[i][0]

            if (revenue_change < greatest_decrease[1]):
                greatest_decrease[1] = revenue_change
                greatest_decrease[0] = rows[i][0]

avg_change = (total_change/count)

#Print out everything
print(" ")
print(" ")
print(" ")
print("Finacial Analysis")
print("------------")
print("Total Months: " + str(count))
print("Total: $" + str(total_revenue))
print(f'Average Change: ${avg_change:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})')
print(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')

#Export File to text
file_to_output = os.path.join('..', 'Data', 'FinancialAnalysis.txt')
with open(file_to_output, "w") as txt_file:
    txt_file.write("Finacial Analysis\n")
    txt_file.write("------------\n")
    txt_file.write(f'Total Months: {count}\n')
    txt_file.write(f'Total: ${total_revenue}\n')
    txt_file.write(f'Average Change: ${avg_change:.2f}\n')
    txt_file.write(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n')
    txt_file.write(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n')
