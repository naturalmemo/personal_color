# from keras.preprocessing.image import load_img
#import tf.keras.utils.load_img
from keras.utils.image_utils import load_img
def finder(Img):
    # 評価の実施
    img_data = load_img(Img)
    print(type(img_data))