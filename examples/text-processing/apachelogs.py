import pyCompute


#text-processing on apache logs

#Obtain all the urls from the log through regular expression : 

file_1 = pyCompute.text.File("apache_logs.txt", name = "log_1")

#operation re_match 
urls = pyCompute.text_ops.re_match(file_1, re = "http.://.\S+", name = "match_1")

#generate a histogram of most common URLS 

hist = pyCompute.text_ops.array_histogram(urls, name = "hist_1")


#create a string session : 
session = pyCompute.StringSession()

result = session.run(pyCompute.default_graph, hist)



print(result)