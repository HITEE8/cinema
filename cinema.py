#=================================================================================
#                    CINEMA TICKET KIOSK
#=================================================================================
ticket_1 = 12.00
ticket_2 = 15.00
ticket_3 = 9.50
ticket_4 = 20.00
ticket_5 = 10.00
ticket_6 = 15.00
ticket_7 = 13.00
popcorn = 2.00
fanta = 1.00
popcorn_fanta = 3.00
water = 1.00
sci_fi_seats = 10
hunted_manor_seats = 5
Spider_Man_seats = 50 
Toy_Story_seats = 30
Avengers_Doomsday_seats = 33
Dune_seats = 35



while True:

       print("\n=============================================================================")
       print(" ⬛              WELCOME TO CINEMA TICKET KIOSK                           ⬛  ")
       print("=============================================================================")


       print("\n=========== Current Showtimes =====================")

       print("1. Sci-Fi odyssey (PG) ")
       print("2. The Hunted Manor (R)  ")
       print("3. Cartoon Adventures (G) ")
       print("4. Spider-Man Brand New Day (PG) ")
       print("5. Toy Story (G) ")
       print("6. Avengers Doomsday (PG) ")
       print("7. Dune (PG) ")
       print("8. Exit")

       print("===================================================")

       choice = input("Select a movie to book: ")

    
       
 #=================================================================================
 #  Sci-Fi odyssey
 #=================================================================================


       if choice == "1":
           print("\n=========== Sci-Fi odyssey (PG) =====================")

           print("============== Price - $12 ==========================")
           print("============== 10 seats left ========================")

           print("=====================================================")
           Pg_rating = input("This movie is rated PG. Please enter your age to verify: ")
           amount = int(input("How many tickets would you like for Sci-Fi odyssey (PG)? "))
           if amount > 1 and amount <= 10:
              print("Please enter a valid ticket number")
              while True:
               print("\n=========== Refreshment =====================")
            
               print("1. Popcorn ")
               print("2. Fanta  ")
               print("3. popcorn and fanta")
               print("4. water ")
               print("5. Next ")

               print("==============================================")
               refreshment = input("Select your preferred choice: ")
            #=================================================================================
            #  POPCORN
            #=================================================================================
               if refreshment == "1":
                  print("\n=========== Popcorn =====================")
                  print("\n=========== $2 =====================")
                  # AMOUNT WITHOUT REFRESHMENT
               
                  total_tickets = amount * ticket_1
               
                  #REMOVED PURCHASED SEATS
               
                  sci_fi_seats -= amount
               
                  #AMOUNT WITH SNACKS
                  total = total_tickets + (popcorn * amount)
            #=================================================================================
            #   FANTA
            #=================================================================================        
               elif refreshment == "2":
                  print("\n=========== Fanta =====================")
                  print("\n=========== $1 ========================")
                  # AMOUNT WITHOUT REFRESHMENT
                  total_tickets = amount * ticket_1
               
                  #REMOVED PURCHASED SEATS
                  sci_fi_seats -= amount
               
                  #AMOUNT WITH SNACKS
                  total = total_tickets + (fanta * amount)
            #=================================================================================
            #  POPCORN AND FANTA 
            #=================================================================================
               elif refreshment == "3":
                  print("\n=========== Popcorn and Fanta =====================")
                  print("\n=========== $3 ========================")
                  # AMOUNT WITHOUT REFRESHMENT
                  total_tickets = amount * ticket_1           
               
                  #REMOVED PURCHASED SEATS
                  sci_fi_seats -= amount
               
                  #AMOUNT WITH SNACKS
                  total = total_tickets + (popcorn_fanta * amount)   
            #=================================================================================
            #  WATER
            #=================================================================================  
               elif refreshment == "4":
                  print("\n=========== WATER=====================")
                  print("\n=========== $1 ========================")
                  # AMOUNT WITHOUT REFRESHMENT
                  total_tickets = amount * ticket_1          
               
                  #REMOVED PURCHASED SEATS
                  sci_fi_seats -= amount
               
                  #AMOUNT WITH SNACKS
                  total = total_tickets + (water * amount)  

                  print("\n===================================================")
                  print("TICKETS PURCHASED SUCCESSFULLY!")
                  print("Movie: The Hunted Manor (R)")
                  print(f"Tickets: {amount}")    
                  print(f"Total : ${total:.2f}")
                  print(f"sci_fi_seatss (R) : {sci_fi_seats} seats left")
                  print("===================================================") 

            #=================================================================================
            #  NEXT
            #=================================================================================                   
               elif refreshment == "5": 
                  total_tickets = amount * ticket_1 
                  sci_fi_seats -= amount
                  print("\n===================================================")
                                                   
                  print("TICKETS PURCHASED SUCCESSFULLY!")
                  print("Movie: The Hunted Manor (R)")
                  print(f"Tickets: {amount}")    
                  print(f"Total : ${total_tickets:.2f}")
                  print(f"sci_fi_seatss(R) : {sci_fi_seats} seats left")
                  print("===================================================")
                  
                  break
           else:
            print("\n⬛ Booking failed. only 10 seats are avialable.")               

 #=================================================================================
 #  The Hunted Manor
 #=================================================================================


       elif choice == "2":
              print("\n=========== The Hunted Manor (R) =====================")
              print("============== Price - $15 ==========================")
              print("============== 5 seats left ========================")
              R_rating = int(input("This movie is rated R. Please enter your age to verify: "))

              if R_rating < 17:
                 print("Booking failed. You must be 17 or older to watch this movie.")
              else:
                amount = int(input("How many tickets would you like for The Hunted Manor (R)? "))
                if amount > 1 and amount <= 5:
                    print("Please enter a valid ticket number")
                    while True:
                     print("\n=========== Refreshment =====================")
                    
                     print("1. Popcorn ")
                     print("2. Fanta  ")
                     print("3. popcorn and fanta")
                     print("4. water ")
                     print("5. Next ")

                     print("===================================================")
                     refreshment = input("Select your preferred choice: ")
                 #=================================================================================
                 #  POPCORN
                 #=================================================================================
                     if refreshment == "1":
                        print("\n=========== Popcorn =====================")
                        print("\n=========== $2 =====================")
                        # AMOUNT WITHOUT REFRESHMENT

                        total_tickets = amount * ticket_2

                        #REMOVED PURCHASED SEATS

                        hunted_manor_seats -= amount

                        #AMOUNT WITH SNACKS
                        total = total_tickets + (popcorn * amount)
                 #=================================================================================
                 #   FANTA
                 #=================================================================================        
                     elif refreshment == "2":
                        print("\n=========== Fanta =====================")
                        print("\n=========== $1 ========================")
                        # AMOUNT WITHOUT REFRESHMENT
                        total_tickets = amount * ticket_2

                        #REMOVED PURCHASED SEATS
                        hunted_manor_seats -= amount

                        #AMOUNT WITH SNACKS
                        total = total_tickets + (fanta * amount)
                 #=================================================================================
                 #  POPCORN AND FANTA 
                 #=================================================================================
                     elif refreshment == "3":
                        print("\n=========== Popcorn and Fanta =====================")
                        print("\n=========== $3 ========================")
                        # AMOUNT WITHOUT REFRESHMENT
                        total_tickets = amount * ticket_2           

                        #REMOVED PURCHASED SEATS
                        hunted_manor_seats -= amount

                        #AMOUNT WITH SNACKS
                        total = total_tickets + (popcorn_fanta * amount)   
                 #=================================================================================
                 #  WATER
                 #=================================================================================  
                     elif refreshment == "4":
                        print("\n=========== WATER=====================")
                        print("\n=========== $1 ========================")
                        # AMOUNT WITHOUT REFRESHMENT
                        total_tickets = amount * ticket_2           

                        #REMOVED PURCHASED SEATS
                        hunted_manor_seats -= amount

                        #AMOUNT WITH SNACKS
                        total = total_tickets + (water * amount)  

                        print("\n===================================================")
                        print("TICKETS PURCHASED SUCCESSFULLY!")
                        print("Movie: The Hunted Manor (R)")
                        print(f"Tickets: {amount}")    
                        print(f"Total : ${total:.2f}")
                        print(f"hunted_manor_seats (R) : {hunted_manor_seats} seats left")
                        print("===================================================")
                 #=================================================================================
                 #  NEXT
                 #=================================================================================
                     elif refreshment == "5":  
                        total_tickets = amount * ticket_1 
                        sci_fi_seats -= amount
                        print("\n===================================================")

                        print("TICKETS PURCHASED SUCCESSFULLY!")
                        print("Movie: The Hunted Manor (R)")
                        print(f"Tickets: {amount}")    
                        print(f"Total : ${total_tickets:.2f}")
                        print(f"hunted_manor_seats(R) : {hunted_manor_seats} seats left")
                        print("===================================================")
                        break    
                else:
                     print("\n⬛ Booking failed. only 5 seats are avialable.")  
                                       
 #=================================================================================
 #  Cartoon Adventures
 #=================================================================================        
       elif choice == "3":
            print("\n=========== Cartoon Adventures (G) =====================")
            print("⬛ This movie is SOLD OUT!")


 #=================================================================================
 #  Brand New Day
 #=================================================================================      
       elif choice == "4":
              print("\n=========== SPIDERMAN BRAND NEW DAY (R) =====================")
              print("============== Price - $20 ==========================")
              print("============== 50 seats left ========================")
              R_rating = int(input("This movie is rated R. Please enter your age to verify: "))
              if R_rating < 17:
                 print("Booking failed. You must be 17 or older to watch this movie.")
              else:
                  amount = int(input("How many tickets would you like for SPIDERMAN BRAND NEW DAY (R)? "))
                  if amount > 1 and amount <= 30:
                    print("Please enter a valid ticket number")
                    while True:
                      print("\n=========== Refreshment =====================")
                                  
                      print("1. Popcorn ")
                      print("2. Fanta  ")
                      print("3. popcorn and fanta")
                      print("4. water ")
                      print("5. Next ")
              
                      print("===================================================")
                      refreshment = input("Select your preferred choice: ")
                   #=================================================================================
                   #  POPCORN
                   #=================================================================================
                      if refreshment == "1":
                          print("\n=========== Popcorn =====================")
                          print("\n=========== $2 =====================")
                          # AMOUNT WITHOUT REFRESHMENT
              
                          total_tickets = amount * ticket_4
              
                          #REMOVED PURCHASED SEATS
              
                          Spider_Man_seats -= amount
              
                          #AMOUNT WITH SNACKS
                          total = total_tickets + (popcorn * amount)
                   #=================================================================================
                   #   FANTA
                   #=================================================================================        
                      elif refreshment == "2":
                        print("\n=========== Fanta =====================")
                        print("\n=========== $1 ========================")
                        # AMOUNT WITHOUT REFRESHMENT
                        total_tickets = amount * ticket_2
              
                        #REMOVED PURCHASED SEATS
                        Spider_Man_seats -= amount
              
                        #AMOUNT WITH SNACKS
                        total = total_tickets + (fanta * amount)
                   #=================================================================================
                   #  POPCORN AND FANTA 
                   #=================================================================================
                      elif refreshment == "3":
                        print("\n=========== Popcorn and Fanta =====================")
                        print("\n=========== $3 ========================")
                        # AMOUNT WITHOUT REFRESHMENT
                        total_tickets = amount * ticket_4           
              
                        #REMOVED PURCHASED SEATS
                        sci_fi_seats -= amount
              
                        #AMOUNT WITH SNACKS
                        total = total_tickets + (popcorn_fanta * amount)   
                   #=================================================================================
                   #  WATER
                   #=================================================================================  
                      elif refreshment == "4":
                        print("\n=========== WATER=====================")
                        print("\n=========== $1 ========================")
                        # AMOUNT WITHOUT REFRESHMENT
                        total_tickets = amount * ticket_4          
              
                        #REMOVED PURCHASED SEATS
                        Spider_Man_seats -= amount
              
                        #AMOUNT WITH SNACKS
                        total = total_tickets + (water * amount) 


                        print("\nThank you for using the Cinema Ticket Kiosk. Enjoy your movie!")
                        print("\n===================================================")
                        print("TICKETS PURCHASED SUCCESSFULLY!")
                        print("Movie: SPIDERMAN BRAND NEW DAY (R)")
                        print(f"Tickets: {amount}")    
                        print(f"Total : ${total:.2f}")
                        print(f"Spider-Man (R) : {Spider_Man_seats} seats left")
                        print("===================================================") 
                   #=================================================================================
                   #  NEXT
                   #=================================================================================
                      elif refreshment == "5":  
                       total_tickets = amount * ticket_1 
                       sci_fi_seats -= amount
                       print("\n===================================================")
                                     
                       print("TICKETS PURCHASED SUCCESSFULLY!")
                       print("Movie: The Hunted Manor (R)")
                       print(f"Tickets: {amount}")    
                       print(f"Total : ${total_tickets:.2f}")
                       print(f"Spider-Man (R) : {Spider_Man_seats} seats left")
                       print("===================================================")
                                                       
                       break
                  else:
                     print("\n⬛ Booking failed. only 50 seats are avialable.")            
               
                        
 #=================================================================================
 #  TOY STORY
 #=================================================================================      
       elif choice == "5":
              print("\n=========== TOY STORY (G) =====================")
              print("============== Price - $15 ==========================")
              print("============== 30 seats left ========================")
              G_rating = int(input("This movie is rated G. Please enter your age to verify: "))
              if G_rating < 0:
                 print("Booking failed. You must be 0 or older to watch this movie.")
              else:
                  amount = int(input("How many tickets would you like for TOY STORY (G)? "))
                  if amount > 1 and amount <= 30:
                    print("Please enter a valid ticket number")
                    while True:
                      print("\n=========== Refreshment =====================")
                                  
                      print("1. Popcorn ")
                      print("2. Fanta  ")
                      print("3. popcorn and fanta")
                      print("4. water ")
                      print("5. Next ")
              
                      print("===================================================")
                      refreshment = input("Select your preferred choice: ")
                   #=================================================================================
                   #  POPCORN
                   #=================================================================================
                      if refreshment == "1":
                          print("\n=========== Popcorn =====================")
                          print("\n=========== $2 =====================")
                          # AMOUNT WITHOUT REFRESHMENT
              
                          total_tickets = amount * ticket_5
              
                          #REMOVED PURCHASED SEATS
              
                          Toy_Story_seats -= amount
              
                          #AMOUNT WITH SNACKS
                          total = total_tickets + (popcorn * amount)
                   #=================================================================================
                   #   FANTA
                   #=================================================================================        
                      elif refreshment == "2":
                        print("\n=========== Fanta =====================")
                        print("\n=========== $1 ========================")
                        # AMOUNT WITHOUT REFRESHMENT
                        total_tickets = amount * ticket_5
              
                        #REMOVED PURCHASED SEATS
                        Toy_Story_seats -= amount
              
                        #AMOUNT WITH SNACKS
                        total = total_tickets + (fanta * amount)
                   #=================================================================================
                   #  POPCORN AND FANTA 
                   #=================================================================================
                      elif refreshment == "3":
                        print("\n=========== Popcorn and Fanta =====================")
                        print("\n=========== $3 ========================")
                        # AMOUNT WITHOUT REFRESHMENT
                        total_tickets = amount * ticket_5           
              
                        #REMOVED PURCHASED SEATS
                        Toy_Story_seats -= amount
              
                        #AMOUNT WITH SNACKS
                        total = total_tickets + (popcorn_fanta * amount)   
                   #=================================================================================
                   #  WATER
                   #=================================================================================  
                      elif refreshment == "4":
                        print("\n=========== WATER=====================")
                        print("\n=========== $1 ========================")
                        # AMOUNT WITHOUT REFRESHMENT
                        total_tickets = amount * ticket_5          
              
                        #REMOVED PURCHASED SEATS
                        Toy_Story_seats -= amount
              
                        #AMOUNT WITH SNACKS
                        total = total_tickets + (water * amount)  

                        print("\nThank you for using the Cinema Ticket Kiosk. Enjoy your movie!")
                        print("\n===================================================")
                        print("TICKETS PURCHASED SUCCESSFULLY!")
                        print("Movie: SPIDERMAN BRAND NEW DAY (R)")
                        print(f"Tickets: {amount}")    
                        print(f"Total : ${total:.2f}")
                        print(f"Toy Story (G) : {Toy_Story_seats} seats left")
                        print("===================================================")
                   #=================================================================================
                   #  NEXT
                   #=================================================================================
                      elif refreshment == "5":  
                       total_tickets = amount * ticket_1 
                       sci_fi_seats -= amount 
                       print("\n===================================================")
                                     
                       print("TICKETS PURCHASED SUCCESSFULLY!")
                       print("Movie: The Hunted Manor (R)")
                       print(f"Tickets: {amount}")    
                       print(f"Total : ${total_tickets:.2f}")
                       print(f"Toy Story (G) : {Toy_Story_seats} seats left")
                       print("===================================================")   
                       break
                  else:
                     print("\n⬛ Booking failed. only 30 seats are avialable.")   
