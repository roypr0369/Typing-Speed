from time import time
def tperror(prompt):
  global inwords
  words = prompt.split()
  errors = 0
  for i in range(len(inwords)):
    if i in (0 , len(inwords) - 1):
      if inwords[i] == words[i]:
        continue
      else:
        errors += 1
    else:
      if inwords[i] == words[i]:
        if(inwords[i + 1] == words[i + 1]) & (inwords[i - 1] == words[i -  1]):
          continue
        else:
          errors += 1
      else:
        errors += 1
  return errors  

#Now Calculating the Speed of Typing Words per minute
def speed(inprompt , stime , etime):
  global time
  global inwords
  inwords = inprompt.split()
  twords = len(inwords)
  speed = twords / time
  return speed
#Calculating Total Elapsed Time

def elapsedtime(stime , etime):
  return etime - stime

if __name__ == '__main__':
  prompt = "King Kohli is the kohl on the eyes of Indian cricket. He has been an outstanding batsman and is being rated as the best in the business in world cricket in present."
  print("Type this: -- >" , prompt)
  input("Press Enter When you are ready to check your speed!!!")

  stime = time()
  inprompt = input()
  etime = time()

  time = round(elapsedtime(stime , etime) , 2)
  speed = speed(inprompt , stime , etime)
  errors = tperror(prompt)
  
  print("Total Time Elapsed:" , time , "seconds")
  print("Your Average Typing Speed was" , speed , "words per minute(w/m)")
  print("with the total of" , errors , "errors ")
