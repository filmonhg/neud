'''
Class to download file
'''

import pytube
import ffmpeg
import tempfile
import os
from ftplib import FTP
import logging
import encodings.idna
class FtpUploadTracker:
    sizeWritten = 0
    totalSize = 0
    lastShownPercent = 0

    def __init__(self, totalSize):
        self.totalSize = totalSize

    def handle(self, block):
        self.sizeWritten += 1024
        percentComplete = round((self.sizeWritten / self.totalSize) * 100)

        if (self.lastShownPercent != percentComplete):
            self.lastShownPercent = percentComplete
            print(str(percentComplete) + " percent complete")


#def __init__(self,youtubelink):
#    self.youtube_link = youtubelink
def download(video_url='https://www.youtube.com/watch?v=tXOIvjbNhts'):
    print(f"start downloading {video_url}")
    logging.info(f"start downloading {video_url}")
    youtube = pytube.YouTube(video_url)
    download_video_name = youtube.title+".mp4"
    logging.info(f"video title for download : {download_video_name}")
    current_dir = os.getcwd()
    logging.info(f" current working dir: {current_dir} and filename : {download_video_name}")
    video = youtube.streams.first()
    #download_video_name = video.download('/tmp')  # path, where to video download.
    video.download(current_dir)  # path, where to video download.
    logging.info("Start converting .. ")
    print("Start converting .. ")
    try:
        xxx = (
            ffmpeg
            .input(os.path.join(current_dir,download_video_name))
            .output(youtube.title+'.mpeg',vcodec='mpeg2video')
            .overwrite_output()
            .run()
        )
    except Exception as e:
        print(f"Error converting : {e}")
        logging.error(e)

    #stream = ffmpeg.input(os.path.join(current_dir,download_video_name))
    output_filename = youtube.title+'.mpeg'
    logging.info(f"Output file name for conversion : {output_filename}")
    #stream = ffmpeg.output(stream,output_filename)
    #ffmpeg.run(stream,overwrite_output=True)
    full_path_output = os.path.join(current_dir,output_filename)
    sz=os.stat(full_path_output).st_size
    logging.info(f"Full output path for download: {full_path_output} and file size is : {sz}")
    upload_ftp(output_filename,full_path_output,sz)


def upload_ftp(input_file, full_path_output_file, file_size):
    upload_tracker = FtpUploadTracker(int(file_size))
    logging.info("Now uploading ... \n \n   .....")
    print("Now uploading ... \n \n   .....")
    ftp = FTP('ftp.stn.eu')
    ftp.login('eritrean_sattv', 'XBD%tgaev45gfqa')
    ftp.encoding='utf-8'
    try:
        #ftp.storbinary("STOR "+input_file, open(output_file, 'rb'), 1024, upload_tracker.handle)
        ftp.storbinary("STOR " + input_file , open(full_path_output_file, 'rb'), 1024, upload_tracker.handle)
    except Exception as e:
        logging.error(f"Exception occured {e}")
    finally:
        ftp.quit()


#download()
