'''
# int /float => float   --> eg 7/3.5 = 2.0
# Default parameters in py must be positioned at end
# to find quotient "//" is used  --> eg 9//5 = 1

'''in assignment, for immutable  x=y makes a copy 
               for mutable  x=y  shares the value 
if we start reassigning a list using "+" we get a new list ; thus list.append() is used to extend the old original list without using concatenation'''
to define function we use def 
eg def print(data):
   print("The name is :" + data)
=> print(Cameroon):
   => "The name is : Cameroon"
eg. def area_trianglr(base,height):
     return base8height/2
     
 # in python // or double slash is called floor division of the number , and it is essentially used for taking the integer part of division( Eg 5//2 = 2 ) 
 
eg def function convert_sec(sec):
    hr=sec//3600
    min=(sec-hr*36000//60
    remaining_min=sec-hr*3600-min*60
    return hr,min,remaining_min
 => hr,sec,remaining_sec=convert_sec(5000)     # as we know that fun will return 3 values , 3 variables are there for assignment of value. 
    print( hr,sec,remaining_sec)
     => 1  23 20 
    
 # none datatype in python is used to indicate that things are empty or they doesnt return anything  
  eg of none result= print(Camerron)
     print(result)
     => none
   
 # boolean values has 2 results true or false
 
=> conditions statements in python
   def hint(username)
      if len(username)<3:   # mindwell, : or colon is used after conditional statements in if
         print("Invalid username")
      elif len(username)>15:      # mindwell, : or colon is used after conditional statements in elif
         print("invalid")
      else :                        # mindwell, : or colon is used just after else 
         print("valid username")
 - for loop no of iteration would be n-1 for given parameter n.
    # 1 parameter
   Eg  for x in range(5)    #here range is function for to generate no. here in sequence manner
         print(x)
       => x=0,1,2,3,4 
- FOR - used to do work sequentially in an fixed manner
  WHILE- to repeat actions untill condition changes
- we can specify the size of iteration from starting to ending like 
   # 2 parameter
   eg.  p=1
       for n in range(1,10)
         p=p*n
      print(p)
   => 3628800
- we can also have 3 parameter, in which 1 and 2nd are same as 2 parameterized loop and additional 3ed parameter saya the jump between 2 no.
   eg. for n in range(0,11,2):
    print(n)
# The loop should print 0, 2, 4, 6, 8, 10
- to pickup single element from an loop
eg.  def greet(frnd)
        for frnd in frnds:
           print("Hii" + frnd)
     greet(["Abhishek","Ram","Krishna","Vishnu"])
   # and output is 
  => Hii Abhishek
     Hii Ram
     Hii Krishna
     Hii Vishnu
  #applying same above function greet
   greet("Abhi")
   => Hii A
      Hii B
      Hii H
      Hii I   #as string are iterable , and for loop will go over each letter of string 
      #soln is if u wanna scan each word than a letter than list should be used, where string(word) is part of list
  -> Recursion 
     def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
