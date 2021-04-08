from datetime import datetime
import random
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("current date and time :",dt_string)


user_info = {}

print('Zuri Bank ATM')

def direct_user():
    valid_options = False
    print('Welcome to Zuri Bank')
    while valid_options==False:
        ask =int(input('Login >> 1\nRegister >> 2\nPlease enter an option: ' ))
        if ask == 1:
            valid_options=True
            login_user()
        elif ask == 2:
            valid_options=True
            register_user()
        else:
            print('You have selected an invalid option')




def register_user():
    print('Create an account with Zuri Bank')
    e_mail=str(input('Email address: '))
    first_name= str(input('First name: ')).capitalize()
    last_name= str(input('Last name: ')).capitalize()
    gend= ['male','female']
    mar_status=['married','single']

    while True:
        try:
            gender = str(input("Gender: ")).lower()
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if gender not in gend:
            print("Please input one of these genders: male, female")
            continue
        else:
            break

    while True:
        try:
            marital = str(input("Marital status: ")).lower()
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if marital not in mar_status:
            print("Please input one of these: married or single")
            continue
        else:
            break

    pass_word= str(input('please create your password: '))

    if gender == 'female' and marital == 'not married':
        print('Account Successfully opened Miss', last_name)
    elif gender == 'female' and marital == 'married':
        print('Account Successfully opened Mrs', last_name)
    elif gender == 'male':
        print('Account Successfully opened Mr', last_name)

    account=acc_num_gen()
    user_info[account]=[first_name,last_name,e_mail,pass_word,gender,marital]
    print('Your Details are;')
    print('Email: ',e_mail)
    print('password: ',pass_word)
    print('account number: ',account)
    login_user()


def acc_num_gen():
    account_num=random.randint(9870000000,9879999999)
    return account_num


def login_user():
    print('Login with your account number and password')

    acc_num_from_user = int(input('Account Number: '))
    pass_word_user = input('Password: ')

    for account_number, user_details in user_info.items():
        if account_number == acc_num_from_user:
            if user_details[3]==pass_word_user:
                bank_operation(user_details)
            else:
                print('Invalid account or password')


    login_user()



def bank_operation(user):
    print("Welcome %s %s " % ( user[0], user[1] ) )

    selected_option = int(input('Deposit >> 1\nWithdraw >> 2\nLogout >> 3\nExit >> 4 \nPlease enter an option: '))

    if(selected_option == 1):

        deposit_operation()
    elif(selected_option == 2):

        withdrawal_operation()
    elif(selected_option == 3):

        logout()
    elif(selected_option == 4):

        exit()
    else:

        print("Invalid option selected")
        bankOperation(user)

def deposit_operation():
    dep_ask= int(input('How much would you like to deposit: '))
    print('Your balance is $',dep_ask)

def withdrawal_operation():
    with_ask = int(input('How much would you like to withdraw: '))
    print('Please take your cash')


def logout():
    login_user()

direct_user()



