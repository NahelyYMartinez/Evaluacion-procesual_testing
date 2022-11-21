"""
Locators login page.
"""


class LoginUi:

    base_url = "http://localhost/Hospital/"
    xpath_image_login = '//*[@id="wrapper"]/section[1]/header/div[1]/nav/div[1]/a/img'
    login = '//*[@id="primary-nav"]/ul/li[5]/a'
    input_user = 'correo'
    input_password = 'contraseña'
    xpath_page_init = '//*[@id="revslider-471"]'
    inicio_login = '/html/body/form/input[3]'
    admin_citas = '/html/body/div[3]/div[1]/div[1]/ul/li[4]'
    reserva_cita = '/html/body/div[3]/div[1]/div[1]/ul/li[4]/ul/li/a'



