
# coding: utf-8

# # Wikipedia Definitions

# In[18]:

import urllib

search_term = raw_input("What would you like to learn about? (Please enter underscores instead of spaces) \n")
search_url = "https://en.wikipedia.org/wiki/"+search_term

get_wiki = urllib.urlopen(search_url)
wiki_text = get_wiki.read()
get_wiki.close()

start_index = wiki_text.find("<p>")
end_index = wiki_text.find("</p>")

trimmed = wiki_text[start_index:end_index]

def text_extraction(txt):
    extract = ""
    i=0
    j=0
    while i != -1:
        i = txt.find("<",j)
        j = txt.find(">",i)
        if j == -1 or j == len(txt)-1:
            break
        if not txt[j+1] == "<":
            extract = extract+txt[j+1:txt.find("<",j+1)]
    if txt[-1] == ".":
        extract = extract+txt[(txt.rfind(">"))+1:]
    return extract        

print "\n"+text_extraction(trimmed)


# In[ ]:



