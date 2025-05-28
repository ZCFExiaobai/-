from requests_html import HTMLSession
from lxml import etree
import requests
import csv
import time
f = open('zhengzhou.csv.csv', mode='a', encoding='utf-8-sig', newline='')
csv.writer = csv.writer(f)
csv.writer.writerow(['名称',
                     '房间数',
                     '层数',
                     '大小',
                     '小区',
                     '区域',
                     '价格',
                     '单价',
                     '建造时间',
                     '特色介绍',
                     '朝向',])
for page in range(1, 100):
    print(f'==正在爬取{page}页==')
    cookies = {
        'aQQ_ajkguid': '5092DA41-92F5-7F78-8880-E2FE8E15CFC7',
        '58tj_uuid': '7c63475f-57e0-461b-8a3e-6800669d07a8',
        'new_uv': '1',
        'id58': 'OVbA5mexa4sb3jJCRXBdAg==',
        '_ga': 'GA1.2.358203394.1739680652',
        'als': '0',
        '_ga_DYBJHZFBX2': 'GS1.2.1739680652.1.0.1739680652.0.0.0',
        'ajk-appVersion': '',
        'xxzlclientid': 'b1a423b0-3285-4385-b392-1732525663312',
        'xxzlxxid': 'pfmxK9y97n5u8l8lDuvaQcop8KdCWZHofxuoRG/FYwDzq1XRQYg5kQeKtnZz+UdMbcu0',
        'seo_source_type': '0',
        'fzq_h': '12d81769c1b5aabfdee606762bc79e1c_1740637121158_633412ca02cb49e1a0d61f534da496b2_47896428588575479773168917644802524118',
        'ctid': '26',
        'sessid': 'BB7F0642-0562-3804-F0CC-E2627E95FB78',
        'twe': '2',
        'fzq_js_anjuke_ershoufang_pc': '1bc35d3dd83a49bc02030d23aef7c065_1740699232878_23',
        'obtain_by': '1',
        'xxzlbbid': 'pfmbM3wxMDM0NnwxLjEwLjB8MTc0MDY5OTIzNDEzNDMwNDE1NXxaMWkyb3Nxa2MrU1dKcmNyNWF2UGJrRmJZdzE2Z2Z5SWFjTGdsQUo4cTVNPXw5MmFlYjUxNDZjMmIzYThiMzMxM2VhNGRhOTNhMmU4MF8xNzQwNjk5MjMyNjM4XzUwNzQyYTA1YWY4ZDQxNDA5NDM0ODM0ZTZmODU5MjNmXzQ3ODk2NDI4NTg4NTA3ODc2MTE5NDI0OTM1MTM0MjM0MzM4ODQ3fDdkODJiNzI2MDI0YWE2NDNjZGUzNDMwM2FlZmE5MWU5XzE3NDA2OTkyMzM0NDJfMjU0',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://zhengzhou.anjuke.com/sale/jinshui/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': 'aQQ_ajkguid=5092DA41-92F5-7F78-8880-E2FE8E15CFC7; 58tj_uuid=7c63475f-57e0-461b-8a3e-6800669d07a8; new_uv=1; id58=OVbA5mexa4sb3jJCRXBdAg==; _ga=GA1.2.358203394.1739680652; als=0; _ga_DYBJHZFBX2=GS1.2.1739680652.1.0.1739680652.0.0.0; ajk-appVersion=; xxzlclientid=b1a423b0-3285-4385-b392-1732525663312; xxzlxxid=pfmxK9y97n5u8l8lDuvaQcop8KdCWZHofxuoRG/FYwDzq1XRQYg5kQeKtnZz+UdMbcu0; seo_source_type=0; fzq_h=12d81769c1b5aabfdee606762bc79e1c_1740637121158_633412ca02cb49e1a0d61f534da496b2_47896428588575479773168917644802524118; ctid=26; sessid=BB7F0642-0562-3804-F0CC-E2627E95FB78; twe=2; fzq_js_anjuke_ershoufang_pc=1bc35d3dd83a49bc02030d23aef7c065_1740699232878_23; obtain_by=1; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjB8MTc0MDY5OTIzNDEzNDMwNDE1NXxaMWkyb3Nxa2MrU1dKcmNyNWF2UGJrRmJZdzE2Z2Z5SWFjTGdsQUo4cTVNPXw5MmFlYjUxNDZjMmIzYThiMzMxM2VhNGRhOTNhMmU4MF8xNzQwNjk5MjMyNjM4XzUwNzQyYTA1YWY4ZDQxNDA5NDM0ODM0ZTZmODU5MjNmXzQ3ODk2NDI4NTg4NTA3ODc2MTE5NDI0OTM1MTM0MjM0MzM4ODQ3fDdkODJiNzI2MDI0YWE2NDNjZGUzNDMwM2FlZmE5MWU5XzE3NDA2OTkyMzM0NDJfMjU0',
    }
    cookies = {
        'aQQ_ajkguid': '5092DA41-92F5-7F78-8880-E2FE8E15CFC7',
        '58tj_uuid': '7c63475f-57e0-461b-8a3e-6800669d07a8',
        'new_uv': '1',
        'id58': 'OVbA5mexa4sb3jJCRXBdAg==',
        '_ga': 'GA1.2.358203394.1739680652',
        'als': '0',
        '_ga_DYBJHZFBX2': 'GS1.2.1739680652.1.0.1739680652.0.0.0',
        'ajk-appVersion': '',
        'xxzlclientid': 'b1a423b0-3285-4385-b392-1732525663312',
        'xxzlxxid': 'pfmxK9y97n5u8l8lDuvaQcop8KdCWZHofxuoRG/FYwDzq1XRQYg5kQeKtnZz+UdMbcu0',
        'seo_source_type': '0',
        'fzq_h': '12d81769c1b5aabfdee606762bc79e1c_1740637121158_633412ca02cb49e1a0d61f534da496b2_47896428588575479773168917644802524118',
        'ctid': '26',
        'sessid': 'BB7F0642-0562-3804-F0CC-E2627E95FB78',
        'twe': '2',
        'fzq_js_anjuke_ershoufang_pc': 'bceafb50f5cdafa87ab3f2fa753099c7_1740699929117_23',
        'obtain_by': '1',
        'xxzlbbid': 'pfmbM3wxMDM0NnwxLjEwLjB8MTc0MDY5OTkzMDgxMzc2NjE0OHxka2xCL01kd2Z4TDE2QytPeHN0NnlVSTdUWStKbnZ1RzlQUzllclJJd0FVPXwzODRiOWY5YzRiMzFkN2Q3ZDZjNjVhZjgxYTQ1MmZhYV8xNzQwNjk5OTI5MDkyX2RkYjRlODMzYjllNzRlOThiMjEyNTc1NmViMWQ0MWRhXzQ3ODk2NDI4NTg4NTA3ODc2MTE5NDI0OTM1MTM0MjM0MzM4ODQ3fDczNGExZTJlOTE0MTJmZWM5ZTBjMTZmZGFkYjE5ZTE4XzE3NDA2OTk5Mjk3MjZfMjU1',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://zhengzhou.anjuke.com/sale/erqic/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': 'aQQ_ajkguid=5092DA41-92F5-7F78-8880-E2FE8E15CFC7; 58tj_uuid=7c63475f-57e0-461b-8a3e-6800669d07a8; new_uv=1; id58=OVbA5mexa4sb3jJCRXBdAg==; _ga=GA1.2.358203394.1739680652; als=0; _ga_DYBJHZFBX2=GS1.2.1739680652.1.0.1739680652.0.0.0; ajk-appVersion=; xxzlclientid=b1a423b0-3285-4385-b392-1732525663312; xxzlxxid=pfmxK9y97n5u8l8lDuvaQcop8KdCWZHofxuoRG/FYwDzq1XRQYg5kQeKtnZz+UdMbcu0; seo_source_type=0; fzq_h=12d81769c1b5aabfdee606762bc79e1c_1740637121158_633412ca02cb49e1a0d61f534da496b2_47896428588575479773168917644802524118; ctid=26; sessid=BB7F0642-0562-3804-F0CC-E2627E95FB78; twe=2; fzq_js_anjuke_ershoufang_pc=bceafb50f5cdafa87ab3f2fa753099c7_1740699929117_23; obtain_by=1; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjB8MTc0MDY5OTkzMDgxMzc2NjE0OHxka2xCL01kd2Z4TDE2QytPeHN0NnlVSTdUWStKbnZ1RzlQUzllclJJd0FVPXwzODRiOWY5YzRiMzFkN2Q3ZDZjNjVhZjgxYTQ1MmZhYV8xNzQwNjk5OTI5MDkyX2RkYjRlODMzYjllNzRlOThiMjEyNTc1NmViMWQ0MWRhXzQ3ODk2NDI4NTg4NTA3ODc2MTE5NDI0OTM1MTM0MjM0MzM4ODQ3fDczNGExZTJlOTE0MTJmZWM5ZTBjMTZmZGFkYjE5ZTE4XzE3NDA2OTk5Mjk3MjZfMjU1',
    }

    response = requests.get('https://zhengzhou.anjuke.com/sale/erqic/p{page}/', cookies=cookies, headers=headers)
    tree = etree.HTML(response.text)
    for div in tree.xpath('//section[@class="list"]/div'):
        title = div.xpath('.//a/div[2]/div[1]/div[1]/h3/text()')[0] #标签
        shi = div.xpath('.//a/div[2]/div[1]/section/div[1]/p/span/text()')#标签
        cun = div.xpath('.//a/div[2]/div[1]/section/div[2]/p[1]/text()')[0] #标签
        cushu = div.xpath('.//a/div[2]/div/section/div/p[4]/text()') #层数
        dx = div.xpath('.//a/div[2]/div[1]/section/div[1]/p[2]/text()')[0].replace('\n', '').replace(' ', '') #层数
        time = div.xpath('.//a/div[2]/div/section/div/p[5]/text()') #建筑时间
        tsjs = div.xpath('.//a/div[2]/div/section/div[3]/span/text()') #建筑时间
        qu = div.xpath('.//a/div[2]/div[1]/section/div[2]/p[2]/span[1]/text()')[0] #标签
        jg = div.xpath('.//a/div[2]/div[2]/p/span/text()')[0] + '万' #标签
        dj = div.xpath('.//a/div[2]/div[2]/p[2]/text()')[0].replace('\n', '').replace(' ', '') #标签
        cx = div.xpath('.//a/div[2]/div/section/div[3]/span/text()')[0]#朝向
        if cushu !=[] and time !=[]:
            cushu = div.xpath('.//a/div[2]/div/section/div/p[4]/text()')[0].replace('\n', '').replace(' ', '')  # 层数
            time = div.xpath('.//a/div[2]/div/section/div/p[5]/text()')[0].replace('\n', '').replace(' ', '')  # 建筑时间
            dict = {
            '名称' : title,
            '房间数' : shi,
            '层数' : cushu,
            '大小' : dx,
            '小区' : cun,
            '区域' : qu,
            '价格' : jg,
            '单价' : dj,
            '建造时间' : time,
            '特色介绍' : tsjs,
            '朝向' : cx,
            }
            print(dict)
            csv.writer.writerow([title, shi, cushu, dx, cun, qu, jg, dj, time, tsjs, cx,])