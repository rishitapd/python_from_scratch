"""
upi id input
payment app url define
qrcode for each payment app
save qr code in system
display qrcode using pillow viewer

"""

import qrcode


#taking upi id as a input
upi_id=input("Enter your upi id: ").strip()

# Validate UPI ID (basic check)
if "@" not in upi_id:
    print("❌ Invalid UPI ID. It must contain '@'.")
    exit()

amount = input("Enter amount (optional): ").strip()
message = input("Enter message (optional): ").strip()
currency = "INR"
#upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE
#defining the payment url based on the upi id and payment app

phoneope_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create qrcode for each payment app
phoneope_qr=qrcode.make(phoneope_url)
paytm_qr=qrcode.make(paytm_url)
google_pay_qr=qrcode.make(google_pay_url)
#save qr code to image file (optional)
#phoneope_qr.save('phonepe_qr.png')
#paytm_qr.save('paytm_qr.png')
#google_pay_qr.save('google_pay_qr.png')

#display the qrcodes(install pillow lib)
show_each = input("Do you want to open each QR image individually? (y/n): ").strip().lower()
if show_each == "y":
    phoneope_qr.show()
    paytm_qr.show()
    google_pay_qr.show()

