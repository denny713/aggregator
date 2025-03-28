import json
import time
from datetime import datetime

import requests


def scrape_tiktok(url_req, size):
    post_id = url_req.split('/')[-1]
    max_size = int(size) if size else 300
    url = 'https://www.tiktok.com/api/comment/list/?WebIdLastTime=1729273214&aid=1988&app_language=en&app_name=tiktok_web&aweme_id={}&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count={}&cursor=0&data_collection_enabled=false&device_id=7427171842932786693&device_platform=web_pc&focus_state=true&from_page=video&history_len=6&is_fullscreen=false&is_page_visible=true&odinId=7427171704705188869&os=windows&priority_region=&referer=&region=CA&screen_height=1080&screen_width=1920&tz_name=Asia%2FTehran&user_is_login=false&webcast_language=en&X-Bogus=DFSzswVYtfhANH-ltQ2xJbJ92U6T'.format(post_id, max_size)

    results = []
    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.6',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Brave";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'Cookie': 'tt_chain_token=foxC95TtnrTWDGHjipxlRA==; tt_csrf_token=6eI8pQcS-vPV_iuvRNRjfSFc_mTLAU1LtE-k; s_v_web_id=verify_m8s9937d_nE7nmjUe_v969_46WW_9XE1_OPIQB4QtLFjR; delay_guest_mode_vid=8; passport_csrf_token=c56e24bb847cd4cd5bfa5b472671bab8; passport_csrf_token_default=c56e24bb847cd4cd5bfa5b472671bab8; multi_sids=7432150019179070471%3A9b7172fa7d0097a950903d86b388c5e2; cmpl_token=AgQQAPOgF-RO0rcao7c6ph0-_UXUFNjMf5ArYNjW9g; passport_auth_status=e73738f85e39a2f41e9bedcc74fe7f33%2C; passport_auth_status_ss=e73738f85e39a2f41e9bedcc74fe7f33%2C; uid_tt=ae5f239b47ae080a2a5628506a4df6d067d5b92584dbf044ae64461e150fd4cc; uid_tt_ss=ae5f239b47ae080a2a5628506a4df6d067d5b92584dbf044ae64461e150fd4cc; sid_tt=9b7172fa7d0097a950903d86b388c5e2; sessionid=9b7172fa7d0097a950903d86b388c5e2; sessionid_ss=9b7172fa7d0097a950903d86b388c5e2; store-idc=alisg; store-country-code=id; store-country-code-src=uid; tt-target-idc=alisg; tt-target-idc-sign=O6LvptbVICTJlQekMOdsNuECUHbnPmL0Q6uSx1qnKf-izQSroNFjflelpW4fFKHRm2sW_tQfFcUD8xv9YO7pTA_R-Z9t2KApcHFsqRtQ6spmSyhthlRe13PRqipbYoJAri7Z-wSALTG1GsLTT5_BdanrmwHOQjb8g5AU3AWpV9JTFDX8glhiBl_dQjGlUV5Z04DtHOLcuRrZD5P4UpGXS3EBjp03IrdrbnBzeJpgUIBKm1QcConNHyH6Vn_In_zW9um_ix3zN7la0G6FEokur5LDD3CIUXcnVFDiVukpvJJXKC63lEeOuhosL9TI93Fbdd2Y2pVMFBDLvOOpPYMJsNGeWHnxLlAaeZUVS6rsIla_DMionQSPLBZsMQ7Jg7-AxNwIXVvzeYrF36rARcFJtN6gVqPmqY0FvF3E4Bm-QAvbrZAb6iJ9YAWP2R54Z0a7UpmcCvxYtpzsbcKGpFRnbEG9IaMNttnaNwOERMUPz6S4UR-06auQc9_dWJ9Ixud3; last_login_method=google; tiktok_webapp_theme_source=auto; tiktok_webapp_theme=dark; ttwid=1%7CEnqlhpLymsw2rjS7h8oL-bn0Y0_HQdmTeYRVBYWM400%7C1743145133%7C38d1363c27d3a2cdd07c91f8d45055118fe2e37483a8b8e64d65e99168be7077; sid_guard=9b7172fa7d0097a950903d86b388c5e2%7C1743145133%7C15551972%7CWed%2C+24-Sep-2025+06%3A58%3A25+GMT; sid_ucp_v1=1.0.0-KDhkYWFhZmVmOWI0Nzg0MjQ3NjhhNTI5ZGExOWNmZmVkMDk3MWJhMWYKGQiHiNOUi6KTkmcQrZGZvwYYsws4CEASSAQQAxoCbXkiIDliNzE3MmZhN2QwMDk3YTk1MDkwM2Q4NmIzODhjNWUy; ssid_ucp_v1=1.0.0-KDhkYWFhZmVmOWI0Nzg0MjQ3NjhhNTI5ZGExOWNmZmVkMDk3MWJhMWYKGQiHiNOUi6KTkmcQrZGZvwYYsws4CEASSAQQAxoCbXkiIDliNzE3MmZhN2QwMDk3YTk1MDkwM2Q4NmIzODhjNWUy; store-country-sign=MEIEDLjmejYY_8fQrfz6WQQguGR1828RlWnroJJSwf5-_EnK75F5Fo1SU2eZ5Lcr7sIEED2Ah4UK8soqxBuJ6_q9ddA; odin_tt=b3340a72db290fcbcc93afbae6d19ae1aeaac2438b346d823a20c508a97929027f962c8db1b7daf3f2e7ba6fe1853592a20c31f4eb57f791e02e723be25adf78df4a96c457197734f3c514a70eed9f65; perf_feed_cache={%22expireTimestamp%22:1743314400000%2C%22itemIds%22:[%227472979623673040134%22%2C%227482069987516091670%22%2C%227479010926151109893%22]}; msToken=yE1Ttc5XJ2ax-7XatKbb4PApZy69C6NLYODyTqS8_OcwXHku9zOIGvXIV2OeoPjdbpMkycj8wUmaFC_RloTHwIS6_oWCSBrhQcVht9IB1UbnZ9oGR9J-xuYRmYnGzjOqQHtXyQL0L0rGyLXTOSH9sc8=; passport_fe_beating_status=false; msToken=Cerfc00YX_2AiB5_8uIPW_k0YhbL381TzMFAkJnVt9iHuhnx4TOkJ8YWahk_TGjB4hPfGJu6EecpWDBva4psEyIE0RWKcGolO6K_a8BrJcJSD-FwWLxmP1gt2Y0mjvxnliXDArQZ-KmVligdrItjoBU=; msToken=Vn_3lIN_5Yj0oU0h_-HOqTdFJe5vGqBCgtOvnH4YfulLQLK7SwBCftTCcpK_88gSBSEMO1YzyDn0klCjeZzKAYhrqXT9vkZKY8ABsMX9wWbU03k3eLIloWrXXaqf9oT4OIUpAXZhevPUGZRiJqYkSFY='
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    comments = data['comments']
    for comment in comments:
        desc = comment['share_info']['desc']
        title = comment["share_info"]["title"]
        created_time = comment["create_time"]

        user = desc.split("’s comment:")[0]
        timestamp = datetime.utcfromtimestamp(created_time).strftime('%Y-%m-%d')
        content = f"{title.strip()} - {desc.split('comment: ')[1]}"

        results.append({
            'user': user,
            'timestamp': timestamp,
            'rating': '',
            'content': content,
            'preview': content
        })

    return results

