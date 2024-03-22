from time import sleep
import pyautogui
from extract_img import ExtractImg, Image
from template_matching import TemplateMatching, cv
import numpy as np


class Step:
    def __init__(self, loc: tuple[int, int], key: str, is_click: bool, delay: int, check_img_src: str) -> None:
        self.loc = loc
        self.key = key
        self.is_click = is_click
        self.delay = delay
        self.check_img = cv.imread(check_img_src)
        pass


class App:
    def __init__(self, check_region: tuple[int, int, int, int], input_text: str, step_1: Step, step_2: Step, step_3: Step) -> None:
        self.check_region = check_region
        self.input_text = input_text
        self.step_1 = step_1
        self.step_2 = step_2
        self.step_3 = step_3
        pass

    def get_check_img(self):
        check_img = pyautogui.screenshot(region=self.check_region)
        return check_img

    @staticmethod
    def get_cv_img(img: Image):
        cv_img = img.convert('RGB')
        cv_img = np.array(cv_img)
        cv_img = cv_img[:, :, ::-1].copy()
        return cv_img

    @staticmethod
    def get_text_from_img(img: Image) -> str:
        return ExtractImg.image_to_string(img)

    @staticmethod
    def execute(step: Step):
        is_end_execute = False

        while is_end_execute == False:
            if step.is_click:
                pyautogui.moveTo(step.loc[0], step.loc[1])
                pyautogui.click()
            else:
                pyautogui.press(step.key)

            sleep(step.delay)

            screen = pyautogui.screenshot()
            screen = __class__.get_cv_img(screen)
            loc = TemplateMatching.matchTemplage(step.check_img, screen, 0.9)

            if loc is not None:
                is_end_execute = True

    def run(self):
        is_end = False

        while is_end == False:
            self.execute(self.step_1)

            check_img = self.get_check_img()
            check_text = self.get_text_from_img(check_img)

            if check_text != self.input_text:
                self.execute(self.step_3)
                is_end = True
            else:
                self.execute(self.step_2)

        print('Done!!!')
