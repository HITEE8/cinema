#=================================================================================
#                    CINEMA TICKET KIOSK
#=================================================================================
ticket_1 = 12.00
ticket_2 = 15.00
ticket_3 = 9.50

while True:

       print("\n=============================================================================")
       print(" ⬛              WELCOME TO CINEMA TICKET KIOSK                           ⬛  ")
       print("=============================================================================")


       print("\n=========== Current Showtimes =====================")

       print("1. Sci-Fi odyssey (PG) - $12.00 (10 seats left)")
       print("2. The Hunted Manor (R) - $15.00 (5 seats left)")
       print("3. Cartoon Adventures (G) - $9.50 (SOLD OUT!)")
       print("4. Exit")

       print("===================================================")

       choice = input("Select a movie to book: ")


 #=================================================================================
 #  Sci-Fi odyssey
 #=================================================================================


       if choice == "1":
           print("\n=========== Sci-Fi odyssey (PG) =====================")
           Pg_rating = input("This movie is rated PG. Please enter your age to verify: ")
           amount = int(input("How many tickets would you like for Sci-Fi odyssey (PG)? "))

           if amount > 10:
                print("\n⬛ Booking failed. only 10 seats are avialable.")

           elif amount < 10:
                total = amount * ticket_1

                print("\n===================================================")

                print("TICKETS PURCHASED SUCCESSFULLY!")
                print("Movie: Sci-Fi odyssey (PG)")
                print(f"Number of tickets: {amount}")    
                print(f"Total cost: ${total:.2f}")
                print("===================================================")

 #=================================================================================
 #  The Hunted Manor
 #=================================================================================


       elif choice == "2":
              print("\n=========== The Hunted Manor (R) =====================")
              R_rating = int(input("This movie is rated R. Please enter your age to verify: "))

              if R_rating < 17:
                 print("Booking failed. You must be 17 or older to watch this movie.")
              else:
                 amount = int(input("How many tickets would you like for The Hunted Manor (R)? "))

                 if amount > 5:
                     print("\n⬛ Booking failed. only 5 seats are avialable.")
    
                 elif amount < 5:
                     total = amount * ticket_2
    
                 print("\n===================================================")
    
                 print("TICKETS PURCHASED SUCCESSFULLY!")
                 print("Movie: The Hunted Manor (R)")
                 print(f"Number of tickets: {amount}")    
                 print(f"Total cost: ${total:.2f}")
                 print("===================================================") 

 #=================================================================================
 #  Cartoon Adventures
 #=================================================================================       

        
       elif choice == "3":
                print("\n=========== Cartoon Adventures (G) =====================")
                print("⬛ This movie is SOLD OUT!")

 #=================================================================================
 #  Exit 
 #================================================================================= 

       elif choice == "4":
                 print("\nThank you for using the Cinema Ticket Kiosk. Enjoy your movie!")
                 break
    
       else:
                 print("\nInvalid choice. Please select a valid option.")   



         
                




           


  

