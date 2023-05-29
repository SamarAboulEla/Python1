monthConversions = {
    "JAN": "January",
    "FEB": "February",
    "MAR": "March",
    "APR": "April",
    "MAY": "May",
    "JUN": "June",
    "JUL": "July",
    "AUG": "August",
    "SEP": "September",
    "OCT": "October",
    "NOV": "November",
    "DEC": "December"
}

print(monthConversions["JUL"])
print(monthConversions.get("OCT"))
print(monthConversions.get("DEC", "Not a valid key"))
print(monthConversions.get("SMR", "Not a valid key"))