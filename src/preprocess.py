from PIL import Image
import os

if __name__ == '__main__':
    # 打开图像
    pics = os.listdir("../raw")
    for pic in pics:
        path = f'../raw/{pic}'

        image = Image.open(path)
        if image.size[0] > 256:
            # 将图像缩放为256*256
            image = image.resize((256, 256), Image.ANTIALIAS)

        # 检查图像是否具有透明度（alpha）通道
        if image.mode == 'RGBA' or image.mode == 'L':
            # 将图像转换为RGB模式，这会自动移除alpha通道
            image = image.convert('RGB')

        pic_name = pic[0:pic.index('.')] # remove suffix
        image.save(f'../test/{pic_name}_256x256.png')
