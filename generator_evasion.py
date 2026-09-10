import os
import random

# 1. 고정 출력 경로 (dist/evasion)
OUTPUT_DIR = "dist/evasion"
DOMAIN = "https://offmoderapy.netlify.app"

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

# 4. 수도권 전 지역 및 모든 구·동 데이터 세트
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
    "seongnam-sujeong": {"name": "성남시 수정구", "dongs": ["신흥동", "태평동", "수진동", "단대동", "산성동", "상적동"]},
    "seongnam-jungwon": {"name": "성남시 중원구", "dongs": ["성남동", "중앙동", "금광동", "은행동", "상대원동", "하대원동"]},
    "seongnam-bundang": {"name": "성남시 분당구", "dongs": ["분당동", "수내동", "정자동", "서현동", "이매동", "야탑동", "판교동", "삼평동"]},
    "goyang-deokyang": {"name": "고양시 덕양구", "dongs": ["원신동", "효자동", "화정동", "행신동", "성사동", "고양동", "능곡동"]},
    "goyang-ilsandong": {"name": "고양시 일산동구", "dongs": ["식사동", "중산동", "정발산동", "백석동", "마두동", "장항동"]},
    "goyang-ilsanseo": {"name": "고양시 일산서구", "dongs": ["일산동", "탄현동", "주엽동", "대화동", "덕이동"]},
    "yongin-cheoin": {"name": "용인시 처인구", "dongs": ["역삼동", "유림동", "동부동", "포곡읍", "모현읍", "이동읍"]},
    "yongin-giheung": {"name": "용인시 기흥구", "dongs": ["신갈동", "구성동", "마북동", "동백동", "보정동", "기흥동"]},
    "yongin-suji": {"name": "용인시 수지구", "dongs": ["풍덕천동", "신봉동", "죽전동", "동천동", "상현동", "성복동"]},
    "bucheon-wonmi": {"name": "부천시 원미구", "dongs": ["원미동", "심곡동", "춘의동", "도당동", "중동", "상동"]},
    "bucheon-sosa": {"name": "부천시 소사구", "dongs": ["소사본동", "범박동", "역곡동", "괴안동", "송내동"]},
    "bucheon-ojeong": {"name": "부천시 오정구", "dongs": ["오정동", "고강동", "원종동", "성곡동"]},
    "anyang-manan": {"name": "안양시 만안구", "dongs": ["안양동", "석수동", "박달동"]},
    "anyang-dongan": {"name": "안양시 동안구", "dongs": ["비산동", "관양동", "평촌동", "호계동"]},
    "ansan-sangrok": {"name": "안산시 상록구", "dongs": ["일동", "이동", "사동", "본오동", "반월동"]},
    "ansan-danwon": {"name": "안산시 단원구", "dongs": ["고잔동", "와동", "원곡동", "초지동", "선부동"]},
    "uijeongbu": {"name": "의정부시", "dongs": ["의정부동", "호원동", "가능동", "녹양동", "신곡동", "송산동"]},
    "gwangmyeong": {"name": "광명시", "dongs": ["광명동", "철산동", "하안동", "소하동"]},
    "pyeongtaek": {"name": "평택시", "dongs": ["비전동", "서정동", "송탄동", "팽성읍", "안중읍"]},
    "dongducheon": {"name": "동두천시", "dongs": ["생연동", "보산동", "불현동", "상패동"]},
    "gwacheon": {"name": "과천시", "dongs": ["중앙동", "갈현동", "문원동", "별양동"]},
    "guri": {"name": "구리시", "dongs": ["갈매동", "동구동", "인창동", "수택동"]},
    "namyangju": {"name": "남양주시", "dongs": ["와부읍", "진접읍", "화도읍", "오남읍", "다산동"]},
    "osan": {"name": "오산시", "dongs": ["중앙동", "서동", "세마동", "초평동", "대원동"]},
    "siheung": {"name": "시흥시", "dongs": ["신천동", "대야동", "은행동", "정왕동", "배곧동"]},
    "gunpo": {"name": "군포시", "dongs": ["군포동", "산본동", "금정동", "대야동"]},
    "uiwang": {"name": "의왕시", "dongs": ["고천동", "부곡동", "내손동", "청계동"]},
    "hanam": {"name": "하남시", "dongs": ["천현동", "신장동", "풍산동", "미사동", "위례동"]},
    "paju": {"name": "파주시", "dongs": ["금촌동", "교하동", "운정동", "문산읍"]},
    "icheon": {"name": "이천시", "dongs": ["증포동", "창전동", "중리동", "부발읍"]},
    "anseong": {"name": "안성시", "dongs": ["안성동", "공도읍", "죽산면"]},
    "gimpo": {"name": "김포시", "dongs": ["사우동", "풍무동", "고촌읍", "통진읍", "장기동", "구래동"]},
    "hwaseong": {"name": "화성시", "dongs": ["진안동", "병점동", "반월동", "동탄동", "봉담읍"]},
    "gwangju-gg": {"name": "광주시", "dongs": ["경안동", "송정동", "광남동", "오포읍"]},
    "yangju": {"name": "양주시", "dongs": ["회천동", "양주동", "옥정동"]},
    "pocheon": {"name": "포천시", "dongs": ["포천동", "소흘읍", "선단동"]},
    "yeoju": {"name": "여주시", "dongs": ["여흥동", "중앙동", "오학동"]},
    "yeoncheon": {"name": "연천군", "dongs": ["연천읍", "전곡읍"]},
    "gapyeong": {"name": "가평군", "dongs": ["가평읍", "설악면", "청평면"]},
    "yangpyeong": {"name": "양평군", "dongs": ["양평읍", "강상면", "용문면"]}
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
    "geomdan": {"name": "검단동", "dongs": ["마전동", "당하동", "원당동", "불로동", "검암동", "아라동"]},
    "ganghwa": {"name": "강화군", "dongs": ["강화읍", "선원면", "길상면"]},
    "ongjin": {"name": "옹진군", "dongs": ["북도면", "연평면", "백령면"]}
}

