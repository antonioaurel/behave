from pages.basepage import basepage



class LoginPage(BasePage):
    face = (By.ID, 'facebook')
    register = (By.ID, 'register_propostas')

    def click_on_face_button(self):
        super().click(self.face)
