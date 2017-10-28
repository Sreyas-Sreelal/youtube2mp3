from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import requests
from gui import app,youtube_screen,ui_youtube
from PyQt5 import QtWidgets
import traceback

def OnExceptSignal(exc_type, exc_value, tb):
    exce = traceback.format_exception(exc_type,exc_value,tb)
    print("[Error dude] "+str(exce))
    
sys.excepthook = OnExceptSignal

def download_file( url , filename):
    try:
        print(url)
        REQUEST_FTP_FILE = requests.get( url , stream = True )
        FILE_SIZE = int( REQUEST_FTP_FILE.headers.get( 'content-length' ) )
    except Exception as e:
        QtWidgets.QMessageBox.warning(youtube_screen,"NetWork error","Please check your internet connection",QtWidgets.QMessageBox.Ok)
        return False
    RECIEVED_STATUS = int( 0 )
    with open( filename , 'wb' ) as chunk_file:
        for buffer in REQUEST_FTP_FILE.iter_content( chunk_size = 1024 ):
            if buffer:
                RECIEVED_STATUS += len( buffer )
                chunk_file.write( buffer )
                done = int( 50 * ( RECIEVED_STATUS / FILE_SIZE ) )
                ui_youtube.progress.setValue(2*done)
    QtWidgets.QMessageBox.information(youtube_screen,"Converted succesfully","The youtube video  is converted to mp3 successfully",QtWidgets.QMessageBox.Ok)
    ui_youtube.progress.hide()
    ui_youtube.progress.setValue(0)
    ui_youtube.progress_label.hide()
    return True

def convert2mp3():
    ui_youtube.progress.show()
    ui_youtube.progress_label.show()
    video = ui_youtube.video_link_line_edit.text()
    id = video.find('?v=')+3
    if id == 2 :
        QtWidgets.QMessageBox.warning(youtube_screen,'Invalid youtube link','Please provide a valid youtube url',QtWidgets.QMessageBox.Ok)
        return False
    vid = video[id:id+11]
    driver = webdriver.PhantomJS('phantomjs.exe')
    driver.set_window_position(0, 0)
    driver.set_window_size(0, 0)
    payload = "http://api.convert2mp3.cc/?v="+ vid + "&f=mp3"
    driver.get(payload)
    elem = driver.find_element_by_class_name("videohref")
    link = elem.get_attribute('href')
    file_name = QtWidgets.QFileDialog.getSaveFileName(youtube_screen, 'Save Mp3', 'song',initialFilter='.mp3',filter='.mp3')
    if file_name:
        download_file(link,file_name[0]+file_name[1])
    driver.close()
    driver.quit()

ui_youtube.progress.hide()
ui_youtube.progress_label.hide()
ui_youtube.convert_button.clicked.connect(convert2mp3)
ui_youtube.video_link_line_edit.returnPressed.connect(convert2mp3)
youtube_screen.show()
sys.exit(app.exec_())

