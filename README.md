# Picture Fixer
A simple command utility to play around with color saturation, brightness, contrast and sharpness of images.

## Usage: 
```bash
usage: main.py [-h] -f IMAGE_PATH -o OUTPUT [-c COLOUR_MAX] [-cp] [-s SHARPNESS_MAX] [-sp] [-b BRIGHTNESS_MAX] [-bp] [-n CONTRAST_MAX] [-np] [-p]
               [-cf CONTROL_FACTOR]

optional arguments:
  -h, --help            show this help message and exit
  -f IMAGE_PATH, --file IMAGE_PATH
                        The original image file
  -o OUTPUT, --output OUTPUT
                        The destination file
  -c COLOUR_MAX, --color COLOUR_MAX
                        Colour balance factor
  -cp, --color-preview  Enable preview of color processing
  -s SHARPNESS_MAX, --sharpness SHARPNESS_MAX
                        Sharpness factor
  -sp, --sharpness-preview
                        Enable preview of sharpness processing
  -b BRIGHTNESS_MAX, --brightness BRIGHTNESS_MAX
                        Brightness factor
  -bp, --brightness-preview
                        Enable preview of brightness processing
  -n CONTRAST_MAX, --contrast CONTRAST_MAX
                        Contrast factor
  -np, --contrast-preview
                        Enable preview of brightness processing
  -p, --preview         Preview the output WITHOUT writing to the output file
  -cf CONTROL_FACTOR, --control-factor CONTROL_FACTOR
                        Modifies the divisor to allow for fine grained control
```