#=================================================================================
#  DOOMS DAY
#=================================================================================      
       elif choice == "6":
            print("\n=========== AVENGERS DOOMS DAY (G) =====================")
            print("============== Price - $15 ==========================")
            print("============== 33 seats left ========================")
            G_rating = int(input("This movie is rated G. Please enter your age to verify: "))
            if G_rating < 0:
                    print("Booking failed. You must be 0 or older to watch this movie.")
            else:
                    amount = int(input("How many tickets would you like for AVENGERS DOOMS DAY (G)? "))
                    if amount > 1 and amount <= 33:
                       print("Please enter a valid ticket number")
                       while True:
                          print("\n=========== Refreshment =====================")
                                     
                          print("1. Popcorn ")
                          print("2. Fanta  ")
                          print("3. popcorn and fanta")
                          print("4. water ")
                          print("5. Next ")
                 
                          print("===================================================")
                          refreshment = input("Select your preferred choice: ")
                      #=================================================================================
                      #  POPCORN
                      #=================================================================================
                          if refreshment == "1":
                             print("\n=========== Popcorn =====================")
                             print("\n=========== $2 =====================")
                             # AMOUNT WITHOUT REFRESHMENT
                 
                             total_tickets = amount * ticket_6
                 
                             #REMOVED PURCHASED SEATS
                 
                             Avengers_dooms_day_seats -= amount
                 
                             #AMOUNT WITH SNACKS
                             total = total_tickets + (popcorn * amount)
                      #=================================================================================
                      #   FANTA
                      #=================================================================================        
                          elif refreshment == "2":
                           print("\n=========== Fanta =====================")
                           print("\n=========== $1 ========================")
                           # AMOUNT WITHOUT REFRESHMENT
                           total_tickets = amount * ticket_6
                 
                           #REMOVED PURCHASED SEATS
                           Avengers_dooms_day_seats -= amount
                 
                           #AMOUNT WITH SNACKS
                           total = total_tickets + (fanta * amount)
                      #=================================================================================
                      #  POPCORN AND FANTA 
                      #=================================================================================
                          elif refreshment == "3":
                           print("\n=========== Popcorn and Fanta =====================")
                           print("\n=========== $3 ========================")
                           # AMOUNT WITHOUT REFRESHMENT
                           total_tickets = amount * ticket_6           
                 
                           #REMOVED PURCHASED SEATS
                           Avengers_dooms_day_seats -= amount
                 
                           #AMOUNT WITH SNACKS
                           total = total_tickets + (popcorn_fanta * amount)   
                      #=================================================================================
                      #  WATER
                      #=================================================================================  
                          elif refreshment == "4":
                           print("\n=========== WATER=====================")
                           print("\n=========== $1 ========================")
                           # AMOUNT WITHOUT REFRESHMENT
                           total_tickets = amount * ticket_6         
                 
                           #REMOVED PURCHASED SEATS
                           Avengers_dooms_day_seats -= amount
                 
                           #AMOUNT WITH SNACKS
                           total = total_tickets + (water * amount)  
   
                           print("\nThank you for using the Cinema Ticket Kiosk. Enjoy your movie!")
                           print("\n===================================================")
                           print("TICKETS PURCHASED SUCCESSFULLY!")
                           print("Movie: SPIDERMAN BRAND NEW DAY (R)")
                           print(f"Tickets: {amount}")    
                           print(f"Total : ${total:.2f}")
                           print(f"Avengers Dooms Day (G) : {Avengers_dooms_day_seats} seats left")
                           print("===================================================")
                      #=================================================================================
                      #  NEXT
                      #=================================================================================
                          elif refreshment == "5":  
                           total_tickets = amount * ticket_1 
                           sci_fi_seats -= amount 
                           print("\n===================================================")
                                        
                           print("TICKETS PURCHASED SUCCESSFULLY!")
                           print("Movie: The Hunted Manor (R)")
                           print(f"Tickets: {amount}")    
                           print(f"Total : ${total_tickets:.2f}")
                           print(f"Avengers Dooms Day (G) : {Avengers_dooms_day_seats} seats left")
                           print("===================================================")   
                           break
                    else:
                        print("\n⬛ Booking failed. only 30 seats are avialable.")  
