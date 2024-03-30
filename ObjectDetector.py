from ultralytics import YOLO
import cv2

model = YOLO("LemonTeaDetection(2).pt")

camera = cv2.VideoCapture(0)
while camera.isOpened():
    success, img = camera.read()
    if not success:
        break

    result = model(img)
    # print(result)
    boxes = result[0].boxes
    names = result[0].names
    # print("class:", boxes.cls)
    # print("conf", boxes.conf)
    # print("Boxes", boxes.xyxy)

    for i in boxes.xyxy:
        a = i.tolist()
        # print(a)
        first_point = (int(a[0]), int(a[1]))
        last_point = (int(a[2]), int(a[3]))
        img = cv2.rectangle(img, first_point, last_point, (0, 255, 0), 2)

        cls = int(boxes.cls[0])

        org = [int(a[0]), int(a[1])]
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (0, 255, 0)
        thickness = 2

        cv2.putText(img, names.get(cls), org, font, fontScale, color, thickness)

    cv2.imshow("image", img)

    key_code = cv2.waitKey(1)
    if key_code in [27, ord('q')]:
        break
camera.release()
cv2.destroyAllWindows()
