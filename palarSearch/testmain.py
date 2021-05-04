import magazineSearch
import queue
from nameSearch import nameSearch

ref = queue.Queue()

# test paper
# sciencedirect:
# s0 = 'Visualizing Hypothalamic Network Dynamics forAppetitive and Consummatory Behaviors'
# nature:
# n1 = 'Somatic mutation landscapes at single-molecule resolution'
# n2 = 'Deep learning Y LeCun'
# n3 = 'C. difficile exploits a host metabolite produced during toxin-mediated disease'
# n4 = 'The central role of DNA damage in the ageing process'

SearchingPaperName = input('searching paper:\n')
link_html = nameSearch(SearchingPaperName)
label = magazineSearch.magzineLabel(link_html)


result = magazineSearch.magazineSearch(SearchingPaperName, label)
for x in result:
    ref.put_nowait(x)

print(ref.queue)