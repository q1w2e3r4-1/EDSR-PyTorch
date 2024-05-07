import matplotlib.pyplot as plt
import cv2

if __name__ == '__main__':
    # 读取两张图片
    img1 = cv2.imread('11.jpg')[:, :, (2, 1, 0)]
    img2 = cv2.imread('11_x4_SR.png')[:, :, (2, 1, 0)]
    # plt.imshow(img1, cmap=plt.get_cmap('gray'))
    # plt.show()

    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    print(img2_gray.shape)
    # 创建一个图像窗口
    plt.figure(figsize=(10, 5))  # 设置图像窗口的大小

    # 在第一个轴上展示第一张图片的灰度图像
    plt.subplot(1, 2, 1)  # 1行2列的第一个位置
    plt.imshow(img1_gray, cmap='gray')
    plt.title('First Image (Greyscale)')  # 设置标题
    plt.axis('off')  # 关闭坐标轴

    # 在第二个轴上展示第二张图片的灰度图像
    plt.subplot(1, 2, 2)  # 1行2列的第二个位置
    plt.imshow(img2_gray, cmap='gray')
    plt.title('Second Image (Greyscale)')  # 设置标题
    plt.axis('off')  # 关闭坐标轴

    # 调整子图之间的间距
    plt.tight_layout()

    # 显示图像
    # plt.colorbar()
    plt.show()
