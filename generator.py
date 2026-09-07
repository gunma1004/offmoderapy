import os

DOMAIN = "https://offmoderapy.netlify.app"
NAVER_VERIFICATION = "a0e02e4f2dcaf270179e713519c690fbe449e8c5"

PARTNER_SHOPS = [
    {"name": "퀸즈홈테라피", "tel": "0507-1280-3296", "desc": "프리미엄 맞춤 홈케어 및 스웨디시 전문"},
    {"name": "한국골든테라피", "tel": "0507-1280-3360", "desc": "정통 힐링 아로마 및 전신 관리"},
    {"name": "한국미인테라피", "tel": "0507-1280-3201", "desc": "편안하고 아늑한 1:1 맞춤 케어"},
    {"name": "오늘밤테라피", "tel": "0507-1280-3199", "desc": "24시 신속 방문 및 피로 회복 전문"},
    {"name": "주주테라피", "tel": "0507-1280-3197", "desc": "감성 힐링 및 전문 테라피 복합 코스"}
]

def make_html(title, depth, links_html=""):
    prefix = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="naver-site-verification" content="{NAVER_VERIFICATION}" />
    <title>{title} | 오프모드건마사랑</title>
    <meta name="description" content="{title} 지역 전문 제휴업체 정보. 30분 내 방문, 아로마 및 스웨디시 100% 후불제 안심 케어.">
    <meta property="og:type" content="website">
    <meta property="og:title" content="{title} | 오프모드건마사랑">
    <meta property="og:description" content="{title} 지역 전문 제휴업체 정보. 30분 내 방문, 아로마 및 스웨디시 100% 후불제 안심 케어.">
    <meta property="og:url" content="{DOMAIN}">
    <link rel="stylesheet" href="{prefix}styles.css">
</head>
<body>
    <h1>{title}</h1>
    {links_html}
</body>
</html>"""

def run():
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(make_html("메인", 0))
    
    os.makedirs("seoul", exist_ok=True)
    with open("seoul/index.html", "w", encoding="utf-8") as f:
        f.write(make_html("서울 전지역", 1))
        
    os.makedirs("gyeonggi", exist_ok=True)
    with open("gyeonggi/index.html", "w", encoding="utf-8") as f:
        f.write(make_html("경기 전지역", 1))
        
    os.makedirs("incheon", exist_ok=True)
    with open("incheon/index.html", "w", encoding="utf-8") as f:
        f.write(make_html("인천 전지역", 1))
        
    print("빌드 완료!")

if __name__ == "__main__":
    run()