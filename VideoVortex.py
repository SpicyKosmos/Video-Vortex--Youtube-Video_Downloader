from pytube import YouTube
from notifypy import Notify
from tkinter import *

master =Tk()
master.title("Video Vortex")
master.resizable(height=False,width=False)
master.iconbitmap("app_pic.ico")

canvas= Canvas(master, height=300,width=600)

canvas.pack()

program_adı_etiket = Label(master,text="VideoVortex",bg="dark blue",font="Verdana 32 bold",fg="white",)
program_adı_etiket.place(relx=0.25,rely=0.1)

frame_main=Frame(master,bg="orange")
frame_main.place(relx=0.20,rely=0.45, relheight=0.18,relwidth=0.60)

url_bar= Text(frame_main,height=1,width=40,font="Verdana 12 bold")
url_bar.pack(pady=15,padx=15)

video_url_lbl= Label(master,text="Video URL",font="Verdana 12 bold")
video_url_lbl.place(relx=0.02,rely=0.50)

noti = Notify(default_notification_icon="app_pic.png",
              default_notification_application_name = "VideoVortex")




def video_dw():

    try:
        url=url_bar.get("1.0", "end-1c")
        path="Downloads"
        yt= YouTube(url)
        yr= yt.streams.get_highest_resolution()
        yr.download(output_path=path)

        #İndirilen videonun kullanıcıya bildirilmesi
        noti.title = "İndirme Tamamlandı"
        noti.message = f"{yt.title}\n{path} klasörüne kaydedildi"
        noti.send()
    except:
        noti.title = "İndirme Hatası"
        noti.message = "Video indirilirken bir hata oluştu lütfen tekrar deneyin"
        noti.send()



fonksiyon_bar=Button(master,text="indir",height=2,width=10,command=video_dw,font=('Helvetica 10 bold'))
fonksiyon_bar.place(rely=0.48,relx=0.82)

master.mainloop()

