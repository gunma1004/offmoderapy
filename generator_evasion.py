import os
import random

# 1. 사이트 설정
DOMAIN = "https://offmoderapy.netlify.app"
OUTPUT_DIR = "dist_evasion"

# 2. 30여 가지 출장 회피형 마사지 키워드 확장 풀
evasion_keywords = [
    "출장 웰니스 마사지", "출장 아로마 마사지", "출장 산후전후 마사지", "출장 스웨디시 마사지",
    "출장 타이 마사지", "출장 홈타이 마사지", "출장 림프 순환 마사지", "출장 딥티슈 마사지",
    "출장 스포츠 마사지", "출장 감성 마사지", "출장 경락 마사지", "출장 족욕 마사지",
    "출장 스톤 마사지", "출장 산전산후 테라피 마사지", "출장 통증완화 마사지", "출장 전신오일 마사지",
    "출장 디톡스 마사지", "출장 파워트리 마사지", "출장 산후조리 마사지", "출장 피로회복 마사지",
    "출장 리프레시 마사지", "출장 순환마사지", "출장 스페셜 마사지", "출장 체형관리 마사지",
    "출장 맞춤 마사지", "출장 스킨케어 마사지", "출장 건식 마사지", "출장 오일 마사지",
    "출장 전신 마사지", "출장 힐링 마사지"
]

# 3. 제휴 업체 정보 데이터
PARTNER_SHOPS = [
    {"name": "퀸즈홈테라피", "tel": "0507-1280-3296", "desc": "프리미엄 맞춤 홈케어 및 스웨디시 전문"},
    {"name": "한국골든테라피", "tel": "0507-1280-3360", "desc": "정통 힐링 아로마 및 전신 관리"},
    {"name": "한국미인테라피", "tel": "0507-1280-3201", "desc": "편안하고 아늑한 1:1 맞춤 케어"},
    {"name": "오늘밤테라피", "tel": "0507-1280-3199", "desc": "24시 신속 방문 및 피로 회복 전문"},
    {"name": "주주테라피", "tel": "0507-1280-3197", "desc": "감성 힐링 및 전문 테라피 복합 코스"}
]

# 4. 서울·경기·인천 전체 지역 및 구·동 데이터 내장
seoul_regions = {
    "jongno": {"name": "종로구", "dongs": ["청운동", "효자동", "삼청동", "부암동", "평창동", "무악동", "교남동", "가회동", "종로1가", "이화동", "혜화동", "창신동", "숭인동"]},
    "jung": {"name": "중구", "dongs": ["소공동", "회현동", "명동", "필동", "장충동", "광희동", "을지로동", "신당동", "다산동", "약수동", "청구동", "황학동", "중림동"]},
    "yongsan": {"name": "용산구", "dongs": ["후암동", "청파동", "원효로동", "효창동", "용문동", "이촌동", "이태원동", "한남동", "서빙고동", "보광동"]},
    "seongdong": {"name": "성동구", "dongs": ["왕십리동", "마장동", "사근동", "행당동", "응봉동", "금호동", "옥수동", "성수동", "송정동", "용답동"]},
    "gwangjin": {"name": "광진구", "dongs": ["중곡동", "능동", "구의동", "광장동", "자양동", "화양동", "군자동"]},
    "dongdaemun": {"name": "동대문구", "dongs": ["신설동", "용두동", "제기동", "전농동", "답십리동", "장안동", "청량리동", "회기동", "휘경동", "이문동"]},
    "jungnang": {"name": "중랑구", "dongs": ["면목동", "상봉동", "중화동", "묵동", "망우동", "신내동"]},
    "seongbuk": {"name": "성북구", "dongs": ["성북동", "삼선동", "동선동", "돈암동", "안암동", "보문동", "정릉동", "길음동", "종암동", "월곡동", "장위동", "석관동"]},
    "gangbuk": {"name": "강북구", "dongs": ["삼양동", "미아동", "번동", "수유동", "우이동", "인수동"]},
    "dobong": {"name": "도봉구", "dongs": ["창동", "도봉동", "쌍문동", "방학동"]},
    "nowon": {"name": "노원구", "dongs": ["월계동", "공릉동", "하계동", "중계동", "상계동"]},
    "eunpyeong": {"name": "은평구", "dongs": ["녹번동", "불광동", "갈현동", "구산동", "대조동", "응암동", "역촌동", "신사동", "증산동", "수색동", "진관동"]},
    "seodaemun": {"name": "서대문구", "dongs": ["천연동", "북아현동", "신촌동", "연희동", "홍제동", "홍은동", "남가좌동", "북가좌동"]},
    "mapo": {"name": "마포구", "dongs": ["아현동", "공덕동", "도화동", "용강동", "대흥동", "염리동", "신수동", "서교동", "합정동", "망원동", "연남동", "성산동", "상암동"]},
    "yangcheon": {"name": "양천구", "dongs": ["목동", "신월동", "신정동"]},
    "gangseo": {"name": "강서구", "dongs": ["염창동", "등촌동", "화곡동", "가양동", "발산동", "공항동", "방화동"]},
    "guro": {"name": "구로구", "dongs": ["신도림동", "구로동", "고척동", "개봉동", "오류동", "수궁동", "항동"]},
    "geumcheon": {"name": "금천구", "dongs": ["가산동", "독산동", "시흥동"]},
    "yeongdeungpo": {"name": "영등포구", "dongs": ["영등포동", "여의동", "당산동", "도림동", "문래동", "양평동", "신길동", "대림동"]},
    "dongjak": {"name": "동작구", "dongs": ["노량진동", "상도동", "흑석동", "사당동", "대방동", "신대방동"]},
    "gwanak": {"name": "관악구", "dongs": ["봉천동", "신림동", "남현동", "보라매동", "청림동", "행운동", "낙성대동"]},
    "seocho": {"name": "서초구", "dongs": ["서초동", "반포동", "방배동", "잠원동", "양재동", "내곡동"]},
    "gangnam": {"name": "강남구", "dongs": ["역삼동", "논현동", "청담동", "삼성동", "대치동", "신사동", "도곡동", "개포동", "일원동", "수서동"]},
    "songpa": {"name": "송파구", "dongs": ["잠실동", "신천동", "풍납동", "송파동", "석촌동", "삼전동", "가락동", "문정동", "방이동", "오금동"]},
    "gangdong": {"name": "강동구", "dongs": ["고덕동", "상일동", "명일동", "암사동", "천호동", "성내동", "둔촌동"]}
}

