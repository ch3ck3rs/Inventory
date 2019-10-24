from FinalParts import *

product_line = '8" RO'
final, num, percent = get_final(product_line, percentage=.2)

summary = pd.DataFrame({'Title':['Product Line', 'Number of Products Considered', 'Percentage used for Most'],
                        'Value':[product_line, num, percent]})

path = r"C:\Users\coffmlv\Documents\1_ESD\Inventory Lead Time\Results\FinalParts_8RO.xlsx"
writer = pd.ExcelWriter(path)

summary.to_excel(writer, sheet_name='SUMMARY')
final[0].to_excel(writer, sheet_name='All BOMs')
final[1].to_excel(writer, sheet_name='Most BOMs')
final[2].to_excel(writer, sheet_name='Every Part')

writer.save()