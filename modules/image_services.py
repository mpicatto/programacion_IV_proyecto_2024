#aca hacemos la funcion que conecta con la camra y saca la foto 
import cv2
import tkinter as tk
from PIL import Image, ImageTk

def accesocam():
    #abre la camara, archivo: accederWebcam
    capture = cv2.VideoCapture(0)
    video_on = True
    while (video_on == True):
        ret, frame = capture.read()
        cv2.imshow('webCam',frame)
        

        if (cv2.waitKey(1) == ord('s')):
            break

    capture.release()
    cv2.destroyAllWindows()



#En lo que quede: HAY QUE LLAMAR CON LA CLASE CameraApp LAS FUNCIONES QUE ESTAN EN archivo foto EN LA FUNCION para sacar la foto y hacer que saque la foto apretando una tecla 


#archivo: foto (funciones para llamar en la principal)
class CameraApp:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        self.vid = cv2.VideoCapture(self.video_source)

        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        self.btn_snapshot = tk.Button(window, text="Capture", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)

        self.update()

        self.window.mainloop()

    def snapshot(self):
        ret, frame = self.vid.read()
        if ret:
            cv2.imwrite("captured_frame.png", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            print("Snapshot taken!")

    def update(self):
        ret, frame = self.vid.read()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(10, self.update)

def main():
    root = tk.Tk()
    app = CameraApp(root, "Camera App")
    
if __name__ == "__main__":
    main()
