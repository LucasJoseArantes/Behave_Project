
MY_ACCOUNT_LOCATORS = {
    "login" : {
        'login_username' : {'type': 'id', 'locator':'username'},
        'login_password' : {'type': 'id', 'locator':'password'},
        'login-btn' : {'type' : 'css selector' ,  'locator':'button[name="login"]'}
    },

    "logged-in-successfully": {
        'success_message_username' : {'type' :'xpath', 'locator' : '//*[@id="post-9"]/div/div/div/p[1]/strong[1]'}, # checks if the username (wich is the start of the email adresss) matches the website message  
        'logout-btn' : {'type' :'css selector', 'locator' : "li[class='woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--customer-logout'] a"}
    }
}

