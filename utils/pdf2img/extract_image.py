import datetime
import os
import fitz

def pyMuPDF_fitz(pdfPath, imagePath,pdf_index):
    startTime_pdf2img = datetime.datetime.now()  # 开始时间
    print("imagePath=" + imagePath)
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        # page.get_pixmap() # int(width) int(length) alpha=False dpi=96
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96 (此处需要调节1-2之间)
        zoom_x = 1  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1
        # 提升分辨率
        # zoom factor in each dimension
        mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
        # apply zoomed matrix to image
        pix = page.getPixmap(matrix=mat, alpha=False, dpi=326)
        # pix = page.get_images(mat)
        # pix = page.get_images()


        if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
            os.makedirs(imagePath)  # 若图片文件夹不存在就创建
        pix.save(imagePath + '/' + '{}_images_{}.png'.format(pdf_index,pg))  # 将图片写入指定的文件夹内

    endTime_pdf2img = datetime.datetime.now()  # 结束时间
    print('pdf2img时间=', (endTime_pdf2img - startTime_pdf2img).seconds)



def pdf_to_img(pdf_root_path,img_root_path):
    """

    Args:
        pdf_root_path: pdf root file3 path
        img_root_path: img from pdf to save path

    Returns: img_root_path

    """

    # 1、PDF地址
    filenames = os.listdir(pdf_root_path)
    pdf_paths = [os.path.join(pdf_root_path, filename) for filename in filenames]
    print(pdf_paths)

    # 2、需要储存图片的目录
    image_root_path = img_root_path
    print(len(os.listdir(image_root_path)))
    for pdf_index,pdf_path in enumerate(pdf_paths):
        # print(pdf_path)
        # pdf_index = pdf_path.split('/')[-1][:2]
        pyMuPDF_fitz(pdf_path, image_root_path, str(pdf_index).zfill(4))

    print('pdf to img all ok.')
    return img_root_path


def get_pdf_names(pdf_root_path):
    """

    Args:
        pdf_root_path:

    Returns:

    """
    filenames = os.listdir(pdf_root_path)
    return  filenames

def get_pdf_paths(pdf_root_path):
    """

    Args:
        pdf_root_path:

    Returns:

    """
    filenames = os.listdir(pdf_root_path)
    pdf_paths = [os.path.join(pdf_root_path, filename) for filename in filenames]
    return pdf_paths

def get_pdf_pages(pdf_path):
    """

    Args:
        pdf_path:

    Returns:

    """
    pdf_doc = fitz.open(pdf_path)
    pdf_pages = int(pdf_doc.pageCount)
    return pdf_pages









# if __name__ == "__main__":
#
#     # 1、PDF地址
#     # pdfPath = './pdf/more_diagrams.pdf'
#     pdf_root_path = './data/pdfs/'
#     filenames = os.listdir(pdf_root_path)
#     pdf_paths = [os.path.join(pdf_root_path,filename) for filename in filenames]
#     print(pdf_paths)
#
#     # 2、需要储存图片的目录
#     image_root_path= './data/pdf_to_image_326/'
#     print(len(os.listdir(image_root_path)))
#
#
#     for pdf_path in pdf_paths:
#         print(pdf_path)
#         pdf_index = pdf_path.split('/')[-1][:2]
#         pyMuPDF_fitz(pdf_path, image_root_path,str(pdf_index).zfill(4))
#
#     print('all ok.')
