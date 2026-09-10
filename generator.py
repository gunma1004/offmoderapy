import os
import random

# 1. 고정 출력 경로 (메인 페이지의 ./evasion/... 링크와 완벽 일치)
OUTPUT_DIR = "dist/evasion"

# 2. 30여 가지 출장 회피형 마사지 및 테라피 키워드 풀
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

# 4. 서울·경기·인천 전체 지역 및 구·동 데이터
seoul_regions = {
    "gangnam": {"name": "강남구", "dongs": ["역삼동", "논현동", "청담동", "삼성동", "대치동", "신사동", "도곡동", "개포동", "일원동", "수서동"]},
    "mapo": {"name": "마포구", "dongs": ["아현동", "공덕동", "도화동", "용강동", "대흥동", "염리동", "신수동", "서교동", "합정동", "망원동", "연남동", "성산동", "상암동"]},
    "seocho": {"name": "서초구", "dongs": ["서초동", "반포동", "방배동", "잠원동", "양재동", "내곡동"]},
    "songpa": {"name": "송파구", "dongs": ["잠실동", "신천동", "풍납동", "송파동", "석촌동", "삼전동", "가락동", "문정동", "방이동", "오금동"]}
}

gyeonggi_regions = {
    "seongnam-bundang": {"name": "성남시 분당구", "dongs": ["분당동", "수내동", "정자동", "서현동", "이매동", "야탑동", "판교동", "삼평동"]},
    "suwon-jangan": {"name": "수원시 장안구", "dongs": ["파장동", "정자동", "영화동", "송죽동", "조원동", "율천동"]},
    "goyang-ilsandong": {"name": "고양시 일산동구", "dongs": ["식사동", "중산동", "정발산동", "백석동", "마두동", "장항동"]},
    "yongin-suji": {"name": "용인시 수지구", "dongs": ["풍덕천동", "신봉동", "죽전동", "동천동", "상현동", "성복동"]}
}

incheon_regions = {
    "namdong": {"name": "남동구", "dongs": ["구월동", "간석동", "만수동", "서창동", "논현동", "고잔동"]},
    "yeonsu": {"name": "연수구", "dongs": ["옥련동", "연수동", "청학동", "동춘동", "송도동"]},
    "bupyeong": {"name": "부평구", "dongs": ["부평동", "산곡동", "청천동", "갈산동", "삼산동", "부개동"]},
    "geomdan": {"name": "검단동", "dongs": ["마전동", "당하동", "원당동", "불로동", "검암동", "아라동"]}
}

all_regions_data = {
    "seoul": {"name": "서울", "districts": seoul_regions},
    "gyeonggi": {"name": "경기", "districts": gyeonggi_regions},
    "incheon": {"name": "인천", "districts": incheon_regions}
}

# 5. 회피형 전문 SEO 템플릿 생성 함수
def get_evasion_html_template(area_title, path_depth, sub_links=None):
    prefix = "../" * path_depth
    kw1, kw2, kw3 = random.sample(evasion_keywords, 3)
    
    sub_links_html = ""
    if sub_links:
        links_box = ""
        for name, url in sub_links.items():
            links_box += f'<a href="{url}" style="display:inline-block; margin:4px; padding:6px 12px; background:#1e1e24; color:#ff6b35; border:1px solid rgba(255,107,53,0.3); border-radius:6px; text-decoration:none; font-size:12px;">{name}</a> '
        sub_links_html = f'''
        <div style="margin:25px 0; background:#16161a; padding:20px; border-radius:12px; border:1px solid rgba(255,255,255,0.05);">
            <h3 style="color:#ff6b35; font-size:15px; margin-bottom:12px;">🔍 {area_title} 하위 세부 지역 선택</h3>
            <div>{links_box}</div>
        </div>'''

    partners_html = ""
    for shop in PARTNER_SHOPS:
        partners_html += f"""
        <div style="background:#18181c; padding:20px; border-radius:12px; margin-bottom:15px; border-left:4px solid #ff6b35; border-top:1px solid rgba(255,255,255,0.05); border-right:1px solid rgba(255,255,255,0.05); border-bottom:1px solid rgba(255,255,255,0.05);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <h4 style="color:#fff; font-size:16px; margin:0;">{shop['name']}</h4>
                <span style="background:rgba(255,107,53,0.15); color:#ff6b35; padding:3px 8px; border-radius:4px; font-size:11px; font-weight:bold;">프리미엄 파트너</span>
            </div>
            <p style="color:#9ca3af; font-size:13px; margin:0 0 12px;">{shop['desc']} - {area_title} 전역 신속 방문</p>
            <a href="tel:{shop['tel']}" style="background:#ff6b35; color:#fff; padding:8px 16px; border-radius:6px; font-weight:bold; text-decoration:none; font-size:12px; display:inline-block;">📞 실시간 예약 전화: {shop['tel']}</a>
        </div>"""

    page_title = f"{area_title} {kw1} 및 {kw2} 전문 안내 센터"
    page_desc = f"{area_title} 전 지역 24시 방문 가능한 {kw1}, {kw2}, {kw3} 서비스. 철저한 1:1 맞춤 케어와 100% 현장 결제 안심 시스템."

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title}</title>
    <meta name="description" content="{page_desc}">
    <link rel="stylesheet" href="{prefix}styles.css">
