import unittest
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver


class ReservedTestCases(unittest.TestCase):

    valid_name = "Name"
    valid_surname = "Surname"
    valid_email = "wsb.test@gmail.com"
    invalid_password = "is"
    valid_email_2 = "wsb.test2@gmail.com"
    valid_password = "is123@"

    # Setup class and configuration
    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.lppsa.app.reserved",
            "appActivity": "com.lppsa.app.presentation.MainActivity"
        }
        # Start the Appium client
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(20)

    # Close the Appium client
    def tearDown(self):
        self.driver.quit()

        # TC: ID001
        # 1. Wybierz kraj "Polska"
        # 2. Kliknij "Więcej"
        # 3. Kliknij "Moje konto"
        # 4. Kliknij "Zarejestruj się"
        # 5. Wpisz imię
        # 6. Wpisz nazwisko
        # 7. Wprowadź adres e-mail
        # 8. Wprowadź za krótkie hasło
        # 9. Zapisz się do newslettera
        # 10. Kliknij Załóż konto
        # Oczekiwany rezultat
        # Rejestracja nie powodzi się
        # Użytkownik dostaje informację, że wprowadzone hasło jest za krótkie

    def testID001_registerNewUserWithToShortPasswordTest(self):

        # Wybierz kraj "Polska"
        country_btn = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Polska • Poland']")
        country_btn.click()

        # Kliknij "Więcej"
        more_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Więcej")
        more_btn.click()

        # Kliknij "Moje konto"
        my_account_btn = self.driver.find_element(AppiumBy.ID, "com.lppsa.app.reserved:id/accountButton")
        my_account_btn.click()

        # Kliknij "Zarejestruj się"
        sign_up_btn = self.driver.find_element(AppiumBy.ID, "com.lppsa.app.reserved:id/signUpButton")
        sign_up_btn.click()

        # Wpisz imię
        name_field = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Imię']")
        name_field.send_keys(self.valid_name)

        # Wpisz nazwisko
        surname_field = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Nazwisko']")
        surname_field.send_keys(self.valid_surname)

        # Wprowadź adres e-mail
        email_field = self.driver.find_element(AppiumBy.XPATH,  "//*[@text='Adres e-mail']")
        email_field.send_keys(self.valid_email)

        # Wprowadź za krótkie hasło
        password_field = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Hasło']")
        password_field.send_keys(self.invalid_password)

        # Zapisz się do newslettera
        newsletter_checkbox = self.driver.find_element(AppiumBy.ID, "com.lppsa.app.reserved:id/newsletterCheckbox")
        newsletter_checkbox.click()

        # Kliknij "Załóż konto"
        create_account_btn = self.driver.find_element(AppiumBy.ID, "com.lppsa.app.reserved:id/button")
        create_account_btn.click()

        # AssertFinalResult
        error_notice = self.driver.find_element(AppiumBy.ID, "com.lppsa.app.reserved:id/textinput_error")
        print(error_notice.get_attribute('text'))
        self.assertEqual(error_notice.get_attribute('text'), "Hasło jest za krótkie")

        # TC: ID002
        # 1. Wybierz kraj "Polska"
        # 2. Kliknij "Więcej"
        # 3. Kliknij "Moje konto"
        # 4. Wprowadź adres email
        # 5. Wprowadź hasło
        # 6. Kliknij "Zaloguj się"
        # 7. Przejdź do zakładki "Dane osobowe"
        # Oczekiwany rezultat
        # Pomyślne zalogowanie do aplikacji
        # W zakładce "Dane osobowe" widnieje poprawny adres email zalogowanego użytkownika

    def testID002_userLoginWithCorrectDataTest(self):

        # Wybierz kraj "Polska"
        country_btn = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Polska • Poland']")
        country_btn.click()

        # Kliknij "Więcej"
        more_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Więcej")
        more_btn.click()

        # Kliknij "Moje konto"
        my_account_btn = self.driver.find_element(AppiumBy.ID, "com.lppsa.app.reserved:id/accountButton")
        my_account_btn.click()

        # Wprowadź adres email
        email_field = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Adres e-mail']")
        email_field.send_keys(self.valid_email_2)

        # Wprowadź hasło
        password_field = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Hasło']")
        password_field.send_keys(self.valid_password)

        # Kliknij "Zaloguj się"
        sign_in_btn = self.driver.find_element(AppiumBy.ID, "com.lppsa.app.reserved:id/button")
        sign_in_btn.click()

        # Przejdź do zakładki "Dane osobowe"
        personal_data_btn = self.driver.find_element(AppiumBy.ID, "com.lppsa.app.reserved:id/personalText")
        personal_data_btn.click()

        # AssertFinalResult
        check_email_field = self.driver.find_element(AppiumBy.XPATH, "//*[@text='" + self.valid_email_2 + "']")
        print(check_email_field.get_attribute('text'))
        self.assertEqual(check_email_field.get_attribute('text'), self.valid_email_2)

        # TC: ID003
        # 1. Wybierz kraj "Polska"
        # 2. Kliknij "Kategorie"
        # 3. Rozwiń kategorię "Mężczyzna"
        # 4. Rozwiń kategorię "Ubrania"
        # 5. Wybierz "Koszule"
        # 6. Wybierz pierwszy produkt z listy
        # 7. Przejdź przez Wskazówkę obługi ekranu
        # 8. Kliknij "Dodaj do koszyka"
        # 9. Wybierz z listy rozmiar L
        # 10. Przejdź do koszyka
        # Oczekiwany rezultat
        # W koszyku znajduje się 1 produkt wybrany przez użytkownika
        # Użytkownik znajduje się na ekranie "Koszyk" z możliwością przejścia do kasy

    def testID003_addingTheProductToTheCartTest(self):

        # Wybierz kraj "Polska"
        country_btn = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Polska • Poland']")
        country_btn.click()

        # Kliknij "Kategorie"
        category_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Kategorie")
        category_btn.click()

        # Rozwiń kategorię "Mężczyzna"
        man_category_btn = self.driver.find_element(AppiumBy.XPATH, "//*[@text='MĘŻCZYZNA']")
        man_category_btn.click()

        # Rozwiń kategorię "Ubrania"
        clothes_category_btn = self.driver.find_element(AppiumBy.XPATH, "//*[@text='UBRANIA']")
        clothes_category_btn.click()

        # Wybierz "Koszule"
        shirt_btn = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Koszule']")
        shirt_btn.click()

        # Wybierz pierwszy produkt z listy
        product_btn = self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.ImageView")
        product_btn.click()

        # Przejdź przez Wskazówkę
        for i in range (0,4):
            next_btn = self.driver.find_element(AppiumBy.ID, "com.lppsa.app.reserved:id/nextButton")
            next_btn.click()

        # Kliknij "Dodaj do koszyka"
        add_to_the_cart = self.driver.find_element(AppiumBy.ID, "com.lppsa.app.reserved:id/button")
        add_to_the_cart.click()

        # Wybierz z listy rozmiar L
        size_btn = self.driver.find_element(AppiumBy.XPATH, "//*[@text='L']")
        size_btn.click()

        # Przejdź do koszyka
        cart_btn = self.driver.find_element(AppiumBy.ID, "com.lppsa.app.reserved:id/cartFab")
        cart_btn.click()

        # AssertFinalResult
        products_count_label = self.driver.find_element(AppiumBy.ID, "com.lppsa.app.reserved:id/productsCount")
        print(products_count_label.get_attribute('text'))
        self.assertEqual(products_count_label.get_attribute('text'), "1 produkt")
    #

# https://codecouple.pl/2016/02/27/python-specjalna-zmienna-__name__/
if __name__ == '__main__':
    unittest.main()
