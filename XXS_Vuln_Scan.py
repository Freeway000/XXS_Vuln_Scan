import requests
from bs4 import BeautifulSoup

def scan_for_xss(url):
  """
  Performs a basic XSS vulnerability scan using a GET request.

  Args:
      url (str): The URL of the web application to scan.

  Returns:
      bool: True if potential XSS vulnerability is found, False otherwise.
  """
  try:
    response = requests.get(url, params={"test": "<script>alert('XSS')</script>"})
    soup = BeautifulSoup(response.content, 'html.parser')
    if soup.find(string=lambda text: text and "<script>alert('XSS')</script>" in text):
      return True
    else:
      return False
  except Exception as e:
    print(f"Error scanning URL: {e}")
    return False

def main():
  """
  Main function for the web application vulnerability scanner.
  """
  print("Web Application Vulnerability Scanner")
  print("1. Scan for Cross-Site Scripting (XSS)")
  choice = input("Enter your choice (1): ")

  if choice == "1":
    url = input("Enter the URL of the web application: ")
    xss_vulnerable = scan_for_xss(url)
    if xss_vulnerable:
      print(f"Potential XSS vulnerability detected in {url}")
    else:
      print(f"No potential XSS vulnerability found in {url} (basic scan)")
  else:
    print("Invalid choice.")

if __name__ == "__main__":
  main()

