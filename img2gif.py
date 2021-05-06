import imageio
import sys
import glob

sys.path.append('..')
import os
import cv2
from pathlib import Path
import numpy as np

FRAME_NPY_PATH = '/mnt/DATA/dataset/acapsol/mock/frames'
dest_folder_path = os.path.join('/mnt/DATA/dataset/acapsol/frames_npy/gifs')
os.makedirs(dest_folder_path, exist_ok=True)

video_ids = ['dSBFcvZy_IM', '6ZduCGreLJw', 'jePy_8rrLZg', 'tvawEAiiYP4', 'LjnG25VY4sw', 'tl_hgY-WGgE',
             'w5kkNA17I3U', '9lT5fbSeBIY', 'x_peJU531R4', 'm6LE4cVHw-E', '1UAXjz-HIoo', 'bZrOqLMEKB0',
             'ue8kacAWmOQ', 'iKR7pSr-g98', 'HnnPAwV_Ju0', '54sxqvQcwiY', 'lew-6GoLLFY', 'R4CK5u-FQMA',
             'h5vE2PgxeSs', 'YuEQFZo1tM8', '9U5JmgBuNaI', '7pLIBMk7w4k', 'zOHRPtwnMWY', 'CgwDCjqWCzc',
             'ZOjmYFysXfs', '_sQDUpJ9hrA', '7r-LYxzajF8', 'CYKSNoDkl8c', '_y0UkyPEOJI', 'QiWeDpXrmqE',
             'aBT49p_Wz5w', 'lHv-UycajJU', 'ah-osEK-ozg', 'UeVR8mXl328', 'HnnPAwV_Ju0', 'xutyn4HbVus',
             'eoiP57vIC3Q', 'Ar0-FckOgy4', 'pnOPhnoeW3E', 'hAMGCbjXs8w', 'ATgj3X43kYI', 'FGvWe3RSiEI',
             '3rxY9q2tKKo', 'LF6d-3xgy1A', 'Zj1s4CFKZYg', 'MUOEFcqI6TM', 'tl_hgY-WGgE', 'EyjymPNcdMY',
             '2ENDDmxOYlo', '8Sb5IvpztgQ', 'HhmF2w-39E8', 'njmHfgtgce8', 'xwx_Hdbi-z8', 'rCYpPFbrgME',
             'qHlhy3nan0M', 'fZ1xOfoEH1k', 'vgmIHHf5VTg', 'UPsnE752le8', 'v9NtsgLl9nk', 'wZgAIdcNQAE',
             'z7ODRzmKUlk', '8bS7PJPCKbc', 'aPpbYgSD1uE', 'ZRyF3B2f5o0', 'YYsUJ5xBbQg', '54sxqvQcwiY',
             'rMbw0fz2FmQ', 'ATgj3X43kYI', 'tl_hgY-WGgE', 'A-NBQs3i8uE', 'J6EFikgiqvg', '6AlIoubugNg',
             '3dDbBo6-EbA', 'MpIFXsSMPEI', '5aW4zK3g6gc', 'twi3re-rI9g', 'rvkCc_1NYXQ', 'IJznXxPMjpw',
             'L6ShSdW9HnA', 'T3skkQ0fhkg', 'pUwtEOdH4Z8', '1ZOwwNjXgOk', 'R4CK5u-FQMA', '1NSWruY65Hw',
             '8THDiRPAGCM', 'FThyItGeTcI', 'IXQUhWTIqqU', '50FA_Rhiv-M', 'iMqcZWLFtFg', '9Q7kyzuJCHc',
             'vnlLaxGQijE', 'eg8nMtd2s6E', 'cop8FimMdVA', '4zyqlcyBFXE', 'DSd65YR2dOU', 'pY2EQVHsx0c',
             'cPgSVAy7NYM', 'wYmYBiFFR4w', 'fOo7u9kGe7U', 'SBJgHwnoTRI', 'zxVNt_Tu6tM', 'HZ7S5JVarqQ',
             ]

for idx, video_id in enumerate(video_ids):
    dest_file_path = os.path.join(dest_folder_path, str(idx) + '.png')
    if glob.glob(dest_file_path):
        continue
    print('VIDEO_ID :' + video_id)
    input_file_path = list(Path(os.path.dirname(FRAME_NPY_PATH)).glob('samples/' + video_id + '*.mp4'))[
        0].as_posix()
    cap = cv2.VideoCapture(input_file_path)
    i = 0
    scale_percent = 60  # percent of original size
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        if i % 505 == 0:
            width = int(frame.shape[1] * scale_percent / 100)
            height = int(frame.shape[0] * scale_percent / 100)
            dim = (width, height)
            resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
            # resized = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
            cv2.imwrite(dest_file_path, resized)
            break
        i += 1
    cap.release()
    cv2.destroyAllWindows()
    print("Completed IMG2GIF operation.")