gyeonggi_regions = {
    "suwon-jangan": {"name": "수원시 장안구", "dongs": ["파장동", "정자동", "영화동", "송죽동", "조원동", "율천동"]},
    "suwon-gwonseon": {"name": "수원시 권선구", "dongs": ["세류동", "권선동", "곡선동", "평동", "호매실동", "서둔동"]},
    "suwon-paldal": {"name": "수원시 팔달구", "dongs": ["매교동", "매산동", "고등동", "화서동", "지동", "우만동", "인계동"]},
    "suwon-yeongtong": {"name": "수원시 영통구", "dongs": ["매탄동", "원천동", "영통동", "망포동", "광교동"]},
    "seongnam-bundang": {"name": "성남시 분당구", "dongs": ["분당동", "수내동", "정자동", "서현동", "이매동", "야탑동", "판교동", "삼평동"]},
    "goyang-deokyang": {"name": "고양시 덕양구", "dongs": ["원신동", "효자동", "화정동", "행신동", "성사동", "고양동", "능곡동"]},
    "goyang-ilsandong": {"name": "고양시 일산동구", "dongs": ["식사동", "중산동", "정발산동", "백석동", "마두동", "장항동"]},
    "goyang-ilsanseo": {"name": "고양시 일산서구", "dongs": ["일산동", "탄현동", "주엽동", "대화동", "덕이동"]},
    "yongin-suji": {"name": "용인시 수지구", "dongs": ["풍덕천동", "신봉동", "죽전동", "동천동", "상현동", "성복동"]},
    "bucheon": {"name": "부천시", "dongs": ["원미동", "심곡동", "소사동", "중동", "상동", "역곡동"]}
}

incheon_regions = {
    "jemulpo": {"name": "제물포구", "dongs": ["신포동", "연안동", "만석동", "송림동", "화수동", "송현동"]},
    "yeongjong": {"name": "영종구", "dongs": ["중산동", "운서동", "운남동"]},
    "michuhol": {"name": "미추홀구", "dongs": ["도화동", "주안동", "학익동", "관교동", "문학동", "숭의동", "용현동"]},
    "yeonsu": {"name": "연수구", "dongs": ["옥련동", "연수동", "청학동", "동춘동", "송도동"]},
    "namdong": {"name": "남동구", "dongs": ["구월동", "간석동", "만수동", "서창동", "논현동", "고잔동"]},
    "bupyeong": {"name": "부평구", "dongs": ["부평동", "산곡동", "청천동", "갈산동", "삼산동", "부개동"]},
    "gyeyang": {"name": "계양구", "dongs": ["효성동", "작전동", "계산동", "임학동"]},
    "seohae": {"name": "서해구", "dongs": ["가좌동", "석남동", "신현동", "가정동", "연희동"]},
    "geomdan": {"name": "검단동", "dongs": ["마전동", "당하동", "원당동", "불로동", "검암동", "아라동"]}
}

all_regions_data = {
    "seoul": {"name": "서울", "districts": seoul_regions},
    "gyeonggi": {"name": "경기", "districts": gyeonggi_regions},
    "incheon": {"name": "인천", "districts": incheon_regions}
}

