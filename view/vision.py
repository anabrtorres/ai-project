import cv2

import threading




class Vision:
    def __init__(self, camera_id=0):
        self.camera = cv2.VideoCapture(camera_id)

        if not self.camera.isOpened():
            raise Exception("Erro ao abrir a câmera.")
        
        self.close_program = False

    
    def read_frame(self):
        ret, frame = self.camera.read()

        if ret:
            return frame
        else:
            print("Erro ao ler o quadro da câmera.")
            return None
    
    def save_image(self, filename):
        frame = self.read_frame()

        if frame is not None:
            cv2.imwrite(filename, frame)
            print(f"Imagem capturada e salva como {filename}")
        else:
            print("Não foi possível capturar a imagem.")
    
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
        cv2.namedWindow('Camera', cv2.WINDOW_NORMAL)

        try:
            while self.close_program is False:
                # Capturar um quadro da câmera
                frame = self.read_frame()
                if frame is not None:
                    cv2.imshow('Camera', frame)
                    
                    # Verifique se a tecla 'X' foi pressionada (maiúscula)
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord('X'):
                        # Capturar e salvar a imagem
                        self.capture_image('imagem_capturada.jpg')
                    elif key == ord('q'):
                        break
        except KeyboardInterrupt:
            pass
    
        cv2.destroyAllWindows()

    def __del__(self):
        self.close()