# def scrape_tiktok(url_req, size):
#     post_id = url_req.split('/')[-1]
#     max_comment = int(size) if size else 300
#
#     headers = {
#         'accept': '*/*',
#         'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
#         'cache-control': 'no-cache',
#         'pragma': 'no-cache',
#         'priority': 'u=1, i',
#         'referer': 'https://www.tiktok.com/explore',
#         'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
#     }
#
#
#     results = []
#     idx = 0
#
#     while 1:
#         try:
#             if len(results) >= max_comment:
#                 print('Sudah mencapai batas jumlah komentar')
#                 break
#
#             url = f'https://www.tiktok.com/api/comment/list/?WebIdLastTime=1729273214&aid=1988&app_language=en&app_name=tiktok_web&aweme_id={post_id}&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=20&cursor={idx}&data_collection_enabled=false&device_id=7427171842932786693&device_platform=web_pc&focus_state=true&from_page=video&history_len=6&is_fullscreen=false&is_page_visible=true&odinId=7427171704705188869&os=windows&priority_region=&referer=&region=CA&screen_height=1080&screen_width=1920&tz_name=Asia%2FTehran&user_is_login=false&webcast_language=en'
#
#             response = session.get(url=url, headers=headers)
#             info = response.text
#             data = json.loads(info)
#             print(response)
#             comment = data['comments']
#             for cm in comment:
#                 print(json.dumps(cm, indent=4, ensure_ascii=False))
#                 desc = cm['share_info']['desc']
#                 title = cm["share_info"]["title"]
#                 created_time = cm["create_time"]
#
#                 user = desc.split("’s comment:")[0]
#                 timestamp = datetime.utcfromtimestamp(created_time).strftime('%Y-%m-%d')
#                 content = f"{title.strip()} - {desc.split('comment: ')[1]}"
#
#                 results.append({
#                     'user': user,
#                     'timestamp': timestamp,
#                     'rating': '',
#                     'content': content,
#                     'preview': content
#                 })
#
#                 if len(results) == max_comment:
#                     print('Sudah mencapai batas jumlah komentar')
#                     break
#
#             if not data.get("has_more", False):
#                 print("Tidak ada komentar tambahan")
#                 break
#
#             idx += 20
#             time.sleep(1)
#         except Exception as e:
#             print('Menemukan error: ' + str(e))
#             break
#
#     return results
