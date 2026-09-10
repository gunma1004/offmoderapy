INDEX_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="naver-site-verification" content="NAVER_VERIFICATION_PLACEHOLDER" />
    <title>오프모드건마사랑 - 서울·경기·인천 프리미엄 힐링·아로마 스웨디시 24시</title>
    <meta name="description" content="서울, 경기, 인천 수도권 전 지역 30분 내 방문. 출장 웰니스 마사지, 출장 아로마 마사지, 출장 산후전후 마사지 등 전문 관리사가 제공하는 100% 후불제 안심 케어 서비스.">
    <meta name="robots" content="index,follow">
    
    <meta property="og:type" content="website">
    <meta property="og:title" content="오프모드건마사랑 - 서울·경기·인천 프리미엄 힐링·아로마 스웨디시 24시">
    <meta property="og:description" content="서울, 경기, 인천 수도권 전 지역 30분 내 방문. 출장 웰니스 마사지, 출장 아로마 마사지, 출장 산후전후 마사지 등 전문 관리사가 제공하는 100% 후불제 안심 케어 서비스.">
    <meta property="og:url" content="DOMAIN_PLACEHOLDER/">
    <meta property="og:site_name" content="오프모드건마사랑">

    <meta name="theme-color" content="#ff6b35">
    <link rel="canonical" href="DOMAIN_PLACEHOLDER/">
    <link rel="stylesheet" href="./styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        :root { --primary: #ff6b35; --text-dark: #1f2430; --text-muted: #5b6472; --bg-section: #fff5f0; }
        html { scroll-behavior: smooth; }
        body { font-family: 'Noto Sans KR', sans-serif; color: var(--text-dark); line-height: 1.7; background: var(--bg-section); }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
        
        .header { position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: rgba(20, 20, 35, 0.95); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(255,255,255,0.1); }
        .header-inner { display: flex; align-items: center; justify-content: space-between; height: 70px; max-width: 1200px; margin: 0 auto; padding: 0 20px; }
        .logo-text { font-size: 1.25rem; font-weight: 700; color: #fff; text-decoration: none; }
        .logo-text span { color: var(--primary); }
        .nav { display: flex; gap: 24px; align-items: center; }
        .nav a { color: #fff; text-decoration: none; font-size: 0.95rem; }
        .nav-cta { background: var(--primary); padding: 8px 18px; border-radius: 20px; font-weight: 700; font-size: 0.9rem; }

        .hero { padding: 150px 20px 80px; text-align: center; background: linear-gradient(180deg, #15151f 0%, #252030 100%); color: #fff; }
        .hero h1 { font-size: clamp(28px, 5vw, 44px); font-weight: 700; margin-bottom: 16px; line-height: 1.3; }
        .hero h1 span { color: var(--primary); }
        .hero p { font-size: 1.05rem; color: #b5b5c6; margin-bottom: 20px; }

        .section { padding: 80px 0; }
        .section-white { background: #fff; }
        .section-title { text-align: center; margin-bottom: 40px; }
        .section-title h2 { font-size: 1.8rem; margin-bottom: 10px; color: var(--text-dark); }
        .section-title p { color: var(--text-muted); }

        .partner-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }
        .card { background: #fdfcfb; border: 1px solid #eee; border-radius: 16px; padding: 25px; text-align: left; box-shadow: 0 2px 10px rgba(0,0,0,0.02); transition: transform 0.2s; }
        .card:hover { transform: translateY(-3px); }
        .card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
        .card h3 { font-size: 1.15rem; color: var(--text-dark); font-weight: 700; }
        .badge { background: #fff5f0; color: var(--primary); padding: 4px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: bold; }
        .card p { color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px; }
        .card-footer { display: flex; justify-content: space-between; align-items: center; }
        .tel { font-weight: bold; color: var(--text-dark); font-size: 0.95rem; }
        .btn-call { background: var(--primary); color: #fff; padding: 8px 16px; border-radius: 8px; text-decoration: none; font-size: 0.85rem; font-weight: bold; }

        /* 완벽하게 구분된 권역별/구별 허브 섹션 스타일 */
        .evasion-hub { background: #121218; color: #fff; padding: 80px 0; }
        .region-group { background: #181822; border: 1px solid rgba(255,107,53,0.2); border-radius: 16px; padding: 30px; margin-bottom: 30px; }
        .region-group h3 { color: var(--primary); font-size: 1.4rem; margin-bottom: 20px; border-bottom: 2px solid rgba(255,107,53,0.3); padding-bottom: 10px; }
        .district-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px; }
        .district-card { background: #1f1f2e; padding: 15px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05); }
        .district-card h4 { color: #fff; font-size: 1.05rem; margin-bottom: 10px; }
        .link-list { display: flex; flex-wrap: wrap; gap: 6px; }
        .link-list a { background: #2a2a3d; color: #d1d5db; padding: 4px 8px; border-radius: 6px; text-decoration: none; font-size: 0.8rem; transition: all 0.2s; }
        .link-list a:hover { background: var(--primary); color: #fff; }

        footer { background: #111; color: #888; padding: 40px 20px; text-align: center; font-size: 0.85rem; line-height: 1.6; }
        footer strong { color: #aaa; }
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

    <!-- 🌟 서울·경기·인천 모든 구·동별 허브 링크 섹션 -->
    <section class="evasion-hub" id="evasion-regions">
        <div class="container">
            <div class="section-title">
                <h2 style="color: #fff;">수도권 출장 웰니스 & 아로마 마사지 지역별 안내</h2>
                <p style="color: #b5b5c6;">서울·경기·인천 모든 구·동 단위 실시간 1:1 안심 방문 제휴 정보</p>
            </div>
            
            <!-- 서울특별시 권역 -->
            <div class="region-group">
                <h3>🏙️ 서울특별시 전지역 안내</h3>
                <div class="district-grid">
                    <div class="district-card">
                        <h4><a href="./evasion/seoul/gangnam/index.html" style="color:#ff6b35; text-decoration:none;">강남구 전역</a></h4>
                        <div class="link-list">
                            <a href="./evasion/seoul/gangnam/역삼동/index.html">역삼동</a><a href="./evasion/seoul/gangnam/논현동/index.html">논현동</a><a href="./evasion/seoul/gangnam/청담동/index.html">청담동</a><a href="./evasion/seoul/gangnam/삼성동/index.html">삼성동</a><a href="./evasion/seoul/gangnam/대치동/index.html">대치동</a><a href="./evasion/seoul/gangnam/신사동/index.html">신사동</a><a href="./evasion/seoul/gangnam/도곡동/index.html">도곡동</a><a href="./evasion/seoul/gangnam/개포동/index.html">개포동</a><a href="./evasion/seoul/gangnam/일원동/index.html">일원동</a><a href="./evasion/seoul/gangnam/수서동/index.html">수서동</a>
                        </div>
                    </div>
                    <div class="district-card">
                        <h4><a href="./evasion/seoul/mapo/index.html" style="color:#ff6b35; text-decoration:none;">마포구 전역</a></h4>
                        <div class="link-list">
                            <a href="./evasion/seoul/mapo/아현동/index.html">아현동</a><a href="./evasion/seoul/mapo/공덕동/index.html">공덕동</a><a href="./evasion/seoul/mapo/도화동/index.html">도화동</a><a href="./evasion/seoul/mapo/용강동/index.html">용강동</a><a href="./evasion/seoul/mapo/대흥동/index.html">대흥동</a><a href="./evasion/seoul/mapo/염리동/index.html">염리동</a><a href="./evasion/seoul/mapo/신수동/index.html">신수동</a><a href="./evasion/seoul/mapo/서교동/index.html">서교동</a><a href="./evasion/seoul/mapo/합정동/index.html">합정동</a><a href="./evasion/seoul/mapo/망원동/index.html">망원동</a><a href="./evasion/seoul/mapo/연남동/index.html">연남동</a><a href="./evasion/seoul/mapo/성산동/index.html">성산동</a><a href="./evasion/seoul/mapo/상암동/index.html">상암동</a>
                        </div>
                    </div>
                    <div class="district-card">
                        <h4><a href="./evasion/seoul/seocho/index.html" style="color:#ff6b35; text-decoration:none;">서초구 전역</a></h4>
                        <div class="link-list">
                            <a href="./evasion/seoul/seocho/서초동/index.html">서초동</a><a href="./evasion/seoul/seocho/반포동/index.html">반포동</a><a href="./evasion/seoul/seocho/방배동/index.html">방배동</a><a href="./evasion/seoul/seocho/잠원동/index.html">잠원동</a><a href="./evasion/seoul/seocho/양재동/index.html">양재동</a><a href="./evasion/seoul/seocho/내곡동/index.html">내곡동</a>
                        </div>
                    </div>
                    <div class="district-card">
                        <h4><a href="./evasion/seoul/songpa/index.html" style="color:#ff6b35; text-decoration:none;">송파구 전역</a></h4>
                        <div class="link-list">
                            <a href="./evasion/seoul/songpa/잠실동/index.html">잠실동</a><a href="./evasion/seoul/songpa/신천동/index.html">신천동</a><a href="./evasion/seoul/songpa/풍납동/index.html">풍납동</a><a href="./evasion/seoul/songpa/송파동/index.html">송파동</a><a href="./evasion/seoul/songpa/석촌동/index.html">석촌동</a><a href="./evasion/seoul/songpa/삼전동/index.html">삼전동</a><a href="./evasion/seoul/songpa/가락동/index.html">가락동</a><a href="./evasion/seoul/songpa/문정동/index.html">문정동</a><a href="./evasion/seoul/songpa/방이동/index.html">방이동</a><a href="./evasion/seoul/songpa/오금동/index.html">오금동</a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 경기도 권역 -->
            <div class="region-group">
                <h3>🏡 경기도 전지역 안내</h3>
                <div class="district-grid">
                    <div class="district-card">
                        <h4><a href="./evasion/gyeonggi/seongnam-bundang/index.html" style="color:#ff6b35; text-decoration:none;">성남시 분당구</a></h4>
                        <div class="link-list">
                            <a href="./evasion/gyeonggi/seongnam-bundang/분당동/index.html">분당동</a><a href="./evasion/gyeonggi/seongnam-bundang/수내동/index.html">수내동</a><a href="./evasion/gyeonggi/seongnam-bundang/정자동/index.html">정자동</a><a href="./evasion/gyeonggi/seongnam-bundang/서현동/index.html">서현동</a><a href="./evasion/gyeonggi/seongnam-bundang/이매동/index.html">이매동</a><a href="./evasion/gyeonggi/seongnam-bundang/야탑동/index.html">야탑동</a><a href="./evasion/gyeonggi/seongnam-bundang/판교동/index.html">판교동</a><a href="./evasion/gyeonggi/seongnam-bundang/삼평동/index.html">삼평동</a>
                        </div>
                    </div>
                    <div class="district-card">
                        <h4><a href="./evasion/gyeonggi/suwon-jangan/index.html" style="color:#ff6b35; text-decoration:none;">수원시 장안구</a></h4>
                        <div class="link-list">
                            <a href="./evasion/gyeonggi/suwon-jangan/파장동/index.html">파장동</a><a href="./evasion/gyeonggi/suwon-jangan/정자동/index.html">정자동</a><a href="./evasion/gyeonggi/suwon-jangan/영화동/index.html">영화동</a><a href="./evasion/gyeonggi/suwon-jangan/송죽동/index.html">송죽동</a><a href="./evasion/gyeonggi/suwon-jangan/조원동/index.html">조원동</a><a href="./evasion/gyeonggi/suwon-jangan/율천동/index.html">율천동</a>
                        </div>
                    </div>
                    <div class="district-card">
                        <h4><a href="./evasion/gyeonggi/goyang-ilsandong/index.html" style="color:#ff6b35; text-decoration:none;">고양시 일산동구</a></h4>
                        <div class="link-list">
                            <a href="./evasion/gyeonggi/goyang-ilsandong/식사동/index.html">식사동</a><a href="./evasion/gyeonggi/goyang-ilsandong/중산동/index.html">중산동</a><a href="./evasion/gyeonggi/goyang-ilsandong/정발산동/index.html">정발산동</a><a href="./evasion/gyeonggi/goyang-ilsandong/백석동/index.html">백석동</a><a href="./evasion/gyeonggi/goyang-ilsandong/마두동/index.html">마두동</a><a href="./evasion/gyeonggi/goyang-ilsandong/장항동/index.html">장항동</a>
                        </div>
                    </div>
                    <div class="district-card">
                        <h4><a href="./evasion/gyeonggi/yongin-suji/index.html" style="color:#ff6b35; text-decoration:none;">용인시 수지구</a></h4>
                        <div class="link-list">
                            <a href="./evasion/gyeonggi/yongin-suji/풍덕천동/index.html">풍덕천동</a><a href="./evasion/gyeonggi/yongin-suji/신봉동/index.html">신봉동</a><a href="./evasion/gyeonggi/yongin-suji/죽전동/index.html">죽전동</a><a href="./evasion/gyeonggi/yongin-suji/동천동/index.html">동천동</a><a href="./evasion/gyeonggi/yongin-suji/상현동/index.html">상현동</a><a href="./evasion/gyeonggi/yongin-suji/성복동/index.html">성복동</a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 인천광역시 권역 -->
            <div class="region-group">
                <h3>🌊 인천광역시 전지역 안내</h3>
                <div class="district-grid">
                    <div class="district-card">
                        <h4><a href="./evasion/incheon/namdong/index.html" style="color:#ff6b35; text-decoration:none;">남동구 전역</a></h4>
                        <div class="link-list">
                            <a href="./evasion/incheon/namdong/구월동/index.html">구월동</a><a href="./evasion/incheon/namdong/간석동/index.html">간석동</a><a href="./evasion/incheon/namdong/만수동/index.html">만수동</a><a href="./evasion/incheon/namdong/서창동/index.html">서창동</a><a href="./evasion/incheon/namdong/논현동/index.html">논현동</a><a href="./evasion/incheon/namdong/고잔동/index.html">고잔동</a>
                        </div>
                    </div>
                    <div class="district-card">
                        <h4><a href="./evasion/incheon/yeonsu/index.html" style="color:#ff6b35; text-decoration:none;">연수구 전역</a></h4>
                        <div class="link-list">
                            <a href="./evasion/incheon/yeonsu/옥련동/index.html">옥련동</a><a href="./evasion/incheon/yeonsu/연수동/index.html">연수동</a><a href="./evasion/incheon/yeonsu/청학동/index.html">청학동</a><a href="./evasion/incheon/yeonsu/동춘동/index.html">동춘동</a><a href="./evasion/incheon/yeonsu/송도동/index.html">송도동</a>
                        </div>
                    </div>
                    <div class="district-card">
                        <h4><a href="./evasion/incheon/bupyeong/index.html" style="color:#ff6b35; text-decoration:none;">부평구 전역</a></h4>
                        <div class="link-list">
                            <a href="./evasion/incheon/bupyeong/부평동/index.html">부평동</a><a href="./evasion/incheon/bupyeong/산곡동/index.html">산곡동</a><a href="./evasion/incheon/bupyeong/청천동/index.html">청천동</a><a href="./evasion/incheon/bupyeong/갈산동/index.html">갈산동</a><a href="./evasion/incheon/bupyeong/삼산동/index.html">삼산동</a><a href="./evasion/incheon/bupyeong/부개동/index.html">부개동</a>
                        </div>
                    </div>
                    <div class="district-card">
                        <h4><a href="./evasion/incheon/geomdan/index.html" style="color:#ff6b35; text-decoration:none;">검단동 전역</a></h4>
                        <div class="link-list">
                            <a href="./evasion/incheon/geomdan/마전동/index.html">마전동</a><a href="./evasion/incheon/geomdan/당하동/index.html">당하동</a><a href="./evasion/incheon/geomdan/원당동/index.html">원당동</a><a href="./evasion/incheon/geomdan/불로동/index.html">불로동</a><a href="./evasion/incheon/geomdan/검암동/index.html">검암동</a><a href="./evasion/incheon/geomdan/아라동/index.html">아라동</a>
                        </div>
                    </div>
                </div>
            </div>

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