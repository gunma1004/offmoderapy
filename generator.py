import os

# 1. 사이트 기본 설정
DOMAIN = "https://offmoderapy.netlify.app"
NAVER_VERIFICATION = "a0e02e4f2dcaf270179e713519c690fbe449e8c5"

# 2. 제휴 업체 정보 데이터
PARTNER_SHOPS = [
    {"name": "퀸즈홈테라피", "tel": "0507-1280-3296", "desc": "프리미엄 맞춤 홈케어 및 스웨디시 전문"},
    {"name": "한국골든테라피", "tel": "0507-1280-3360", "desc": "정통 힐링 아로마 및 전신 관리"},
    {"name": "한국미인테라피", "tel": "0507-1280-3201", "desc": "편안하고 아늑한 1:1 맞춤 케어"},
    {"name": "오늘밤테라피", "tel": "0507-1280-3199", "desc": "24시 신속 방문 및 피로 회복 전문"},
    {"name": "주주테라피", "tel": "0507-1280-3197", "desc": "감성 힐링 및 전문 테라피 복합 코스"}
]

# 3. 수도권 전 지역 및 모든 구·동 데이터 세트 (메인 및 evasion 공용)
seoul_regions = {
    "gangnam": {"name": "강남구", "dongs": ["역삼동", "논현동", "청담동", "삼성동", "대치동", "신사동", "도곡동", "개포동", "일원동", "수서동"]},
    "mapo": {"name": "마포구", "dongs": ["아현동", "공덕동", "도화동", "용강동", "대흥동", "염리동", "신수동", "서교동", "합정동", "망원동", "연남동", "성산동", "상암동"]},
    "seocho": {"name": "서초구", "dongs": ["서초동", "반포동", "방배동", "잠원동", "양재동", "내곡동"]},
    "songpa": {"name": "송파구", "dongs": ["잠실동", "신천동", "풍납동", "송파동", "석촌동", "삼전동", "가락동", "문정동", "방이동", "오금동"]},
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
    "yangcheon": {"name": "양천구", "dongs": ["목동", "신월동", "신정동"]},
    "gangseo": {"name": "강서구", "dongs": ["염창동", "등촌동", "화곡동", "가양동", "발산동", "공항동", "방화동"]},
    "guro": {"name": "구로구", "dongs": ["신도림동", "구로동", "고척동", "개봉동", "오류동", "수궁동", "항동"]},
    "geumcheon": {"name": "금천구", "dongs": ["가산동", "독산동", "시흥동"]},
    "yeongdeungpo": {"name": "영등포구", "dongs": ["영등포동", "여의동", "당산동", "도림동", "문래동", "양평동", "신길동", "대림동"]},
    "dongjak": {"name": "동작구", "dongs": ["노량진동", "상도동", "흑석동", "사당동", "대방동", "신대방동"]},
    "gwanak": {"name": "관악구", "dongs": ["봉천동", "신림동", "남현동", "보라매동", "청림동", "행운동", "낙성대동"]},
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
    "guri": {"name": "구리시", "dongs": ["갈매동", "동구동", "인창동", "수택동"]},
    "namyangju": {"name": "남양주시", "dongs": ["와부읍", "진접읍", "화도읍", "오남읍", "다산동"]},
    "siheung": {"name": "시흥시", "dongs": ["신천동", "대야동", "은행동", "정왕동", "배곧동"]},
    "gunpo": {"name": "군포시", "dongs": ["군포동", "산본동", "금정동", "대야동"]},
    "hanam": {"name": "하남시", "dongs": ["천현동", "신장동", "풍산동", "미사동", "위례동"]},
    "paju": {"name": "파주시", "dongs": ["금촌동", "교하동", "운정동", "문산읍"]},
    "gimpo": {"name": "김포시", "dongs": ["사우동", "풍무동", "고촌읍", "통진읍", "장기동", "구래동"]},
    "hwaseong": {"name": "화성시", "dongs": ["진안동", "병점동", "반월동", "동탄동", "봉담읍"]}
}

