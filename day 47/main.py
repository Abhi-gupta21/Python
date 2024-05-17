import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get("https://www.amazon.com/Versace-Eros-EDP-EROS-PARFUM/dp/B08F5FMLCQ/ref=sr_1_29?crid=IFRC5X4BLWQ1&dib=eyJ2IjoiMSJ9.Ldqgr90aePanktAuKPKiPz0_yC9Bnen6Qc-3yGRv1Hy7Ca5hskmC3n4MN9_14Je44FIGPm6wPLwCzcrNr5dq0OLWtGVT4fb-PmrFGZSAzLthP5Y-iFHzIJ0cmx4rA3xPTsdDrmEscqb-35botHdKwVo6kLMwsWrWdAaFGc5yTlgjoOKxYMIvLjVsRBcnaoROK0cS7rM-Ztm3UTDzeoCfAQRNdHLk2ut1w6WgzT4KizOvMr7sAMC6nekPNBV7XJIFgc815UY8foWE2CngqXCUnpwWjP66ss8Mx__JTNkFeAE.xzG-kC_IF7qQcl1bYUXbZNDNlqvDQ-SYQKjGyqoRpjo&dib_tag=se&keywords=perfumes+for+men&qid=1713377323&sprefix=perfumes+for+men%2Caps%2C378&sr=8-29", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"})

html = response.text
soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-offscreen")
print(price)
