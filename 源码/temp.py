import cv2
window_name="face"
cv2.namedWindow(window_name)
cap = cv2.VideoCapture(0)
    # 告诉OpenCV使用人脸识别分类器
    classfier = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_alt2.xml")
    # 识别出人脸后要画的边框的颜色，RGB格式
    color = (0, 255, 0)
    while cap.isOpened():
        ok, frame = cap.read()  # 读取一帧数据
        if not ok:
            break
            # 将当前帧转换成灰度图像
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(faceRects) > 0:  # 大于0则检测到人脸
            for faceRect in faceRects:  # 单独框出每一张人脸
                x, y, w, h = faceRect
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)

        # 显示图像
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(100)
        # if c & 0xFF == ord('q'):
        if c & 0xFF == 27:
            break
        # 判断是否点击了右上角的关闭按钮
        if cv2.getWindowProperty(window_name,0) == -1:
            break
    # 释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()