# 5. HTML 생성 함수
def get_evasion_html_template(area_title, path_depth, sub_links=None):
    prefix = "../" * path_depth
    kw1, kw2, kw3 = random.sample(evasion_keywords, 3)
    
    sub_links_html = ""
    if sub_links:
        links_box = ""
        for name, url in sub_links.items():
            links_box += f'<a href="{url}" style="display:inline-block; margin:5px; padding:8px 12px; background:#1e1e24; color:#f59e0b; border-radius:8px; text-decoration:none; font-size:13px;">{name}</a> '
        sub_links_html = f'<div style="margin:20px 0;"><h3>하위 지역 선택</h3>{links_box}</div>'

    partners_html = ""
    for shop in PARTNER_SHOPS:
        partners_html += f"""
        <div style="background:#18181c; padding:20px; border-radius:12px; margin-bottom:15px; border:1px solid rgba(255,255,255,0.05);">
            <h3 style="color:#f59e0b; margin:0 0 5px;">{shop['name']}</h3>
            <p style="color:#bbb; font-size:13px; margin:0 0 10px;">{shop['desc']}</p>
            <a href="tel:{shop['tel']}" style="background:#f59e0b; color:#000; padding:8px 16px; border-radius:6px; font-weight:bold; text-decoration:none; font-size:12px; display:inline-block;">📞 예약 전화: {shop['tel']}</a>
        </div>"""

    page_title = f"{area_title} {kw1} 및 {kw2} 안내 - 유레스트"
    page_desc = f"{area_title} 전문 {kw1}, {kw2}, {kw3} 서비스! 선입금 없는 100% 현장 결제로 안전하고 편안한 웰니스 피로회복을 누려보세요."

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title}</title>
    <meta name="description" content="{page_desc}">
    <link rel="stylesheet" href="{prefix}styles.css">
</head>
<body style="background:#08080a; color:#fff; font-family:sans-serif; margin:0; padding:20px;">
    <div style="max-width:800px; margin:0 auto; background:#121216; padding:30px; border-radius:20px; border:1px solid rgba(245,158,11,0.3);">
        <nav style="margin-bottom:20px;"><a href="{prefix}index.html" style="color:#f59e0b; text-decoration:none; font-weight:bold;">← 메인으로</a></nav>
        <span style="background:rgba(245,158,11,0.1); color:#f59e0b; padding:5px 12px; border-radius:20px; font-size:12px; font-weight:bold;">📍 수도권 웰니스 회피형 케어 가이드</span>
        
        <h1 style="font-size:26px; margin-top:15px; color:#fff;">{area_title} {kw1} & {kw2} 안내</h1>
        <p style="color:#bbb; line-height:1.6; font-size:14px;">
            {area_title} 주민 여러분을 위한 24시 프리미엄 홈케어 서비스입니다. 
            숙련된 전문 테라피스트가 직접 방문하여 {kw1}, {kw2}, {kw3} 등 고객님 컨디션에 맞춘 1:1 맞춤형 힐링 프로그램을 선사합니다.
        </p>
        
        {sub_links_html}

        <div style="margin-top:30px;">
            <h2 style="font-size:18px; color:#fff; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:10px;">🏆 추천 제휴 센터</h2>
            {partners_html}
        </div>
    </div>
</body>
</html>
"""

# 6. 실행 함수
def generate_evasion_sites():
    print("🚀 [회피형 키워드 전용] 독립 빌드 시작...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    page_count = 0
    for reg_key, reg_val in all_regions_data.items():
        reg_dir = os.path.join(OUTPUT_DIR, reg_key)
        os.makedirs(reg_dir, exist_ok=True)
        
        dist_links = {d_val["name"]: f"./{d_key}/" for d_key, d_val in reg_val["districts"].items()}
        with open(os.path.join(reg_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(get_evasion_html_template(f"{reg_val['name']} 전지역", 1, sub_links=dist_links))
        page_count += 1

        for dist_key, dist_val in reg_val["districts"].items():
            dist_dir = os.path.join(reg_dir, dist_key)
            os.makedirs(dist_dir, exist_ok=True)
            
            dong_links = {dong: f"./{dong}/" for dong in dist_val["dongs"]}
            with open(os.path.join(dist_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(get_evasion_html_template(f"{reg_val['name']} {dist_val['name']}", 2, sub_links=dong_links))
            page_count += 1

            for dong in dist_val["dongs"]:
                dong_dir = os.path.join(dist_dir, dong)
                os.makedirs(dong_dir, exist_ok=True)
                
                with open(os.path.join(dong_dir, "index.html"), "w", encoding="utf-8") as f:
                    f.write(get_evasion_html_template(f"{reg_val['name']} {dist_val['name']} {dong}", 3))
                page_count += 1

    print(f"✨ 총 {page_count}개의 구·동 회피형 페이지가 '{OUTPUT_DIR}' 폴더에 성공적으로 생성되었습니다!")

if __name__ == "__main__":
    generate_evasion_sites()