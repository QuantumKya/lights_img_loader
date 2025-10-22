from PIL import Image, GifImagePlugin, ImageSequence
from img import get_img_data

# returns array of (pixel_data, colorlist) tuples
def get_gif_data(filepath, brightness = 0.05):
    
    img = Image.open(filepath)
    
    width, height = img.size
    
    frame_data_arr = []
    colorlist_arr = []
    for frame in ImageSequence.Iterator(img):
        frame_data, colorlist = get_img_data(img)
        frame_data_arr.append(frame_data)
        colorlist_arr.append(colorlist)
    
    true_colorlist = []
    color_conversion_map = []
    for cl in colorlist_arr:
        for col in cl:
            if col not in true_colorlist: true_colorlist.append(col)
            else: 
        


if __name__ == "__main__":
    get_gif_data("./abc.gif")