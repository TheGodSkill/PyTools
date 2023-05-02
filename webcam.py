import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class WebcamTester:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        self.root = tk.Tk()
        self.root.title("Webcam Tester")

#It can take about 20 seconds for the program to open

        self.canvas = tk.Canvas(self.root, width=640, height=480)
        self.canvas.pack()

        self.btn_snapshot = tk.Button(self.root, text="Snapshot", command=self.take_snapshot)
        self.btn_snapshot.pack(fill="x")

        self.delay = 15
        self.update()

        self.root.mainloop()

    def update(self):
        ret, frame = self.cap.read()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.root.after(self.delay, self.update)

    def take_snapshot(self):
        ret, frame = self.cap.read()
        if ret:
            cv2.imwrite("snapshot.jpg", frame)

WebcamTester()
