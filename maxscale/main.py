import mysql.connector

def query_database(config, query):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        cursor.execute(query)
        result = cursor.fetchall()

        cursor.close()
        conn.close()

        return result

    except mysql.connector.Error as e:
        print("Error connecting to MaxScale:", e)
        return None

# Define your MaxScale connection details for zipcodes_one
config_one = {
    'user': 'maxuser',
    'password': 'maxpwd',
    'host': '127.0.0.1',
    'port': 4000,
    'database': 'zipcodes_one'
}

# Define your MaxScale connection details for zipcodes_two
config_two = {
    'user': 'maxuser',
    'password': 'maxpwd',
    'host': '127.0.0.1',
    'port': 4000,
    'database': 'zipcodes_two'
}

# Query for the largest zipcode in zipcodes_one
largest_zipcode_one = query_database(config_one, "SELECT MAX(zipcode) FROM zipcodes_one;")
if largest_zipcode_one:
    print("Largest Zipcode in zipcodes_one:", largest_zipcode_one[0][0])

# Query for zipcodes where state=KY (Kentucky) in zipcodes_one
ky_zipcodes_one = query_database(config_one, "SELECT zipcode FROM zipcodes_one WHERE state='KY';")
if ky_zipcodes_one:
    print("Zipcodes in Kentucky (zipcodes_one):")
    for zipcode in ky_zipcodes_one:
        print(zipcode[0])

# Query for zipcodes where state=KY (Kentucky) in zipcodes_two
ky_zipcodes_two = query_database(config_two, "SELECT zipcode FROM zipcodes_two WHERE state='KY';")
if ky_zipcodes_two:
    print("Zipcodes in Kentucky (zipcodes_two):")
    for zipcode in ky_zipcodes_two:
        print(zipcode[0])

# Query for zipcodes between 40000 and 41000 in zipcodes_one
zipcodes_range_one = query_database(config_one, "SELECT zipcode FROM zipcodes_one WHERE zipcode BETWEEN 40000 AND 41000;")
if zipcodes_range_one:
    print("Zipcodes between 40000 and 41000 (zipcodes_one):")
    for zipcode in zipcodes_range_one:
        print(zipcode[0])

# Query for zipcodes between 40000 and 41000 in zipcodes_two
zipcodes_range_two = query_database(config_two, "SELECT zipcode FROM zipcodes_two WHERE zipcode BETWEEN 40000 AND 41000;")
if zipcodes_range_two:
    print("Zipcodes between 40000 and 41000 (zipcodes_two):")
    for zipcode in zipcodes_range_two:
        print(zipcode[0])

# Query for TotalWages where state=PA (Pennsylvania) in zipcodes_one
total_wages_pa_one = query_database(config_one, "SELECT TotalWages FROM your_table WHERE state='PA';")
if total_wages_pa_one:
    print("Total Wages in Pennsylvania (zipcodes_one):")
    for wages in total_wages_pa_one:
        print(wages[0])

# Query for TotalWages where state=PA (Pennsylvania) in zipcodes_two
total_wages_pa_two = query_database(config_two, "SELECT TotalWages FROM your_table WHERE state='PA';")
if total_wages_pa_two:
    print("Total Wages in Pennsylvania (zipcodes_two):")
    for wages in total_wages_pa_two:
        print(wages[0])