incheon_regions = {
    "jemulpo": {"name": "제물포구", "dongs": ["신포동", "연안동", "만석동", "송림동", "화수동", "송현동"]},
    "yeongjong": {"name": "영종구", "dongs": ["중산동", "운서동", "운남동"]},
    "michuhol": {"name": "미추홀구", "dongs": ["도화동", "주안동", "학익동", "관교동", "문학동", "숭의동", "용현동"]},
    "yeonsu": {"name": "연수구", "dongs": ["옥련동", "연수동", "청학동", "동춘동", "송도동"]},
    "namdong": {"name": "남동구", "dongs": ["구월동", "간석동", "만수동", "서창동", "논현동", "고잔동"]},
    "bupyeong": {"name": "부평구", "dongs": ["부평동", "산곡동", "청천동", "갈산동", "삼산동", "부개동"]},
    "gyeyang": {"name": "계양구", "dongs": ["효성동", "작전동", "계산동", "임학동"]},
    "geomdan": {"name": "검단동", "dongs": ["마전동", "당하동", "원당동", "불로동", "검암동", "아라동"]}
}

all_regions_data = {
    "seoul": {"name": "서울특별시", "districts": seoul_regions},
    "gyeonggi": {"name": "경기도", "districts": gyeonggi_regions},
    "incheon": {"name": "인천광역시", "districts": incheon_regions}
}

