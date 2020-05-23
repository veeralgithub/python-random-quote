import random

def head():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last=18
  
  #rnd=random.randint(0,last)
  #print(quotes[rnd])
  print(random.sample(quotes,2))
  
if __name__== "__main__":
 head()






