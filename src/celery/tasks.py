from .celery import celery

import asyncio

from src.api.dependencies import regular_alert_service, worker_regular_alert_service, offer_service

from dotenv import load_dotenv
import os
from smtplib import SMTP_SSL
from email.mime.text import MIMEText

load_dotenv()

MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
MAIL_PORT = os.environ.get("MAIL_PORT")
MAIL_SERVER = os.environ.get("MAIL_SERVER")
MAIL_FROM = os.environ.get("MAIL_FROM")

def send_code_to_email_utils(send_to_emails: list, header: str, text: str, MAIL_USERNAME: str, MAIL_SERVER: str, MAIL_PORT: str, MAIL_PASSWORD: str) -> bool:
    try:
        msg = MIMEText(text, "html")
        msg['Subject'] = f'{header}'
        msg['From'] = f'MAIL_FROM <{MAIL_USERNAME}>'
        msg['To'] = ", ".join(send_to_emails)

        # Connect to the email server
        server = SMTP_SSL(MAIL_SERVER, MAIL_PORT)
        server.login(MAIL_USERNAME, MAIL_PASSWORD)

        # Send the email
        server.send_message(msg)

        server.quit()
        return True

    except Exception as e:
        print(e)
        return False
    

def msg_generator(offer_service):
    offer_service = asyncio.get_event_loop().run_until_complete(offer_service.get_entities())
    offer_service.reverse()
    count = 0
    if len(offer_service) > 5:
        count = 5
    else:
        count = len(offer_service)

    list_of_offers = ""

    for i in range(count):
        list_of_offers += f'''<!-- LIST ITEM -->
			<tr>
				<td align="left" valign="top" style="font-size: 17px; font-weight: 400; line-height: 160%; border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0;
					padding-top: 25px;
					color: #000000;
					font-family: sans-serif;" class="paragraph">
						<b style="color: #333333;">{offer_service[i].name}</b><br/>
						{offer_service[i].description}
				</td>

			</tr>
            <!-- LINE -->

            <tr>	
                <td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 6.25%; padding-right: 6.25%; width: 87.5%;
                    padding-top: 25px;" class="line"><hr
                    color="#E0E0E0" align="center" width="100%" size="1" noshade style="margin: 0; padding: 0;" />
                </td>
            </tr>'''
    
    text = '''<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8">
  	<meta name="viewport" content="width=device-width, initial-scale=1.0;">
 	<meta name="format-detection" content="telephone=no"/>

	<!-- Responsive Mobile-First Email Template by Konstantin Savchenko, 2015.
	https://github.com/konsav/email-templates/  -->

	<style>
/* Reset styles */ 
body { margin: 0; padding: 0; min-width: 100%; width: 100% !important; height: 100% !important;}
body, table, td, div, p, a { -webkit-font-smoothing: antialiased; text-size-adjust: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; line-height: 100%; }
table, td { mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-collapse: collapse !important; border-spacing: 0; }
img { border: 0; line-height: 100%; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; }
#outlook a { padding: 0; }
.ReadMsgBody { width: 100%; } .ExternalClass { width: 100%; }
.ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div { line-height: 100%; }

/* Rounded corners for advanced mail clients only */ 
@media all and (min-width: 560px) {
	.container { border-radius: 8px; -webkit-border-radius: 8px; -moz-border-radius: 8px; -khtml-border-radius: 8px;}
}

/* Set color for auto links (addresses, dates, etc.) */ 
a, a:hover {
	color: #127DB3;
}
.footer a, .footer a:hover {
	color: #999999;
}

 	</style>

	<!-- MESSAGE SUBJECT -->
	<title>New vacancies on our website!</title>

</head>

<!-- BODY -->
<!-- Set message background color (twice) and text color (twice) -->
<body topmargin="0" rightmargin="0" bottommargin="0" leftmargin="0" marginwidth="0" marginheight="0" width="100%" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; width: 100%; height: 100%; -webkit-font-smoothing: antialiased; text-size-adjust: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; line-height: 100%;
	background-color: #F0F0F0;
	color: #000000;"
	bgcolor="#F0F0F0"
	text="#000000">

<!-- SECTION / BACKGROUND -->
<!-- Set message background color one again -->
<table width="100%" align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; width: 100%;" class="background"><tr><td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0;"
	bgcolor="#F0F0F0">

<!-- WRAPPER -->
<!-- Set wrapper width (twice) -->
<table border="0" cellpadding="0" cellspacing="0" align="center"
	width="560" style="border-collapse: collapse; border-spacing: 0; padding: 0; width: inherit;
	max-width: 560px;" class="wrapper">

	<tr>
		<td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 6.25%; padding-right: 6.25%; width: 87.5%;
			padding-top: 20px;
			padding-bottom: 20px;">

			<!-- PREHEADER -->
			<!-- Set text color to background color -->
			<div style="display: none; visibility: hidden; overflow: hidden; opacity: 0; font-size: 1px; line-height: 1px; height: 0; max-height: 0; max-width: 0;
			color: #F0F0F0;" class="preheader">
				Available on&nbsp;GitHub and&nbsp;CodePen. Highly compatible. Designer friendly. More than 50%&nbsp;of&nbsp;total email opens occurred on&nbsp;a&nbsp;mobile device&nbsp;— a&nbsp;mobile-friendly design is&nbsp;a&nbsp;must for&nbsp;email campaigns.</div>

			<!-- LOGO -->
			<!-- Image text color should be opposite to background color. Set your url, image src, alt and title. Alt text should fit the image size. Real image size should be x2. URL format: http://domain.com/?utm_source={{Campaign-Source}}&utm_medium=email&utm_content=logo&utm_campaign={{Campaign-Name}} -->
			<a target="_blank" style="text-decoration: none;"
				href="https://github.com/konsav/email-templates/"><svg width="124" height="60" viewBox="0 0 124 60" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M45.5018 14.1941L57.2163 14.2062L60.8487 3.8935L64.4563 14.2136L76.1708 14.2257L66.6859 20.5918L70.2935 30.912L60.8239 24.5263L51.339 30.8925L54.9714 20.5798L45.5018 14.1941Z" fill="#22D13E" fill-opacity="0.7"/>
                    <path d="M57.0597 59.7686L39.6819 32.699L73.6879 32.2982L57.0597 59.7686Z" fill="#D46666" fill-opacity="0.7"/>
                    <rect x="63.1484" y="23.1771" width="19.0705" height="17.6588" fill="#6671D4" fill-opacity="0.7"/>
                    <ellipse cx="41.6942" cy="28.6955" rx="14.3028" ry="13.2441" fill="#6671D4" fill-opacity="0.7"/>
                    <path d="M20.2905 22.8547C20.3143 23.0215 20.3262 23.1763 20.3262 23.3191C20.3262 23.462 20.3262 23.6049 20.3262 23.7478V25.2124L20.1119 43.7525V44.1097C20.1119 44.2526 20.0761 44.467 20.0047 44.7528C19.9809 44.8718 19.9452 45.0028 19.8975 45.1457C19.8499 45.2648 19.8023 45.3958 19.7546 45.5387C19.6356 45.8244 19.4689 46.0388 19.2545 46.1817C19.064 46.3722 18.7544 46.5032 18.3257 46.5746C17.6589 46.7175 17.0516 46.658 16.5039 46.396C16.1943 46.2055 15.9799 45.9673 15.8609 45.6815C15.8132 45.6339 15.7656 45.5625 15.718 45.4672C15.718 45.4196 15.6942 45.3481 15.6465 45.2529C15.5989 45.1338 15.5632 45.0147 15.5394 44.8956C15.5156 44.7528 15.4917 44.6099 15.4679 44.467C15.4679 44.3479 15.456 44.2288 15.4322 44.1097C15.4322 43.9907 15.4203 43.8716 15.3965 43.7525C15.3488 43.6334 15.325 43.5382 15.325 43.4667C15.325 43.3715 15.325 43.2643 15.325 43.1452C15.3727 43.05 15.3965 42.8714 15.3965 42.6094L15.4322 39.7873L15.4679 35.2862H13.5389L6.28719 35.322L6.21575 43.7525V44.1097C6.21575 44.2526 6.18002 44.467 6.10858 44.7528C6.08476 44.8718 6.04904 45.0028 6.00141 45.1457C5.95378 45.2648 5.90615 45.3958 5.85852 45.5387C5.73944 45.8244 5.57274 46.0388 5.3584 46.1817C5.16788 46.3722 4.85828 46.5032 4.42961 46.5746C3.76279 46.7175 3.1555 46.658 2.60776 46.396C2.3696 46.2531 2.14336 46.015 1.92902 45.6815C1.88139 45.5863 1.85758 45.5148 1.85758 45.4672L1.75041 45.2529C1.70278 45.1338 1.66706 45.0147 1.64324 44.8956C1.61943 44.7528 1.59561 44.6099 1.5718 44.467C1.5718 44.3479 1.55989 44.2288 1.53608 44.1097C1.51226 43.9907 1.48845 43.8716 1.46463 43.7525C1.44081 43.562 1.44081 43.3596 1.46463 43.1452V42.6094L1.50035 39.7873L1.5718 34.5361C1.59561 33.774 1.60752 32.9881 1.60752 32.1784C1.60752 31.3687 1.60752 30.5351 1.60752 29.6778C1.58371 28.8204 1.5718 28.0584 1.5718 27.3915C1.59561 26.7247 1.63134 25.9745 1.67897 25.141V24.9981C1.70278 24.76 1.71469 24.5218 1.71469 24.2837C1.71469 24.0217 1.7266 23.7597 1.75041 23.4978C1.77423 23.2596 1.80995 23.0334 1.85758 22.819C1.92902 22.5809 2.02429 22.3427 2.14336 22.1046C2.21481 21.9141 2.31007 21.7593 2.42914 21.6402C2.54822 21.4973 2.69111 21.3663 2.85781 21.2472C3.23886 21.0567 3.6199 20.9614 4.00094 20.9614C4.19146 20.9614 4.35817 20.9734 4.50106 20.9972C4.64395 20.9972 4.78684 21.0091 4.92973 21.0329C5.21551 21.0567 5.48939 21.1996 5.75135 21.4616C5.94187 21.6283 6.07286 21.8188 6.1443 22.0331C6.26338 22.3427 6.33482 22.6166 6.35864 22.8547C6.38245 23.0215 6.39436 23.1763 6.39436 23.3191C6.39436 23.462 6.39436 23.6049 6.39436 23.7478V25.2124L6.32291 31.1067C6.51344 31.1067 6.72777 31.1067 6.96592 31.1067C7.22789 31.1067 7.52558 31.0948 7.85899 31.071C9.09738 31.071 10.3239 31.0829 11.5384 31.1067C12.7768 31.1305 14.0747 31.1424 15.4322 31.1424H15.4679C15.4679 30.0707 15.4679 29.0467 15.4679 28.0703C15.4917 27.0938 15.5275 26.0698 15.5751 24.9981C15.5751 24.76 15.5751 24.5218 15.5751 24.2837C15.5989 24.0217 15.6227 23.7597 15.6465 23.4978C15.6703 23.2596 15.7061 23.0334 15.7537 22.819C15.8251 22.5809 15.9204 22.3427 16.0395 22.1046C16.0871 21.9141 16.1705 21.7593 16.2895 21.6402C16.4324 21.4973 16.5991 21.3663 16.7897 21.2472C17.1231 21.0567 17.4922 20.9614 17.8971 20.9614C18.0876 20.9614 18.2543 20.9734 18.3972 20.9972C18.5639 20.9972 18.7068 21.0091 18.8259 21.0329C19.1593 21.0805 19.4331 21.2234 19.6475 21.4616C19.838 21.5806 19.969 21.7712 20.0404 22.0331C20.0881 22.176 20.1238 22.3189 20.1476 22.4618C20.1952 22.5809 20.2429 22.7119 20.2905 22.8547ZM35.5575 41.502C35.8432 41.4305 36.129 41.3829 36.4148 41.3591C36.7244 41.3353 36.9983 41.371 37.2364 41.4663C37.4984 41.5615 37.7127 41.7282 37.8794 41.9664C38.0461 42.1807 38.1295 42.4903 38.1295 42.8952C38.1295 43.181 38.058 43.4548 37.9152 43.7168C37.7723 43.9788 37.5937 44.2169 37.3793 44.4312C37.165 44.6456 36.9268 44.8361 36.6649 45.0028C36.4029 45.1457 36.1528 45.2648 35.9147 45.36C35.2241 45.6696 34.4262 45.9078 33.5213 46.0745C32.6401 46.2412 31.7232 46.3007 30.7706 46.2531C29.4846 46.2055 28.2462 45.9554 27.0555 45.5029C25.8885 45.0266 24.9716 44.2526 24.3048 43.181C23.6856 42.1331 23.3165 40.9661 23.1974 39.6801C23.0783 38.3941 23.1379 37.1795 23.376 36.0364C23.638 34.6551 24.0786 33.5358 24.6978 32.6785C25.3408 31.7973 26.1029 31.0948 26.984 30.5708C28.0557 29.9517 29.2584 29.6302 30.592 29.6063C31.9257 29.5825 33.1998 29.8445 34.4143 30.3922C35.224 30.7495 35.9504 31.2377 36.5934 31.8569C37.2364 32.4522 37.7246 33.1786 38.058 34.0359C38.1533 34.2503 38.2248 34.5123 38.2724 34.8218C38.3438 35.1314 38.3915 35.4649 38.4153 35.8221C38.4391 36.1555 38.4391 36.4889 38.4153 36.8223C38.3915 37.1557 38.3319 37.4534 38.2367 37.7154C38.0938 38.1441 37.9152 38.4775 37.7008 38.7156C37.4865 38.9538 37.2126 39.1324 36.8792 39.2515C36.5458 39.3705 36.1409 39.4539 35.6646 39.5015C35.2121 39.5253 34.6644 39.5491 34.0214 39.573C33.4498 39.5968 32.914 39.6087 32.4139 39.6087C31.9137 39.6087 31.4017 39.6087 30.8778 39.6087C30.3539 39.5849 29.8061 39.573 29.2345 39.573C28.6868 39.5491 28.0676 39.5253 27.377 39.5015C27.3055 39.9778 27.3651 40.3946 27.5556 40.7518C27.7699 41.0852 28.0557 41.371 28.4129 41.6092C28.7702 41.8235 29.175 41.9902 29.6275 42.1093C30.08 42.2284 30.5206 42.2998 30.9492 42.3236C31.7589 42.3712 32.5329 42.3117 33.2712 42.145C34.0095 41.9545 34.7716 41.7401 35.5575 41.502ZM34.0214 34.5718C33.5689 34.0479 33.0926 33.6668 32.5925 33.4287C32.2114 33.262 31.8066 33.1905 31.3779 33.2143C30.9731 33.2143 30.5801 33.2739 30.1991 33.3929C29.5084 33.5596 28.925 33.9169 28.4486 34.4646C28.401 34.5123 28.3177 34.6313 28.1986 34.8218C28.0795 34.9886 27.9604 35.1672 27.8414 35.3577C27.7461 35.5482 27.6747 35.7268 27.627 35.8935C27.5794 36.0602 27.6032 36.1436 27.6985 36.1436H34.7001C34.6763 35.8102 34.6168 35.5363 34.5215 35.322C34.4262 35.0838 34.2595 34.8338 34.0214 34.5718ZM46.8215 43.5382C46.7977 43.6573 46.7739 43.7763 46.7501 43.8954C46.7501 43.9907 46.7501 44.0978 46.7501 44.2169L46.5358 44.9671C46.4881 45.0623 46.4524 45.1219 46.4286 45.1457L46.3214 45.36C46.2024 45.622 45.988 45.8363 45.6784 46.003C45.1069 46.2888 44.4996 46.3603 43.8566 46.2174C43.4517 46.1698 43.1302 46.0507 42.8921 45.8602C42.6539 45.6935 42.4872 45.491 42.3919 45.2529C42.2967 45.0147 42.2252 44.7766 42.1776 44.5384C42.1062 44.3003 42.0704 44.0859 42.0704 43.8954V23.8907C42.0704 23.724 42.0704 23.5811 42.0704 23.462C42.0942 23.3191 42.1181 23.1882 42.1419 23.0691C42.1657 22.9024 42.1895 22.7595 42.2133 22.6404C42.261 22.5213 42.3086 22.3904 42.3562 22.2475C42.4277 22.0093 42.5586 21.8188 42.7492 21.6759C43.0349 21.4616 43.3088 21.3425 43.5708 21.3187C43.7375 21.271 43.8923 21.2472 44.0352 21.2472C44.1781 21.2234 44.3448 21.2115 44.5353 21.2115C44.8687 21.2115 45.2498 21.3068 45.6784 21.4973C46.0118 21.6878 46.25 21.9498 46.3929 22.2832C46.631 22.7595 46.7501 23.2001 46.7501 23.6049C46.7739 23.8431 46.7858 24.2003 46.7858 24.6766C46.8096 25.1529 46.8215 25.5101 46.8215 25.7483V25.8912C46.8692 26.6533 46.893 27.3915 46.893 28.106C46.893 28.7966 46.8811 29.5587 46.8573 30.3922C46.8573 31.2019 46.8454 31.9878 46.8215 32.7499C46.8215 33.4882 46.8215 34.2265 46.8215 34.9647V42.4665C46.8215 42.5618 46.8215 42.657 46.8215 42.7523C46.8454 42.8237 46.8573 42.9071 46.8573 43.0023C46.8573 43.2405 46.8454 43.4191 46.8215 43.5382ZM60.5151 30.3208C61.2057 30.6066 61.8368 31.0233 62.4084 31.5711C62.9799 32.095 63.4681 32.7023 63.873 33.3929C64.3017 34.0836 64.6232 34.8338 64.8375 35.6435C65.0757 36.4294 65.1947 37.2272 65.1947 38.0369C65.2185 39.2515 64.9328 40.3946 64.3374 41.4663C63.7658 42.5379 62.8251 43.3596 61.5153 43.9311C60.5151 44.336 59.4791 44.6456 58.4074 44.8599C57.3596 45.0504 56.2641 45.1814 55.1209 45.2529V51.7901C55.1209 51.933 55.0971 52.064 55.0495 52.1831C55.0257 52.3021 55.0138 52.4212 55.0138 52.5403C54.9661 52.7784 54.9066 52.9928 54.8351 53.1833C54.7875 53.3738 54.7161 53.5763 54.6208 53.7906C54.5256 53.9335 54.4303 54.0645 54.335 54.1835C54.2398 54.3026 54.1326 54.4217 54.0135 54.5408C53.442 54.8265 52.8466 54.8861 52.2274 54.7194C51.8464 54.6956 51.5368 54.5765 51.2986 54.3622C51.0843 54.1478 50.9295 53.9216 50.8342 53.6834C50.7389 53.4453 50.6556 53.1714 50.5842 52.8618C50.5603 52.7427 50.5365 52.6237 50.5127 52.5046C50.5127 52.4093 50.5127 52.3021 50.5127 52.1831V32.2855C50.5127 32.1426 50.5127 31.9998 50.5127 31.8569C50.5365 31.6902 50.5603 31.5235 50.5842 31.3567C50.608 31.071 50.6794 30.7852 50.7985 30.4994C51.0128 29.904 51.4534 29.4992 52.1202 29.2848C52.787 29.0705 53.5372 28.9752 54.3708 28.9991C54.9423 29.0229 55.5258 29.0824 56.1212 29.1777C56.7404 29.2729 57.3238 29.392 57.8716 29.5349C58.4431 29.654 58.9552 29.7849 59.4077 29.9278C59.8601 30.0707 60.2293 30.2017 60.5151 30.3208ZM60.5865 38.0369C60.6818 37.3701 60.5984 36.8104 60.3364 36.3579C60.0983 35.8816 59.753 35.5006 59.3005 35.2148C58.848 34.9052 58.3241 34.667 57.7287 34.5003C57.1571 34.3336 56.5856 34.2146 56.014 34.1431C55.9426 34.1193 55.8235 34.1074 55.6568 34.1074C55.5139 34.1074 55.3472 34.1074 55.1567 34.1074C55.1567 34.8695 55.1567 35.6077 55.1567 36.3222C55.1805 37.0128 55.1805 37.763 55.1567 38.5727V40.9661C55.7044 40.9423 56.276 40.8828 56.8713 40.7875C57.4905 40.6923 58.0621 40.5375 58.586 40.3231C59.11 40.1088 59.5505 39.823 59.9078 39.4658C60.2888 39.1086 60.5151 38.6323 60.5865 38.0369ZM87.3495 21.9974C87.5876 22.307 87.7067 22.6166 87.7067 22.9262C87.7305 23.0691 87.7305 23.2477 87.7067 23.462C87.7067 23.6764 87.6948 23.8431 87.671 23.9622C87.5995 24.2003 87.4328 24.4385 87.1709 24.6766C87.0994 24.7481 87.0161 24.8195 86.9208 24.8909C86.8256 24.9386 86.7065 24.9862 86.5636 25.0338C86.4207 25.0815 86.2778 25.1172 86.1349 25.141C85.992 25.141 85.8372 25.1529 85.6705 25.1767C85.5038 25.2005 85.349 25.2244 85.2061 25.2482C85.0632 25.2482 84.9084 25.2482 84.7417 25.2482H82.7055V25.8555C82.6817 27.9988 82.7174 30.1422 82.8127 32.2855C82.9318 34.4289 82.9199 36.5723 82.777 38.7156C82.7055 39.4301 82.5984 40.1683 82.4555 40.9304C82.3126 41.6687 82.0744 42.3712 81.741 43.0381C81.4314 43.6811 81.0147 44.2765 80.4907 44.8242C79.9668 45.3719 79.3 45.8006 78.4903 46.1102C77.7282 46.396 76.8946 46.5984 75.9897 46.7175C75.0847 46.8366 74.1678 46.8485 73.239 46.7532C72.3341 46.658 71.4648 46.4555 70.6313 46.1459C69.7977 45.8363 69.0952 45.4077 68.5236 44.8599C68.214 44.5741 67.9283 44.2288 67.6663 43.824C67.4043 43.3953 67.2257 42.9547 67.1304 42.5022C67.0352 42.0259 67.059 41.5734 67.2019 41.1448C67.3448 40.6923 67.6782 40.3231 68.2021 40.0374C68.6546 39.7754 69.0595 39.7159 69.4167 39.8587C69.7977 40.0016 70.155 40.2279 70.4884 40.5375C70.8456 40.8471 71.2028 41.1686 71.5601 41.502C71.9411 41.8354 72.3579 42.0497 72.8104 42.145C73.7868 42.3831 74.5846 42.3951 75.2038 42.1807C75.823 41.9426 76.3112 41.5734 76.6684 41.0733C77.0256 40.5732 77.2757 39.9659 77.4186 39.2515C77.5853 38.537 77.6805 37.8106 77.7044 37.0724C77.752 36.3341 77.7639 35.6197 77.7401 34.929C77.7163 34.2384 77.7163 33.6549 77.7401 33.1786C77.7639 31.9164 77.7639 30.678 77.7401 29.4634C77.7163 28.2489 77.7044 27.0105 77.7044 25.7483V25.6054C77.7282 25.5578 77.7401 25.4863 77.7401 25.3911H77.6329C77.49 25.3672 77.1923 25.3553 76.7398 25.3553C76.2874 25.3315 75.7992 25.3196 75.2752 25.3196C74.7513 25.3196 74.2512 25.3196 73.7749 25.3196C73.3224 25.2958 73.0247 25.2839 72.8818 25.2839H72.3817V25.2482C72.1912 25.2244 72.0006 25.1886 71.8101 25.141C71.6196 25.0934 71.4291 25.0457 71.2386 24.9981C70.7861 24.8552 70.4408 24.629 70.2026 24.3194C70.0835 24.2003 69.9883 24.0098 69.9168 23.7478C69.8692 23.4859 69.8454 23.2596 69.8454 23.0691C69.8454 22.95 69.8454 22.819 69.8454 22.6761C69.8454 22.5332 69.8692 22.4023 69.9168 22.2832C69.9644 22.0212 70.1312 21.7831 70.4169 21.5687C70.6075 21.4258 70.8337 21.3187 71.0957 21.2472C71.2624 21.1996 71.4291 21.1639 71.5958 21.1401C71.7625 21.1162 71.9411 21.0924 72.1316 21.0686C72.2983 21.0448 72.465 21.0329 72.6317 21.0329C72.7984 21.0329 72.9771 21.0329 73.1676 21.0329H76.597C76.7398 21.0329 76.9066 21.0329 77.0971 21.0329C77.2876 21.0329 77.5019 21.021 77.7401 20.9972C78.6689 20.9972 79.5858 20.9972 80.4907 20.9972C81.3957 20.9972 82.2769 21.0091 83.1342 21.0329H83.3485C83.6105 21.0329 83.8606 21.0448 84.0987 21.0686C84.3607 21.0686 84.6227 21.0686 84.8846 21.0686C85.4324 21.0924 85.9444 21.1996 86.4207 21.3901C86.8017 21.4854 87.1113 21.6878 87.3495 21.9974ZM92.6925 30.2493C93.4784 29.8683 94.3001 29.5944 95.1574 29.4277C96.0147 29.261 96.8602 29.2253 97.6937 29.3206C98.5511 29.4158 99.3727 29.6421 100.159 29.9993C100.968 30.3565 101.707 30.8566 102.373 31.4996C102.921 32.0474 103.397 32.7142 103.802 33.5001C104.207 34.2622 104.505 35.0124 104.695 35.7506C105.1 37.0605 105.16 38.3822 104.874 39.7159C104.588 41.0495 104.1 42.2879 103.409 43.431C103.076 43.9549 102.659 44.4312 102.159 44.8599C101.683 45.2648 101.171 45.5982 100.623 45.8602C99.9085 46.1936 99.1345 46.4198 98.301 46.5389C97.4675 46.6818 96.6578 46.7175 95.8719 46.6461C94.4429 46.5746 93.1807 46.2174 92.0853 45.5744C91.0136 44.9314 90.1443 44.1097 89.4775 43.1095C88.8345 42.1093 88.4058 40.9781 88.1915 39.7159C88.001 38.4298 88.0843 37.12 88.4415 35.7864C88.8226 34.3575 89.3703 33.2024 90.0848 32.3213C90.823 31.4163 91.6923 30.7256 92.6925 30.2493ZM93.7642 35.0362C93.407 35.3696 93.1331 35.7864 92.9426 36.2865C92.7521 36.7866 92.633 37.3105 92.5854 37.8583C92.5377 38.3822 92.5735 38.918 92.6925 39.4658C92.8354 39.9897 93.0498 40.466 93.3355 40.8947C93.5737 41.2519 94.0024 41.5496 94.6216 41.7878C95.2408 42.0259 95.8838 42.1688 96.5506 42.2164C97.3127 42.2641 97.9795 42.0616 98.5511 41.6092C99.1226 41.1329 99.5513 40.5494 99.8371 39.8587C100.147 39.1681 100.29 38.4179 100.266 37.6082C100.242 36.7985 100.028 36.0602 99.6227 35.3934C99.337 34.9171 98.9321 34.5718 98.4082 34.3575C97.908 34.1193 97.3722 34.0002 96.8006 34.0002C96.2529 33.9764 95.7051 34.0598 95.1574 34.2503C94.6097 34.417 94.1453 34.679 93.7642 35.0362ZM107.971 23.8193C108.018 22.9619 108.28 22.2713 108.757 21.7473C109.257 21.2234 109.959 21.0805 110.864 21.3187C111.293 21.4378 111.602 21.6164 111.793 21.8545C112.007 22.0927 112.15 22.3784 112.222 22.7119C112.317 23.0215 112.365 23.3668 112.365 23.7478C112.365 24.105 112.365 24.4623 112.365 24.8195V29.7492C112.341 29.9397 112.329 30.1303 112.329 30.3208C112.353 30.4875 112.365 30.6423 112.365 30.7852V31.2496H113.258C113.52 31.2496 113.77 31.2496 114.008 31.2496C114.27 31.2496 114.496 31.2377 114.687 31.2139C115.996 31.2139 117.116 31.4044 118.044 31.7854C118.997 32.1665 119.759 32.7023 120.331 33.3929C120.926 34.0598 121.355 34.8695 121.617 35.8221C121.903 36.7509 122.034 37.7749 122.01 38.8942C121.986 40.2279 121.772 41.371 121.367 42.3236C120.962 43.2762 120.39 44.0621 119.652 44.6813C118.914 45.3005 118.021 45.7649 116.973 46.0745C115.949 46.3603 114.794 46.5032 113.508 46.5032C112.031 46.5032 110.912 46.4913 110.15 46.4674C109.388 46.4436 108.84 46.2293 108.507 45.8244C108.197 45.4196 108.03 44.717 108.006 43.7168C107.983 42.7166 107.971 41.2519 107.971 39.3229C107.971 37.4653 107.971 35.6316 107.971 33.8216C107.994 32.0117 107.994 30.1898 107.971 28.356C107.971 28.1179 107.959 27.8678 107.935 27.6059C107.935 27.3439 107.935 27.0462 107.935 26.7128C107.935 26.3794 107.935 25.9864 107.935 25.5339C107.935 25.0576 107.947 24.4861 107.971 23.8193ZM114.651 42.5022C115.961 42.4308 116.866 42.0736 117.366 41.4305C117.628 41.0733 117.83 40.6446 117.973 40.1445C118.116 39.6444 118.175 39.1443 118.152 38.6442C118.128 38.1441 118.021 37.6678 117.83 37.2153C117.663 36.739 117.39 36.346 117.009 36.0364C116.675 35.7506 116.342 35.5482 116.008 35.4291C115.675 35.2862 115.33 35.2029 114.972 35.1791C114.615 35.1314 114.234 35.1195 113.829 35.1434C113.424 35.1434 112.96 35.1553 112.436 35.1791V39.4658L112.365 42.4308C112.603 42.4546 112.853 42.4784 113.115 42.5022C113.567 42.5499 114.079 42.5499 114.651 42.5022Z" fill="#3E49B9"/>
                    </svg>
                    </a>

		</td>
	</tr>

<!-- End of WRAPPER -->
</table>

<!-- WRAPPER / CONTEINER -->
<!-- Set conteiner background color -->
<table border="0" cellpadding="0" cellspacing="0" align="center"
	bgcolor="#FFFFFF"
	width="560" style="border-collapse: collapse; border-spacing: 0; padding: 0; width: inherit;
	max-width: 560px;" class="container">

	<!-- HEADER -->
	<!-- Set text color and font family ("sans-serif" or "Georgia, serif") -->
	<tr>
		<td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 6.25%; padding-right: 6.25%; width: 87.5%; font-size: 24px; font-weight: bold; line-height: 130%;
			padding-top: 25px;
			color: var(--primary1, #3E49B9);
			font-family: Clash Display;
            font-size: 28px;
            font-style: normal;
            font-weight: 600;
            line-height: normal;"
             class="header">
            New vacancies on the Help Job website!
		</td>
	</tr>
	

	<!-- LINE -->
	<!-- Set line color -->
	<tr>	
		<td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 6.25%; padding-right: 6.25%; width: 87.5%;
			padding-top: 25px;" class="line"><hr
			color="#E0E0E0" align="center" width="100%" size="1" noshade style="margin: 0; padding: 0;" />
		</td>
	</tr>

	<!-- LIST -->
	<tr>
		<td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 6.25%; padding-right: 6.25%;" class="list-item"><table align="center" border="0" cellspacing="0" cellpadding="0" style="width: inherit; margin: 0; padding: 0; border-collapse: collapse; border-spacing: 0;">
			''' + list_of_offers + '''
		</table></td>
	</tr>

    <!-- BUTTON -->
	<!-- Set button background color at TD, link/text color at A and TD, font family ("sans-serif" or "Georgia, serif") at TD. For verification codes add "letter-spacing: 5px;". Link format: http://domain.com/?utm_source={{Campaign-Source}}&utm_medium=email&utm_content={{Button-Name}}&utm_campaign={{Campaign-Name}} -->
	<tr>
		<td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 6.25%; padding-right: 6.25%; width: 87.5%;
			padding-top: 25px;
			padding-bottom: 5px;" class="button"><a
			href="#" target="_blank" style="text-decoration: underline;">
				<table border="0" cellpadding="0" cellspacing="0" align="center" style="max-width: 240px; min-width: 120px; border-collapse: collapse; border-spacing: 0; padding: 0;"><tr><td align="center" valign="middle" style="padding: 12px 24px; margin: 0; text-decoration: underline; border-collapse: collapse; border-spacing: 0; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px;"
					bgcolor="#3E49B9"><a target="_blank" style="
					color: #FFFFFF; font-family: sans-serif; font-size: 17px; font-weight: 400; line-height: 120%;"
					href="#">
						<b>SEE MORE<b>
					</a>
			</td></tr></table></a>
		</td>
	</tr>

	<!-- LINE -->
	<!-- Set line color -->
	<tr>
		<td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 6.25%; padding-right: 6.25%; width: 87.5%;
			padding-top: 25px;" class="line"><hr
			color="#E0E0E0" align="center" width="100%" size="1" noshade style="margin: 0; padding: 0;" />
		</td>
	</tr>

    

	<!-- PARAGRAPH -->
	<!-- Set text color and font family ("sans-serif" or "Georgia, serif"). Duplicate all text styles in links, including line-height -->
	<tr>
		<td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 6.25%; padding-right: 6.25%; width: 87.5%; font-size: 17px; font-weight: 400; line-height: 160%;
			padding-top: 20px;
			padding-bottom: 25px;
			color: #000000;
			font-family: sans-serif;" class="paragraph">
				Have a&nbsp;question? <a href="mailto:support@ourteam.com" target="_blank" style="color: #127DB3; font-family: sans-serif; font-size: 17px; font-weight: 400; line-height: 160%;">support@ourteam.com</a>
		</td>
	</tr>

<!-- End of WRAPPER -->
</table>

<!-- WRAPPER -->
<!-- Set wrapper width (twice) -->
<table border="0" cellpadding="0" cellspacing="0" align="center"
	width="560" style="border-collapse: collapse; border-spacing: 0; padding: 0; width: inherit;
	max-width: 560px;" class="wrapper">

	<!-- SOCIAL NETWORKS -->
	<!-- Image text color should be opposite to background color. Set your url, image src, alt and title. Alt text should fit the image size. Real image size should be x2 -->
	<tr>
		<td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 6.25%; padding-right: 6.25%; width: 87.5%;
			padding-top: 25px;" class="social-icons"><table
			width="256" border="0" cellpadding="0" cellspacing="0" align="center" style="border-collapse: collapse; border-spacing: 0; padding: 0;">
			<tr>

				<!-- ICON 1 -->
				<td align="center" valign="middle" style="margin: 0; padding: 0; padding-left: 10px; padding-right: 10px; border-collapse: collapse; border-spacing: 0;"><a target="_blank"
					href="https://raw.githubusercontent.com/konsav/email-templates/"
				style="text-decoration: none;"><img border="0" vspace="0" hspace="0" style="padding: 0; margin: 0; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border: none; display: inline-block;
					color: #000000;"
					alt="F" title="Facebook"
					width="44" height="44"
					src="https://raw.githubusercontent.com/konsav/email-templates/master/images/social-icons/facebook.png"></a></td>

				<!-- ICON 2 -->
				<td align="center" valign="middle" style="margin: 0; padding: 0; padding-left: 10px; padding-right: 10px; border-collapse: collapse; border-spacing: 0;"><a target="_blank"
					href="https://raw.githubusercontent.com/konsav/email-templates/"
				style="text-decoration: none;"><img border="0" vspace="0" hspace="0" style="padding: 0; margin: 0; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border: none; display: inline-block;
					color: #000000;"
					alt="T" title="Twitter"
					width="44" height="44"
					src="https://raw.githubusercontent.com/konsav/email-templates/master/images/social-icons/twitter.png"></a></td>				

				<!-- ICON 3 -->
				<td align="center" valign="middle" style="margin: 0; padding: 0; padding-left: 10px; padding-right: 10px; border-collapse: collapse; border-spacing: 0;"><a target="_blank"
					href="https://raw.githubusercontent.com/konsav/email-templates/"
				style="text-decoration: none;"><img border="0" vspace="0" hspace="0" style="padding: 0; margin: 0; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border: none; display: inline-block;
					color: #000000;"
					alt="G" title="Google Plus"
					width="44" height="44"
					src="https://raw.githubusercontent.com/konsav/email-templates/master/images/social-icons/googleplus.png"></a></td>		

				<!-- ICON 4 -->
				<td align="center" valign="middle" style="margin: 0; padding: 0; padding-left: 10px; padding-right: 10px; border-collapse: collapse; border-spacing: 0;"><a target="_blank"
					href="https://raw.githubusercontent.com/konsav/email-templates/"
				style="text-decoration: none;"><img border="0" vspace="0" hspace="0" style="padding: 0; margin: 0; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border: none; display: inline-block;
					color: #000000;"
					alt="I" title="Instagram"
					width="44" height="44"
					src="https://raw.githubusercontent.com/konsav/email-templates/master/images/social-icons/instagram.png"></a></td>

			</tr>
			</table>
		</td>
	</tr>

	<!-- FOOTER -->
	<!-- Set text color and font family ("sans-serif" or "Georgia, serif"). Duplicate all text styles in links, including line-height -->
	<tr>
		<td align="center" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 6.25%; padding-right: 6.25%; width: 87.5%; font-size: 13px; font-weight: 400; line-height: 150%;
			padding-top: 20px;
			padding-bottom: 20px;
			color: #999999;
			font-family: sans-serif;" class="footer">

				This email template was sent to&nbsp;you becouse we&nbsp;want to&nbsp;make the&nbsp;world a&nbsp;better place. You&nbsp;could change your <a href="https://github.com/konsav/email-templates/" target="_blank" style="text-decoration: underline; color: #999999; font-family: sans-serif; font-size: 13px; font-weight: 400; line-height: 150%;">subscription settings</a> anytime.

				<!-- ANALYTICS -->
				<!-- http://www.google-analytics.com/collect?v=1&tid={{UA-Tracking-ID}}&cid={{Client-ID}}&t=event&ec=email&ea=open&cs={{Campaign-Source}}&cm=email&cn={{Campaign-Name}} -->
				<img width="1" height="1" border="0" vspace="0" hspace="0" style="margin: 0; padding: 0; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border: none; display: block;"
				src="https://raw.githubusercontent.com/konsav/email-templates/master/images/tracker.png" />

		</td>
	</tr>

<!-- End of WRAPPER -->
</table>

<!-- End of SECTION / BACKGROUND -->
</td></tr></table>

</body>
</html>'''
    return text

@celery.task
def regular_alert_weekly():
    regular_alert = asyncio.get_event_loop().run_until_complete(regular_alert_service().get_entities())
    emails = [rec.email for rec in regular_alert if rec.period == "weekly"]

    send_code_to_email_utils(emails, "Help Job: New vacancies!", msg_generator(offer_service()), MAIL_USERNAME, MAIL_SERVER, MAIL_PORT, MAIL_PASSWORD)
    return emails


@celery.task
def regular_alert_daily():
    regular_alert = asyncio.get_event_loop().run_until_complete(regular_alert_service().get_entities())
    emails = [rec.email for rec in regular_alert if rec.period == "daily"]
    worker_regular_alert = asyncio.get_event_loop().run_until_complete(worker_regular_alert_service().get_entities())
    emails.extend([rec.user['email'] for rec in worker_regular_alert])

    send_code_to_email_utils(emails, "Help Job: New vacancies!", msg_generator(offer_service()), MAIL_USERNAME, MAIL_SERVER, MAIL_PORT, MAIL_PASSWORD)

    return emails