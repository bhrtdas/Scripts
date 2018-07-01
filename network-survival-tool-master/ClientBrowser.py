import urllib.request
import os

# Define a function so you can rip the html from a target domain and print to filepath

def html_rip(targeturl, filepath):
    with urllib.request.urlopen(targeturl) as response:
      html = str(response.read())
      tempfile = open(filepath, "w")
      tempfile.write(html)
      tempfile.close


# Specify the target domain

html_rip(input("Whats the complete url of the target? "), input("What's the absolute path of the filepath you want to create? "))
