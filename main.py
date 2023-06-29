import os
import openai
import random

openai.api_key ="enter your API key"

def get_completion_from_messages(messages,
                                 model="gpt-3.5-turbo",
                                 temperature=0,
                                 max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]

def get_welcome_message():
    welcome_messages = [
        "Hi, welcome to our coffee shop! How can I assist you today?",
        "Hello there! Thank you for choosing our coffee shop. How may I help you?",
        "Welcome! We're delighted to serve you. What can I get for you today?",
    ]
    return random.choice(welcome_messages)

def display_menu():
    menu = {
        "1. Espresso": "$3.99",
        "2. Cappuccino": "$4.49",
        "3. Latte": "$4.99",
        "4. Americano": "$3.99",
        "5. Mocha": "$4.99",
        "6. Macchiato": "$4.49",
        "7. Frappuccino": "$5.49",
        "8. Hot Chocolate": "$3.99",
        "9. Tea": "$2.99",
        "10. Drip Coffee": "$2.99",
        "11. Iced Coffee": "$3.99",
        "12. Affogato": "$4.99",
        "13. Irish Coffee": "$5.99",
        "14. Flat White": "$4.99",
        "15. Turkish Coffee": "$3.99",
        "16. Chai Latte": "$4.49",
        "17. Matcha Latte": "$4.99",
        "18. Hot Cocoa": "$3.99",
        "19. Cold Brew": "$4.49",
        "20. Green Tea": "$2.99",
    }
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: {price}")
    print()

def chatbot():
    delimiter = "####"
    system_message = f"""
    you are an AI chatbot for a coffee shop. \
    You will be provided with coffee shop customers' orders. \
    you should start the conversation with welcoming message like\
    "Hi, welcome to our coffee shop! How can I assist you today?",
    "Hello there! Thank you for choosing our coffee shop. How may I help you?",
    "Welcome! We're delighted to serve you. What can I get for you today? 
    Follow these steps to answer the customer orders\
    The customer order will be delimited with four hashtags,\
    i.e. {delimiter}. 

    Step 1:{delimiter} First decide whether the customer is \
    asking a question about a specific item or items. \
    

    Step 2:{delimiter} If the user is asking about \
    specific items, identify whether \
    the products are in the following list.
    All available Items: 

    1. Item: Espresso
       Price: $3.49
    2. Item: Cappuccino
       Price: $4.49
    3. Item: Latte
       Price: $4.99
    4. Item: Americano
       Price: $3.99
    5. Item: Mocha
       Price: $4.99
    6. Item: Macchiato
       Price: $4.49
    7. Item: Frappuccino
       Price: $5.49
    8. Item: Hot Chocolate
       Price: $3.99
    9. Item: Tea
       Price: $2.99
    10. Item: Drip Coffee
        Price: $2.99
    11. Item: Iced Coffee
        Price: $3.99
    12. Item: Affogato
        Price: $4.99
    13. Item: Irish Coffee
        Price: $5.99
    14. Item: Flat White
        Price: $4.99
    15. Item: Turkish Coffee
        Price: $3.99
    16. Item: Chai Latte
        Price: $4.49
    17. Item: Matcha Latte
        Price: $4.99
    18. Item: Hot Cocoa
        Price: $3.99
    19. Item: Cold Brew
        Price: $4.49
    20. Item: Green Tea
        Price: $2.99

    Step 3:{delimiter} If the message contains items \
    in the list ask the customer for any additions syrups, suger ,wipe cream and so on \
    ask the user one question per time.
    

    Step 4:{delimiter}:tell the customer the total price \
    and ask for payment method \
    ask the customer if he have any coupons \
    ar points to use \
    if the customer have coupons or points \
    ask him to enter the code or the points number \
    if the customer don't have coupons or points \
     ask him if he want to pay by cash or credit card \
    it the payment process is completed \
    tell that to the customer and\
     say goodbye to the customer and thank him for his visit \
    

    Step 5:{delimiter}: if the customer is ordering a normal item \
     that can be found at the coffeeshop but  it is not in the menu \ 
     First, politely apologize to the customer \
     and explain the item is not available \
      ask the customer to select something else \
    
    Step 6:{delimiter} :If the user asking something unlogical \
     strange item that can't usually be found at the coffeeshop \ 
    for example order coffee with cheese  \ 
    First, politely correct the \
    customer's incorrect order if applicable. \
    explain that something is wrong is the order \ 
    Only mention or reference items in the list of \
    Respond in a friendly and helpful tone, \
    with very concise answers. \
    Make sure to ask the user relevant follow up questions \
    to get all the information you need. 
    
    
    Use the following format:
    Step 1:{delimiter} <step 1 reasoning>
    Step 2:{delimiter} <step 2 reasoning>
    Step 3:{delimiter} <step 3 reasoning>
    Step 4:{delimiter} <step 4 reasoning>
    Step 5:{delimiter} <step 5 reasoning>
    Step 6:{delimiter} <step 6 reasoning>
    Response to user:{delimiter} <response to customer>

    Make sure to include {delimiter} to separate every step.
    """


    chat_history = [
        {'role': 'system',
         'content': system_message},
     ]

    customer_id = input("Please enter your ID: ")
    display_menu()
    print(get_welcome_message())


    while True:
        user_input = input("customer: ")

        if user_input.lower() in ["goodbye", "bye", "see you later", "exit"]:
            print("AI: Thank you for your order! What would you like to do next?")
            print("1. Exit")
            print("2. Proceed to the next customer")
            user_input = input("Customer: ")
            if user_input.lower() == "1":
                break
            elif user_input.lower() == "2":
                chat_history = [
                    {"role": "system", "content": get_welcome_message()}
                ]
                customer_id = input("Please enter your ID: ")
                display_menu()
                print("Welcome to our coffee shop!")
                print(get_welcome_message())
                continue


            break


        user_message = f"{delimiter}{user_input}{delimiter}"
        messages = chat_history + [
            {'role': 'user',
             'content': f"{delimiter}{user_message}{delimiter}"},
        ]

        response = get_completion_from_messages(messages)
        try:
            final_response = response.split(delimiter)[-1].strip()
        except Exception as e:
            final_response = "Sorry, I'm having trouble right now, please try asking another question."
        chat_history.append({"role": "user", "content": user_message})
        chat_history.append({"role": "system", "content": response})
        print("AI:", final_response)

chatbot()
