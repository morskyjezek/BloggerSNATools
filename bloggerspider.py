import requests
from urllib import urlopen
import urllib2
from bs4 import BeautifulSoup

root_url = raw_input('Enter the URL you want to search: ')
seed_post = root_url

def get_links_in_blogger_post():
  response = requests.get(seed_post)
  soup = BeautifulSoup(response.text)
  return [a.attrs.get('href') for a in soup.select('div.post-body a[href]')]

def get_years_posts_from_blogger():
  try:
    year = raw_input('What year\'s archive do you want? ')
    year = int(year)

    if year < 1990 or year > 2020:
      print 'Invalid year.'
      exit()
    else:
      print 'Results for',year,':'
  except:
    print 'Error: no response for that year.'

  yearBegin = str(year)
  yearEnd = str(year + 1)
  arcUrl = "search?updated-min="+yearBegin+"-01-01T00:00:00%2B01:00&updated-max="+yearEnd+"-01-01T00:00:00%2B01:00"
  archiveURL = root_url + arcUrl
  response = requests.get(archiveURL)
  soup = BeautifulSoup(response.text)
  return [a.attrs.get('href') for a in soup.select('div.post-body a[href]')]

def get_older_post_link():
  response = requests.get(seed_post)
  soup = BeautifulSoup(response.text)
  return [a.attrs.get('href') for a in soup.select('div.blog-pager a.blog-pager-older-link')]

def return_posts_on_blogger_page():
  response = requests.get(seed_post)
  soup = BeautifulSoup(response.text)
  posts = soup.select('div.post-body')
  return len(posts)

#get the links in a single post - url to post must be specified at input
postLinks = get_links_in_blogger_post()
linkCount = 0
print 'Found the following links: '
for link in postLinks:
  print link
  linkCount += 1
print 'Found',linkCount,'links in all.'

#get the link to the previous post - for a post url specified at input as root_url
prevPost = get_older_post_link()
if len(prevPost) > 1:
  print 'This found more than one link to previous posts:',len(prevPost),'posts found.'
else:
  print 'Link to previous post: '
  for u in prevPost: print u

#count the posts found - not working
postCount = 0
#posts = page_soup.find_all('div.post-body')
#for post in posts:
#  postCount += 1

numPosts = return_posts_on_blogger_page()
if numPosts >= 1:
  print 'Found',numPosts,'posts.'
else:
  print 'The post count is not working at this time.'

#get the links from a year's worth of posts based on the root_url, which should be specified as the blogger front page
archiveLinks = get_years_posts_from_blogger()
archiveLinkCount = 0
archiveLinkList = []
for link in archiveLinks:
  print link
  archiveLinkCount += 1
  archiveLinkList.append(link)
print archiveLinkList
print 'Found',archiveLinkCount,'links on the page for posts from year requested.'
