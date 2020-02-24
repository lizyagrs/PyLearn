import matplotlib.pyplot as plt

#打开指定图片
image = plt.imread('hanititian.jpg')
#指定图片中的红波段
im_r = image[:, :, 0]  # 红色通道
#图片显示红波段
plt.imshow(im_r)
#窗口中展示图片
plt.show()
# 加载灰度图，可以添加 cmap 参数解决
plt.imshow(im_r, cmap='Greys_r')
#窗口中展示灰度图
plt.show()