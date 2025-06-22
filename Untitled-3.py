def main():
  print("Welcome to indentation Race!")
for i in range(5):
   print("Current number:",i)
   if i % 2 == 0:
      print("Even number.")
else:
  print("Odd number.")
  print("Racecompleted!")
  main()


  #Challenge two
def calculate_total_price(item_price,quantity):
   item_total= item_price * quantity 
   tax_rate= 0.07
   tax_amount= item_total * tax_rate
   total_price= item_total + tax_amount
   discount= 0.1
   discounted_price= total_price - (total_price * discount)
   return discounted_price 
item_price = 25.0
quantity = 4
print("Total price:", calculate_total_price (item_price, quantity))


#Challenge three
def calculate_average(numbers):
   total = 0
   for number in numbers:
      total += number
      average = total / len(numbers)
      return average
def classify_average(average):
   if average >= 90:
      return "A"
   elif average>= 80:
      return "B"
   elif average>= 70:
      return "C"
   elif average>= 60:
      return "D"
   else:
      return "F"
   
   student_scores = {95, 88, 72, 65, 79}
   average_score = calculate_averagea(student_score)
   letter_grade = classify_average(average_score)
   print("Average score:", average_score)
   print("Letter grade:", letter_grade)


   #Challenge four
def investigate_scene():
   print("You arrive at a dimly lit room with clues scattered around.")
   if flashlight_available:  # type: ignore
      print("You can see better with your flashlight,")
      print("Youn find a note on the table.")
      if flashlight_available: # type: ignore
         print("The note reads, 'The code to the safe is 4732.'")
      else:
         print("The note reads, ;You need to find the flashlight first.'")

def open_safe(code):
   if code == 4732:
      print("The safe opens, revealing a hidden treasure.")
      print("Congratulations! You solved the mystery.")
   else:
      print("The sfe remains locked. Try agian.")

      flashlight_available = True

      investigate_scene()
      safe_code = 4732
      open_safe(safe_code)       


 #Challenge five        
def display_student_info(name, age):
   print("Students Name:", name)
   print("Students Age:", age)
   if age < 18:
      print("Status: Minor")
   else:
      print("Status: Adult")

student_name = "Alice"
student_age = 20

display_student_info(student_name, student_age)


#Challenge six
def calculate_average(numbers):
   sum = 0
   for number in number:
      sum += number
      average = sum / len(number)
      return average
   
   average = calculate_average(numbers)
   print("Average:", average)