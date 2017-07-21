
import datetime as dt
import pathlib
import exifread

def make_image_exif_name(path,note='iPY'):
    if not isinstance(path,pathlib.Path):
        path=pathlib.Path(path)
    with open(path,'rb') as fh:
        tags = exifread.process_file(fh)

    tokens={}
    tokens['DatetimeOriginal'] = dt.datetime.strptime(tags['EXIF DateTimeOriginal'].values, '%Y:%m:%d %H:%M:%S')

    try:
        tokens['SubSecTimeOriginal']= int( tags['EXIF SubSecTimeOriginal'].values )
    except KeyError:
        tokens['SubSecTimeOriginal'] = 0
    tokens['note'] = note
    tokens['stem'] = path.stem
    tokens['suffixes'] = path.suffixes
    name = "{0:}_{1:}{2:03d}_{3:}__{4:}{5:}".format( tokens['DatetimeOriginal'].strftime("%Y%m%d"),
                                                    tokens['DatetimeOriginal'].strftime("%H%M%S"),
                                                    tokens['SubSecTimeOriginal'],
                                                    tokens['note'],
                                                    tokens['stem'],
                                                    "".join(tokens['suffixes']))

    return tokens, name

if __name__=="__main__":
    pass

    tokens, name = make_image_exif_name(path=r"E:\U_David\OneDrive\Pictures\New folder\20170705_005119067_iOS.jpg")
    print(tokens)
    print(name)
    tokens, name = make_image_exif_name(path=r"E:\U_David\Media\Pictures\2017\0704_Alaska\RX100\images\New folder\DSC02482.jpg")
    print(tokens)
    print(name)
