import cv2
import threading


class Vision:
    """
    Class represents the robot's vision methods.
    Camera and capture.
    """

    def __init__(self, camera_id=0):
        self.camera = cv2.VideoCapture(camera_id)

        if not self.camera.isOpened():
            raise Exception("Erro ao abrir a câmera.")

        self.close_program = False

    def read_frame(self):
        ret, frame = self.camera.read()

        if ret:
            frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
            return cv2.flip(frame, 1)
        else:
            print("Erro ao ler o quadro da câmera.")
            return None

    def save_image(self, frame, filename="imagem_captured.jpg"):
        if frame is not None:
            cv2.imwrite(filename, frame)
        else:
            print("Unable to capture image.")

    def start_capture_video(self):
        self.thread_video = threading.Thread(target=self._capture_video)
        self.thread_video.start()

    def stop_capture_video(self):
        self.close_program = True
        self.thread_video.join()
        self.close()

    def close(self):
        self.camera.release()

    def _capture_video(self):
        cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)

        try:
            while self.close_program is False:
                # Capturar um quadro da câmera
                frame = self.read_frame()
                if frame is not None:
                    cv2.imshow("Camera", frame)

                    # Listen to the keyboard for presses.
                    keyboard_input = cv2.waitKey(1)

                    # 27 is the ASCII for the esc key on your keyboard.
                    if keyboard_input == 27:
                        break
        except KeyboardInterrupt:
            pass

        cv2.destroyAllWindows()

    def __del__(self):
        self.close()
