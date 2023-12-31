import cv2

def generate_data():
    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def face_cropped(img):
        if img is not None:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)

            if len(faces) == 0:
                return None

            for (x, y, w, h) in faces:
                cropped_face = img[y:y+h, x:x+w]
                return cropped_face
        return None

    cap = cv2.VideoCapture(0)
    img_id = 1

    while True:
        ret, frame = cap.read()

        if face_cropped(frame) is not None:
            face = cv2.resize(face_cropped(frame), (200, 200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            file_name_path = "data/Shree." + str(img_id) + ".jpg"
            cv2.imwrite(file_name_path, face)

            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow("Cropped_Face", face)

            if cv2.waitKey(1) == 13 or int(img_id) == 1000:
                break

            img_id += 1

    cap.release()
    cv2.destroyAllWindows()

    print("Collecting samples is completed.")

# Call the function to start generating data
generate_data()
