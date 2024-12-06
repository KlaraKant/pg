
import sys


jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length):
    
    with open(file_name, "rb") as file_name: 
        header_length = file_name.read(8) 

    return header_length


def is_jpeg(file_name):
    
   
    header = read_header(file_name, len(jpeg_header))

    if jpeg_header in header:  
        return True
    else:
        return False
  

def is_gif(file_name):
    
   
    header = read_header(file_name, len(gif_header1))
    if gif_header1 in header: 
        return True
    elif gif_header2 in header: 
        return True
    else:
        return False
    

def is_png(file_name):
   
    header = read_header(file_name, len(png_header))
    if png_header in header: 
        return True
    else:
        return False


def print_file_type(file_name):
    
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')


if __name__ == '__main__':
    
    try: 
        file_name = sys.argv[1]
        print_file_type(file_name)

    except FileNotFoundError:
        print(f'Soubor {sys.argv[1]} nenalezen.')

    except Exception:
        print("Byla vyvolána výjimka")

