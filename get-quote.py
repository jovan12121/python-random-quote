import random
def p():
    #print("Keep it logically awesome.")

    f = open("quotes.txt","a")
    f.write("Get busy living or get busy dying")
    f.close()
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    last = len(quotes)
    rnd = random.randint(0,last)
    print(quotes[rnd],end = "")
    print(quotes[15])


if __name__== "__main__":
  p()
