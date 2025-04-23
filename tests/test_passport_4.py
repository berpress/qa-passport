import time


class TestPassport4:
    def test_passport_add_valid_data(self, passport_page_4):
        """
        1. Добаваляем валидные данные
        """
        # добавляем данные
        passport_page_4.add_passport(name_text="Иван",
                                   last_name_text="Иванов",
                                   date_text="11.03.2019",
                                   about_text="about")
        # time.sleep(4)

    def test_passport_add_minimal_name(self, passport_page_4):
        """
        1. Добаваляем валидные данные, имя 2 символа
        """
        passport_page_4.add_passport(name_text="Ив",
                                   last_name_text="Иванов",
                                   date_text="11.03.2019",
                                   about_text="about")
        # time.sleep(4)


    def test_passport_add_invalid_name(self, passport_page_4):
        """
        1. Добаваляем валидные данные, имя 1 символа
        """
        passport_page_4.add_passport(name_text="И",
                                   last_name_text="Иванов",
                                   date_text="11.03.2019",
                                   about_text="about")
        # time.sleep(4)
