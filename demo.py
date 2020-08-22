import argparse
from argparse import RawTextHelpFormatter
import glob
from os import makedirs
from os.path import join, exists, basename, splitext
import cv2
from tqdm import tqdm
# project
from exposure_enhancement import enhance_image_exposure
from PIL import Image
import PIL


# TODO: Add function to check if enhanced image exits and skip that file

def process_img():
    # load images
    imdir = "C:\\Users\\sarth\\PycharmProjects\\Image-Quality-Enhancement\\demo\\"
    ext = ['png', 'jpg', 'bmp', 'jpeg']
    # Add image formats here
    files = []
    [files.extend(glob.glob(imdir + '*.' + e)) for e in ext]
    for file in files:
        iw = Image.open(file)
        wid, hei = iw.size[:2]
        if wid > 600 or hei > 400:
            wpercent = (800 / float(iw.size[0]))
            hsize = int((float(iw.size[1]) * float(wpercent)))
            iw = iw.resize((800, hsize), Image.ANTIALIAS)
            iw.save(file)

    images = [cv2.imread(file) for file in files]

    # create save directory
    directory = join("C:\\Users\\sarth\\PycharmProjects\\Image-Quality-Enhancement\\", "static")
    if not exists(directory):
        makedirs(directory)

    # enhance images
    for i, image in tqdm(enumerate(images), desc="Enhancing images"):
        enhanced_image = enhance_image_exposure(image)
        filename = basename(files[i])
        name, ext = splitext(filename)
        method = "DUAL"
        corrected_name = f"{name}{ext}"
        cv2.imwrite(join(directory, corrected_name), enhanced_image)


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(
#         description="Python implementation of two low-light image enhancement techniques via illumination map "
#                     "estimation.",
#         formatter_class=RawTextHelpFormatter
#     )
#     parser.add_argument("-f", '--folder', default='./demo/', type=str,
#                         help="folder path to test images.")
#     parser.add_argument("-g", '--gamma', default=0.6, type=float,
#                         help="the gamma correction parameter.")
#     parser.add_argument("-l", '--lambda_', default=0.1, type=float,
#                         help="the weight for balancing the two terms in the illumination refinement optimization objective.")
#     parser.add_argument("-ul", "--lime", action='store_true',
#                         help="Use the LIME method. By default, the DUAL method is used.")
#     parser.add_argument("-s", '--sigma', default=3, type=int,
#                         help="Spatial standard deviation for spatial affinity based Gaussian weights.")
#     parser.add_argument("-bc", default=1, type=float,
#                         help="parameter for controlling the influence of Mertens's contrast measure.")
#     parser.add_argument("-bs", default=1, type=float,
#                         help="parameter for controlling the influence of Mertens's saturation measure.")
#     parser.add_argument("-be", default=1, type=float,
#                         help="parameter for controlling the influence of Mertens's well exposedness measure.")
#     parser.add_argument("-eps", default=1e-3, type=float,
#                         help="constant to avoid computation instability.")
#
#     args = parser.parse_args()
#     main(args)