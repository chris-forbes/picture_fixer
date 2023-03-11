from PIL import Image, ImageEnhance, ImageFilter


class ImageCorrectionService:

    def __init__(self, path: str, control_factor: float = 4.0):
        self.image: Image = Image.open(path, 'r')
        self.__control_factor__ = control_factor

    def __log_factor(self, factor: int, correction_name: str):
        print(f'{correction_name} : {factor}')

    def correct_colour_balance(self, max: float, enable_processing_display: bool = False) -> None:
        colour_balance = ImageEnhance.Color(self.image)
        if enable_processing_display:
            for i in range(max):
                factor = i / self.__control_factor__
                self.__log_factor(factor, 'Color correction')
                colour_balance.enhance(factor).show(f'Color balance factor: {factor}')
        else:
            factor = max / self.__control_factor__
            self.__log_factor(factor, 'Color correction')
            self.image = colour_balance.enhance(factor)

    def correct_sharpner(self, max: float, enable_processing_display: bool = False) -> None:
        sharpner = ImageEnhance.Sharpness(self.image)
        if enable_processing_display:
            for i in range(max):
                factor = i / self.__control_factor__
                self.__log_factor(factor, 'Sharpness correction')
                sharpner.enhance(factor).show(f'Sharpness balance factor: {factor}')
        else:
            factor = max / self.__control_factor__
            self.__log_factor(factor, 'Sharpness correction')
            self.image = sharpner.enhance(factor)

    def correct_contrast(self, max: float, enable_processing_display: bool = False) -> None:
        contraster = ImageEnhance.Contrast(self.image)
        if enable_processing_display:
            for i in range(max):
                factor = i / self.__control_factor__
                self.__log_factor(factor, 'Contrast correction')
                contraster.enhance(factor).show(f'Contrastor: {factor}')
        else:
            factor = max / self.__control_factor__
            self.__log_factor(factor, 'Contrast correction')
            self.image = contraster.enhance(factor)

    def correct_brightness(self, max: float, enable_processing_display: bool = False) -> None:
        brightness = ImageEnhance.Brightness(self.image)
        if enable_processing_display:
            for i in range(max):
                factor = i / self.__control_factor__
                self.__log_factor(factor, 'Brightness correction')
                brightness.enhance(factor).show(f'Brightness: {factor}')
        else:
            factor = max / self.__control_factor__
            self.__log_factor(factor, 'Brightness correction')
            self.image = brightness.enhance(factor)

    def save_processed_file(self, path: str) -> None:
        self.image.save(path)

    def preview(self) -> None:
        self.image.show('Preview')