#=================================================================================
#  DUNE
#=================================================================================      
       elif choice == "7":
            print("\n=========== DUNE (PG-13) =====================")
            print("============== Price - $13 ==========================")
            print("============== 35 seats left ========================")
            G_rating = int(input("This movie is rated G. Please enter your age to verify: "))
            if G_rating < 0:
                    print("Booking failed. You must be 0 or older to watch this movie.")
            else:
                    amount = int(input("How many tickets would you like for DUNE (PG-13)? "))
                    if amount > 1 and amount <= 35:
                       print("Please enter a valid ticket number")
                       while True:
                          print("\n=========== Refreshment =====================")
                                     
                          print("1. Popcorn ")
                          print("2. Fanta  ")
                          print("3. popcorn and fanta")
                          print("4. water ")
                          print("5. Next ")
                 
                          print("===================================================")
                          refreshment = input("Select your preferred choice: ")
                      #=================================================================================
                      #  POPCORN
                      #=================================================================================
                          if refreshment == "1":
                             print("\n=========== Popcorn =====================")
                             print("\n=========== $2 =====================")
                             # AMOUNT WITHOUT REFRESHMENT
                 
                             total_tickets = amount * ticket_7
                 
                             #REMOVED PURCHASED SEATS
                 
                             Avengers_dooms_day_seats -= amount
                 
                             #AMOUNT WITH SNACKS
                             total = total_tickets + (popcorn * amount)
                      #=================================================================================
                      #   FANTA
                      #=================================================================================        
                          elif refreshment == "2":
                           print("\n=========== Fanta =====================")
                           print("\n=========== $1 ========================")
                           # AMOUNT WITHOUT REFRESHMENT
                           total_tickets = amount * ticket_7
                 
                           #REMOVED PURCHASED SEATS
                           Avengers_dooms_day_seats -= amount
                 
                           #AMOUNT WITH SNACKS
                           total = total_tickets + (fanta * amount)
                      #=================================================================================
                      #  POPCORN AND FANTA 
                      #=================================================================================
                          elif refreshment == "3":
                           print("\n=========== Popcorn and Fanta =====================")
                           print("\n=========== $3 ========================")
                           # AMOUNT WITHOUT REFRESHMENT
                           total_tickets = amount * ticket_7           
                 
                           #REMOVED PURCHASED SEATS
                           Avengers_dooms_day_seats -= amount
                 
                           #AMOUNT WITH SNACKS
                           total = total_tickets + (popcorn_fanta * amount)   
                      #=================================================================================
                      #  WATER
                      #=================================================================================  
                          elif refreshment == "4":
                           print("\n=========== WATER=====================")
                           print("\n=========== $1 ========================")
                           # AMOUNT WITHOUT REFRESHMENT
                           total_tickets = amount * ticket_7         
                 
                           #REMOVED PURCHASED SEATS
                           Avengers_dooms_day_seats -= amount
                 
                           #AMOUNT WITH SNACKS
                           total = total_tickets + (water * amount)  
   
                           print("\nThank you for using the Cinema Ticket Kiosk. Enjoy your movie!")
                           print("\n===================================================")
                           print("TICKETS PURCHASED SUCCESSFULLY!")
                           print("Movie: SPIDERMAN BRAND NEW DAY (R)")
                           print(f"Tickets: {amount}")    
                           print(f"Total : ${total:.2f}")
                           print(f"DUNE (PG-13) : {Dune_seats} seats left")
                           print("===================================================")
                      #=================================================================================
                      #  NEXT
                      #=================================================================================
                          elif refreshment == "5":  
                           total_tickets = amount * ticket_1 
                           sci_fi_seats -= amount 
                           print("\n===================================================")
                                        
                           print("TICKETS PURCHASED SUCCESSFULLY!")
                           print("Movie: DUNE (PG-13)")
                           print(f"Tickets: {amount}")    
                           print(f"Total : ${total_tickets:.2f}")
                           print(f"DUNE (PG-13) : {Dune_seats} seats left")
                           print("===================================================")   
                           break
                    else:
                        print("\n⬛ Booking failed. only 35 seats are avialable.")                                 
                                
 #=================================================================================
 #  Exit 
 #================================================================================= 

       elif choice == "8":
           print("\n===================================================")
           print("Thank you for using the Cinema Ticket Kiosk!")
           print("Enjoy your movie!")
           print("===================================================")
           break
#=================================================================================
#                    INVALID MOVIE CHOICE
#=================================================================================

       else:

        print("\n===================================================")
        print("Invalid choice.")
        print("Please select a movie from 1 to 8.")
        print("===================================================")     
                




           


  