# 4. 동적 허브 HTML 생성 함수
def generate_hub_html():
    hub_sections_html = ""
    
    for reg_key, reg_val in all_regions_data.items():
        dist_cards_html = ""
        for dist_key, dist_val in reg_val["districts"].items():
            dong_links_html = ""
            for dong in dist_val["dongs"]:
                dong_links_html += f'<a href="./evasion/{reg_key}/{dist_key}/{dong}/index.html">{dong}</a>'
            
            dist_cards_html += f"""
            <div class="district-card">
                <h4><a href="./evasion/{reg_key}/{dist_key}/index.html" style="color:#ff6b35; text-decoration:none;">{dist_val['name']}</a></h4>
                <div class="link-list">
                    {dong_links_html}
                </div>
            </div>"""
        
        hub_sections_html += f"""
        <div class="region-group">
            <h3>🏙️ {reg_val['name']} 전지역 안내</h3>
            <div class="district-grid">
                {dist_cards_html}
            </div>
        </div>"""

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="naver-site-verification" content="{NAVER_VERIFICATION}" />
    <title>오프모드건마사랑 - 서울·경기·인천 프리미엄 힐링·아로마 스웨디시 24시</title>
    <meta name="description" content="서울, 경기, 인천 수도권 전 지역 30분 내 방문. 출장 웰니스 마사지, 출장 아로마 마사지, 출장 산후전후 마사지 등 전문 관리사가 제공하는 100% 후불제 안심 케어 서비스.">
    <meta name="robots" content="index,follow">
    
    <meta property="og:type" content="website">
    <meta property="og:title" content="오프모드건마사랑 - 서울·경기·인천 프리미엄 힐링·아로마 스웨디시 24시">
    <meta property="og:description" content="서울, 경기, 인천 수도권 전 지역 30분 내 방문. 출장 웰니스 마사지, 출장 아로마 마사지, 출장 산후전후 마사지 등 전문 관리사가 제공하는 100% 후불제 안심 케어 서비스.">
    <meta property="og:url" content="{DOMAIN}/">
    <meta property="og:site_name" content="오프모드건마사랑">

    <meta name="theme-color" content="#ff6b35">
    <link rel="canonical" href="{DOMAIN}/">
    <link rel="stylesheet" href="./styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        :root {{ --primary: #ff6b35; --text-dark: #1f2430; --text-muted: #5b6472; --bg-section: #fff5f0; }}
        html {{ scroll-behavior: smooth; }}
        body {{ font-family: 'Noto Sans KR', sans-serif; color: var(--text-dark); line-height: 1.7; background: var(--bg-section); }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
        
        .header {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: rgba(20, 20, 35, 0.95); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(255,255,255,0.1); }}
        .header-inner {{ display: flex; align-items: center; justify-content: space-between; height: 70px; max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
        .logo-text {{ font-size: 1.25rem; font-weight: 700; color: #fff; text-decoration: none; }}
        .logo-text span {{ color: var(--primary); }}
        .nav {{ display: flex; gap: 24px; align-items: center; }}
        .nav a {{ color: #fff; text-decoration: none; font-size: 0.95rem; }}
        .nav-cta {{ background: var(--primary); padding: 8px 18px; border-radius: 20px; font-weight: 700; font-size: 0.9rem; }}

        .hero {{ padding: 150px 20px 80px; text-align: center; background: linear-gradient(180deg, #15151f 0%, #252030 100%); color: #fff; }}
        .hero h1 {{ font-size: clamp(28px, 5vw, 44px); font-weight: 700; margin-bottom: 16px; line-height: 1.3; }}
        .hero h1 span {{ color: var(--primary); }}
        .hero p {{ font-size: 1.05rem; color: #b5b5c6; margin-bottom: 20px; }}

        .section {{ padding: 80px 0; }}
        .section-white {{ background: #fff; }}
        .section-title {{ text-align: center; margin-bottom: 40px; }}
        .section-title h2 {{ font-size: 1.8rem; margin-bottom: 10px; color: var(--text-dark); }}
        .section-title p {{ color: var(--text-muted); }}

        .partner-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }}
        .card {{ background: #fdfcfb; border: 1px solid #eee; border-radius: 16px; padding: 25px; text-align: left; box-shadow: 0 2px 10px rgba(0,0,0,0.02); transition: transform 0.2s; }}
        .card:hover {{ transform: translateY(-3px); }}
        .card-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }}
        .card h3 {{ font-size: 1.15rem; color: var(--text-dark); font-weight: 700; }}
        .badge {{ background: #fff5f0; color: var(--primary); padding: 4px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: bold; }}
        .card p {{ color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px; }}
        .card-footer {{ display: flex; justify-content: space-between; align-items: center; }}
        .tel {{ font-weight: bold; color: var(--text-dark); font-size: 0.95rem; }}
        .btn-call {{ background: var(--primary); color: #fff; padding: 8px 16px; border-radius: 8px; text-decoration: none; font-size: 0.85rem; font-weight: bold; }}

        .evasion-hub {{ background: #121218; color: #fff; padding: 80px 0; }}
        .region-group {{ background: #181822; border: 1px solid rgba(255,107,53,0.2); border-radius: 16px; padding: 30px; margin-bottom: 30px; }}
        .region-group h3 {{ color: var(--primary); font-size: 1.4rem; margin-bottom: 20px; border-bottom: 2px solid rgba(255,107,53,0.3); padding-bottom: 10px; }}
        .district-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 15px; }}
        .district-card {{ background: #1f1f2e; padding: 15px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05); }}
        .district-card h4 {{ color: #fff; font-size: 1.05rem; margin-bottom: 10px; }}
        .link-list {{ display: flex; flex-wrap: wrap; gap: 6px; max-height: 150px; overflow-y: auto; padding-right: 4px; }}
        .link-list::-webkit-scrollbar {{ width: 4px; }}
        .link-list::-webkit-scrollbar-thumb {{ background: rgba(255,107,53,0.5); border-radius: 2px; }}
        .link-list a {{ background: #2a2a3d; color: #d1d5db; padding: 4px 8px; border-radius: 6px; text-decoration: none; font-size: 0.8rem; transition: all 0.2s; }}
        .link-list a:hover {{ background: var(--primary); color: #fff; }}

        footer {{ background: #111; color: #888; padding: 40px 20px; text-align: center; font-size: 0.85rem; line-height: 1.6; }}
        footer strong {{ color: #aaa; }}
    </style>
</head>
<body>

    <header class="header">
        <div class="header-inner">
            <a href="/" class="logo-text">오프모드<span>건마사랑</span></a>
            <nav class="nav">
                <a href="#partners">공식제휴샵</a>
                <a href="#evasion-regions">출장지역안내</a>
                <a href="tel:050712803344" class="nav-cta">제휴 문의</a>
            </nav>
        </div>
    </header>

    <section class="hero">
        <div class="container">
            <div style="margin-bottom: 30px; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
                <img src="images/banner.jpg" alt="오프모드건마사랑 프리미엄 배너" style="width: 100%; height: auto; display: block; max-height: 400px; object-fit: cover;">
            </div>
            <span style="color: var(--primary); font-size: 0.85rem; letter-spacing: 2px; font-weight: 700; display: inline-block; margin-bottom: 15px;">24H 수도권 프라이빗 힐링 플랫폼</span>
            <h1>일상의 긴장을 끄고(Off),<br>완벽한 휴식을 켜다 <span>오프모드건마사랑</span></h1>
            <p>서울·경기·인천 수도권 전 지역 신속 방문 · 100% 후불제 안심 케어 서비스</p>
        </div>
    </section>

    <section class="section section-white" id="partners">
        <div class="container">
            <div class="section-title">
                <h2>공식 제휴 힐링샵 안내</h2>
                <p>엄선된 전문 관리사의 맞춤형 프리미엄 케어 서비스</p>
            </div>
            <div class="partner-grid">
                <div class="card">
                    <div class="card-header">
                        <h3>퀸즈홈테라피</h3>
                        <span class="badge">제휴점</span>
                    </div>
                    <p>프리미엄 맞춤 홈케어 및 스웨디시 전문 관리 프로그램</p>
                    <div class="card-footer">
                        <span class="tel">📞 0507-1280-3296</span>
                        <a href="tel:050712803296" class="btn-call">전화 연결</a>
                    </div>
                </div>
                <div class="card">
                    <div class="card-header">
                        <h3>한국골든테라피</h3>
                        <span class="badge">제휴점</span>
                    </div>
                    <p>정통 힐링 아로마 및 피로 회복 전신 관리 시스템</p>
                    <div class="card-footer">
                        <span class="tel">📞 0507-1280-3360</span>
                        <a href="tel:050712803360" class="btn-call">전화 연결</a>
                    </div>
                </div>
                <div class="card">
                    <div class="card-header">
                        <h3>한국미인테라피</h3>
                        <span class="badge">제휴점</span>
                    </div>
                    <p>편안하고 아늑한 환경에서 진행되는 1:1 맞춤 케어</p>
                    <div class="card-footer">
                        <span class="tel">📞 0507-1280-3201</span>
                        <a href="tel:050712803201" class="btn-call">전화 연결</a>
                    </div>
                </div>
                <div class="card">
                    <div class="card-header">
                        <h3>오늘밤테라피</h3>
                        <span class="badge">제휴점</span>
                    </div>
                    <p>24시 신속 방문 및 일상 속 깊은 피로 회복 전문</p>
                    <div class="card-footer">
                        <span class="tel">📞 0507-1280-3199</span>
                        <a href="tel:050712803199" class="btn-call">전화 연결</a>
                    </div>
                </div>
                <div class="card">
                    <div class="card-header">
                        <h3>주주테라피</h3>
                        <span class="badge">제휴점</span>
                    </div>
                    <p>부드러운 감성 힐링과 전문 테라피 복합 코스</p>
                    <div class="card-footer">
                        <span class="tel">📞 0507-1280-3197</span>
                        <a href="tel:050712803197" class="btn-call">전화 연결</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 🌟 동적으로 렌더링된 수도권 전 지역 허브 링크 섹션 -->
    <section class="evasion-hub" id="evasion-regions">
        <div class="container">
            <div class="section-title">
                <h2 style="color: #fff;">수도권 출장 웰니스 & 아로마 마사지 지역별 안내</h2>
                <p style="color: #b5b5c6;">서울·경기·인천 모든 구·동 단위 실시간 1:1 안심 방문 제휴 정보</p>
            </div>
            
            {hub_sections_html}

        </div>
    </section>

    <footer>
        <div class="container">
            <p><strong>오프모드건마사랑</strong> | 수도권 힐링 정보 플랫폼</p>
            <p>본 사이트는 제휴 업체의 정보를 안내하는 정보 플랫폼이며 통신판매의 당사자가 아닙니다. 서비스 이용 관련 사항은 각 제휴점에 직접 문의하시기 바랍니다.</p>
            <p style="margin-top: 20px;">&copy; 2026 오프모드건마사랑 All rights reserved.</p>
        </div>
    </footer>

</body>
</html>"""

# 5. 실행부 (루트 및 dist에 index.html 동시 생성)
if __name__ == "__main__":
    output_dir = "dist"
    os.makedirs(output_dir, exist_ok=True)
    
    final_index_html = generate_hub_html()
    
    # dist/index.html 생성
    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(final_index_html)
        
    # 최상단 루트 index.html 생성 (Netlify 404 방지)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(final_index_html)
        
    print("✨ 수도권 모든 지역 링크가 동적으로 포함된 메인 index.html 생성 완료!")