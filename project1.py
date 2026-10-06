class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.logedin=False
        self.menu()

    def menu(self):
        user_input=input("""Welcome to chatbook!! How would you like to proceed?
                         1.press 1 to signup
                         2.press 2 to signin
                         3.press 3 to write a post
                         4.press 4 to message a friend
                         5.press any other key to exit""")
        print("\n")

        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.my_post()
        elif user_input=="4":
            self.sending()
        else:
            exit()

    def signup(self):
        email=input("Enter your email here-> ")
        password=input("Enter your password here-> ")
        self.username=email
        self.password=password
        print("You have signed up successfully!!")
        print("\n")
        self.menu()
        print("\n")

    def signin(self):
        if self.username=='' and  self.password=='':
            print("Please signup first by pressing 1 in main menu")

        else:
          email=input("Enter your email here-> ")
          password=input("Enter your password here-> ")

          if self.username==email and  self.password==password:
              print("You have signed in successfull !")
              self.logedin=True

          else:
              print("Please input the correct credentials")

        print("\n")
        self.menu()

    def  my_post(self):
        if self.logedin==True:
            txt=input("Enter Your msg here -> ")
            print(f"Your post has been created successfully!!->{txt}")

        else:
            print("You need to sign in first before posting") 

        print("\n")
        self.menu()     

    def  sending(self):
      if self.logedin==True:
          txt=input("Enter Your msg here -> ")
          friend=input("Whom to send the msg?")
          print(f"Your msg has been sent successfully !!->  {txt}")

      else:
          print("You need to sign in first")


obj=chatbook()