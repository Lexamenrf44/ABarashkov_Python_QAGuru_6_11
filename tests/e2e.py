import allure
from selene import have, command
from pages.app import RegistrationPage


@allure.title('Успешное заполнение формы регистрации студента')
def test_register_demo_user_using_practice_form(setup_browser):
    browser = setup_browser

    app = RegistrationPage()

    with allure.step("Should open demoqa registration form"):
        app.open_demoqa_practice_form()

    with allure.step("Should get rid off banner"):
        app.script_trick()

    with allure.step("Should fill the demoqa registration form"):
        browser.element(app.first_name).type("Alexander")
        browser.element(app.last_name).type("Barashkov")
        browser.element(app.user_email).type("abarashka@email.com")
        app.select_gender('Male')
        browser.element(app.phone_number).type("1234567890")
        app.select_date_of_birth('1', 'December', '1998')
        app.select_hobby('Sports')
        browser.element(app.subject).type("Computer Science").press_enter()
        app.upload_image("chatgpt_logo.png")
        app.fill_current_address("Tbilisi")
        app.select_state("NCR")
        app.select_city("Delhi")

    with allure.step("Should submit the filled form"):
        browser.element(app.submit_button).perform(command.js.click)

    with allure.step("Should check the registration results"):
        app.should_registered_user_with.should(
            have.exact_texts(
                'Alexander Barashkov',
                'abarashka@email.com',
                'Male',
                '1234567890',
                '01 December,1998',
                'Computer Science',
                'Sports',
                'chatgpt_logo.png',
                'Tbilisi',
                'NCR Delhi'
            )

        )

