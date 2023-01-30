from scholarly import scholarly
from scholarly import ProxyGenerator

pg = ProxyGenerator()
pg.FreeProxies()
scholarly.use_proxy(pg)

# Retrieve the author's data, fill-in, and print
# Get an iterator for the author results
search_query = scholarly.search_author('Mihaela Breaban')
first_author_result = next(search_query)
author = scholarly.fill(first_author_result )
# print(first_author_result)
#scholarly.pprint(next(search_query))
first_publication = author['publications'][20]
first_publication_filled = scholarly.fill(first_publication)
# print(first_publication_filled['bib']['author'].split(" and "))
print(first_publication_filled)

# publication_titles = [pub['bib']['title'] for pub in author['publications']]
# print(publication_titles)

#print(scholarly.citedby(first_publication_filled))

#help(scholarly)
# Retrieve the first result from the iterator
# first_author_result = next(search_query)
# scholarly.pprint(first_author_result)

# # Retrieve all the details for the author
# author = scholarly.fill(first_author_result )
# scholarly.pprint(author)

# # Take a closer look at the first publication
# first_publication = author['publications'][0]
# first_publication_filled = scholarly.fill(first_publication)
# scholarly.pprint(first_publication_filled)

# # Print the titles of the author's publications
# publication_titles = [pub['bib']['title'] for pub in author['publications']]
# print(publication_titles)

# # Which papers cited that publication?
# citations = [citation['bib']['title'] for citation in scholarly.citedby(first_publication_filled)]
# print(citations)