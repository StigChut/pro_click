

import pyautogui

from my_logger import logger
from func.random_clic import rand_clik

def find_and_interact(image_path, title, second_image_path=None, self_click=False):
    """
    Функция для поиска изображений и взаимодействия с ними.
    
    :param image_path: Путь до первого изображения для поиска
    :param second_image_path: Путь до второго изображения для поиска в регионе найденного первого изображения
    :param click_self: Флаг, указывающий следует ли кликнуть на найденное первое изображение
    :return: True, если операция выполнена успешно, иначе False
    """

    # Точность поиска
    confidence_val=0.8

    try:
        # Ищем первое изображение
        first_image = pyautogui.locateOnWindow(image_path, title, confidence=confidence_val)
        
        if first_image:
            logger.debug(f"Изображение {image_path} найдено")

            # Если задан второй путь, ищем второе изображение в области первого
            if second_image_path:
                region = (first_image.left, first_image.top, first_image.width, first_image.height)
                second_image = pyautogui.locateOnScreen(second_image_path, region=region, confidence=confidence_val)
                
                if second_image:
                    logger.debug(f"Изображение {second_image_path} найдено в области первого")
                    # Кликаем на второе изображение
                    rand_clik(second_image)
                    logger.debug(f"Клик по второму изображению {second_image_path} выполнен")
                    return True
                else:
                    logger.debug(f"Изображение {second_image_path} не найдено в области первого")
                    return False
                
            # Если включен флаг клика по первому изображению
            elif self_click:
                rand_clik(first_image)
                logger.debug(f"Клик по первому изображению {image_path} выполнен")
                return True
            else:
                return True
        else:
            logger.debug(f"Изображение {image_path} не найдено")
            return False
    except pyautogui.ImageNotFoundException:
        pass
    except Exception as e:
        logger.exception(f"Ошибка во время выполнения поиска/взаимодействия: {e}")
        return False