all_regions_data = {
    "seoul": {"name": "서울", "districts": seoul_regions},
    "gyeonggi": {"name": "경기", "districts": gyeonggi_regions},
    "incheon": {"name": "인천", "districts": incheon_regions}
}

# 5. 회피형 전문 SEO 템플릿 생성 함수 (Open Graph 태그 포함)
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
    
    <!-- Open Graph (SNS 및 검색엔진 미리보기 최적화) -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="{page_title}">
    <meta property="og:description" content="{page_desc}">
    <meta property="og:url" content="{DOMAIN}/">
    <meta property="og:site_name" content="오프모드건마사랑">

    <link rel="stylesheet" href="{prefix}styles.css">
</head>
<body style="background:#0a0a0f; color:#e5e7eb; font-family:'Noto Sans KR', sans-serif; margin:0; padding:20px; line-height:1.6;">
    <div style="max-width:850px; margin:30px auto; background:#121218; padding:35px; border-radius:20px; border:1px solid rgba(255,107,53,0.2); box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
        
        <nav style="margin-bottom:20px; display:flex; justify-content:space-between; align-items:center;">
            <a href="{prefix}../../index.html" style="color:#ff6b35; text-decoration:none; font-weight:bold; font-size:14px;">← 오프모드 메인으로 돌아가기</a>
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

# 6. 실행 함수 (전체 지역 대량 빌드)
def generate_evasion_sites():
    print("🚀 [수도권 전 지역 완벽 포함] 구·동 3단계 계층 구조 빌드 시작...")
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

    print(f"✨ 총 {page_count}개의 수도권 전 지역 회피형 페이지가 '{OUTPUT_DIR}' 폴더에 성공적으로 생성되었습니다!")

if __name__ == "__main__":
    generate_evasion_sites()