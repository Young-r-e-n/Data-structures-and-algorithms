import requests
import bs4

# Make a request to the website to get the scholarship data
res = requests.get('https://www.scholarships.com/financial-aid/college-scholarships/scholarship-directory/deadline/deadline-in-the-next-30-days')

# Parse the response using Beautiful Soup
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Find all of the scholarship elements on the page
scholarships = soup.find_all(class_='col-xs-12 col-sm-4')

# Print the data for each scholarship
for scholarship in scholarships:
  # Find the title element and print the text
  title = scholarship.find(class_='title')
  print(title.text)

  # Find the deadline element and print the text
  deadline = scholarship.find(class_='deadline')
  print(deadline.text)

  # Find the amount element and print the text
  amount = scholarship.find(class_='amount')
  print(amount.text)
