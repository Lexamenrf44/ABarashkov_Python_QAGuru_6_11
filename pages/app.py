from selene import browser, have, command, be
from conftest import path


class RegistrationPage:

    def __init__(self):
        self.should_registered_user_with = browser.element('.table').all('td').even

    def open_demoqa_practice_form(self):
        browser.open('/automation-practice-form')

    def script_trick(self):
        browser.execute_script('document.querySelector("#fixedban").remove()')
        browser.element('footer').execute_script('element.remove()')
        return self

    def select_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()
        return self

    def select_date_of_birth(self, day, month, year):
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('[class="react-datepicker__year-select"]').type(year)
        browser.element(f'.react-datepicker__day--00{day}').click()
        return self

    def select_hobby(self, hobby):
        browser.all('[for^= hobbies]').element_by(have.text(hobby)).element('..').click()

        return self

    def upload_image(self, file_name):
        browser.element(self.upload_picture).send_keys(path(file_name))

    def fill_current_address(self, value):
        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('#currentAddress').should(be.blank).type(value)

        return self

    def select_state(self, state):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.all("[id^=react-select][id*=option]").element_by(have.exact_text(state)).click()

        return self

    def select_city(self, city):
        browser.element('#city').click()
        browser.all("[id^=react-select][id*=option]").element_by(have.exact_text(city)).click()

    # Common locators

    first_name = '#firstName'
    last_name = '#lastName'
    user_email = '#userEmail'
    phone_number = '#userNumber'
    subject = '#subjectsInput'
    submit_button = '#submit'
    upload_picture = '#uploadPicture'

