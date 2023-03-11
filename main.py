from ImageCorrector.image_correction import ImageCorrectionService
import argparse
import os


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('-f', '--file', help="The original image file", dest='image_path', required=True)
    args.add_argument('-o', '--output', help="The destination file", dest='output', required=True)
    args.add_argument('-c', '--color', help="Colour balance factor", type=float, dest='colour_max', default=4.0)
    args.add_argument('-cp', '--color-preview', help='Enable preview of color processing', dest='colour_preview',
                      default=False, action='store_true')
    args.add_argument('-s', '--sharpness', help="Sharpness factor", type=float, dest='sharpness_max', default=4.0)
    args.add_argument('-sp', '--sharpness-preview', help='Enable preview of sharpness processing',
                      dest='sharpness_preview', default=False, action='store_true')
    args.add_argument('-b', '--brightness', help="Brightness factor", type=float, dest='brightness_max', default=4.0)
    args.add_argument('-bp', '--brightness-preview', help="Enable preview of brightness processing",
                      dest='brightness_preview', default=False, action='store_true')
    args.add_argument('-n', '--contrast', help="Contrast factor", type=float, dest='contrast_max', default=4.0)
    args.add_argument('-np', '--contrast-preview', help='Enable preview of brightness processing', default=False,
                      dest='contrast_preview', action='store_true')
    args.add_argument('-p', '--preview', help="Preview the output WITHOUT writing to the output file", default=False,
                      dest='preview', action='store_true')
    args.add_argument('-cf', '--control-factor', help='Modifies the divisor to allow for fine grained control',
                      type=float, default=4.0, dest='control_factor')
    argz = args.parse_args()

    image_path = './Input/before.png'
    if os.path.exists(image_path):
        image_service = ImageCorrectionService(image_path, control_factor=argz.control_factor)
        image_service.correct_colour_balance(argz.colour_max, enable_processing_display=argz.colour_preview)
        image_service.correct_sharpner(argz.sharpness_max, enable_processing_display=argz.sharpness_preview)
        image_service.correct_contrast(argz.contrast_max, enable_processing_display=argz.contrast_preview)
        image_service.correct_brightness(argz.brightness_max, enable_processing_display=argz.brightness_preview)
        if argz.preview:
            image_service.preview()
        else:
            image_service.save_processed_file(argz.output)
    else:
        print(f'[!]\tFailed to find file {image_path}')