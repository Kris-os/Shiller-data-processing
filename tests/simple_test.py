from shiller_data_processing import data_extraction

shiller_data_location = r'C:\Users\krist\Google Drive\Opul\Data\2024 09\[raw data 2024 09]ie_data.xls'
test = data_extraction.read_shiller_data(shiller_data_location)
print(test)