</head>
<body style="background:#0a0a0f; color:#e5e7eb; font-family:'Noto Sans KR', sans-serif; margin:0; padding:20px; line-height:1.6;">
    <div style="max-width:850px; margin:30px auto; background:#121218; padding:35px; border-radius:20px; border:1px solid rgba(255,107,53,0.2); box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
        
        <nav style="margin-bottom:20px; display:flex; justify-content:space-between; align-items:center;">
            <a href="{prefix}../index.html" style="color:#ff6b35; text-decoration:none; font-weight:bold; font-size:14px;">← 오프모드 메인으로 돌아가기</a>
            <span style="background:rgba(255,107,53,0.1); color:#ff6b35; padding:4px 12px; border-radius:20px; font-size:11px; font-weight:bold;">✨ SEO 최적화 회피형 특별 페이지</span>
        </nav>
        
        <div style="border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:20px; margin-bottom:25px;">
            <h1 style="font-size:24px; color:#fff; margin:0 0 10px; font-weight:700;">{area_title} <span style="color:#ff6b35;">{kw1}</span> & <span style="color:#ff6b35;">{kw2}</span> 가이드</h1>
            <p style="color:#9ca3af; font-size:14px; margin:0;">
                바쁜 일상에 지친 몸과 마음을 위한 {area_title} 맞춤형 프리미엄 홈케어입니다. 
                전문 테라피스트가 고객님 계신 곳으로 직접 방문하여 {kw1}, {kw2}, {kw3} 등 최고급 힐링 프로그램을 제공해 드립니다.
            </p>
        </div>
        
        {sub_links_html}

        <div style="margin-top:30px;">
            <h2 style="font-size:17px; color:#fff; margin-bottom:15px; border-left:3px solid #ff6b35; padding-left:10px;">🏆 {area_title} 공식 인증 제휴 센터</h2>
            {partners_html}
        </div>

        <div style="margin-top:40px; text-align:center; color:#6b7280; font-size:12px; border-top:1px solid rgba(255,255,255,0.05); padding-top:20px;">
            <p>본 페이지는 검색엔진 최적화를 위해 제공되는 {area_title} 지역 맞춤형 정보 안내 페이지입니다.</p>
            <p>&copy; 2026 오프모드건마사랑 All rights reserved.</p>
        </div>
    </div>
</body>
</html>
"""

# 6. 실행 함수
def generate_evasion_sites():
    print("🚀 [회피형 키워드 전용] dist/evasion 폴더로 빌드 시작...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    page_count = 0
    for reg_key, reg_val in all_regions_data.items():
        reg_dir = os.path.join(OUTPUT_DIR, reg_key)
        os.makedirs(reg_dir, exist_ok=True)
        
        for dist_key, dist_val in reg_val["districts"].items():
            dist_dir = os.path.join(reg_dir, dist_key)
            os.makedirs(dist_dir, exist_ok=True)
            
            dong_links = {dong: f"./{dong}/index.html" for dong in dist_val["dongs"]}
            with open(os.path.join(dist_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(get_evasion_html_template(f"{reg_val['name']} {dist_val['name']}", 2, sub_links=dong_links))
            page_count += 1

            for dong in dist_val["dongs"]:
                dong_dir = os.path.join(dist_dir, dong)
                os.makedirs(dong_dir, exist_ok=True)
                
                with open(os.path.join(dong_dir, "index.html"), "w", encoding="utf-8") as f:
                    f.write(get_evasion_html_template(f"{reg_val['name']} {dist_val['name']} {dong}", 3))
                page_count += 1

    print(f"✨ 총 {page_count}개의 회피형 페이지가 '{OUTPUT_DIR}' 폴더에 성공적으로 생성되었습니다!")

if __name__ == "__main__":
    generate_evasion_sites()