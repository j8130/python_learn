# pip install pdfminer3k

from io import StringIO
# pdf 资源管理器 进程
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
# 文字转换
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams


pdf_file = open("F:\\000简历\\xxx简历\\xxx-简历.pdf", "rb")
rsrcmgr = PDFResourceManager()
retstr = StringIO()
laparams = LAParams()
device = TextConverter(rsrcmgr=rsrcmgr, outfp=retstr, laparams=laparams)
process_pdf(rsrcmgr=rsrcmgr, device=device, fp=pdf_file)
device.close()
content = retstr.getvalue()
retstr.close()
pdf_file.close()
print(content)
